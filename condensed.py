
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend


class AESRoutine(object):


    global backend
    backend = default_backend()
    # retrieve needed variables
    #unused variables can safely be set to None
    #checking that these variables are correct size will happen elsewhere
    def staging(self, key, mode, iv, nonceVal):

        global AESKEY
        global cipherMode
        global initVector
        global nonce
        global ciphertext
        global plaintext

        AESKEY = key

        CipherModeNotChecked = mode

        if CipherModeNotChecked.Upper == "CBC":

            initVector = iv
            cipherMode = modes.CBC(initVector)

        elif CipherModeNotChecked.Upper == "CTR":

            nonce = nonceVal
            cipherMode = modes.CTR(nonce)

        # OFB does not require Padding
        elif CipherModeNotChecked.Upper == "OFB":

            initVector = iv
            cipherMode = modes.OFB(initVector)

        elif CipherModeNotChecked.Upper == "CFB":

            cipherMode = modes.CFB

        elif CipherModeNotChecked.Upper == "GCM":

            print "Coming soon!"
            exit(0)

        else:

            print "Invalid mode"
            exit(1)

    def EncryptionRoutine(self, message):

        cipherInstance = Cipher(algorithms.AES(AESKEY),cipherMode, backend = backend)

        cryptorInstance = cipherInstance.encryptor()

        messageByte = str.encode(message)
        ciphertext = cryptorInstance.update(messageByte) + cryptorInstance.finalize()
        print ciphertext
        return ciphertext
                        # are keys needed? they;re global and set using the staging func
    def DecryptionRoutine(self, ciphertext):

         cipherInstance = Cipher(algorithms.AES(AESKEY),cipherMode, backend=backend)

         decryptorInstance = cipherInstance.decryptor()

         plaintext = decryptorInstance.update(ciphertext) + decryptorInstance.finalize()
         print plaintext
         return plaintext







from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend

class CamelliaRoutine(object):


    backend = default_backend()
    # retrieve needed variables
    #unused variables can safely be set to None
    #checking that these variables are correct size will happen elsewhere
    def staging(self, key, mode, iv, nonceVal):

        global cipherMode
        global initVector
        global nonce
        global ciphertext
        global plaintext
        global CAMELLIAKEY

        CAMELLIAKEY = key

        CipherModeNotChecked = mode

        if CipherModeNotCheked.Upper == "CBC":

            initVector = iv
            cipherMode = modes.CBC(initVector)

        elif CipherModeNotChecked.Upper == "CTR":

            nonce = nonceVal
            cipherMode = modes.CTR(nonce)

        # OFB does not require Padding
        elif CipherModeNotChecked.Upper == "OFB":

            initVector = iv
            cipherMode = modes.OFB(initVector)

        elif CipherModeNotChecked.Upper == "CFB":

            cipherMode = modes.CFB

        elif CipherModeNotChecked.Upper == "GCM":

            print "Coming soon!"
            exit(0)

        else:

            print "Invalid mode"
            exit(1)

    def EncryptionRoutine(self, message):

        cipherInstance = Cipher(algorithms.Camellia(CAMELLIAKEY),cipherMode, backend = backend)

        cryptorInstance = cipherInstance.encryptor()

        messageByte = str.encode(message)
        ciphertext = cryptorInstance.update(messageByte) + cryptorInstance.finalize()

        return ciphertext

    def DecryptionRoutine(self, ciphertext):

         cipherInstance = Cipher(algorithms.Camellia(CAMELLIAKEY),cipherMode, backend = backend)

         decryptorInstance = cipherInstance.decryptor()

         plaintext = decryptorInstance.update(ciphertext) + decryptorInstance.finalize()

         return plaintext

import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend

backend = default_backend()

random = os.urandom(16)
iv = os.urandom(16)
mode = modes.OFB(iv)
def EncryptionRoutine(message):

    cipherInstance = Cipher(algorithms.AES(random),mode, backend = backend)

    cryptorInstance = cipherInstance.encryptor()

    messageByte = str.encode(message)
    ciphertext = cryptorInstance.update(messageByte) + cryptorInstance.finalize()
    print ciphertext
    return ciphertext
    
def DecryptionRoutine(x):

    cipherInstance = Cipher(algorithms.AES(random),mode, backend = backend)
    decryptorInstance = cipherInstance.decryptor()

    plaintext = decryptorInstance.update(x) + decryptorInstance.finalize()
    print plaintext
    return plaintext


# see similarities in the ciphertext? That's because OFB is a stream mode and the string is the same in the beginning!
DecryptionRoutine(EncryptionRoutine("the quick brown fox jumped over the lazy log"))
DecryptionRoutine(EncryptionRoutine("the quick brown fox jumped over the lazy log."))



from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend

class TripleDESRoutine(object):


    backend = default_backend()

    def staging(self, key, mode, iv, nonceVal):

        global DESx3KEY
        global cipherMode
        global initVector
        global nonce
        global ciphertext
        global plaintext

        DESx3KEY = key

        CipherModeNotChecked = mode

        if CipherModeNotCheked.Upper == "CBC":

            initVector = iv
            cipherMode = modes.CBC(initVector)
        elif CipherModeNotChecked.Upper == "CTR":
            nonce = nonceVal
            cipherMode = modes.CTR(nonce)

        # OFB does not require Padding
        elif CipherModeNotChecked.Upper == "OFB":

            initVector = iv
            cipherMode = modes.OFB(initVector)

        elif CipherModeNotChecked.Upper == "CFB":

            cipherMode = modes.CFB

        elif CipherModeNotChecked.Upper == "GCM":

            print "Coming soon!"
            exit(0)

        else:

            print "Invalid mode"
            exit(1)

    def EncryptionRoutine(self, message,):

        cipherInstance = Cipher(algorithms.TripleDES(DESx3KEY),cipherMode, backend = backend)

        cryptorInstance = cipherInstance.encryptor()

        messageByte = str.encode(message)
        ciphertext = cryptorInstance.update(messageByte) + cryptorInstance.finalize()

        return ciphertext
                        # are keys needed? they;re global
    def DecryptionRoutine(self, ciphertext):

         cipherInstance = Cipher(algorithms.TripleDES(DESx3KEY),cipherMode, backend = backend)

         decryptorInstance = cipherInstance.decryptor()

         plaintext = decryptorInstance.update(ciphertext) + decryptorInstance.finalize()

         return plaintext

from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

backend = default_backend()
class MD5(object):

    def MD5(self, message):

        print "WARN: MD5 has known collision attacks (see FLAME malware forgery)"
        hasher = hashes.Hash(hashes.MD5(), backend=backend)

        messageBytes = str.encode(message)
        hasher.update(message)

        hasher.finalize

testObj = MD5()
testObj.MD5("test")
from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

backend = default_backend()
class RIPEMD(object):

    def RIPEMD160(self, message):

        hasher = hashes.Hash(hashes.RIPEMD160(), backend=backend)

        messageBytes = str.encode(message)
        hasher.update(message)

        hasher.finalize

testObj = RIPEMD()
testObj.RIPEMD160("test")
from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

backend = default_backend()


class SHAFamily(object):

    def sha1(self, message):

        print("WARN: SHA1 is not recommended, use SHA[224,256,384,512] instead!")
        hasher = hashes.Hash(hashes.SHA1(), backend=backend)
        
        messageBytes = str.encode(message)
        hasher.update(message)

        # does this automatically print out?
        hasher.finalize()

    def sha224(self, message):

        hasher = hashes.Hash(hashes.SHA224(), backend=backend)

        messageBytes = str.encode(message)
        hasher.update(message)

        hasher.finalize()

    def sha256(self, message):

        hasher = hashes.Hash(hashes.SHA256(), backend=backend)

        messageBytes = str.encode(message)
        hasher.update(message)

        hasher.finalize()

    def sha384(self, message):

        hasher = hashes.Hash(hashes.SHA384(), backend=backend)

        messageBytes = str.encode(message)
        hasher.update(message)

        hasher.finalize()

    def sha512(self, message):

        hasher = hashes.Hash(hashes.SHA512(), backend=backend)

        messageBytes = str.encode(message)
        hasher.update(message)

        hasher.finalize()

testObj = SHAFamily()

testObj.sha1("test")
testObj.sha224("test")
testObj.sha256("test")
testObj.sha512("test")
from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

backend = default_backend()
class Whirlpool(object):

    def Whirlpool(self, message):

        hasher = hashes.Hash(hashes.Whirlpool(), backend=backend)

        hasher.update(message)

        hasher.finalize

testObj = Whirlpool()
testObj.Whirlpool("test")
# Input Handler

# tests


class InputHandler(object):
    
    def TalkBack(self):
        while True:
        
            hear = raw_input("PCE ~ > ")
            print hear

    def CipherSpawner(self, cipher):
        
        if cipher == "AES":
            
            import CipherAES
            cipherObj = AESRoutine()
            
            return cipherObj
            
        elif cipher == "CAMELLIA":
            
            import CipherCamellia
            cipherObj = CamelliaRoutine()
            
            return cipherObj
        
        elif cipher == "TRIPLEDES" or cipher == "DESX3":
            
            import CipherTripleDES
            cipherObj = TripleDESRoutine()
            
            return cipherObj
        
        
        
    def Listener(self):
        
        while True:
        
            userInput = raw_input("PCE ~ > ")
            
            userInputUpper = userInput.Upper()
            
            if "AES" in userInputUpper:
                
                self.CipherSpawner("AES")
                
                
            
                
                
    
# perhaps make this leaner by passing the cipher as an argument instead
# of having 10000 files

# BUGS:
#   have ciphertype so only one file
#    must be a multiple of 16 unless stream cryptography has padding class
# Use bytes
from SE:
my_str = "hello world"
bytes = str.encode(my_str)
type(bytes) # insures its bytes
my_decoded_str = str.decode(bytes)
type(my_decoded_str) # insures its string