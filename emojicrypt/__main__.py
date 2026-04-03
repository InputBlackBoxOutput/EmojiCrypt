import argparse
import sys
from . import EmojiCrypt


def main():
    parser = argparse.ArgumentParser(description="Emoji Cipher")
    parser.add_argument(
        "-k", type=str, help="Keyword used for AES encryption and Vigenere cipher"
    )
    parser.add_argument(
        "-vc", action="store_true", help="Use Vigenere cipher instead of AES"
    )

    parser.add_argument(
        "-e",
        nargs="?",
        const=True,
        default=False,
        help="Encrypt the specified string, or use as a flag with -i for file input",
    )
    parser.add_argument(
        "-d",
        nargs="?",
        const=True,
        default=False,
        help="Decrypt the specified string, or use as a flag with -i for file input",
    )

    parser.add_argument("-i", type=str, help="Input file for encryption/decryption")
    parser.add_argument(
        "-o",
        type=str,
        help="Output file for encryption/decryption [Default: encrypted.txt or decrypted.txt]",
    )

    args = parser.parse_args()

    if args.k:
        cipher = EmojiCrypt(args.k)
    else:
        print("Please specify keyword using the -k option")
        sys.exit()

    if args.e and args.d:
        print("Please specify either encryption or decryption operation")
        sys.exit()

    if args.i:
        if args.e:
            operation = "encrypt"
            output = "encrypted.txt"
        elif args.d:
            operation = "decrypt"
            output = "decrypted.txt"
        else:
            print("Please specify -e or -d when using -i")
            sys.exit()

        filepath = {"input": args.i, "output": args.o if args.o else output}

        cipher.fileio(filepath, operation)
        print("Done")
        sys.exit()

    if args.e:
        if args.e is True:
            print("Please provide text to encrypt with -e when not using -i")
            sys.exit()
        print(cipher.encrypt(args.e, "vc" if args.vc else "aes"))
        sys.exit()

    if args.d:
        if args.d is True:
            print("Please provide text to decrypt with -d when not using -i")
            sys.exit()
        print(cipher.decrypt(args.d, "vc" if args.vc else "aes"))
        sys.exit()

    print("Please specify an operation (-e or -d), and optional -i for file processing")
    sys.exit()


if __name__ == "__main__":
    main()
