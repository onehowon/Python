from random import*

def genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    password = ""

    for i in range(5):
        a_index = randrange(len(alphabet))
        n_index = randrange(len(numbers))
        password = alphabet[a_index] + password + numbers[n_index]
    return password

print(genPass())
print(genPass())
print(genPass())
