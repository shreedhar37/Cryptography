def pubkey(p,x,y,c):
    pub_key_alice = (c**x)%p
    pub_key_bob = (c**y)%p
    return pub_key_alice,pub_key_bob

def secret_key(pubkeyalice,pub_key_bob,x,y,p):
    secret_key_alice = (pub_key_bob**x)%p
    secret_key_bob = (pubkeyalice**y)%p
    return secret_key_alice,secret_key_bob
    
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

if __name__ == "__main__":
    p = int(input("Enter the prime number p: "))
    x = int(input("Enter the private key for alice: "))
    y = int(input("Enter the private key for bob: "))
    primitive_roots = primRoots(p)
    print("primitive roots: ",primitive_roots)
    c = int(input("Select any primitive number from above: "))
    pubkeyalice,publickeybob = pubkey(p,x,y,c)
    secret_key_alice,secret_key_bob = secret_key(pubkeyalice,publickeybob,x,y,p)
    print("Public key of alice: ",pubkeyalice)
    print("Public key of bob: ",publickeybob)
    print("secret key of alice:",secret_key_alice)
    print("secret key of bob: ",secret_key_bob)