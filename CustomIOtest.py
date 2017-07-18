import io

class IOOps(object):
    
    def getFile(self,FILE):
        self.FILE = str(FILE)
    
    def openFileBytemode(self):
        self.openFile = open(self.FILE,'rb')

obj = IOOps()
obj.getFile("test.file")
obj.openFileBytemode()
