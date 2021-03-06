import re 

def autoencrypt(text, key):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        #check for position to apply given key
        if i == 0:
            if (char.isupper()):
            # formula : ciphertext = (plaintext + key ) mod 26 
                result += chr(((ord(char) - 65) + key) % 26 + 65)
            else:
                result += chr(((ord(char) - 97) + key) % 26 + 97)
        elif (char.isupper()):
            if text[i-1].isupper():
                #formula : Ciphertext = (plaintext[i] + plaintext[i-1]) mod 26                
                result += chr(((ord(char) - 65) + (ord(text[i-1]) - 65)) % 26 + 65 )
            else:
                result += chr(((ord(char) - 65) + (ord(text[i-1]) - 97)) % 26 + 65 )        
        else:
            if text[i-1].isupper():
                result += chr(((ord(char) - 97) + (ord(text[i-1]) - 65)) % 26 + 97 )
            else:
                result += chr(((ord(char) - 97) + (ord(text[i-1]) - 97)) % 26 + 97 )                  
    return result

def autodecrypt(text, plain_text, key):
    result = ""
   #extract one character from string at a time and decrypt it.
    for i in range(len(text)):
        char = text[i]
        #check for position to apply given key
        if i == 0:
            if (char.isupper()):
            # formula : ciphertext = (plaintext - key ) mod 26 
                result += chr(((ord(char) - 65) - key) % 26 + 65)
            else:
                result += chr(((ord(char) - 97) - key) % 26 + 97)
        elif (char.isupper()):
            if text[i-1].isupper():
                #formula : Ciphertext = (plaintext[i] - plaintext[i-1]) mod 26
                result += chr(((ord(char) - 65) - (ord(plain_text[i-1]) - 65)) % 26 + 65 )
            else:
                result += chr(((ord(char) - 65) - (ord(plain_text[i-1]) - 97)) % 26 + 65 )        
        else:
            if text[i-1].isupper():
                result += chr(((ord(char) - 97) - (ord(plain_text[i-1]) - 65)) % 26 + 97 )
            else:
                result += chr(((ord(char) - 97) - (ord(plain_text[i-1]) - 97)) % 26 + 97 )                  
    return result

if __name__ == "__main__": 
    plain_text = input("Enter your message: ")
    plain_text = plain_text.replace(" ","")
    plain_text = plain_text.replace('.',"")
    plain_text = re.sub(r'[0-9]','', plain_text)
    key_range = [1,3,5,7,9,11,15,17,19,21,23,25]
    print("Enter the key from range: ",key_range)
    k = int(input())
    print("Encryption (Cipher text): " +autoencrypt(plain_text, k))
    print("Decryption (Plain text): " +autodecrypt(autoencrypt(plain_text, k), plain_text, k))