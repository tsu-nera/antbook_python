N = 6
S = "ACDBCB"

T = ""

a = 0
b = N - 1

while a <= b:
    left = False
    for i in range(0, b - a):
        if S[a + 1] < S[b - i]:
            left = True
            break
        elif S[a + 1 > S[b - 1]]:
            left = False
            break

    if left:
        print S[a]
        a += 1
    else:
        print S[b]
        b -= 1
