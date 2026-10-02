n = str(input())
pl = ""
s = 1;
mrl = ""
mrc = 1

for char in n:
    if char == pl:
        s += 1;
        
        if s > mrc:
            mrl = char
            mrc = s
    else:
        s = 1
    pl = char;
    
print(mrc)