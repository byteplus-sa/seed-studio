import argparse
import os
import sys
from pathlib import Path


def inventory(repository, skill):
    bundle = repository / ".agents/skills" / skill
    for path in (repository, repository / ".agents", bundle.parent, bundle):
        if path.is_symlink():
            raise ValueError(f"symlink in bundle path: {path}")
        if not path.is_dir():
            raise ValueError(f"missing bundle directory: {path}")
    paths = {}

    def visit(directory):
        with os.scandir(directory) as entries:
            for entry in sorted(entries, key=lambda item: item.name):
                if entry.name in {".DS_Store", "__pycache__"}:
                    continue
                path = Path(entry.path)
                relative = path.relative_to(bundle)
                if relative.parts[0] == "agents":
                    continue
                if entry.is_symlink():
                    raise ValueError(f"symlink in sync scope: {path}")
                if entry.is_dir(follow_symlinks=False):
                    paths[relative] = "directory"
                    visit(path)
                elif entry.is_file(follow_symlinks=False):
                    paths[relative] = "file"
                else:
                    raise ValueError(f"unsupported file type in sync scope: {path}")

    visit(bundle)
    return paths


def preview(source, destination, skills):
    needs_ownership = False
    for skill in skills:
        if not skill or any(character not in
                            "abcdefghijklmnopqrstuvwxyz0123456789-" for character in skill):
            raise ValueError(f"invalid skill name: {skill!r}")
        upstream = inventory(source, skill)
        local = inventory(destination, skill)
        for relative in sorted(upstream.keys() & local.keys()):
            if upstream[relative] != local[relative]:
                raise ValueError(
                    f"file/directory conflict: {skill}/{relative}; "
                    "resolve ownership explicitly before syncing"
                )
        destination_only = local.keys() - upstream.keys()
        if destination_only:
            needs_ownership = True
            print(f"destination-only ownership unresolved: {skill}")
            for relative in sorted(destination_only):
                print(f"    preserve {str(relative)!r}")
    return needs_ownership


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("skills", nargs="+")
    arguments = parser.parse_args()
    try:
        needs_ownership = preview(
            arguments.source, arguments.destination, arguments.skills,
        )
    except (OSError, ValueError) as error:
        print(f"ERROR: ownership preview failed: {error}", file=sys.stderr)
        return 1
    if needs_ownership:
        print(
            "ERROR: destination-only paths may be committed overlays or upstream "
            "deletions. Nothing copied; retain them through a selective manual "
            "merge, or resolve each path with explicit owner authorization (exit 6).",
            file=sys.stderr,
        )
        return 6
    return 0


if __name__ == "__main__":
    sys.exit(main())
