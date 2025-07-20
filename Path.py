import os
import sys


def get_path(path: str) -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return os.path.relpath(
            os.path.normpath(path), start=os.path.dirname(sys.executable)
        )
    else:
        return os.path.relpath(
            os.path.normpath(path), start=os.path.dirname(__file__)
        )
