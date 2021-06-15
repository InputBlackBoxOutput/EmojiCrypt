import emojicrypt

cipher = emojicrypt.EmojiCrypt("apple")

print(cipher.encrypt("ABCDEF123!@#$%"))

print(cipher.decrypt("💧🥋👑🗒👣🌏🤣🌊💧🗒🎣🐘😂🐎🍴🚨🎃🚰🌿🍍😍😆🌿👌🙃🐅🎃🚨🚹😀😎🌪😆📂🎈🍵🔬⏩🎅🤣"))