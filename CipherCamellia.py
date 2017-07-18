
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

        CAMELLIAKEY = str.encode(key)

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

        messageBytes = str.encode(message)
        
        cipherInstance = Cipher(algorithms.Camellia(CAMELLIAKEY),cipherMode, backend = backend)

        cryptorInstance = cipherInstance.encryptor()

                                            #this is weird
        ciphertext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()

        return ciphertext

    def DecryptionRoutine(self, ciphertextBytes):
        
         
         cipherInstance = Cipher(algorithms.Camellia(CAMELLIAKEY),cipherMode, backend = backend)

         decryptorInstance = cipherInstance.decryptor()

         plaintext = decryptorInstance.update(ciphertextBytes) + decryptorInstance.finalize()

         return plaintext
