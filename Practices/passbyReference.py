def swap(s1, s2):
    return s2, s1

s1 = 'a'
s2 = 'b'
print("Before swapping: x =", s1, ", y =", s2)
s1, s2 = swap(s1, s2)
print("After swapping: x =", s1, ", y =", s2)