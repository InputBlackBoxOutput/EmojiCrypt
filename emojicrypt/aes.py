from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64

class AESCipher:

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        # raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        enc = base64.b64encode(iv + cipher.encrypt(raw.encode()))
        return str(enc)[2:-1]

    def decrypt(self, strg):
        try:
            enc = bytes(strg, "utf8")
            enc = base64.b64decode(enc)
            iv = enc[: AES.block_size]
            cipher = AES.new(self.key, AES.MODE_CFB, iv)
            return cipher.decrypt(enc[AES.block_size :]).decode("utf-8")
        except:
            print(
                "\nLooks like the entered cipher text is invalid or the keyword is wrong!"
            )
            import sys

            sys.exit()

    # Padding required for GCM and CBC modes (Not used)
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[: -ord(s[len(s) - 1 :])]
