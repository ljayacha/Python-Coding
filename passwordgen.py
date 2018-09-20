import string
from random import *

char = string.ascii_letters+string.digits+string.punctuation
password = "".join(choice(char) for x in range(randint(3, 20)))
print(password)
