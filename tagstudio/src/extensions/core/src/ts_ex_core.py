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
    """ Base extension class

    """    
    def __init__(self, config: dict,  path: str) -> None:
        """ Creates base class

        Args:
            config (dict): json part 
            path (str): extension path
        """        
        self.name = config.get("name")
        self.version = config.get("version")
        self.dependencies = config.get("dedependencies")
        self.image_path = os.path.join(path, config.get("image"))
        self.active=False
        print(self)
        
class CoreExtension(Extension):
    """Core extension class


    Args:
        Extension (class): Base extension class

    """    
    def __init__(self, path:str) -> None:
        """ Creates core extension class

        Args:
            path (str): extension path
        """        
        self.path=os.path.join(path,"tagstudio","src","extensions")
        self.config=os.path.join(self.path,"ts_ex_library.json")
        print(self.config)
        file=open(self.config)
        self.config=json.load(file)
        self.extensions=self.config.get("extensions")
        Extension.__init__(self,self.extensions[0],path)
        
            
        



class TSApi:
    """_summary_

    Args:
        object (_type_): _description_
    """    
    def __init__(self, path) -> None:
        self.path = path
