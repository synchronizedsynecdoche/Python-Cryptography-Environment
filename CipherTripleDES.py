
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

        DESx3KEY = str.encode(key)

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
        cipherInstance = Cipher(algorithms.TripleDES(DESx3KEY),cipherMode, backend = backend)

        cryptorInstance = cipherInstance.encryptor()


        ciphertext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()

        return ciphertext
                        # are keys needed? they;re global
    def DecryptionRoutine(self, ciphertextBytes):

         cipherInstance = Cipher(algorithms.TripleDES(DESx3KEY),cipherMode, backend = backend)

         decryptorInstance = cipherInstance.decryptor()

         plaintext = decryptorInstance.update(ciphertextBytes) + decryptorInstance.finalize()

         return plaintext







