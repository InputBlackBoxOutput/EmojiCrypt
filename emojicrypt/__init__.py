# Convert characters to emojis
# �🏴✉����������🙃���������🎤�����👌������🚫��
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created 24 Sept 2020

# ------------------------------------------------------------------------------

from Crypto.Cipher import AES
from Crypto import Random

import hashlib
import base64
import re

EMOJI_LIST = "🍎 🍌 🏎 🚪 👁 👣 😀 🖐 ℹ 😂 🥋 ✉ 🚹 🌉 👌 🍍 👑 👉 🎤 🚰 ☂ 🐍 💧 ✖ ☀ 🦓 🏹 🎈 😎 🎅 🐘 🌿 🌏 🌪 ☃ 🍵 🍴 🚨 📮 🕹 📂 🛩 ⌨ 🔄 🔬 🐅 🙃 🐎 🌊 🚫 ❓ ⏩ 😁 😆 💵 🤣 ☺ 😊 😇 😡 🎃 😍 ✅ 🔪 🗒 🤾 👶 🤞 🎳 🙊 🗝 🚋 👢 🍦 🕊 🏕 😧 🏴 🍗 🙄 🚉 🎣 📲 🧐 🛎 🐼 🙄 🎻 🐠 🥠 🏄 🗜 😋".split(" ")
CHARACTERS = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! \" # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~".split(" ")

# ------------------------------------------------------------------------------
from .emojicrypt import EmojiCrypt
from .aes import AESCipher
from .vigeneres import VigeneresCipher
