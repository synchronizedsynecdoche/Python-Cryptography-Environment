from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

backend = default_backend()
class RIPEMD(object):

    def RIPEMD160(self, message):

        hasher = hashes.Hash(hashes.RIPEMD160(), backend=backend)

        hasher.update(message)

        hasher.finalize

testObj = RIPEMD()
testObj.RIPEMD160("test")
