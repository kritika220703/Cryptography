from utils.helper_functions import *
from utils.constants import *
from utils.operators import *
import datetime
import random

#convert K values in hex form to list of lists containing K values in bit form
k=[]
for word in K:
    kvalue=[]
    for c in bin(int(word,16))[2:].zfill(32):
        kvalue.append(int(c))
    k.append(kvalue)

#for buffer values
buffers=[]
for word in buffer_values:
    bufferValue=[]
    for c in bin(int(word,16))[2:].zfill(32):
        bufferValue.append(int(c))
    buffers.append(kvalue)

def SHA_256(message):
    #converting string to bit form and appending bits
    msg_bits = appending_bits(message)

    #breaking bits in chunks of 512
    chunks = chunking(msg_bits, 512)

    for chunk in chunks:
        w = chunking(chunk, 32)

        for i in range(48):
            w.append(32*[0])

        for i in range(16,64):
            s0 = XOR2(right_rotate(w[i-15],7), right_rotate(w[i-15],18), shift_right(w[i-15],3))
            s1 = XOR2(right_rotate(w[i-2],17), right_rotate(w[i-2],19), shift_right(w[i-2],10))
            w[i] = add(add(add(w[i-16],s0),w[i-7]),s1)

        a, b, c, d, e, f, g, h = buffers

        for i in range(64):
            ch = XOR1(AND(e,f), AND(NOT(e),g))
            ma = XOR2(AND(a,b), AND(a,c), AND(b,c))
            s0 = XOR2(right_rotate(a,2), right_rotate(a,13), right_rotate(a,22))
            s1 = XOR2(right_rotate(e,6), right_rotate(e,11), right_rotate(e,25))
            t1 = add(add(add(add(h, s1),ch), k[i]), w[i])
            t2 = add(s0,ma)

            h = g
            g = f
            f = e
            e = add(d,t1)
            d = c
            c = b
            b = a
            a = add(t1, t2)

        buffers[0] = add(buffers[0], a)
        buffers[1] = add(buffers[1], b)
        buffers[2] = add(buffers[2], c)
        buffers[3] = add(buffers[3], d)
        buffers[4] = add(buffers[4], e)
        buffers[5] = add(buffers[5], f)
        buffers[6] = add(buffers[6], g)
        buffers[7] = add(buffers[7], h)

    has_val = ""
    for i in range(len(buffers)):
        has_val += bin2hex(buffers[i])
    
    return has_val

def otp():
    current_datetime = datetime.datetime.now()
    hash_value = SHA_256(str(current_datetime))
    hash_value = int(hash_value,16)
    n = random.randint(100000,999999)
    print("OTP IS: ",hash_value%n)
    
    
msg = input("Type your message: ")
print("Your input: ", msg)
print("Hash value: ", SHA_256(msg))
otp()

        

