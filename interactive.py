
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
        
            userInput = raw_input("PCE ~ > ") 
            userInputUpper = userInput.Upper()

            if "considerations":

            # turn all of this crap into a function
            if "help" in userInputUpper:
                
                if "mode" in userInputUpper:
                    
                    if "CBC" in userInputUpper:
                        
                
                elif "cipher" in userInputUpper:
                    
                    if "AES" in userInputUpper:


                    if "CAMELLIA" in userInputUpper:


                    if "DES" in userInputUpper:
                    
                    else:
                        
                       print "That is unknown even to me"
                
                elif "HASH" in userInputUpper:
                
                        
                    if "SHA" in userInputUpper:
                        
                    
                    if "WHIRLPOOL" in userInputUpper:
                    
                    
                    if "MD5" in userInputUpper:
                     #maybe demonstrate a collision!

            
            if "AES" in userInputUpper and "help" not in userInputUpper:
                
                self.CipherSpawner("AES")
                
                userMode = raw_input("PCE AES/MODE > ")
                
                #def staging(self, key, mode, iv, nonceVal)
                
                # do that thing where it sys.std.out.flush thing
                userKey =raw_input("PCE AES/KEY > ")
                userKeyBytes = str.encode(userKey)

                
                #have I made the pbkdf module yet???

                
                
               
                
testObj = InputHandler()
testObj.Listener()            
            
                
                
    
