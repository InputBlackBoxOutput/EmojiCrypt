# Convert characters to emojis
# �🏴✉����������🙃���������🎤�����👌������🚫��
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

# ------------------------------------------------------------------------------

from Crypto.Cipher import AES
from Crypto import Random

import hashlib
import base64
import argparse, sys
import re

EMOJI_LIST = "🍎 🍌 🏎 🚪 👁 👣 😀 🖐 ℹ 😂 🥋 ✉ 🚹 🌉 👌 🍍 👑 👉 🎤 🚰 ☂ 🐍 💧 ✖ ☀ 🦓 🏹 🎈 😎 🎅 🐘 🌿 🌏 🌪 ☃ 🍵 🍴 🚨 📮 🕹 📂 🛩 ⌨ 🔄 🔬 🐅 🙃 🐎 🌊 🚫 ❓ ⏩ 😁 😆 💵 🤣 ☺ 😊 😇 😡 🎃 😍 ✅ 🔪 🗒 🤾 👶 🤞 🎳 🙊 🗝 🚋 👢 🍦 🕊 🏕 😧 🏴 🍗 🙄 🚉 🎣 📲 🧐 🛎 🐼 🙄 🎻 🐠 🥠 🏄 🗜 😋".split(" ")
CHARACTERS = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! \" # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~".split(" ")

# ------------------------------------------------------------------------------
class EmojiCrypt:
    def __init__(self, keyword):
        self._CHARACTERS = CHARACTERS.copy()

        self.keyword = self.sanitize(keyword)

        self._EMOJI_LIST = EMOJI_LIST.copy()
        self._EMOJI_LIST = self._EMOJI_LIST[len(self.keyword):] + self._EMOJI_LIST[0:len(self.keyword)]

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
            repl = char.replace('\\', '\\\\')
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


class VigeneresCipher:
    def __init__(self, keyword):
        self.keyword = keyword
        self.characters = CHARACTERS.copy()
        self.square = self.generate_square()

    def generate_square(self):
        square = []
        for i in range(len(self.characters)):
            square.append(self.characters[i:] + self.characters[0:i])

        return square

    def decrypt(self, txt):
        it = 0
        loc = 0
        out = ""

        for char in txt:
            if char in self.characters:
                loc = self.characters.index(self.keyword[it])
                it += 1

                if it >= len(self.keyword):
                    it = 0

                out += self.characters[self.square[loc].index(char)]
            else:
                out += char

        return out

    def encrypt(self, txt):
        out = ""
        it = 0

        for char in txt:
            if char in self.characters:
                out += self.square[self.characters.index(self.keyword[it])][
                    self.characters.index(char)
                ]
                it += 1

                if it >= len(self.keyword):
                    it = 0
            else:
                out += char

        return out


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
            sys.exit()

    # Padding required for GCM and CBC modes (Not used)
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[: -ord(s[len(s) - 1 :])]


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Emoji Cipher")
    parser.add_argument("-k", type=str, help="Keyword used for AES encryption and Vigenere cipher")
    parser.add_argument("-vc", action="store_true", help="Use Vigenere cipher instead of AES")

    parser.add_argument("-e", nargs='?', const=True, default=False,
                        help="Encrypt the specified string, or use as a flag with -i for file input")
    parser.add_argument("-d", nargs='?', const=True, default=False,
                        help="Decrypt the specified string, or use as a flag with -i for file input")

    parser.add_argument("-i", type=str, help="Input file for encryption/decryption")
    parser.add_argument("-o", type=str, help="Output file for encryption/decryption [Default: encrypted.txt or decrypted.txt]")

    args = parser.parse_args()

    if args.k:
        cipher = EmojiCrypt(args.k)
    else:
        print("Please specify keyword using the -k option")
        sys.exit()

    if args.e and args.d:
        print("Please specify either encryption or decryption operation")
        sys.exit()

    if args.i:
        if args.e:
            operation = "encrypt"
            output = "encrypted.txt"
        elif args.d:
            operation = "decrypt"
            output = "decrypted.txt"
        else:
            print("Please specify -e or -d when using -i")
            sys.exit()

        filepath = {
            "input": args.i,
            "output": args.o if args.o else output
        }

        cipher.fileio(filepath, operation)
        print("Done")
        sys.exit()

    if args.e:
        if args.e is True:
            print("Please provide text to encrypt with -e when not using -i")
            sys.exit()
        print(cipher.encrypt(args.e, "vc" if args.vc else "aes"))
        sys.exit()

    if args.d:
        if args.d is True:
            print("Please provide text to decrypt with -d when not using -i")
            sys.exit()
        print(cipher.decrypt(args.d, "vc" if args.vc else "aes"))
        sys.exit()

    print("Please specify an operation (-e or -d), and optional -i for file processing")
    sys.exit()

# ------------------------------------------------------------------------------
# EOF
