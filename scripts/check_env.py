from __future__ import annotations

import importlib.util
import platform
import sys


PACKAGES = [
    "torch",
    "torchaudio",
    "transformers",
    "datasets",
    "evaluate",
    "jiwer",
    "librosa",
    "soundfile",
    "numpy",
]


def package_status(name: str) -> str:
    spec = importlib.util.find_spec(name)
    return "ok" if spec is not None else "missing"


def main() -> int:
    print("Audio LLM Lab environment check")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print("")

    missing: list[str] = []
    for package in PACKAGES:
        status = package_status(package)
        print(f"{package:12} {status}")
        if status == "missing":
            missing.append(package)

    print("")
    if missing:
        print("Missing packages:")
        for package in missing:
            print(f"- {package}")
        print("")
        print("Install project dependencies with:")
        print("  uv sync --extra dev")
        return 1

    print("All checked packages are available.")

    try:
        import torch

        print("")
        print(f"torch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        print(f"MPS available: {torch.backends.mps.is_available()}")
    except Exception as exc:
        print("")
        print(f"Could not inspect torch backend: {exc}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
