# Convert characters to emojis
# �🏴✉����������🙃���������🎤�����👌������🚫��
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

# ------------------------------------------------------------------------------
import emojify

from Crypto.Cipher import AES
from Crypto import Random

import hashlib
import base64
import argparse, sys

# ------------------------------------------------------------------------------
class EmojiCrypt:
	def __init__(self, keyword):
		self.emoji_list = ["🍎", "🍌", "🏎", "🚪", "👁", "👣", "😀", "🖐", "ℹ", "😂", "🥋", "✉", "🚹", "🌉", "👌", "🍍", "👑", "👉", "🎤", "🚰", "☂", "🐍", "💧", "✖", "☀", "🦓", "🏹", "🎈", "😎", "🎅", "🐘", "🌿", "🌏", "🌪", "☃", "🍵", "🍴", "🚨", "📮", "🕹", "📂", "🛩", "⌨", "🔄", "🔬", "🐅", "🙃", "🐎", "🌊", "🚫", "❓", "⏩", "😁", "😆", "💵", "🤣", "☺", "😊", "😇", "😡", "🎃", "😍", "✅", "🔪", "🗒", "🤾", "👶", "🤞", "🎳", "🙊", "🗝", "🚋", "👢", "🍦", "🕊", "🏕", "😧", "🏴", "🍗", "🙄", "🚉", "🎣", "📲", "🧐", "🛎", "🐼", "🙄", "🎻", "🐠", "🥠", "🏄", "🗜", "😋"]
		self.characters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! \" # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~".split(" ")

		self.keyword =  self.sanitize(keyword)
		self.shift_emoji_list()

		self.aes = AESCipher(self.keyword)
		self.vc = VigeneresCipher(self.keyword)

	def shift_emoji_list(self):
		shift = len(self.keyword)
		self.emoji_list = self.emoji_list[shift:] + self.emoji_list[0:shift]

	def sanitize(self, keyword):
		out = ""
		for char in keyword:
			if char in self.characters:
				out += char

		return out

	def encrypt(self, inpt):
		return emojify.encode(self.aes.encrypt(inpt), self.emoji_list)

	def decrypt(self, inpt):
		return self.aes.decrypt(emojify.decode(inpt, self.emoji_list))


	def encrypt_vc(self, inpt):
		# print(self.vc.encrypt(inpt))
		return emojify.encode(self.vc.encrypt(inpt), self.emoji_list)

	def decrypt_vc(self, inpt):
		# print(emojify.decode(inpt, self.emoji_list))
		return self.vc.decrypt(emojify.decode(inpt, self.emoji_list))


	def decrypt_file(self, filepath):
		try:
			with open(filepath, 'r') as file:
				lines = file.readlines()	
			file.close()

			with open(filepath, 'w') as file:
				lines = map(self.decrypt_vc, lines)
				for each in list(lines):
					file.write(each)
		
		except FileNotFoundError:
			print(f"File not found: {filepath}")
		
		except:
			print("Something went wrong while decrypting the file")

	def encrypt_file(self, filepath):
		try:
			with open(filepath, 'r') as file:
				lines = file.readlines()
			file.close()

			with open(filepath, 'w') as file:
				lines = map(self.encrypt_vc, lines)
				for each in list(lines):
					file.write(each)
		
		except FileNotFoundError:
			print(f"File not found: {filepath}")
		
		except:
			print("Something went wrong while encrypting the file")

	def unit_test(self, test_txt="ABC abc 123 !@#"):
		print(self.encrypt(test_txt))
		print(self.decrypt(self.encrypt(test_txt)))

		print(emojify.encode(test_txt, self.emoji_list))
		print(emojify.decode(emojify.encode(test_txt, self.emoji_list), self.emoji_list))

	def unit_test_file(self):
		self.encrypt_file("test/text.txt")
		self.decrypt_file("test/encrypted.txt")

class VigeneresCipher:
	def __init__(self, keyword):
		self.keyword = keyword
		self.characters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! \" # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~".split(" ")
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
				out += self.square[self.characters.index(self.keyword[it])][self.characters.index(char)]
				it += 1

				if it >= len(self.keyword):
					it = 0
			else:
				out += char

		return out

	def unit_test(self, test = "ABCabc123(]!"):
		print(self.encrypt(test))
		print(self.decrypt(self.encrypt(test)))

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
		enc = bytes(strg, 'utf8')
		enc = base64.b64decode(enc)
		iv = enc[:AES.block_size]
		cipher = AES.new(self.key, AES.MODE_CFB, iv)
		return cipher.decrypt(enc[AES.block_size:]).decode('utf-8')
		# return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

	# Padding required for GCM and CBC modes (Not used)
	def _pad(self, s):
		return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

	@staticmethod
	def _unpad(s):
		return s[:-ord(s[len(s)-1:])]
		
	def unit_test(self):
		test = "ABCabc123(]!"  
		print(self.encrypt(test))
		print(self.decrypt(self.encrypt(test)))

# ------------------------------------------------------------------------------
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Emoji Cipher")
	parser.add_argument('-k', type=str, help="keyword")
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-e', type=str, help="encrypt")
	group.add_argument('-d', type=str, help="decrypt")
	group.add_argument('-ef', type=str, help="encrypt file")
	group.add_argument('-df', type=str, help="decrypt file")
	args = parser.parse_args()

	if args.k:
		cipher = EmojiCrypt(args.k)
		# cipher.unit_test()

	else:
		print("Please specify keyword using the -k option")
		sys.exit()

	if args.e:
		print(cipher.encrypt_vc(args.e))
	
	elif args.d:
		print(cipher.decrypt_vc(args.d))

	elif args.ef:
		print("Encrypting file....", end="")
		cipher.encrypt_file(args.ef)
		print("Done")

	elif args.df:
		print("Decrypting file....", end="")
		cipher.decrypt_file(args.df)
		print("Done")

# ------------------------------------------------------------------------------
# EOF
