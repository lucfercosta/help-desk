
#!/usr/bin/env bash

set -euo pipefail

OUTPUT="project_dump.txt"

{
    echo "PROJECT DUMP"
    echo "Generated: $(date)"
    echo "Project: $(basename "$PWD")"
    echo

    echo "=============================="
    echo "PROJECT STRUCTURE"
    echo "=============================="

    find . \
        -path './.git' -prune -o \
        -path './.venv' -prune -o \
        -path './__pycache__' -prune -o \
        -path '*/__pycache__' -prune -o \
        -type f -print | sort

    echo
    echo "=============================="
    echo "FILE CONTENTS"
    echo "=============================="

    find . \
        -path './.git' -prune -o \
        -path './.venv' -prune -o \
        -path './__pycache__' -prune -o \
        -path '*/__pycache__' -prune -o \
        -type f \
        \( -name '*.py' \
        -o -name '*.toml' \
        -o -name '*.md' \
        -o -name '*.json' \
        -o -name '*.yml' \
        -o -name '*.yaml' \
        -o -name '*.ini' \
        -o -name '*.cfg' \
        -o -name '*.sh' \
        -o -name '.gitignore' \) \
        ! -name 'project_dump.txt' \
        ! -name 'dump_project.sh' \
        -print | sort |
    while IFS= read -r file; do
        echo
        echo "----------------------------------------"
        echo "FILE: $file"
        echo "----------------------------------------"
        cat "$file"
        echo
    done

} > "$OUTPUT"

echo "Project dump created: $OUTPUT"