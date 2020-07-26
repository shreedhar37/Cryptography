import re
def vigenre_encrypt(text, key):
    result = ""
    
    #extract one character from string at a time and encrypt it
    for i in range(len(text)):
        pt = text[i]
        kt = key[i]
        
        if pt.isupper():
            if kt.isupper():
                # formula: (plaintext[i] + key[i]) mod 26
                result += chr(((ord(pt) - 65) + (ord(kt) - 65)) % 26 + 65)
            else:
                result += chr(((ord(pt) - 65) + (ord(kt) - 97)) % 26 + 97)
        else:
            if kt.isupper():
                result += chr(((ord(pt) - 97) + (ord(kt) - 65)) % 26 + 97)
            else:
                result += chr(((ord(pt) - 97) + (ord(kt) - 65)) % 26 + 97)       

    return result

def vigenre_decrypt(text, key):
    result = ""
    #extract one character from string at a time and decrypt it.
    for i in range(len(text)):
        ct = text[i]
        kt = key[i]
                
        if ct.isupper():
            if kt.isupper():
                # formula : ciphertext = (plaintext[i] - key[i]) mod 26 
                result += chr(((ord(ct) - 65) - (ord(kt) - 65)) % 26 + 65)
            else:
                result += chr(((ord(ct) - 65) - (ord(kt) - 97)) % 26 + 65)
        else:
            if kt.isupper():
                result += chr(((ord(ct) - 97) - (ord(kt) - 65)) % 26 + 97)
            else:
                result += chr(((ord(ct) - 97) - (ord(kt) - 97)) % 26 + 97)       

    return result

if __name__ == "__main__":
    plain_text = input("Enter your message: ")
    plain_text = plain_text.replace(" ","")
    plain_text = plain_text.replace('.',"")
    plain_text = re.sub(r'[0-9]','', plain_text)
    key = input("Enter the key like (PASCAL): ")
    key = key.replace(" ","")
    
    if len(key) < len(plain_text):
        diff = len(plain_text) - len(key)

        for i in range(diff):
            key = key + key[i]

    elif len(key) > len(plain_text):
        diff = len(key) - len(plain_text)
        key = key[ :diff]
        
    print("Encryption (Cipher Text): " +vigenre_encrypt(plain_text, key))
    print("Decryption (Plain Text): " +vigenre_decrypt(vigenre_encrypt(plain_text, key), key))
