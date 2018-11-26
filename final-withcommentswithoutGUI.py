import random
import math

#dictionary letters that is mapping characters to their ASCII values. 
letters={chr(i):i for i in range(256)}

#dictionary numbers that is mapping ASCII values to their charcters.
numbers={}
for letter,num in letters.items():
    numbers[num]=letter
   

def exponentMod(a,b,c) :

    # Base cases 
    if (a == 0):
        return 0
    if (b == 0):
        return 1 
  
    # If b is even 
   
    if (b % 2 == 0):
        y = exponentMod(a,b / 2,c)
        y = (y * y) % c
    
  
    # If b is odd 
    else:
        y = a % c
        y = (y * exponentMod(a, b - 1,c) % c) % c 
   
    return (int)((y + c) % c) 

#to check whether a number is a prime numberor not.
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

#to find the GCD of two numbers. 
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)

def gen_public_key(n,phi):
	#selecting random e such that e is not a factor of n and 1<e<phi also e and phi are coprimes.
	#here we are creating a list of numbers which are satisfying the conditions required for e and choosing 1 random number from the list.	
	list_random_e=[i for i in range(1,phi) if (n%i!=0 and gcd(i,phi) ==1)]
	e=random.choice(list_random_e)
	return (n,e)

def gen_private_key(n,phi,e):
	list_random_k=[i for i in range(1,phi) if (((i*phi)+1)%e ==0)]
	k=random.choice(list_random_k)
	print "k=",k
	d=((k*phi)+1)/e
	return (n,d)

f=open("toBeEncrypted.txt","r")
z=f.read()                            #Using file handling to read from the file and the input is stored as a string in z.
f.close()		


primes=[i for i in range(26,1000) if isPrime(i)]
p=random.choice(primes)
primes.remove(p)
q=random.choice(primes)
print "p=",p
print "q=",q

n=p*q
phi=(p-1)*(q-1)

public_key=gen_public_key(n,phi)
print "public key (n,e) : ",public_key
private_key=gen_private_key(n,phi,public_key[1])
print "private key (n,d) ",private_key

#To add padding(random digit) at alternate positions after encryption
def change(c):
	d=""
	while(c>0):
		digit=c%10
		e=random.randint(0,9)
		d+=str(e)+str(digit)   #adding random then actual digit , on reversing we get actual digit followed by random no
		c=c/10
	return d[::-1]
	

#Encrypts character by character using function plaintext raised to the power e mod n using public key.
def Encrypt():
	for i in z:
		c=exponentMod(letters[i],public_key[1],n)
		print "each letter encrypted=",c
		s=change(c)
		print "each letter after padding: ",s
		f=open("encrypted.txt","a+")               #Opens encrypted.txt in append mode
		s=s+" "
		f.write(s)                               #Writes encrypted text iteratively.
		f.close()

Encrypt()

#Removes padding before decryption.
def changeback(i):
	print i
	original=""
	for n in range(0,len(i)):
		if(n%2==0):
			original+=i[n]
		
	return int(original)

#Decrypts character by character using the function ciphertext raised to the power d mod n using private key
def Decrypt():
	f=open("encrypted.txt","r")
	s=f.read().split()                #Splits at space and makes a list of the strings.
	f.close()
	for i in s:
		cipher=changeback(i)
		print "cipher :",cipher
		decryp=exponentMod(cipher,private_key[1],n)
		print "each letter decrypted=",decryp
		dmsg=numbers[decryp]
		print "The decrypted charcter is :",dmsg
		f=open("Decrypted.txt","a+")    #Opens Decrypted.txtin append mode.       
		f.write(dmsg)                  #Writes decrypted code iteratively 
	f.close()
	
	
Decrypt()


