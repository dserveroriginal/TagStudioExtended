from pathlib import Path
from tagstudio.src.extensions.core.src.ts_ex_core import CoreExtension
# from src.extensions.core.src.ts_ex_core import CoreExtension this one doesnt work on some systems

path = str(Path.cwd())
extension = CoreExtension(path)


def test_construction():
    assert (
        extension.statistics().get("active") is True
        and extension.statistics().get("name") == "core"
    )


def test_refresh():
    empty = extension.refresh_library()
    extensions = extension.get_extensions()
    assert empty is None  # and extensions[0]["name"]=="core"
