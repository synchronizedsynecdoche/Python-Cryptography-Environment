
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend


class CryptoRoutine(object):

    def __init__(self,choice):

        self.choice = choice.upper
        self.KEY = ''
        self.backend = ''
        self.cipherMode = ''
        self.initVector = ''
        self.nonce = ''
        self.mode = ''
        self.backend = default_backend()
        self.plaintext = ''
        self.ciphertext = ''

    # retrieve needed variables
    #unused variables can safely be set to None

    #checking that these variables are correct size will happen elsewhere

    def staging(self, key, xmode, iv, nonceVal):

        self.KEY = str.encode(key)

        xmode = xmode.upper

        if xmode == "CBC":

            self.initVector = iv
            self.cipherMode = modes.CBC(self.initVector)

        elif xmode == "CTR":

            self.nonce = nonceVal

            self.cipherMode = modes.CTR(self.nonce)

        # OFB does not require Padding
        elif xmode == "OFB":

            self.initVector = iv

            self.cipherMode = modes.OFB(self.initVector)

        elif xmode == "CFB":

            self.cipherMode = modes.CFB

        elif xmode == "GCM":

            print "Coming soon!"
            exit(0)

        else:

            print "Invalid mode \"{}\"".format(xmode)
            exit(1)

    def Encrypt(self, message):

        if self.choice == "AES":
            messageBytes = str.encode(message)
        
            cipherInstance = Cipher(algorithms.AES(self.KEY),self.mode, backend=self.backend)

            cryptorInstance = cipherInstance.encryptor()

            ciphertext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()
            print ciphertext
            return ciphertext

        if self.choice == "CAMELLIA":
            messageBytes = str.encode(message)

            cipherInstance = Cipher(algorithms.Camellia(self.KEY), self.mode, backend=self.backend)

            cryptorInstance = cipherInstance.encryptor()

            ciphertext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()
            print ciphertext
            return ciphertext

        if "DES" in self.choice:
            messageBytes = str.encode(message)

            cipherInstance = Cipher(algorithms.TripleDES(self.KEY), self.mode, backend=self.backend)

            cryptorInstance = cipherInstance.encryptor()

            ciphertext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()
            print ciphertext
            return ciphertext
                        # are keys needed? they;re global and set using the staging func

    def Decrypt(self, ciphertextBytes):

        if self.choice == "AES":
            messageBytes = str.encode(message)

            cipherInstance = Cipher(algorithms.AES(self.KEY), self.mode, backend=self.backend)

            cryptorInstance = cipherInstance.decryptor()

            plaintext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()
            print plaintext
            return plaintext

        if self.choice == "CAMELLIA":
            messageBytes = str.encode(message)

            cipherInstance = Cipher(algorithms.Camellia(self.KEY), self.mode, backend=self.backend)

            cryptorInstance = cipherInstance.decryptor()

            plaintext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()
            print plaintext
            return plaintext

        if "DES" in self.choice:
            messageBytes = str.encode(message)

            cipherInstance = Cipher(algorithms.TripleDES(self.KEY), self.mode, backend=self.backend)

            cryptorInstance = cipherInstance.decryptor()

            plaintext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()
            print plaintext
            return plaintext




