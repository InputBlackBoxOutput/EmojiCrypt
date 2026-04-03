# Convert characters to emojis
# �🏴✉����������🙃���������🎤�����👌������🚫��
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

# ------------------------------------------------------------------------------

from .aes import AESCipher
from .vigeneres import VigeneresCipher
from . import CHARACTERS, EMOJI_LIST

import re

class EmojiCrypt:
    def __init__(self, keyword):
        self._CHARACTERS = CHARACTERS.copy()

        self.keyword = self.sanitize(keyword)

        self._EMOJI_LIST = EMOJI_LIST.copy()
        self._EMOJI_LIST = (
            self._EMOJI_LIST[len(self.keyword) :]
            + self._EMOJI_LIST[0 : len(self.keyword)]
        )

        self.aes = AESCipher(self.keyword)
        self.vc = VigeneresCipher(self.keyword)

    # Sanitize input keyword by removing characters not in the character set
    def sanitize(self, keyword):
        sanitized = ""
        for char in keyword:
            if char in self._CHARACTERS:
                sanitized += char

        return sanitized

    # Replace all characters with their emojis
    def emojify(self, txt):
        map = dict(zip(self._CHARACTERS, self._EMOJI_LIST))

        for char, emoji in map.items():
            txt = re.sub(re.escape(char), emoji, txt)

        return txt

    # Replace all emojis with their characters
    def demojify(self, txt):
        map = dict(zip(self._EMOJI_LIST, self._CHARACTERS))

        for emoji, char in map.items():
            repl = char.replace("\\", "\\\\")
            txt = re.sub(re.escape(emoji), repl, txt)

        return txt

    def encrypt(self, inpt, encrption="aes"):
        if encrption == "aes":
            encrypted = self.aes.encrypt(inpt)
            encoded = self.emojify(encrypted)
        elif encrption == "vc":
            encrypted = self.vc.encrypt(inpt)
            encoded = self.emojify(encrypted)
        else:
            raise ValueError("Invalid encryption method specified. Use 'aes' or 'vc'.")

        return encoded

    def decrypt(self, inpt, encrption="aes"):
        if encrption == "aes":
            decoded = self.demojify(inpt)
            decrypted = self.aes.decrypt(decoded)
        elif encrption == "vc":
            decoded = self.demojify(inpt)
            decrypted = self.vc.decrypt(decoded)
        else:
            raise ValueError("Invalid decryption method specified. Use 'aes' or 'vc'.")

        return decrypted

    def fileio(self, filepath, operation):
        try:
            with open(filepath["input"], "r") as file:
                lines = file.readlines()

            with open(filepath["output"], "w") as file:
                if operation == "encrypt":
                    for line in lines:
                        file.write(self.encrypt(line, "vc"))
                elif operation == "decrypt":
                    for line in lines:
                        file.write(self.decrypt(line, "vc"))
                else:
                    raise ValueError(
                        "Invalid operation specified. Use 'encrypt' or 'decrypt'."
                    )

        except FileNotFoundError:
            print(f"File not found: {filepath['input']}")

        except Exception as e:
            print(f"Something went wrong while processing the file: {e}")
