from math import pow

def checkprime(n):
    if n > 0:  
        for i in range(2,int(n ** 0.5) + 1):  
            if (n % i) == 0:  
                return 0                
        
        else: 
            return 1  
    else:
        return 0      
    



def pubkey(p, x, y, c):
    pub_key_alice = (c ** x) % p
    pub_key_bob = (c ** y) % p
    return pub_key_alice, pub_key_bob

def secret_key(pubkeyalice, pub_key_bob, x, y, p):
    secret_key_alice = (pub_key_bob ** x) % p
    secret_key_bob = (pubkeyalice ** y) % p
    return secret_key_alice, secret_key_bob
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def primeroots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

if __name__ == "__main__":
    
    global p
    
    try:
        p = int(input("Enter prime number p:"))
        while checkprime(p) == 0:
            p = int(input("Please enter prime number only, p: "))

        
    except ValueError:
        print("Please enter value in numbers only!")
        
        p = int(input("Enter prime number p:"))
        while checkprime(p) == 0:
            p = int(input("Please enter prime number only, p: "))

   
    x = int(input("Enter the private key for alice: "))
    y = int(input("Enter the private key for bob: "))
    
    primitive_roots = primeroots(p)
    
    try:
        print(primitive_roots)
        c = int(input("Select any public key from given range: "))
        while c not in primitive_roots:
            print(primitive_roots)
            c = int(input("Select public key from given range only!: "))
    except ValueError:
        print("Please enter value in numbers only!")
        print(primitive_roots)
        c = int(input("Select any public key from given range: "))
        while c not in primitive_roots:
            print(primitive_roots)
            c = int(input("Select any public key from given range only: "))


    pubkeyalice,publickeybob = pubkey(p, x, y, c)
    secret_key_alice,secret_key_bob = secret_key(pubkeyalice, publickeybob ,x ,y, p)
    
    print("Public key of alice: ", pubkeyalice)
    print("Public key of bob: ", publickeybob)
    print("shared secret key of alice:", secret_key_alice)
    print("shared secret key of bob: ", secret_key_bob)
