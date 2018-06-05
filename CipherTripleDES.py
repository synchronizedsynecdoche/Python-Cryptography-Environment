
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend

class TripleDESRoutine(object):


   global backend
   backend = default_backend()

    def staging(self, key, mode, iv, nonceVal):

        global DESx3KEY
        global cipherMode
        global initVector
        global nonce

        DESx3KEY = str.encode(key)


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
        cipherInstance = Cipher(algorithms.TripleDES(DESx3KEY),cipherMode, backend=backend)

        cryptorInstance = cipherInstance.encryptor()


        ciphertext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()

        return ciphertext
                        # are keys needed? they;re global

    def DecryptionRoutine(self, ciphertextBytes):

        cipherInstance = Cipher(algorithms.TripleDES(DESx3KEY),cipherMode, backend=backend)
        decryptorInstance = cipherInstance.decryptor()
        plaintext = decryptorInstance.update(ciphertextBytes) + decryptorInstance.finalize()

        return plaintext







