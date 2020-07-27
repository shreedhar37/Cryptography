import re

def railfence_encrypt(text):
    
    result= ""
    echr = [] #even position letter list
    ochr = [] #odd position letter list
    
    for i in range(len(text)):
        if i % 2 == 0: 
            echr.append(text[i])
        else:
            ochr.append(text[i])
    
    echr.extend(ochr) #extending odd list to even list.
    
    for i in echr:  #converting list to string.
        result += i 
    
    return result 

def encrypt(text, k):
    
    result = ""
    
    #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process      
        # checks if character is upper case or lower case.
        if (char.isupper()):
            # formula : ciphertext = (plaintext * key ) mod 26 
            result += chr(((ord(char) - 65) * k) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) * k) % 26 + 97)
    
    return result

# function that will calculate and return multiplicative inverse of key.
def inverse(key):
    
    for i in range(26):
        if (key * i) % 26 == 1:
            return i

def railfence_decrypt(ct):
    ciphertext = ct

    if len(ciphertext) % 2 != 0:
        ciphertext += " "
    
    plain_text= ""
    mid = len(ciphertext) // 2
    
    for i in range(0,mid):
        plain_text = plain_text + ciphertext[i] + ciphertext[i + mid]        
    
    plain_text = plain_text.replace(" ","")
    
    return plain_text


def muldecrypt(enc, kinv):
    result = ""
    
    for i in range(len(enc)):
        char = enc[i]
        
        if (char.isupper()):
            # formula: plaintext = (ciphertext * key⁻¹) mod 26
            result += chr(((ord(char) - 65) * kinv) % 26 + 65)
        
        else:
            result += chr(((ord(char) - 97) * kinv) % 26 + 97 )
    
    return result        


if __name__ == "__main__": 
    plain_text = input("Enter the plaintext: ")
    plain_text = plain_text.replace(" ","")
    plain_text = plain_text.replace('.',"")
    plain_text = re.sub(r'[0-9]','', plain_text)
    keyrange = [1,3,5,7,9,11,15,17,19,21,23,25]
    print("Enter key from range: ", keyrange)
    key = int(input())
    ct = railfence_encrypt((encrypt(plain_text, key)))
    print("Encryption (Cipher text) after applying Multiplicative Cipher and Railfence Cipher: " + ct)
    print("Decryption (Plain text) after applying Railfence and Multiplicative Cipher: " + muldecrypt(railfence_decrypt(ct), inverse(key)))