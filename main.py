import emojicrypt

if __name__ == '__main__':
	keyword = str(input("Enter keyword: "))
	cipher = emojicrypt.EmojiCrypt(keyword)

	print("Select operation:\n1- Encrypt\n2- Decrypt")
	choice = int(input("Enter choice:"))
	if choice == 1:
		print(cipher.encrypt(str(input("Enter text: "))))
	elif choice == 2:
		print(cipher.decrypt(str(input("Enter encrypted text: "))))
	else:
		print("Invalid choice")