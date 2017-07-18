import io

class IOOps(object):
    
    def getFile(self,FILE):
        self.FILE = str(FILE)
    
    def openFileBytemode(self):
        self.openFile = open(self.FILE,'rb')
    
    def readFileBytes(self):
        self.openFileBytemode()
        self.openFileBytemode.close()
    
    def shiftByte(self,shift):
        byte = self.openFile.read(1)
        shift = str.encode(shift)
        i = 0
        while byte != '':
            i += 1
            byte = self.openFile.read(i)+shift
            byte = self.openFile.read(i)
            
        
obj = IOOps()
obj.getFile("test.file")
obj.openFileBytemode()
obj.getFile("test.file")
obj.shiftByte('1')

#http://stackoverflow.com/questions/42952623/stop-python-module-from-printing
