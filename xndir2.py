#xndir2.py to remove the  n-th index character from a nonempty string.
z = "abcdefg"
n = 3
i = z[:n]+z[n+1:]
print(i)