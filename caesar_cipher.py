letters = "abcdefghijklmnopqrstuvwxyz"

text = input("Enter the text to be encrypted: ")
key = 3

def encrypt(pt):

    cipher_text = ""
    for j in range(len(pt)):
        for i in range(26):
            if(pt[j] == letters[i]):
                position = i
                break
        cipher = (position + key) % 26
        cipher_text += letters[cipher]
    return cipher_text
    
def decrypt(ct):
    plain_text = ""
    for j in range(len(ct)):
        for i in range(26):
            if(ct[j] == letters[i]):
                position = i
                break
        cipher = (position - key) % 26
        plain_text += letters[cipher]
    return plain_text


print("Encrypted text:"+encrypt(text))
print("Decrypted text:"+decrypt(encrypt(text)))