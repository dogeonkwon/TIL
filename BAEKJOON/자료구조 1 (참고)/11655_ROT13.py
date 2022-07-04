import sys

line = sys.stdin.readline().rstrip('\n')
ans = ''
for i in line:
    if i.isalpha():
        if i.isupper():
            k = ord(i) + 13
            if k > 90:
                k = 65 + (k-91)
                ans += chr(k)
            else:
                ans += chr(k)
        else:
            k = ord(i) + 13
            if k > 122:
                k = 97 + (k-123)
                ans += chr(k)
            else:
                ans += chr(k)
    else:
        ans += i
print(ans)