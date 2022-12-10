import jellyfish
from fuzzywuzzy import fuzz

word = 'Harshit'
cw1 = jellyfish.soundex(word)

ans = []

for l in open('./input_file.txt' , 'r').readlines():
    l = l.strip()
    cw2 = jellyfish.soundex(l)
    if fuzz.ratio(cw1,cw2) == 100:
        ans.append(l)


for w in ans:
    print(w)
