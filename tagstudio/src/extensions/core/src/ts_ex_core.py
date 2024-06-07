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

# Core Extension

import json
import os


class Extension:
    """Base extension class"""

    def __init__(self, config: dict, path: str) -> None:
        """Creates base class

        Args:
            config (dict): json part
            path (str): extension path
        """
        self.name = config.get("name")
        self.version = config.get("version")
        self.dependencies = config.get("dedependencies")
        self.image_path = path + "/" + config.get("image")
        self.active = False
        return

    def activate(self) -> None:
        """virtual activation method"""
        self.active = True
        return

    def deactivate(self) -> None:
        """virtual deactivation method"""
        self.active = False
        return

    def statistics(self) -> dict:
        """returns all data about extension

        Returns:
            dict: all dat
        """
        return {
            "name": self.name,
            "version": self.version,
            "dependencies": self.dependencies,
            "image": self.image_path,
            "active": self.active,
        }


class CoreExtension(Extension):
    """Core extension class


    Args:
        Extension (class): Base extension class

    """

    def __init__(self, path_str: str) -> None:
        """Creates core extension class

        Args:
            path (str): extension path
        """
        self.path = path_str + "/tagstudio/src/extensions"
        self.config = self.path + "/ts_ex_library.json"
        file = open(self.config)
        self.config = json.load(file)
        core = self.path + "/core/stats.json"
        core = open(core)
        core = json.load(core)
        self.extensions = self.config.get("extensions")
        Extension.__init__(self, core, self.path)
        self.activate()
        return

    def gen_tg_ex_library(self) -> None:
        base = self.path + "/core/assets/ts_ex_library_base.json"

        return base

    def activate(self) -> None:
        self.active = True
        return

    def deactivate(self) -> None:
        # self.active=False
        # should not be deactivated
        return


class TSApi:
    """_summary_

    Args:
        object (_type_): _description_
    """

    def __init__(self, path) -> None:
        self.path = path
