from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

backend = default_backend()


class SHAFamily(object):

    def sha1(self, message):

        print("WARN: SHA1 is not recommended, use SHA[224,256,384,512] instead!")

        hasher = hashes.Hash(hashes.SHA1(), backend=backend)
        hasher.update(message)
        hasher.finalize()

    def sha224(self, message):

        hasher = hashes.Hash(hashes.SHA224(), backend=backend)
        hasher.update(message)
        hasher.finalize()

    def sha256(self, message):

        hasher = hashes.Hash(hashes.SHA256(), backend=backend)
        hasher.update(message)
        hasher.finalize()

    def sha384(self, message):

        hasher = hashes.Hash(hashes.SHA384(), backend=backend)
        hasher.update(message)
        hasher.finalize()

    def sha512(self, message):

        hasher = hashes.Hash(hashes.SHA512(), backend=backend)
        hasher.update(message)
        hasher.finalize()
