# Convert characters to emojis
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

# ------------------------------------------------------------------------------
import emojify

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


# ------------------------------------------------------------------------------
if __name__ == '__main__':
	cipher = EmojiCrypt("cool")
	test_txt = "aAbBcC 190 #$%"

	print(cipher.encrypt(test_txt))
	print(cipher.decrypt(cipher.encrypt(test_txt)))

# ------------------------------------------------------------------------------
# EOF