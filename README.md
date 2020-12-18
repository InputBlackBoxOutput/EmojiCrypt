# EmojiCrypt
AES encryption encoded using emojis

![GIF](https://github.com/InputBlackBoxOutput/EmojiCrypt/blob/master/EmojiCrypt.gif)

* EmojiCrypt's output can be effectively copied to the clipboard in some CLIs only

|CLI|Copyable|
|--|--|
|Linux terminal (Ubuntu 20.04LTS)| ✔️|
|Command prompt (Windows 10)| ❌|

* File encryption uses Vigenere's cipher instead of AES cipher to reduce computation

*This project was inspired by the website: [emojicrypt.com](https://emojicrypt.com/)*

## Installation
This software does not require installation however the user should have Python (3.8 or above) installed.

Python can be downloaded from www.python.org

## Usage
<code> emojicrypt.py [-h] [-k K] (-e E | -d D | -ef EF | -df DF) </code>
  
|Option| Description|
|--|--|
|-k| Keyword|
|-e| Encrypt text|
|-d| Decrypt text|
|-ef| Encrypt file|
|-df| Decrypt file|
|-h, --help|show the help message and exit|

## Disclaimer:
*Under no circumstances will the creator/s of this application be held responsible or liable in any way for any claims, damages, losses, expenses, costs or liabilities whatsoever (including, without limitation, any direct or indirect damages for loss of profits, business interruption or loss of information) resulting or arising directly or indirectly from your use of or inability to use this application even if the creator/s of this application have been advised of the possibility of such damages in advance.*

### Made with lots of ⏱️, 📚 and ☕ by [InputBlackBoxOutput](https://github.com/InputBlackBoxOutput)
