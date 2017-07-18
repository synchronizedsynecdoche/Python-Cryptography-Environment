# implement constant time functions for key verification!
# must define insecOK prior to calling
class KDF:
    
    def PBKCheck(self):
        
        try:

            #import Password Based Key Derivation Function
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
            from cryptography.hazmat.backends import default_backend
            

        except ImportError:

            # make the abscence of PBKDF2 run the script in SHA256 mode (!less secure!)

            print "You do not have PKDF2 required for secure password derivation\nUse less secure SHA256 derivation mode?\n"

            insecOK = raw_input(">>>")
            insecOK = insecOK.upper()

            if insecOK[0] == "Y":
            
                global insecOK
            
                insecOK = True
      
    def SHAEnable(self, insecOK):
        
        if insecOK:
            
            import HashSHA
            
            print "SHA256 key derivation enabled"
            
            key = str.encode(raw_input(" enter a key >"))
            
            shaObj = HashSHA.sha256(key)
            
            return shaObj
       
       else:
            print "No usable key deviation function found\nyou must use random keys"
    

    def random(self, size):
        
        if size != 16 and size != 24 and size !=32:
            
            print "invalid key size"    
            
            return 1
        
        rawRandom = os.urandom(size)

        return rawRandom
    def pbkdf(self, suppliedPhrase, iterations, check):

        if iterations < 100000:

            print "unsafe iteration count"
            os.exit(1)

        pbkdfSalt = os.urandom(16)
        backend = default_backend()
        pbkdfObj = PBKDF2HMAC(algorithm=hashes.SHA512(), length=32, salt=pbkdfsalt, iterations=iterations, backend=backend)

        suppliedPhraseBytes = str.encode(suppliedPhrase)

        derivedKey = pbkdfObj.derive(suppliedPhraseBytes)

        #this verify was used in the documentation example, but since it would effectively double the time taken to return the pass, I made it optional

        if check:

            try:
                pbkdfObj.verify(suppliedPhraseBytes,suppliedPhrase)

            except cryptography.exceptions.InvalidKey:

                print "problem with PBKDF2, not proceeding"
                os.exit(1)
        
        return derivedKey

                    
                

            
            
                    
            

