from Tkinter import *
import random
import math

letters={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

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
def gen_public_key(n,phi):
	list_random_e=[i for i in range(1,phi) if (n%i!=0 and gcd(i,phi) ==1)]
	e=random.choice(list_random_e)
	return (n,e)
def gen_private_key(n,phi,e):
	list_random_k=[i for i in range(1,phi) if (((i*phi)+1)%e ==0)]
	k=random.choice(list_random_k)
	print "k=",k
	d=((k*phi)+1)/e
	return (n,d)

'''create=[]
z=raw_input("enter what has to be encrypted   :")
for i in range(0,len(z)):
	if(z[i].isupper()):
		create.append(-1)
	else:
		create.append(0)
z=z.lower()'''

z=raw_input("enter what has to be encrypted   :")
print "z=",z		
msg=0
i=0
for ch in z[::-1]:
	msg+=(letters[ch]*(26**i))
	i+=1
print "Original message=\t",msg

primes=[i for i in range(msg/2,msg) if isPrime(i)]
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

cipher=exponentMod(msg,public_key[1],n)

def Encrypt():
	c=exponentMod(msg,public_key[1],n)
	print "encrypted=",c
	listbox.insert(0,c)

def Decrypt():
	decryp=exponentMod(cipher,private_key[1],n)
	print "decrypted=",decryp
	dmsg=""
	while(decryp>0):
		r=decryp%26
		dmsg+=numbers[r]
		decryp/=26
	dmsg=dmsg[::-1]
	print "The decrypted message is :",dmsg
	listbox2.insert(0,dmsg)






root = Tk()    
# GUI title                
root.title('RSA ENCRYPTOR AND DECRYPTOR')   

# ******************plaintext input*****************
l = Label(root,text='Input the plaintext')
l.pack() 

# input plaintext
entryvalue = Entry(root) 
entryvalue.pack()

# click the Encrypt button
button = Button(root,text="Encrypt",command=Encrypt) 
button.pack()

# show the ciphertext info.
show = Label(root,text='Show Ciphertext:')
show.pack() 
listbox  = Listbox(root,height = 1, width = 40)        
listbox.pack() 
# ******************plaintext input ending*****************





# ******************ciphertext input*****************
label = Label(root,text='Input the ciphertext')
label.pack() 

# input ciphertext
entryvalue2 = Entry(root) 
entryvalue2.pack()

# click the Decrypt button
button2 = Button(root,text="Decrypt",command=Decrypt) 
button2.pack()

# show the plaintext info.
show2 = Label(root,text='Show Plaintext:')
show2.pack() 
listbox2  = Listbox(root,height = 1, width = 40)         
listbox2.pack() 
# ******************ciphertext input ending*****************


root.mainloop()                 




	

	
	

















