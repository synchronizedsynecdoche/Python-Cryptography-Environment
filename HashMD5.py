from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

backend = default_backend()
class MD5(object):

    def hash(self, message):

        print("WARN: MD5 has known collision attacks (see FLAME malware forgery)")
        hasher = hashes.Hash(hashes.MD5(), backend=backend)
        hasher.update(message)
        hasher.finalize

