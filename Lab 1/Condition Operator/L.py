a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a == c or b == d) or (a + b == c + d or a - b == c - d):
    print("YES")
else:
    print("NO")