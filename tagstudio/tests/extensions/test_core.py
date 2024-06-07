from pathlib import Path
from tagstudio.src.extensions.core.src.ts_ex_core import CoreExtension

path = str(Path.cwd())
extension = CoreExtension(path)


def test_construction():
    assert extension.statistics().get("active") is True


def test_refresh():
    path = extension.gen_tg_ex_library()
    assert path is not None and path != ""
