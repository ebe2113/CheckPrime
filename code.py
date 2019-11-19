'''Returns a boolean value (True or False) depending on whether the input n is prime.
'''

def prime_check_trial(n): 
    
    if n>1 :
        for i in range (2, int(math.sqrt(n)) +1):
            if n % i == 0:
                return False  
            return True
        else: 
            return False
     # boolean True or False depending on prime or not



def prime_check_sieve(n):
    prime = True
    count = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0 and n>=i*i: 
            count+=1
    if count>0:
        prime = False 
    else:
        prime = True
    return prime # boolean True or False depending on prime or not


def prime_check_fermat(n):
    k=20
    while (k>0): 
       a = random.randint(2,n-2) 
       if pow(a,n-1,n)!=1:
           return False 
       k-=1
    return True
