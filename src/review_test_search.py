import random

def random_str(x, char_list):
    return "".join([random.choice(char_list) for _ in range(x)])

def search_string(string, pattern):
    i = 0
    j = 0
    lp = len(pattern)
    ls = len(string)
    ans = []
    while i <= ls-1:
        if string[i] == pattern[j]:
            if j == lp-1:
                ans.append(i-lp+1)
                i +=1
                j = 0
            else:
                i += 1
                j += 1
        else:
            i = i-j+1
            j = 0
    if not ans:
        ans = -1
    return ans

string = random_str(10000,["A","B","C","D","E"])
print(search_string(string,"ABCDE"))

import re

L =[]
check = re.finditer(r"ABCDE", string)
for i in check:
    L.append(i.span()[0])
print(L)