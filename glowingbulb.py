



def num_glowing(n, primes):
    if len(primes) == 0:
        return 0
    p = primes[0]
    m = n // p
    
    ps = primes[1:]
    return m + num_glowing(n, ps) - num_glowing(m, ps)
 
 

s = ["0110000000000000000000000000000000000000",
"0010000000000000000000000000000000000000",
"0100000000100000001000100000101000001000"]
k = [5, 5, 16807]

for _ in range(t):
    switches = []
    for i in range(len(s)):
        if s[i] == '1':
            switches.append(i + 1)
    left = 1
    right = 40 * k
    u = 0
    v = num_glowing(right, switches)
    while left + 1 < right:
        mid = (left * (v - k) + right * (k - u)) // (v - u)
        if mid <= left:
            mid += 1
        if mid >= right:
            mid -= 1
        x = num_glowing(mid, switches)
        if x >= k:
            right = mid
            v = x
        else:
            left = mid
            u = x
    print(right)