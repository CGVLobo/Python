import os.path as path
class FileManager:
    def __init__(self,filePath):
        self.filePath=filePath
        self.fileStatus=False
        if(path.exists(self.filePath)):
            self.fileStatus=True
            self.fileAccess=open(self.filePath)
        else:
            self.fileAccess=None

    def readFile(self):
        if self.fileStatus:
            return self.fileAccess
        else:
            return None