def string2bits(message):
    unicode_form=[]
    for i in message:
        unicode_form.append(ord(i))

    byte_form=[]
    for word in unicode_form:
        byte_form.append(bin(word)[2:].zfill(8))

    bits=[]
    for byte in byte_form:
        for bit in byte:
            bits.append(int(bit))

    return bits

def appending_bits(message):
    preprocessed_msg_bits=string2bits(message)
    length=len(preprocessed_msg_bits)

    length_bits=[]
    for c in bin(length)[2:].zfill(64):
        length_bits.append(int(c))

    preprocessed_msg_bits.append(1)

    while((len(preprocessed_msg_bits) + 64) % 512 != 0):
        preprocessed_msg_bits.append(0)

    preprocessed_msg_bits=preprocessed_msg_bits+length_bits

    return preprocessed_msg_bits

def chunking(bits, chunk_length):
    chunks=[]
    length=len(bits)
    for i in range(0,length,chunk_length):
        chunks.append(bits[i:i+chunk_length])

    return chunks

def bin2hex(msg):
    s1=""
    for i in msg:
        s1 = s1 + str(i)

    bin_value = "0b" + s1
    hex_value = hex(int(bin_value,2))
    return hex_value[2:]
