a = "0100000000100000001000100000101000001000"
b = 16807
import re
def pos_1(a, d = []):
    if "1" in a:
        i = a.index("1")
        a[i] = 0
        d.append(i+1)
        pos_1(a, d)
    return d
    
print(pos_1(list(a)))        
    
