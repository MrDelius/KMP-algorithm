n = "лилила"
m = "лилилось лилилась"

p = [0]*len(n)
i=0
j=1

# while the suffix is less than the length of massive n
while j<len(n):
    # if prefix is equivalent to suffix
    if n[i] == n[j]:
        print()
        # add 1 to the suffix
        p[j] = i+1
        # and move both prefix and suffix forward to 1
        i+=1
        j+=1
    # if prefix is not equivalent to suffix
    else:
        # check if i- prefix position is 0 (remember here we check the position of prefix not the value)
        if i == 0:
            # make suffix = 0 and go to the next suffix to check
            p[j]=0
            j+=1
        # else if prefix position is not 0, go back 1 by 1 every previous prefix for equivalency with the suffix
        else:
            i = p[i-1]

print(n)
print(p)

a = len(m)
b = len(n)
i = 0
j = 0

while i < a:
    if m[i] == n[j]:
        i += 1
        j += 1
        if j == b:
            print("the word is found")
            break
    else:
        if j > 0:
            j = p[j-1]
            print("i =", i, '\n', "j =", j)
        else:
            i += 1

if i == a:
    print("the word is not found")

"""
else:
    if j > 0:
        j = p[j-1]
    else:
        i += 1
If there was a partial match (i.e., j > 0), the code updates j to p[j-1].
This effectively tells the algorithm to skip checking the characters of the pattern that have already matched, utilizing the information stored in the p array.
The value p[j-1] gives the length of the longest prefix of the pattern that is also a suffix. This allows you to check only the necessary part of the pattern rather than starting from scratch.
"""