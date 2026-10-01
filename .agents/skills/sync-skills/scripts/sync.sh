#!/usr/bin/env bash
# Mirror allowlisted skill bundles from the upstream source checkout.
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
# Exit codes: 0 ok, 1 error, 2 usage, 3 dirty source scope needs confirmation.
set -euo pipefail

ALLOWLIST="brief-intake prompt-review seedance-prompt-25 seedance-prompt-25-filipino seedance-prompt-20 seedance-acting-console seedance-animation-styles seedance-camera-presets seedance-graybox-world seedance-lens-presets seedance-lighting-presets seedance-pacing-presets seedance-motion-design seedance-music-video seedance-restoration seedance-vfx-prompt seedream-prompt seedream-character-sheet seedream-location-asset seed-audio-prompt ugc-ad-modes ugc-motion-presets color-grade-palettes tig-blocking-map tig-scene-engine"
EXCLUDES=(--exclude='.DS_Store' --exclude='__pycache__')

MODE="${1:-}"
case "$MODE" in
  plan|apply) shift ;;
  *) echo "usage: sync.sh plan|apply [all | skill-name ...]" >&2; exit 2 ;;
esac

ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"
cd "$ROOT"

# 1. Preflight
SRC="${SKILLS_SOURCE:-../ark-director}"
if [ ! -f "$SRC/.agents/skills/seedance-prompt-25/SKILL.md" ]; then
  echo "ERROR: upstream checkout not found at $SRC — stop and report" >&2
  exit 1
fi
echo "source ok: $SRC"
echo "source revision: $(git -C "$SRC" rev-parse --short HEAD)"
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

# 4. Diff, and sync when applying
echo "--- skills:"
for s in $SKILLS; do
  if diff -rq "${EXCLUDES[@]}" "$SRC/.agents/skills/$s" ".agents/skills/$s" >/dev/null 2>&1; then
    echo "unchanged  $s"
  else
    echo "updated    $s"
    diff -rq "${EXCLUDES[@]}" "$SRC/.agents/skills/$s" ".agents/skills/$s" 2>/dev/null | sed 's/^/    /' || true
    if [ "$MODE" = "apply" ]; then
      rsync -a --delete "${EXCLUDES[@]}" "$SRC/.agents/skills/$s/" ".agents/skills/$s/"
    fi
  fi
done
if [ "$MODE" = "plan" ]; then
  echo "plan only: nothing copied"
  if [ "$NEEDS_CONFIRM" = "1" ]; then
    echo "CONFIRM: the sync would copy unreviewed upstream work; ask the user before applying" >&2
    exit 3
  fi
fi
exit 0
