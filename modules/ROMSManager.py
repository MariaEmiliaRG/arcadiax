import os
import re
import shutil
import json

class ROMAlreadyExistsException(Exception):
    """Excepción lanzada cuando la ROM ya existe en el directorio."""
    pass

class ROMSManager: 
    def __init__(self):
        self.ROMSDir = "../roms"
        if not os.path.exists(self.ROMSDir):
            os.makedirs(self.ROMSDir)

        with open(os.path.join(self.ROMSDir,"ROMSExt.json"), "r") as file:
            self.ROMSExtensions = json.load(file)

        return
    
    def changeROMName(self, fileName):
        name, extension = os.path.splitext(fileName)
        name = re.sub(r'[\(\[].*?[\)\]]', '', name)
        name = re.sub(r'[^A-Za-z0-9 ]', ' ', name)
        name = name.split()
        name = "-".join(name)
        name = name.upper()

        return name + extension

    def ROMExist(self, fileName):
        return os.path.exists(os.path.join(self.ROMSDir, fileName))

    def copyROM(self, originPath, fileName):
        newFileName = self.changeROMName(fileName)
        if self.ROMExist(newFileName):
            raise ROMAlreadyExistsException(f"El videojuego {fileName} ya existe.")
        try:
            shutil.copy(os.path.join(originPath, fileName), os.path.join(self.ROMSDir, newFileName))
        except Exception as e:
            raise

        return

    def getROMSFromADir(self, dirPath):

        ROMSFiles = []

        for fileName in os.listdir(dirPath):
            filePath = os.path.join(dirPath, fileName)
            if os.path.isfile(filePath):
                
                for ext in self.ROMSExtensions:
                    if fileName.lower().endswith(ext):
                        ROMSFiles.append(fileName)
                        break
            
        return ROMSFiles
        
