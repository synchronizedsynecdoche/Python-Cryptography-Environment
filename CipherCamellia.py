
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend

class CamelliaRoutine(object):


    backend = default_backend()
    # retrieve needed variables
    # unused variables can safely be set to None
    # checking that these variables are correct size will happen elsewhere
    
    def staging(self, key, mode, iv, nonceVal):

        global cipherMode
        global initVector
        global nonce
        global ciphertext
        global plaintext
        global CAMELLIAKEY

        CAMELLIAKEY = str.encode(key)


        if mode.upper == "CBC":

            initVector = iv
            cipherMode = modes.CBC(initVector)

        elif mode.upper == "CTR":

            nonce = nonceVal
            cipherMode = modes.CTR(nonce)

        # OFB does not require Padding
        elif mode.upper == "OFB":

            initVector = iv
            cipherMode = modes.OFB(initVector)

        elif mode.upper == "CFB":

            cipherMode = modes.CFB

        elif mode.upper == "GCM":

            print("Coming soon!")
            exit(0)

        else:

            print("Invalid mode")
            exit(1)

    def EncryptionRoutine(self, message):

        messageBytes = str.encode(message)
        
        cipherInstance = Cipher(algorithms.Camellia(CAMELLIAKEY),cipherMode, backend=self.backend)
        cryptorInstance = cipherInstance.encryptor()
        ciphertext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()

        return ciphertext

    def DecryptionRoutine(self, ciphertext):

         ciphertextBytes = str.encode(ciphertext
                                     )
         cipherInstance = Cipher(algorithms.Camellia(CAMELLIAKEY),cipherMode, backend=self.backend)
         decryptorInstance = cipherInstance.decryptor()
         plaintext = decryptorInstance.update(ciphertextBytes) + decryptorInstance.finalize()

         return plaintext
