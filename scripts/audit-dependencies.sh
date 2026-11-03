#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

audit_dir="$(mktemp -d)"
trap 'rm -rf "$audit_dir"' EXIT

# lockfile에서 고정한 runtime/dev 전체를 검사한다. 의존성을 다시 선택하지 않는다.
uv export --locked --python 3.12 --all-groups --format requirements-txt \
  --no-emit-project --output-file "$audit_dir/requirements.txt" >/dev/null
uvx --python 3.12 --from pip-audit==2.10.1 pip-audit \
  --requirement "$audit_dir/requirements.txt" --require-hashes --disable-pip --strict
