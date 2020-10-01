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
		self.keyword =  keyword
		self.shift_emoji_list()

	def shift_emoji_list(self):
		shift = len(self.keyword)
		self.emoji_list = self.emoji_list[shift: len(self.emoji_list)] + self.emoji_list[0:shift]

	def decrypt(self, txt):
		return emojify.decode(txt, self.emoji_list)

	def encrypt(self, txt):
		return emojify.encode(txt, self.emoji_list)

	def unit_test(self, test_txt="This is a test text: ABC abc 123 !@#"):
		print(cipher.encrypt(test_txt))
		print(cipher.decrypt(cipher.encrypt(test_txt)))

# ------------------------------------------------------------------------------
if __name__ == '__main__':
	cipher = EmojiCrypt("cool")
	# cipher.unit_test()

	parser = argparse.ArgumentParser(description="Emoji Cipher")
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-e', type=str, help="encrypt")
	group.add_argument('-d', type=str, help="decrypt")
	args = parser.parse_args()

	if args.e:
		print(cipher.encrypt(args.e))
	
	if args.d:
		print(cipher.decrypt(args.d))

# ------------------------------------------------------------------------------
# EOF