### password generator
import random
import string

def Generator(size, type):
    char=string.ascii_uppercase+string.ascii_lowercase
    if type=='strong':
            password=''.join(random.choice(char) for _ in range(size-2))+random.choice(string.punctuation)+random.choice(string.digits)
    elif type=='weak':
            password=''.join(random.choice(char) for _ in range(size))
    else:
            print("I don't recognize the type!")
            password=''
    return password

if __name__ == '__main__':
    user_pass=input("Please tell me strong or weak password you need?")
    size_pass=int(input("Please tell me password lenght you need?"))
    password=Generator(size_pass,user_pass)
    print("Your password is '%s'" %password)
