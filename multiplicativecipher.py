def encrypt(text,k):
    result = ""
   
    for i in range(len(text)):
        char = text[i]
     
        if char==" ":
            result += " "      
        elif (char.isupper()):
            result += chr(((ord(char)-65) * k) % 26 + 65)
      
        else:
            result += chr(((ord(char)-97) * k) % 26 + 97)
    return result

def inverse(s):
    for i in range(1,27):
        if (s*i)%26==1:
            return i

def decrypt(enc,kinv):
    result = ""
    for i in range(len(enc)):
        char = enc[i]
        if char==" ":
            result += " "
        elif (char.isupper()):
            result += chr(((ord(char) - 65) * kinv) % 26 + 65)
        else:
            result += chr(((ord(char) - 97) * kinv) % 26 + 97 )
    return result        
text = "Cryptography is fun"
k = 15
kinv = inverse(k)
enc = encrypt(text,k)
print ("Plain Text : " + text)
print ("Shift pattern : " + str(k))
print ("Encryption (Cipher text): " + encrypt(text, k))
print("Decryption (Plain text): " + decrypt(enc, kinv))