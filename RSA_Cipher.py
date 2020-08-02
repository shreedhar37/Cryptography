import re  # regular expression module to check particular pattern in given string.
import sympy #to generate prime numbers.
import math #for gcd

def checkprime(n):
    if n > 1:  
        for i in range(2,n):  
            if (n % i) == 0:  
                return 1                
            else:  
                return 0  
    else:  
        return 1  

def coprime(a, b):
    return math.gcd(a, b) == 1

def public_key(phi_of_n, p, q):
    # Generates prime numbers from range 2 to phi_of_n
    li = list(sympy.primerange(2, phi_of_n))
    # Generates the list possible public keys such that public key and phi_of_n are coprime.
    li1 = []
    for i in li:     
        x = coprime(i, phi_of_n)
        if x == 1 and (i != p and i != q):
            li1.append(i)    
    return li1

def private_key(e, phi_of_n):
    for i in range(phi_of_n + 1):
        if ((e * i ) % phi_of_n) == 1:
            return i

# def plain_text_to_no(plain_text):
    plain_text_no = ""
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        
        if char.isupper():
            plain_text_no += str(ord(char) - 65)
        else:
            plain_text_no += str(ord(char) - 97)
    
    return plain_text_no            

def RSA_Encryption(plain_text, e, n):
    # Formula: Cipher text = (Plaint text ^ Public key) mod n
    x = []
    for i in range(len(plain_text)):
        if plain_text[i].isupper():
            r = (((ord(plain_text[i]) - 65) ** e) % n)
            x.append(r)
        else:
            r = (((ord(plain_text[i]) - 97) ** e) % n)
            x.append(r) 
    
    result = ""
    for i in x:
        result += str(i)
    
    return result, x    

def RSA_Decryption(x, d, n):
    # Formula: Plain text = (Cipher text ^ Private key ) mod n
    y = x
    p = []
    for i in range(len(y)):
        r = (x[i] ** d) % n
        r = chr(r + 65)
        p.append(r)

    result = ""
    for i in p:
        result += str(i)
    
    return result    

         
    
if __name__ == "__main__":
    
    global p, q
    
    try:
        p = int(input("Enter prime number p:"))
        while checkprime(p) == 1:
            p = int(input("Please enter prime number only, p: "))

        q = int(input("Enter prime number q: "))
        while checkprime(q) == 1:
            q = int(input("Please enter prime number only, q: "))
    
    except ValueError:
        print("Please enter value in numbers only!")
        
        p = int(input("Enter prime number p:"))
        while checkprime(p) == 1:
            p = int(input("Please enter prime number only, p: "))
        
        q = int(input("Enter prime number q: "))
        while checkprime(q) == 1:
            q = int(input("Please enter prime number only, q: "))    
    
    while p == q :
        print("Please do not enter same values for p and q!")
        try:
            p = int(input("Enter prime number p:"))
            while checkprime(p) == 1:
                p = int(input("Please enter prime number only, p: "))

            q = int(input("Enter prime number q: "))
            while checkprime(q) == 1:
                q = int(input("Please enter prime number only, q: "))
    
        except ValueError:
            print("Please enter value in numbers only!")
        
            p = int(input("Enter prime number p:"))
            while checkprime(p) == 1:
                p = int(input("Please enter prime number only, p: "))
        
            q = int(input("Enter prime number q: "))
            while checkprime(q) == 1:
                q = int(input("Please enter prime number only, q: "))

    plain_text = input("Enter your message: ")
    plain_text = plain_text.upper()
    plain_text = plain_text.replace(" ", "")
    plain_text = re.sub(r'[0-9]','', plain_text)
    print("Message after removing space and numbers: " + plain_text)
    n = p * q
    print("n:", n)
    phi_of_n = (p - 1) * (q - 1)
    print("phi_of_n:", phi_of_n)
    key_range = public_key(phi_of_n, p, q)
    
    try:
        print("Select any public key from given range:", key_range)
        e = int(input())
        while e not in key_range:
            print("Select any public key from given range only:", key_range)
            e = int(input())
    except ValueError:
        print("Please enter value in numbers only!")
        print("Select any public key from given range:", key_range)
        e = int(input())
        while e not in key_range:
            print("Select any public key from given range only:", key_range)
            e = int(input())
    
    print("Public key:", e)
    d = private_key(e, phi_of_n)
    print("Private key:", d)
    ct, x = RSA_Encryption(plain_text, e, n)
    pt = RSA_Decryption(x, d, n)
    choice = int(input("1.Encryption\n2.Decryption\nSelect option number: "))
    
    if choice == 1:
        print("Encryption (Cipher Text): ",ct)
    else: 
        print("Decryption (Plain Text): ",pt)
    
    

 