import random
import math

##Function for computing binary exponentiation
def binexp(num1,num2,m):
    num1=num1%m
    ans=1
    while num2>0:
        if num2&1:
            ans=(ans*num1)%m
        num2=num2>>1
        num1=(num1*num1)%m
    return ans

##Miller Rabin's Test for determining weather the number is prime or not
def millertest(d,num):
    y=2+random.randint(1,num-4)
    x=binexp(y,d,num)
    if (x==1)or(x==num-1):
        return True
    while (d!=(num-1)):
        x=(x*x)%num
        d*=2
        if (x==1):
            return False
        if (x==num-1):
            return True
    return False

#Function to check prime number
def isprime(num,k):
    if num==1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    
    ##Expressing num of the form num=1+(2^r)*d
    d=num-1
    r=0
    while d%2==0:
        d=d//2
        r+=1
    for i in range(k):
        b=millertest(d,num)
        if (b==False):
            return False
    return True

def getprime(length):
    p=random.getrandbits(length)
    #setting least and most significant bit to 1
    p+=(1<<(length-1))|1
    return p

#Function to get prime number of (length) bits
def primegenerator(length):
    #Giving first non-prime no.
    y=4
    while (isprime(y,128)==False):
        y=getprime(length)
    return y

def gcd(a,b):
    math.gcd(a,b)

#Generate e such that gcd(e,phi)=1 also satisfying the condition: 1<e<phi
def generate_e(length,phi):
    e=primegenerator(length)
    while(math.gcd(e,phi)!=1):
        e=primegenerator(length)
    return e

#Generate d such that is satisfies the property: (d*e)%(phi)=1
#Here we will generate d using modinverse function
#We need phi*(x)+e*(y)=gcd(phi,e)=1
#Finding d using extended euclid algorithm
def gcdExtended(e,phi):
  a1,a2,b1,b2,d1,d2=1,0,0,1,phi,e

  while d2!=1:
    k=(d1//d2)
    temp=a2
    a2=a1-(a2*k)
    a1=temp
    temp=b2
    b2=b1-(b2*k)
    b1=temp
    temp=d2
    d2=d1-(d2*k)
    d1=temp
    d=b2
  if d>phi:
    d=d%phi
  elif d<0:
    d=d+phi
  return d

#For encrypting text message
def encryption(message,e,N):
    #List for storing ASCII value
    encrypted=[]
    length=len(message)
    for i in range(length):
        encrypted.append(binexp(ord(message[i]),e,N))
    return encrypted

#For decrypting cipher
def decryption(encrypted,d,N):
    decrypted_message=''
    length=len(encrypted)
    for i in range(length):
        decrypted_message+=chr(binexp(encrypted[i],d,N))
    return decrypted_message

#For encrypting number
def encryption_num(number,e,N):
    cipher=binexp(number,e,N)
    return cipher

#For decrypting cipher number
def decryption_cipher(cipher,d,n):
    decrypted_num=binexp(cipher,d,N)
    return decrypted_num

length=int(input("Enter length of prime no.: "))
p=primegenerator(length)
q=primegenerator(length)
print(p)
print(q)

#Calculate N=p*q and Euler Totient Function=(p-1)*(q-1)
N=p*q
print("N",N)
phi=(p-1)*(q-1)
print("phi(N)",phi)
#generate public key e
e=generate_e(length,phi)
print("public key",e)
#generate private key d
d=gcdExtended(e,phi)
print("private key",d)
message=input("Enter message to be encrypted :")
if(message.isdigit()):
    message_num=int(message)
    cipher=encryption_num(message_num,e,N)
    print("cipher",cipher)
    decrypted_num=decryption_cipher(cipher,d,N)
    print("decrypted_num",decrypted_num)
else:
    encrypted=encryption(message,e,N)
    print("encrypted matrix",encrypted)
    decrypted_message=decryption(encrypted,d,N)
    print("decrypted_message",decrypted_message)

