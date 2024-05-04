import numpy as np

# the rules of the ipExchange,the keyExchange1 and the keyExchange2 :
ipExchange = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17, 9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7,
]

keyExchange1 = [
    57,49,41,33,25,17,9,1,
    58,50,42,34,26,18,10,2,
    59,51,43,35,27,19,11,3,
    60,52,44,36,63,55,47,39,
    31,23,15,7,62,54,46,38,
    30,22,14,6,61,53,45,37,
    29,21,13,5,28,20,12,4
]

keyExchange2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

E_extentionBox = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]
# S_Box
S_Box1 = np.array([
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
    ])
S_Box2 = np.array([
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
    ])
S_Box3 = np.array([
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
    ])
S_Box4 = np.array([
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
    ])
S_Box5 = np.array([
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
    ])
S_Box6 = np.array([
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
    ])
S_Box7 = np.array([
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
    ])
S_Box8 = np.array([
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11],
    ])
S_Box = np.array([S_Box1,S_Box2,S_Box3,S_Box4,S_Box5,S_Box6,S_Box7,S_Box8])

# P-Box：
P_Box = [
    16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25,
]

# reverseReplacement:
re_Box = [
    40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,33,1,41, 9,49,17,57,25,
]

# the plaintext and the key:
plainText = "0011100011010101101110000100001011010101001110011001010111100111"

Key = "1010101100110100100001101001010011011001011100111010001011010011"

# Initial IP replacement:
def initialIpReplacement():
    text = [0]*64
    for i in range(64):
        text[i] = plainText[ipExchange[i]-1]
    return text

# key genration:
def keyGenration():
    KEY = []
    key0 = [0]*56
    for i in range(56):
        key0[i] = Key[keyExchange1[i]-1] 
    c = key0[0:28]
    d = key0[28:56]
    for _ in range(16):
        key = [0]*48
        if _ == 0 or _ == 1 or _ == 8 or _ == 15:
            c = c[1:28] + c[0:1]
            d = d[1:28] + d[0:1]
        else:
            c = c[2:28] + c[0:2]
            d = d[2:28] + d[0:2]
        unionkey = c + d
        # print(unionkey)
        for j in range(48):
           key[j] = unionkey[keyExchange2[j]-1]
        # print(key)
        KEY.append(key)
        # print(KEY[_])
    return KEY

# E-extention：
def E_extention( R ):
    rightText = [0]*48
    for i in range(48):
        rightText[i] = R[E_extentionBox[i]-1]
    return rightText

# S-Box replacement:
def S_BoxReplacement(KEY, rightText):
    changedtext = [0]*8
    tmp = [0]*48
    result = [0]*32
    rightText = E_extention(rightText)
    for k in range(48):
        tmp[k] = int(rightText[k]) ^ int(KEY[k])
    for i in range(8):
        changedtext[i] = bin(S_Box[i,tmp[i*6+0]*2+tmp[i*6+5],tmp[i*6+1]*8+tmp[i*6+2]*4+tmp[i*6+3]*2+tmp[i*6+4]])[2:].zfill(4)
    for i in range(32):
        for j in range(8):
            for k in range(4):
                result[i] = changedtext[j][k]
    return result

# P-Box replacement:
def P_BoxReplacement(S_BoxResult):
    result = [0]*32
    for i in range(32):
        result[i] = S_BoxResult[P_Box[i]-1]
    return result

if __name__ == "__main__":

    chengedIp = initialIpReplacement()
    leftText = chengedIp[0:32]
    rightText = chengedIp[32:64]
    KEY = keyGenration()
    for i in range(16):
        print(KEY[i])

    for i in range(16):
        tmp = leftText[:]
        leftText = rightText[:]
        P_Text = P_BoxReplacement( S_BoxReplacement(KEY[i],rightText) )
        for j in range(32):
            rightText[j] = int(tmp[j]) ^  int(P_Text[j])
        print("LeftText:",leftText)
        print("RightText:",rightText)

    secretText = [0]*64
    for i in range(64):
        secretText[i] = (leftText+rightText)[re_Box[i]-1]
    
    for i in range(16):
        print(secretText[i*4+0],end = '')
        print(secretText[i*4+1],end = '')
        print(secretText[i*4+2],end = '')
        print(secretText[i*4+3],end = ' ')