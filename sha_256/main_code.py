from utils.helper_functions import *
from utils.constants import *

#convert K values in hex form to list of lists containing K values in bit form
k=[]
for word in K:
    kvalue=[]
    for c in bin(word)[2:].zfill(32):
        kvalue.append(int(c))
    k.append(kvalue)

#for buffer values
buffers=[]
for word in buffer_values:
    bufferValue=[]
    for c in bin(word)[2:].zfill(32):
        bufferValue.append(int(c))
    buffers.append(kvalue)

def SHA_256(message):
    #converting string to bit form and appending bits
    msg_bits = appending_bits(message)

    #breaking bits in chunks of 512
    chunks = chunking(msg_bits, 512)

    
