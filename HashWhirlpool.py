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
