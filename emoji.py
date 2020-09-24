# Convert characters to emojis
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

import re
 
class EmojiCrypt:
	def __init__(self):
		self.emoji_alpha = ["🍎", "🍌","🏎", "🚪", "👁", "👣", "😀", "🖐", "ℹ", "😂", "🥋", "✉", "🚹", "🌉", "👌", "🍍", "👑", "👉", "🎤", "🚰", "☂", "🐍", "💧", "✖", "☀", "🦓", "🏹", "🎈", "😎", "🎅", "🐘", "🌿", "🌏", "🌪", "☃", "🍵", "🍴", "🚨", "📮", "🕹", "📂", "🛩", "⌨", "🔄", "🔬", "🐅", "🙃", "🐎", "🌊", "🚫", "❓", "⏩", "😁", "😆", "💵", "🤣", "☺", "😊", "😇", "😡", "🎃", "😍", "✅", "🔪", "🗒"]
		self.emoji_digit = ["❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾", "⓿"]

		# self.emoji_alpha = [u"\U0001F609", add custom & random......]
		# self.shift = shift # Cyclic shift, maybe ROT13

	def encrypt(self, txt):
		# Alphabets
		txt = re.sub("[aA]", self.emoji_alpha[0], txt)
		txt = re.sub("[bB]", self.emoji_alpha[1], txt)
		txt = re.sub("[cC]", self.emoji_alpha[2], txt)
		txt = re.sub("[dD]", self.emoji_alpha[3], txt)
		txt = re.sub("[eE]", self.emoji_alpha[4], txt)

		txt = re.sub("[fF]", self.emoji_alpha[5], txt)
		txt = re.sub("[gG]", self.emoji_alpha[6], txt)
		txt = re.sub("[hH]", self.emoji_alpha[7], txt)
		txt = re.sub("[iI]", self.emoji_alpha[8], txt)
		txt = re.sub("[jJ]", self.emoji_alpha[9], txt)

		txt = re.sub("[kK]", self.emoji_alpha[10], txt)
		txt = re.sub("[lL]", self.emoji_alpha[11], txt)
		txt = re.sub("[mM]", self.emoji_alpha[12], txt)
		txt = re.sub("[nN]", self.emoji_alpha[13], txt)
		txt = re.sub("[oO]", self.emoji_alpha[14], txt)

		txt = re.sub("[pP]", self.emoji_alpha[15], txt)
		txt = re.sub("[qQ]", self.emoji_alpha[16], txt)
		txt = re.sub("[rR]", self.emoji_alpha[17], txt)
		txt = re.sub("[sS]", self.emoji_alpha[18], txt)
		txt = re.sub("[tT]", self.emoji_alpha[19], txt)

		txt = re.sub("[uU]", self.emoji_alpha[20], txt)
		txt = re.sub("[vV]", self.emoji_alpha[21], txt)
		txt = re.sub("[wW]", self.emoji_alpha[22], txt)
		txt = re.sub("[xX]", self.emoji_alpha[23], txt)
		txt = re.sub("[yY]", self.emoji_alpha[24], txt)

		txt = re.sub("[zZ]", self.emoji_alpha[25], txt)

		# Digits
		txt = re.sub("1", self.emoji_digit[0], txt)
		txt = re.sub("2", self.emoji_digit[1], txt)
		txt = re.sub("3", self.emoji_digit[2], txt)
		txt = re.sub("4", self.emoji_digit[3], txt)
		txt = re.sub("5", self.emoji_digit[4], txt)
		txt = re.sub("6", self.emoji_digit[5], txt)
		txt = re.sub("7", self.emoji_digit[6], txt)
		txt = re.sub("8", self.emoji_digit[7], txt)
		txt = re.sub("9", self.emoji_digit[8], txt)
		txt = re.sub("0", self.emoji_digit[9], txt)

		return txt

	def decrypt(self, txt):
		# Alphabets
		txt = re.sub(self.emoji_alpha[0], "A", txt)
		txt = re.sub(self.emoji_alpha[1], "B", txt)
		txt = re.sub(self.emoji_alpha[2], "C", txt)
		txt = re.sub(self.emoji_alpha[3], "D", txt)
		txt = re.sub(self.emoji_alpha[4], "E", txt)

		txt = re.sub(self.emoji_alpha[5], "F", txt)
		txt = re.sub(self.emoji_alpha[6], "G", txt)
		txt = re.sub(self.emoji_alpha[7], "H", txt)
		txt = re.sub(self.emoji_alpha[8], "I", txt)
		txt = re.sub(self.emoji_alpha[9], "J", txt)

		txt = re.sub(self.emoji_alpha[10], "K", txt)
		txt = re.sub(self.emoji_alpha[11], "L", txt)
		txt = re.sub(self.emoji_alpha[12], "M", txt)
		txt = re.sub(self.emoji_alpha[13], "N", txt)
		txt = re.sub(self.emoji_alpha[14], "O", txt)

		txt = re.sub(self.emoji_alpha[15], "P", txt)
		txt = re.sub(self.emoji_alpha[16], "Q", txt)
		txt = re.sub(self.emoji_alpha[17], "R", txt)
		txt = re.sub(self.emoji_alpha[18], "S", txt)
		txt = re.sub(self.emoji_alpha[19], "T", txt)

		txt = re.sub(self.emoji_alpha[20], "U", txt)
		txt = re.sub(self.emoji_alpha[21], "V", txt)
		txt = re.sub(self.emoji_alpha[22], "W", txt)
		txt = re.sub(self.emoji_alpha[23], "X", txt)
		txt = re.sub(self.emoji_alpha[24], "Y", txt)

		txt = re.sub(self.emoji_alpha[25], "Z", txt)

		# Digits
		txt = re.sub(self.emoji_digit[0], "1",txt)
		txt = re.sub(self.emoji_digit[1], "2",txt)
		txt = re.sub(self.emoji_digit[2], "3",txt)
		txt = re.sub(self.emoji_digit[3], "4",txt)
		txt = re.sub(self.emoji_digit[4], "5",txt)
		txt = re.sub(self.emoji_digit[5], "6",txt)
		txt = re.sub(self.emoji_digit[6], "7",txt)
		txt = re.sub(self.emoji_digit[7], "8",txt)
		txt = re.sub(self.emoji_digit[8], "9",txt)
		txt = re.sub(self.emoji_digit[9], "0",txt)


		return txt


if __name__ == '__main__':
	cipher = EmojiCrypt()
	print(cipher.encrypt("abcdefghijklmnopqrstuvwxyz 1234567890"))
	print(cipher.decrypt("🍎🍌🏎🚪👁👣😀🖐ℹ😂🥋✉🚹🌉👌🍍👑👉🎤🚰☂🐍💧✖☀🦓 ❶❷❸❹❺❻❼❽❾⓿"))
