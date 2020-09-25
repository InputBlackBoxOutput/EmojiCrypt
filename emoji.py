# Convert characters to emojis
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

import re
import random

class EmojiCrypt:
	def __init__(self, ROT13=False):
		self.emoji_alpha = ["🍎", "🍌","🏎", "🚪", "👁", "👣", "😀", "🖐", "ℹ", "😂", "🥋", "✉", "🚹", "🌉", "👌", "🍍", "👑", "👉", "🎤", "🚰", "☂", "🐍", "💧", "✖", "☀", "🦓", "🏹", "🎈", "😎", "🎅", "🐘", "🌿", "🌏", "🌪", "☃", "🍵", "🍴", "🚨", "📮", "🕹", "📂", "🛩", "⌨", "🔄", "🔬", "🐅", "🙃", "🐎", "🌊", "🚫", "❓", "⏩", "😁", "😆", "💵", "🤣", "☺", "😊", "😇", "😡", "🎃", "😍", "✅", "🔪", "🗒"]
		self.emoji_digit = ["❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾", "⓿"]
		self.shift = 13 if ROT13 else random.randint(0, 25)
		self.shift_emoji_list()
		# self.emoji_alpha = [u"\U0001F609", add custom & random......]
		# self.shift = shift # Cyclic shift, maybe ROT13

	def shift_emoji_list(self):
		length = len(self.emoji_alpha)
		self.emoji_alpha = self.emoji_alpha[self.shift: length] + self.emoji_alpha[0:self.shift]

	def encrypt(self, txt):
		# Uppercase alphabets
		txt = re.sub("A", self.emoji_alpha[0], txt)
		txt = re.sub("B", self.emoji_alpha[1], txt)
		txt = re.sub("C", self.emoji_alpha[2], txt)
		txt = re.sub("D", self.emoji_alpha[3], txt)
		txt = re.sub("E", self.emoji_alpha[4], txt)

		txt = re.sub("F", self.emoji_alpha[5], txt)
		txt = re.sub("G", self.emoji_alpha[6], txt)
		txt = re.sub("H", self.emoji_alpha[7], txt)
		txt = re.sub("I", self.emoji_alpha[8], txt)
		txt = re.sub("J", self.emoji_alpha[9], txt)

		txt = re.sub("K", self.emoji_alpha[10], txt)
		txt = re.sub("L", self.emoji_alpha[11], txt)
		txt = re.sub("M", self.emoji_alpha[12], txt)
		txt = re.sub("N", self.emoji_alpha[13], txt)
		txt = re.sub("O", self.emoji_alpha[14], txt)

		txt = re.sub("P", self.emoji_alpha[15], txt)
		txt = re.sub("Q", self.emoji_alpha[16], txt)
		txt = re.sub("R", self.emoji_alpha[17], txt)
		txt = re.sub("S", self.emoji_alpha[18], txt)
		txt = re.sub("T", self.emoji_alpha[19], txt)

		txt = re.sub("U", self.emoji_alpha[20], txt)
		txt = re.sub("V", self.emoji_alpha[21], txt)
		txt = re.sub("W", self.emoji_alpha[22], txt)
		txt = re.sub("X", self.emoji_alpha[23], txt)
		txt = re.sub("Y", self.emoji_alpha[24], txt)

		txt = re.sub("Z", self.emoji_alpha[25], txt)

		# Lowercase alphabets
		txt = re.sub("a", self.emoji_alpha[26], txt)
		txt = re.sub("b", self.emoji_alpha[27], txt)
		txt = re.sub("c", self.emoji_alpha[28], txt)
		txt = re.sub("d", self.emoji_alpha[29], txt)
		txt = re.sub("e", self.emoji_alpha[30], txt)

		txt = re.sub("f", self.emoji_alpha[31], txt)
		txt = re.sub("g", self.emoji_alpha[32], txt)
		txt = re.sub("h", self.emoji_alpha[33], txt)
		txt = re.sub("i", self.emoji_alpha[34], txt)
		txt = re.sub("j", self.emoji_alpha[35], txt)

		txt = re.sub("k", self.emoji_alpha[36], txt)
		txt = re.sub("l", self.emoji_alpha[37], txt)
		txt = re.sub("m", self.emoji_alpha[38], txt)
		txt = re.sub("n", self.emoji_alpha[39], txt)
		txt = re.sub("o", self.emoji_alpha[40], txt)

		txt = re.sub("p", self.emoji_alpha[41], txt)
		txt = re.sub("q", self.emoji_alpha[42], txt)
		txt = re.sub("r", self.emoji_alpha[43], txt)
		txt = re.sub("s", self.emoji_alpha[44], txt)
		txt = re.sub("t", self.emoji_alpha[45], txt)

		txt = re.sub("u", self.emoji_alpha[46], txt)
		txt = re.sub("v", self.emoji_alpha[47], txt)
		txt = re.sub("w", self.emoji_alpha[48], txt)
		txt = re.sub("x", self.emoji_alpha[49], txt)
		txt = re.sub("y", self.emoji_alpha[50], txt)

		txt = re.sub("z", self.emoji_alpha[51], txt)

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
		
		# txt = str(self.shift) + txt
		return txt

	def decrypt(self, txt):
		# Uppercase alphabets
		txt = re.sub(self.emoji_alpha[0], "A",txt)
		txt = re.sub(self.emoji_alpha[1], "B",txt)
		txt = re.sub(self.emoji_alpha[2], "C",txt)
		txt = re.sub(self.emoji_alpha[3], "D",txt)
		txt = re.sub(self.emoji_alpha[4], "E",txt)

		txt = re.sub(self.emoji_alpha[5], "F",txt)
		txt = re.sub(self.emoji_alpha[6], "G",txt)
		txt = re.sub(self.emoji_alpha[7], "H",txt)
		txt = re.sub(self.emoji_alpha[8], "I",txt)
		txt = re.sub(self.emoji_alpha[9], "J",txt)

		txt = re.sub(self.emoji_alpha[10], "K",txt)
		txt = re.sub(self.emoji_alpha[11], "L",txt)
		txt = re.sub(self.emoji_alpha[12], "M",txt)
		txt = re.sub(self.emoji_alpha[13], "N",txt)
		txt = re.sub(self.emoji_alpha[14], "O",txt)

		txt = re.sub(self.emoji_alpha[15], "P",txt)
		txt = re.sub(self.emoji_alpha[16], "Q",txt)
		txt = re.sub(self.emoji_alpha[17], "R",txt)
		txt = re.sub(self.emoji_alpha[18], "S",txt)
		txt = re.sub(self.emoji_alpha[19], "T",txt)

		txt = re.sub(self.emoji_alpha[20], "U",txt)
		txt = re.sub(self.emoji_alpha[21], "V",txt)
		txt = re.sub(self.emoji_alpha[22], "W",txt)
		txt = re.sub(self.emoji_alpha[23], "X",txt)
		txt = re.sub(self.emoji_alpha[24], "Y",txt)

		txt = re.sub(self.emoji_alpha[25], "Z",txt)

		# Lowercase alphabets
		txt = re.sub(self.emoji_alpha[26], "a",txt)
		txt = re.sub(self.emoji_alpha[27], "b",txt)
		txt = re.sub(self.emoji_alpha[28], "c",txt)
		txt = re.sub(self.emoji_alpha[29], "d",txt)
		txt = re.sub(self.emoji_alpha[30], "e",txt)

		txt = re.sub(self.emoji_alpha[31], "f",txt)
		txt = re.sub(self.emoji_alpha[32], "g",txt)
		txt = re.sub(self.emoji_alpha[33], "h",txt)
		txt = re.sub(self.emoji_alpha[34], "i",txt)
		txt = re.sub(self.emoji_alpha[35], "j",txt)

		txt = re.sub(self.emoji_alpha[36], "k",txt)
		txt = re.sub(self.emoji_alpha[37], "l",txt)
		txt = re.sub(self.emoji_alpha[38], "m",txt)
		txt = re.sub(self.emoji_alpha[39], "n",txt)
		txt = re.sub(self.emoji_alpha[40], "o",txt)

		txt = re.sub(self.emoji_alpha[41], "p",txt)
		txt = re.sub(self.emoji_alpha[42], "q",txt)
		txt = re.sub(self.emoji_alpha[43], "r",txt)
		txt = re.sub(self.emoji_alpha[44], "s",txt)
		txt = re.sub(self.emoji_alpha[45], "t",txt)

		txt = re.sub(self.emoji_alpha[46], "u",txt)
		txt = re.sub(self.emoji_alpha[47], "v",txt)
		txt = re.sub(self.emoji_alpha[48], "w",txt)
		txt = re.sub(self.emoji_alpha[49], "x",txt)
		txt = re.sub(self.emoji_alpha[50], "y",txt)

		txt = re.sub(self.emoji_alpha[51], "z",txt)

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
	print(cipher.encrypt("aAbBcC 190"))
	print(cipher.decrypt("🏹🍎🎈🍌😎🏎 ❶❾⓿"))
