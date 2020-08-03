import re 

def encrypt(text, k1, k2):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process      
        # checks if character is upper case or lower case.
        if (char.isupper()):
            # formula : ciphertext = ((plaintext * key1 )+key2) mod 26 
            result += chr(((ord(char)-65) * k1 + k2) % 26 + 65)
      
        else:
            result += chr(((ord(char)-97) * k1 + k2) % 26 + 97)
    return result

#below function is used to calculate multiplicative inverse of key.
def inverse(k1):
    r1, r2, t1, t2 = 26, k1, 0, 1
    
    while r2 > 0:
        q = r1 // r2
        r = r1 - (q * r2)
        r1 = r2
        r2 = r
        t = t1 - (q * t2)
        t1 = t2 
        t2 = t
        if r1 == 1:
            r1 = t1
            break

    # negative numbers are not used in cryptography so we make addition of modulo value and negative number to make it positive.        
    if t1 == -t1: 
        return (26 + t1)         
    
    else:
        return r1 

    

def decrypt(enc, kinv, k2):
    result = ""
    for i in range(len(enc)):
        char = enc[i]
        if (char.isupper()):
            # formula: plaintext = ((ciphertext-key2) * key⁻¹) mod 26
            result += chr((((ord(char) - 65)-k2) * kinv) % 26 + 65)
        else:
            result += chr((((ord(char) - 97)-k2) * kinv) % 26 + 97 )
    return result        

if __name__ == "__main__": 
    plain_text = input("Enter the plaintext: ")
    plain_text = plain_text.replace(" ","")
    plain_text = plain_text.replace('.',"")
    plain_text = re.sub(r'[0-9]','', plain_text)
    key_range = [1,3,5,7,9,11,15,17,19,21,23,25]
    print("Enter key pair like 5, 2 from given key range: ", key_range)
    k1, k2 = [int(x) for x in input().split(', ')]
    kinv = inverse(k1)
    enc = encrypt(plain_text, k1, k2)
    print ("Encryption (Cipher text): " + encrypt(plain_text, k1, k2))
    print("Decryption (Plain text): " + decrypt(enc, kinv, k2))
