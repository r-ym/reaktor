import os
# dic = {}

base = "P"

with open("2.txt", "r") as f:
    sig = f.readline()
    b = "P"
    while True:
        dic = {}
        for i in range(0,len(sig)):
            if sig[i] == b:
                if sig[i+1] in dic:
                    dic[sig[i+1]] += 1
                else:
                    dic[sig[i+1]] = 0
        b = max(dic, key=lambda k: dic[k])
        if b == ";":
            break
        else:
            base += b

# base = max(dic, key=lambda k: dic[k])
print(base)

