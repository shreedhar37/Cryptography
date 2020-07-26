import re

def railfence(text):
    
    result= ""
    echr =[] #even position letter list
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


    

if __name__ == "__main__": 
    plain_text = input("Enter the plaintext: ")
    plain_text = plain_text.replace(" ","")
    plain_text = plain_text.replace('.',"")
    plain_text = re.sub(r'[0-9]','', plain_text)
    keyrange = [1,3,5,7,9,11,15,17,19,21,23,25]
    print("Enter key from range: ", keyrange)
    key = int(input())
    ct = railfence((encrypt(plain_text, key)))
    print("Encryption (Cipher text) after applying Multiplicative Cipher and Railfence Cipher: " + ct)
