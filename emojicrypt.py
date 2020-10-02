# Convert characters to emojis
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

# ------------------------------------------------------------------------------
import emojify
import argparse, sys

# ------------------------------------------------------------------------------
class EmojiCrypt:
	def __init__(self, keyword):
		self.emoji_list = ["🍎", "🍌","🏎", "🚪", "👁", "👣", "😀", "🖐", "ℹ", "😂", "🥋", "✉", "🚹", "🌉", "👌", "🍍", "👑", "👉", "🎤", "🚰", "☂", "🐍", "💧", "✖", "☀", "🦓", "🏹", "🎈", "😎", "🎅", "🐘", "🌿", "🌏", "🌪", "☃", "🍵", "🍴", "🚨", "📮", "🕹", "📂", "🛩", "⌨", "🔄", "🔬", "🐅", "🙃", "🐎", "🌊", "🚫", "❓", "⏩", "😁", "😆", "💵", "🤣", "☺", "😊", "😇", "😡", "🎃", "😍", "✅", "🔪", "🗒", "🤾", "👶", "🤞", "🎳", "🙊", "🗝", "🚋", "👢", "🍦", "🕊", "🏕", "😧", "🏴", "🍗", "🙄", "🚉", "🎣", "📲", "🧐", "🛎", "🐼", "🙄", "🎻", "🐠", "🥠", "🏄", "🗜", "😋"]
		self.characters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! \" # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~".split(" ")

		self.keyword =  self.sanitize(keyword)
		self.shift_emoji_list()
		self.square = self.create_square()

	def shift_emoji_list(self):
		shift = len(self.keyword)
		self.emoji_list = self.emoji_list[shift:] + self.emoji_list[0:shift]

	def sanitize(self, keyword):
		out = ""
		for char in keyword:
			if char in self.characters:
				out += char

		return out

	def create_square(self):
		square = []
		for i in range(len(self.characters)):
			square.append(self.characters[i:] + self.characters[0:i])

		return square

	def decrypt(self, txt):
		txt = emojify.decode(txt, self.emoji_list)
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
				out += self.square[self.characters.index(self.keyword[it])][self.characters.index(char)];
				it += 1

				if it >= len(self.keyword):
					it = 0
			else:
				out += char

		# return out
		return emojify.encode(out, self.emoji_list)

	def unit_test(self, test_txt="ABC abc 123 !@#"):
		print(self.encrypt(test_txt))
		print(self.decrypt(self.encrypt(test_txt)))

# ------------------------------------------------------------------------------
if __name__ == '__main__':
	# parser = argparse.ArgumentParser(description="Emoji Cipher")
	# parser.add_argument('-k', type=str, help="keyword")
	# group = parser.add_mutually_exclusive_group(required=True)
	# group.add_argument('-e', type=str, help="encrypt")
	# group.add_argument('-d', type=str, help="decrypt")
	# group.add_argument('-ef', type=str, help="encrypt file")
	# group.add_argument('-df', type=str, help="decrypt file")
	# args = parser.parse_args()

	# cipher = EmojiCrypt(args.k)
	# # cipher.unit_test()

	# if args.e:
	# 	print(cipher.encrypt(args.e))
	
	# elif args.d:
	# 	print(cipher.decrypt(args.d))

	# elif args.ef:
	# 	print("Encrypting file....", end="")
	# 	cipher.encrypt_file(args.ef)
	# 	print("Done")

	# elif args.ef:
	# 	print("Decrypting file....", end="")
	# 	cipher.decrypt_files(args.df)
	# 	print("Done")

	cipher = EmojiCrypt("Cool")
	cipher.unit_test()

# ------------------------------------------------------------------------------
# EOF