import random
import math

letters={chr(i):i for i in range(256)}

numbers={}
for letter,num in letters.items():
    numbers[num]=letter
   

def exponentMod(A,B,C) :
	    # Base cases 
    if (A == 0):
	return 0
    if (B == 0):
	return 1 
  
    # If B is even 
   
    if (B % 2 == 0):
	y = exponentMod(A, B / 2, C)
	y = (y * y) % C 
    
  
    # If B is odd 
    else:
	y = A % C
	y = (y * exponentMod(A, B - 1, C) % C) % C 
   
    return (int)((y + C) % C) 

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
	if n%i==0:
	    return False
    return True

def gcd(a,b): 
    if(b==0): 
	return a 
    else: 
	return gcd(b,a%b)

def gen_private_key(n,phi,e):
	list_random_k=[i for i in range(1,phi) if (((i*phi)+1)%e ==0)]
	k=random.choice(list_random_k)
	d=((k*phi)+1)/e
	return (n,d)
def gen_public_key(n,phi):
	list_random_e=[i for i in range(1,phi) if (n%i!=0 and gcd(i,phi) ==1)]
	e=random.choice(list_random_e)
	return (n,e)
	

primes=[i for i in range(26,1000) if isPrime(i)]
p=random.choice(primes)
primes.remove(p)
q=random.choice(primes)
n=p*q
phi=(p-1)*(q-1)
	
public_key=gen_public_key(n,phi)
private_key=gen_private_key(n,phi,public_key[1])



#Encrpt begin

def Encrypt(z):
	
	def change(c):
		d=""
		while(c>0):
			digit=c%10
			e=random.randint(0,9)
			d+=str(e)+str(digit)   #adding random then actual digit , on reversing we get actual digit followed by random no
			c=c/10
		return d[::-1]
	

	tog=""
	for i in z:
		c=exponentMod(letters[i],public_key[1],n)
		s=change(c)
		tog=tog+s+" "

	return tog
		
#Encrypt end		

#Decrypt start

def Decrypt(s):
	list_of=s.split()
	
	def changeback(i):
		original=""
		for n in range(0,len(i)):
			if(n%2==0):
				original+=i[n]
		
		return int(original)

	decrypted_pwd=""
	for i in list_of:
		cipher=changeback(i)
		decryp=exponentMod(cipher,private_key[1],n)
		dmsg=numbers[decryp]
		decrypted_pwd=decrypted_pwd+dmsg
	
	return decrypted_pwd
#DEcrypt end


		




