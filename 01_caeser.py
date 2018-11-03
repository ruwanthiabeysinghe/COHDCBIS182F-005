def encrypt(string):

    ci=''
    shift=3
    for char in string:
        if char == '':
            ci=ci+char
        elif char.isupper():
            ci=ci+chr((ord(char) + shift - 65)% 26+65)
        else:
            ci=ci+chr((ord(char)+ shift-97)%26+97)

    return ci

msg= input("Enter message")

print("Encrypted message is: ",encrypt(msg))
