# Convert characters to emojis
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

import re

class EmojiCrypt:
	def __init__(self):
		self.emoji_list = ["🍎", "🍌","🏎", "🚪", "👁", "👣", "😀", "🖐", "ℹ", "😂", "🥋", "✉", "🚹", "🌉", "👌", "🍍", "👑", "👉", "🎤", "🚰", "☂", "🐍", "💧", "✖", "☀", "🦓", "🏹", "🎈", "😎", "🎅", "🐘", "🌿", "🌏", "🌪", "☃", "🍵", "🍴", "🚨", "📮", "🕹", "📂", "🛩", "⌨", "🔄", "🔬", "🐅", "🙃", "🐎", "🌊", "🚫", "❓", "⏩", "😁", "😆", "💵", "🤣", "☺", "😊", "😇", "😡", "🎃", "😍", "✅", "🔪", "🗒"]
		# self.emoji_list = [u"\U0001F609", add custom & random......]
		# self.shift = shift # Cyclic shift, maybe ROT13

	def encrypt(self, txt):
		txt = re.sub("[aA]", self.emoji_list[0], txt)
		txt = re.sub("[bB]", self.emoji_list[1], txt)
		txt = re.sub("[cC]", self.emoji_list[2], txt)
		txt = re.sub("[dD]", self.emoji_list[3], txt)
		txt = re.sub("[eE]", self.emoji_list[4], txt)

		txt = re.sub("[fF]", self.emoji_list[5], txt)
		txt = re.sub("[gG]", self.emoji_list[6], txt)
		txt = re.sub("[hH]", self.emoji_list[7], txt)
		txt = re.sub("[iI]", self.emoji_list[8], txt)
		txt = re.sub("[jJ]", self.emoji_list[9], txt)

		txt = re.sub("[kK]", self.emoji_list[10], txt)
		txt = re.sub("[lL]", self.emoji_list[11], txt)
		txt = re.sub("[mM]", self.emoji_list[12], txt)
		txt = re.sub("[nN]", self.emoji_list[13], txt)
		txt = re.sub("[oO]", self.emoji_list[14], txt)

		txt = re.sub("[pP]", self.emoji_list[15], txt)
		txt = re.sub("[qQ]", self.emoji_list[16], txt)
		txt = re.sub("[rR]", self.emoji_list[17], txt)
		txt = re.sub("[sS]", self.emoji_list[18], txt)
		txt = re.sub("[tT]", self.emoji_list[19], txt)

		txt = re.sub("[uU]", self.emoji_list[20], txt)
		txt = re.sub("[vV]", self.emoji_list[21], txt)
		txt = re.sub("[wW]", self.emoji_list[22], txt)
		txt = re.sub("[xX]", self.emoji_list[23], txt)
		txt = re.sub("[yY]", self.emoji_list[24], txt)

		txt = re.sub("[zZ]", self.emoji_list[25], txt)
		return txt

	def decrypt(self, txt):
		txt = re.sub(self.emoji_list[0], "A", txt)
		txt = re.sub(self.emoji_list[1], "B", txt)
		txt = re.sub(self.emoji_list[2], "C", txt)
		txt = re.sub(self.emoji_list[3], "D", txt)
		txt = re.sub(self.emoji_list[4], "E", txt)

		txt = re.sub(self.emoji_list[5], "F", txt)
		txt = re.sub(self.emoji_list[6], "G", txt)
		txt = re.sub(self.emoji_list[7], "H", txt)
		txt = re.sub(self.emoji_list[8], "I", txt)
		txt = re.sub(self.emoji_list[9], "J", txt)

		txt = re.sub(self.emoji_list[10], "K", txt)
		txt = re.sub(self.emoji_list[11], "L", txt)
		txt = re.sub(self.emoji_list[12], "M", txt)
		txt = re.sub(self.emoji_list[13], "N", txt)
		txt = re.sub(self.emoji_list[14], "O", txt)

		txt = re.sub(self.emoji_list[15], "P", txt)
		txt = re.sub(self.emoji_list[16], "Q", txt)
		txt = re.sub(self.emoji_list[17], "R", txt)
		txt = re.sub(self.emoji_list[18], "S", txt)
		txt = re.sub(self.emoji_list[19], "T", txt)

		txt = re.sub(self.emoji_list[20], "U", txt)
		txt = re.sub(self.emoji_list[21], "V", txt)
		txt = re.sub(self.emoji_list[22], "W", txt)
		txt = re.sub(self.emoji_list[23], "X", txt)
		txt = re.sub(self.emoji_list[24], "Y", txt)

		txt = re.sub(self.emoji_list[25], "Z", txt)
		return txt


if __name__ == '__main__':
	cipher = EmojiCrypt()
	print(cipher.encrypt("abcdefghijklmnopqrstuvwxyz"))
	print(cipher.decrypt("🍎🍌🏎🚪👁👣😀🖐ℹ😂🥋✉🚹🌉👌🍍👑👉🎤🚰☂🐍💧✖☀🦓"))
