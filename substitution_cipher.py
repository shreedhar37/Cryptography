import re 

def additiveencrypt(text, k):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process   
        # checks if character is upper case or lower case.
        if (char.isupper()):
            # formula : ciphertext = (plaintext + key) mod 26 
            result += chr(((ord(char) - 65) + k) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) + k) % 26 + 97)
    return result

def additivedecrypt(text, k):
    result = ""
   #extract one character from string at a time and decrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process     
        # checks if character is upper case or lower case.
        if (char.isupper()):
            # formula : ciphertext = (plaintext - key) mod 26 
            result += chr(((ord(char) - 65) - k) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) - k) % 26 + 97)
    return result

def mulencrypt(text, k):
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
            
    # negative numbers are not used in cryptography so we make addition of modulo value and negative number to make it positive.        
    if t1 < 0 : 
        r1 = (26 + t1)         
    
    return r1 

def muldecrypt(enc,kinv):
    result = ""
    for i in range(len(enc)):
        char = enc[i]
        if (char.isupper()):
            # formula: plaintext = (ciphertext * key⁻¹) mod 26
            result += chr(((ord(char) - 65) * kinv) % 26 + 65)
        else:
            result += chr(((ord(char) - 97) * kinv) % 26 + 97 )
    return result  

def affineencrypt(text, k1, k2):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process      
        # checks if character is upper case or lower case.
        if (char.isupper()):
            # formula : ciphertext = ((plaintext * key1 )+key2) mod 26 
            result += chr(((ord(char) - 65) * k1 + k2) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) * k1 + k2) % 26 + 97)
    return result

def affinedecrypt(enc, kinv, k2):
    result = ""
    for i in range(len(enc)):
        char = enc[i]
        if (char.isupper()):
            # formula: plaintext = ((ciphertext-key2) * key⁻¹) mod 26
            result += chr((((ord(char) - 65) - k2) * kinv) % 26 + 65)
        else:
            result += chr((((ord(char) - 97) - k2) * kinv) % 26 + 97 )
    return result        

if __name__ == "__main__": 
    while(1):
        print("\n1.Additive Cipher\n2.Multiplicative Cipher\n3.Affine Cipher\n4.Exit")
        n = int(input("Enter your choice: "))
        if n == 1:
            plain_text = input("\nEnter the plaintext: ")
            plain_text = plain_text.replace(" ","")
            plain_text = plain_text.replace('.',"")
            plain_text = re.sub(r'[0-9]','', plain_text)   
            key_range = [1,3,5,7,9,11,15,17,19,21,23,25]
            print("Enter the key from range: ",key_range)
            k = int(input())
            choice = int(input("\n1.Encryption\n2.Decryption\nEnter your choice: "))
            if choice == 1:
                print("\nEncryption: "+additiveencrypt(plain_text, k))
            else:
                print("Decryption: "+additivedecrypt(additiveencrypt(plain_text, k), k)) 
            
        elif n == 2:
            plain_text = input("\nEnter the plaintext: ") 
            plain_text = plain_text.replace(" ","")
            plain_text = plain_text.replace('.',"")
            plain_text = re.sub(r'[0-9]','', plain_text)
            key_range = [1,3,5,7,9,11,15,17,19,21,23,25]
            print("Enter the key from range: ",key_range)
            k = int(input())
            choice = int(input("\n1.Encryption\n2.Decryption\nEnter your choice: "))
            if choice == 1:
                print("\nEncryption: "+mulencrypt(plain_text, k))
            else:
                print("Decryption: "+muldecrypt(mulencrypt(plain_text, k), inverse(k)))

            
        elif n == 3:
            plain_text = input("\nEnter the plaintext: ")
            plain_text = plain_text.replace(" ","")
            plain_text = plain_text.replace('.',"")
            plain_text = re.sub(r'[0-9]','', plain_text)
            key_range = [1,3,5,7,9,11,15,17,19,21,23,25]
            print("Enter key pair like 5, 2 from given key range: ", key_range)
            k1, k2 = [int(x) for x in input().split(', ')]
            kinv = inverse(k1)
            choice = int(input("\n1.Encryption\n2.Decryption\nEnter your choice: "))
            if choice == 1:
                print("\nEncryption: "+affineencrypt(plain_text, k1, k2))
            else:
                key_inv = inverse(k1)
                ct = affineencrypt(plain_text, k1, k2)
                print("Decryption: " + affinedecrypt(ct, key_inv, k2))
                
        
        else:
            exit(0)