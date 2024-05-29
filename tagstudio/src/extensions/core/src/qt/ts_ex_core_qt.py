"""
Copyright (c) 2024 Lukas Pahomovs (dserveroriginal)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

"""

# Core Extension GUI
import ctypes
import logging
import math
import os
import sys
import time
import typing
import webbrowser
from datetime import datetime as dt
from pathlib import Path
from queue import Queue
from typing import Optional
from PIL import Image
from PySide6 import QtCore
from PySide6.QtCore import QObject, QThread, Signal, Qt, QThreadPool, QTimer, QSettings
from PySide6.QtGui import (
    QGuiApplication,
    QPixmap,
    QMouseEvent,
    QColor,
    QAction,
    QFontDatabase,
    QIcon,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QScrollArea,
    QFileDialog,
    QSplashScreen,
    QMenu,
    QMenuBar,
)
from humanfriendly import format_timespan

from src.core.enums import SettingItems
from src.core.library import ItemType
from src.core.ts_core import TagStudioCore
from src.core.constants import (
    PLAINTEXT_TYPES,
    TAG_COLORS,
    DATE_FIELDS,
    TEXT_FIELDS,
    BOX_FIELDS,
    ALL_FILE_TYPES,
    SHORTCUT_TYPES,
    PROGRAM_TYPES,
    ARCHIVE_TYPES,
    PRESENTATION_TYPES,
    SPREADSHEET_TYPES,
    DOC_TYPES,
    AUDIO_TYPES,
    VIDEO_TYPES,
    IMAGE_TYPES,
    LIBRARY_FILENAME,
    COLLAGE_FOLDER_NAME,
    BACKUP_FOLDER_NAME,
    TS_FOLDER_NAME,
    VERSION_BRANCH,
    VERSION,
)
from src.core.utils.web import strip_web_protocol
from src.qt.flowlayout import FlowLayout
from src.qt.main_window import Ui_MainWindow
from src.qt.helpers.function_iterator import FunctionIterator
from src.qt.helpers.custom_runnable import CustomRunnable
from src.qt.widgets.collage_icon import CollageIconRenderer
from src.qt.widgets.panel import PanelModal
from src.qt.widgets.thumb_renderer import ThumbRenderer
from src.qt.widgets.progress import ProgressWidget
from src.qt.widgets.preview_panel import PreviewPanel
from src.qt.widgets.item_thumb import ItemThumb
from src.qt.modals.build_tag import BuildTagPanel
from src.qt.modals.tag_database import TagDatabasePanel
from src.qt.modals.file_extension import FileExtensionModal
from src.qt.modals.fix_unlinked import FixUnlinkedEntriesModal
from src.qt.modals.fix_dupes import FixDupeFilesModal
from src.qt.modals.folders_to_tags import FoldersToTagsModal
from src.extensions.core.src.ts_ex_core import CoreExtension


def format_menu(menu: QMenu, core_extension: CoreExtension) -> QMenu:
    """Formats the menu

    Args:
        menu (QMenu): initial menu
        core_extension (CoreExtension) : extensions core

    Returns:
        QMenu: formatted menu
    """

    open_extensions_action = QAction("&Open Extensions Window", menu)
    open_extensions_action.setShortcut(
        QtCore.QKeyCombination(
            QtCore.Qt.KeyboardModifier(QtCore.Qt.KeyboardModifier.ControlModifier),
            QtCore.Qt.Key.Key_E,
        )
    )
    open_extensions_action.setToolTip("Ctrl+E")
    menu.addAction(open_extensions_action)
    return menu
