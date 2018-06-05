
import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend

backend = default_backend()

random = os.urandom(16)
iv = os.urandom(16)
mode = modes.OFB(iv)
def EncryptionRoutine(message):
    
    messageBytes = str.encode(message)
    
    cipherInstance = Cipher(algorithms.AES(random),mode, backend=backend)
    cryptorInstance = cipherInstance.encryptor()
    ciphertext = cryptorInstance.update(messageBytes) + cryptorInstance.finalize()

    return ciphertext
    
def DecryptionRoutine(x):
    
    
    cipherInstance = Cipher(algorithms.AES(random),mode, backend = backend)
    decryptorInstance = cipherInstance.decryptor()
    plaintext = decryptorInstance.update(x) + decryptorInstance.finalize()

    return plaintext


# see similarities in the ciphertext? That's because OFB is a stream mode and the string is the same in the beginning!
DecryptionRoutine(EncryptionRoutine(b"the quick brown fox jumped over the lazy log"))
DecryptionRoutine(EncryptionRoutine(b"the quick brown fox jumped over the lazy log."))


