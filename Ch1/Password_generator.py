from abc import ABC, abstractmethod
import string
import random

class PasswordGeneratorAbstract(ABC):

    @abstractmethod
    def password_generator(self, length=8):
        pass


class NumericPasswordGenerator(PasswordGeneratorAbstract):
    nums = string.digits

    def password_generator(self, length=8):
        result = ''
        for i in range(length):
            result += random.choice(self.nums)

        return result


class LetterPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters

    def password_generator(self, length=8):
        result = ''
        for i in range(length):
            result += random.choice(self.letters)

        return result


class MixedPasswordGenerator(PasswordGeneratorAbstract):

    all_chars = string.ascii_letters + string.digits + string.punctuation

    def password_generator(self, length=16):
        return ''.join(random.choice(self.all_chars) for _ in range(length))


print(MixedPasswordGenerator().password_generator())

