import os
import sys
from shutil import rmtree
from subprocess import run as cmd_run

"""
Do not execute scripts/ directly. Only use 'poetry' tool to run them.

Examples:
$> poetry run make <command>
"""

PROJ_ROOT = os.getcwd()
proj_toml = os.path.join(PROJ_ROOT, "pyproject.toml")
if not os.path.isfile(proj_toml):
    raise Exception(
        "This script should be executed from project root only using poetry."
    )

PROTO_ROOT = os.path.join(PROJ_ROOT, "api/proto")
TIGRIS_PROTO_DIR = os.path.join(PROTO_ROOT, "server/v1")
GENERATED_PROTO_DIR = os.path.join(PROJ_ROOT, "api/generated")


def generate():
    if not os.path.exists(GENERATED_PROTO_DIR):
        os.makedirs(GENERATED_PROTO_DIR)
    proto_sources = []
    for pd in ["google/api", "openapiv3"]:
        pd_path = os.path.join(PROTO_ROOT, pd)
        for pd_file in os.listdir(pd_path):
            if pd_file.endswith(".proto"):
                proto_sources.append(os.path.join(pd_path, pd_file))

    for pf in ["api.proto", "search.proto", "auth.proto", "observability.proto"]:
        pf_path = os.path.join(TIGRIS_PROTO_DIR, pf)
        proto_sources.append(pf_path)

    # compile proto
    for proto_file in proto_sources:
        cmd_run(
            f"python -m grpc_tools.protoc --proto_path={PROTO_ROOT}"
            f" --python_out={GENERATED_PROTO_DIR} --pyi_out={GENERATED_PROTO_DIR} "
            f"--grpc_python_out={GENERATED_PROTO_DIR} {proto_file}",
            shell=True,
            check=True,
        )

    # fix imports in generated files
    fixable_imports = {
        "from google.api": "from {rp}google.api",
        "from openapiv3": "from {rp}openapiv3",
        "from server.v1": "from {rp}server.v1",
    }
    replace_targets = []
    for subdir, _dirs, files in os.walk(GENERATED_PROTO_DIR):
        for f in files:
            if "pb2" in f and (f.endswith(".py") or f.endswith(".pyi")):
                fp = os.path.join(subdir, f)
                with open(fp, "r") as fopen:
                    fdata = fopen.read()
                    for find, replace in fixable_imports.items():
                        replace_with = ".." if "/openapiv3/" in fp else "..."
                        fdata = fdata.replace(find, replace.format(rp=replace_with))
                    replace_targets.append((fp, fdata))

    for fp, fdata in replace_targets:
        with open(fp, "w") as f:
            f.write(fdata)

    print(f"SUCCESS! Compiled proto stubs available in:\n{GENERATED_PROTO_DIR}")


def clean():
    if os.path.exists(GENERATED_PROTO_DIR):
        rmtree(GENERATED_PROTO_DIR)


def main():
    valid_args = {
        "generate": "generate api from proto",
        "clean": "clean generated api",
    }
    usage = [
        'Not enough arguments to "make".',
        "\nUSAGE:",
        "poetry run make <command>",
        "\nCOMMANDS:",
    ]
    usage.extend(map(lambda k: "{:<16} {:<25}".format(k, valid_args[k]), valid_args))
    usage_str = "\n".join(usage)
    if not len(sys.argv) == 2 or sys.argv[1] not in valid_args:
        print(usage_str)
        exit(1)

    arg = sys.argv[1]
    if arg == "generate":
        generate()
    elif arg == "clean":
        clean()
    else:
        print(usage_str)
