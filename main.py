import emojicrypt
import datetime

def test():
	keyword = "P@ssw0rd"
	cipher = emojicrypt.EmojiCrypt(keyword)

	print("Encrypt:Some Text 123 *?")
	encrypted = cipher.encrypt("Some Text 123 *?")
	print(encrypted)

	print(f"\nDecrypt: {encrypted}")
	print(cipher.decrypt(encrypted))

	print(f"\nDecrypt:'    {encrypted}   '")
	print(cipher.decrypt(f"    {encrypted}   "))

	print(f"\nDecrypt:'TEXT{encrypted}'")
	print(cipher.decrypt(f"TEXT{encrypted}"))

	cipher_wrong = emojicrypt.EmojiCrypt("Wr0ng")
	print("\nDecrypt with wrong keyword:'🍵📮😁🕹😇🛩📂🐎😆🚫📮🙃🚉🚰🚫🚹😂😍🌏🗒☀💧👉🔄✉📮📮🤾😍🤞🏹📂🐎☺🐠🐠'")
	print(cipher_wrong.decrypt("🍵📮😁🕹😇🛩📂🐎😆🚫📮🙃🚉🚰🚫🚹😂😍🌏🗒☀💧👉🔄✉📮📮🤾😍🤞🏹📂🐎☺🐠🐠"))

def get_greeting():
	now = datetime.datetime.now()
	hour = int(now.strftime("%H"))
	
	if 6 < hour and hour < 12:
		return "Good morning"
	elif 12 <= hour and hour < 17:
		return "Good afternoon"
	elif 17 <= hour and hour < 20:
		return "Good evening"
	else:
		return "Greetings"

if __name__ == '__main__':
	print(65 * '-')
	print("E M O J I C R Y P T")
	print(f"{get_greeting()}! What would you like to encrypt/decrypt today?")
	print(65 * '-')

	# test()

	keyword = str(input("Enter keyword: "))
	cipher = emojicrypt.EmojiCrypt(keyword)

	print("\nSelect operation:\n1- Encrypt\n2- Decrypt")
	choice = int(input("\nEnter choice:"))
	if choice == 1:
		print(cipher.encrypt(str(input("\nEnter plain text: "))))
	elif choice == 2:
		print(cipher.decrypt(str(input("\nEnter cipher text: "))))
	else:
		print("Please enter a valid choice!")

# -----------------------------------------------------------------------
# EOF