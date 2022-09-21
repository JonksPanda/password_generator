import random
import string

class password:

    def __init__(self, length, symbols = (string.ascii_letters + string.digits + string.punctuation)) -> None:
        self.length = length
        self.symbols = symbols

    #generates strong password with random letters, numbers and symbols
    #length of password can be set
    def generate_strong(self):
        password = ''
        for x in range(int(self.length)):
            password += random.choice(self.symbols)
        return password

    #changes up letters to symbols from inserted word
