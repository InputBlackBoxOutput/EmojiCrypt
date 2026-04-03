from . import CHARACTERS

class VigeneresCipher:
    def __init__(self, keyword):
        self.keyword = keyword
        self.characters = CHARACTERS.copy()
        self.square = self.generate_square()

    def generate_square(self):
        square = []
        for i in range(len(self.characters)):
            square.append(self.characters[i:] + self.characters[0:i])

        return square

    def decrypt(self, txt):
        it = 0
        loc = 0
        out = ""

        for char in txt:
            if char in self.characters:
                loc = self.characters.index(self.keyword[it])
                it += 1

                if it >= len(self.keyword):
                    it = 0

                out += self.characters[self.square[loc].index(char)]
            else:
                out += char

        return out

    def encrypt(self, txt):
        out = ""
        it = 0

        for char in txt:
            if char in self.characters:
                out += self.square[self.characters.index(self.keyword[it])][
                    self.characters.index(char)
                ]
                it += 1

                if it >= len(self.keyword):
                    it = 0
            else:
                out += char

        return out
