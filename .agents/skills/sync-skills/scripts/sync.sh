#!/usr/bin/env bash
# Update allowlisted skill bundles from the upstream source checkout.
#
# Usage: sync.sh plan|apply [all | skill-name ...]
#   plan   preflight, resolve the skill set, check the source scope, list diffs;
#          changes nothing
#   apply  the same checks, then rsync each changed skill into this repo
#
# SKILLS_SOURCE overrides the source checkout (default ../ark-director,
# resolved from this repo's root). apply refuses to copy while dirty source
# paths intersect the sync scope unless SYNC_ALLOW_DIRTY=1, which is set only
# after the user confirms.
#
# Each skill's agents/ folder is local metadata: it is never copied from the
# source and never deleted, so local-only agents/ folders and local policy
# edits (such as prompt-review's implicit-invocation setting) survive a sync.
#
# plan previews how many references to tools or skills this workspace does not
# ship (see forbidden-refs.txt) each updated skill would bring in. apply scans
# the synced skills for them and exits 4 until they are scrubbed.
#
# Exit codes: 0 ok, 1 error, 2 usage, 3 dirty source scope needs confirmation,
# 4 scrub required, 5 dirty destination, 6 destination-only ownership unresolved.
set -euo pipefail

ALLOWLIST="brief-intake prompt-review seedance-prompt-25 seedance-prompt-25-filipino seedance-prompt-20 seedance-animation-styles seedance-camera-presets seedance-lens-presets seedance-lighting-presets seedance-pacing-presets seedance-motion-design seedance-restoration seedance-vfx-prompt seedream-prompt seedream-character-sheet seedream-location-asset seed-audio-prompt ugc-ad-modes ugc-motion-presets color-grade-palettes omnihuman-prompt-20"
EXCLUDES=(--exclude='.DS_Store' --exclude='__pycache__')
RSYNC_EXCLUDES=("${EXCLUDES[@]}" --exclude='/agents')
RSYNC_OPTIONS=(-a --checksum --omit-dir-times "${RSYNC_EXCLUDES[@]}")

MODE="${1:-}"
case "$MODE" in
  plan|apply) shift ;;
  *) echo "usage: sync.sh plan|apply [all | skill-name ...]" >&2; exit 2 ;;
esac

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR" && git rev-parse --show-toplevel)"
cd "$ROOT"

# 1. Preflight
SRC="${SKILLS_SOURCE:-../ark-director}"
if [ ! -f "$SRC/.agents/skills/seedance-prompt-25/SKILL.md" ]; then
  echo "ERROR: upstream checkout not found at $SRC — stop and report" >&2
  exit 1
fi
echo "source ok: $SRC"
SOURCE_REVISION="$(git -C "$SRC" rev-parse --short HEAD)" || {
  echo "ERROR: source revision unavailable; nothing copied" >&2
  exit 1
}
echo "source revision: $SOURCE_REVISION"
echo "--- this repo working-tree changes:"
git status --short

# 2. Resolve the skill set
ARGS="$*"
[ "$ARGS" = "all" ] && ARGS=""
if [ -z "$ARGS" ]; then
  SKILLS="$ALLOWLIST"
  echo "full run: $(echo $SKILLS | wc -w | tr -d ' ') skills"
else
  SKILLS="$ARGS"
  for s in $SKILLS; do
    case " $ALLOWLIST " in
      *" $s "*) ;;
      *) echo "ERROR: $s is not allowlisted — stop and report" >&2; exit 1 ;;
    esac
  done
  echo "scoped run: $SKILLS"
fi
for s in $SKILLS; do
  [ -d "$SRC/.agents/skills/$s" ] || { echo "ERROR: $s missing from source — stop and report" >&2; exit 1; }
  [ -d ".agents/skills/$s" ] || { echo "ERROR: $s missing here; a sync never creates skill directories — stop and report" >&2; exit 1; }
done

DESTINATION_SCOPE=()
for s in $SKILLS; do
  DESTINATION_SCOPE+=(
    ".agents/skills/$s"
    ":(exclude).agents/skills/$s/agents"
    ":(exclude,glob).agents/skills/$s/**/.DS_Store"
    ":(exclude,glob).agents/skills/$s/**/__pycache__/**"
  )
done
DESTINATION_DIRTY="$(git status --porcelain=v1 --untracked-files=all --ignored -- "${DESTINATION_SCOPE[@]}")"
if [ -n "$DESTINATION_DIRTY" ]; then
  printf '%s\n' "$DESTINATION_DIRTY"
  echo "ERROR: destination work intersects the sync scope; resolve these paths explicitly before syncing (exit 5)" >&2
  echo "Nothing copied. SYNC_ALLOW_DIRTY applies only to source changes and cannot bypass this guard." >&2
  exit 5
fi

# 3. Source scope check
SCOPE_PATHS=()
for s in $SKILLS; do SCOPE_PATHS+=(".agents/skills/$s"); done
DIRTY="$(git -C "$SRC" status --short -- "${SCOPE_PATHS[@]}")"
NEEDS_CONFIRM=0
echo "--- dirty source paths intersecting the sync scope:"
if [ -n "$DIRTY" ]; then
  echo "$DIRTY"
  if [ "$MODE" = "plan" ]; then
    NEEDS_CONFIRM=1
  elif [ "${SYNC_ALLOW_DIRTY:-0}" != "1" ]; then
    echo "CONFIRM: the sync would copy unreviewed upstream work; ask the user before applying" >&2
    exit 3
  else
    echo "(proceeding: SYNC_ALLOW_DIRTY=1)"
  fi
else
  echo "(none)"
fi
OTHER_DIRTY="$(git -C "$SRC" status --short | wc -l | tr -d ' ')"
echo "source dirty paths overall: $OTHER_DIRTY (informational)"

OWNERSHIP_STATUS=0
python3 -B "$SCRIPT_DIR/ownership.py" "$SRC" "$ROOT" $SKILLS || OWNERSHIP_STATUS=$?
case "$OWNERSHIP_STATUS" in
  0|6) ;;
  *) exit 1 ;;
esac

# 4. Diff, and sync when applying
echo "--- skills:"
CHANGED=""
for s in $SKILLS; do
  if ! PREVIEW="$(rsync "${RSYNC_OPTIONS[@]}" --dry-run --itemize-changes "$SRC/.agents/skills/$s/" ".agents/skills/$s/")"; then
    echo "ERROR: preview failed for $s; nothing copied" >&2
    exit 1
  fi
  if [ -z "$PREVIEW" ]; then
    echo "unchanged  $s"
  else
    echo "updated    $s"
    printf '%s\n' "$PREVIEW" | sed 's/^/    /'
    CHANGED="$CHANGED $s"
    if [ "$MODE" = "plan" ]; then
      N="$(python3 "$SCRIPT_DIR/leaks.py" --count "$SRC/.agents/skills/$s")"
      [ "$N" != "0" ] && echo "    would bring in $N reference(s) to tools or skills not shipped here; scrub after applying"
    fi
  fi
done
if [ "$OWNERSHIP_STATUS" != "0" ]; then
  exit "$OWNERSHIP_STATUS"
fi
if [ "$MODE" = "apply" ] && [ -n "$CHANGED" ]; then
  for s in $CHANGED; do
    rsync "${RSYNC_OPTIONS[@]}" "$SRC/.agents/skills/$s/" ".agents/skills/$s/"
  done
  echo "--- scan of synced skills for references this workspace does not ship:"
  SCAN_ARGS=()
  for s in $CHANGED; do SCAN_ARGS+=(".agents/skills/$s"); done
  if ! python3 "$SCRIPT_DIR/leaks.py" "${SCAN_ARGS[@]}"; then
    echo "SCRUB REQUIRED: remove the references above, then run verify.py" >&2
    exit 4
  fi
fi
if [ "$MODE" = "plan" ]; then
  echo "plan only: nothing copied"
  if [ "$NEEDS_CONFIRM" = "1" ]; then
    echo "CONFIRM: the sync would copy unreviewed upstream work; ask the user before applying" >&2
    exit 3
  fi
fi
exit 0
