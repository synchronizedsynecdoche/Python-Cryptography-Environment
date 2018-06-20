
class InputHandler(object):

    def TalkBack(self):
        while True:
        
            hear = raw_input("PCE ~ > ")
            print hear

    def CipherSpawner(self, cipher):
        
        if cipher == "AES":
            
            import CipherAES
            cipherObj = CipherAES.AESRoutine()
            
            return cipherObj
            
        elif cipher == "CAMELLIA":
            
            import CipherCamellia
            cipherObj = CipherCamellia.CamelliaRoutine()
            
            return cipherObj
        
        elif cipher == "TRIPLEDES" or cipher == "DESX3":
            
            import CipherTripleDES
            cipherObj = CipherTripleDES.TripleDESRoutine()
            
            return cipherObj
        
        
        
    def Listener(self):

        print "It is strongly recommended to view the considerations (\"considerations\")" \
              "prior to using the Python Cryptography Environment"
        while True:
        
            userInput = raw_input("PCE ~ > ").upper()

"""
            if "considerations":

           # if "help" in userInput:
                
                if "mode" in userInput:
                    
                    if "CBC" in userInput:
                        
                
                elif "cipher" in userInput:
                    
                    if "AES" in userInput:


                    if "CAMELLIA" in userInput:


                    if "DES" in userInput:
                    
                    else:
                        
                       print "That is unknown even to me"
                
                elif "HASH" in userInput:
                
                        
                    if "SHA" in userInput:
                        
                    
                    if "WHIRLPOOL" in userInput:
                    
                    
                    if "MD5" in userInput:

            
            if "AES" in userInput and "help" not in userInput:
                
                self.CipherSpawner("AES")
                
                userMode = raw_input("PCE AES/MODE > ")
                
                #def staging(self, key, mode, iv, nonceVal)
                
                # do that thing where it sys.std.out.flush thing
                userKey =raw_input("PCE AES/KEY > ").encode(userKey)


                
                
"""
                
testObj = InputHandler()
testObj.Listener()            
            
                
                
    
