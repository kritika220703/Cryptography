def xor(x, y):
    if((x==1 and y==0) or (x==0 and y==1)):
        return 1
    else:
        return 0
    
def XOR1(l1,l2):
    ans=[]
    for (i,j) in zip(l1, l2):
        ans.append(xor(i,j))
    return ans
    
def XOR2(l1, l2, l3):
    ans=[]
    for (i,j,k) in zip(l1, l2, l3):
        ans.append(xor(xor(i,j),k))
    return ans

def add(l1, l2):
    length = len(l1)
    sum = list(range(length))
    carry = 0

    for i in range(length-1, -1, -1):
        sum[i]=xor(xor(l1[i],l2[i]),carry)
        carry = (l1[i]&l2[i]) | ((l1[i]&carry) | (l2[i]&carry))

    return sum

def shift_right(l, steps):
    return [0]*steps + l[:-steps]

def right_rotate(l, steps):
    return l[-steps:] + l[:-steps]

def NOT(l):
    ans=[]
    for i in l:
        if(i==0):
            ans.append(1)
        else:
            ans.append(0)
    return ans

def AND(l1, l2):
    ans=[]
    for (i,j) in zip(l1,l2):
        if(i==1 and j==1):
            ans.append(1)
        else:
            ans.append(0)
    return ans

