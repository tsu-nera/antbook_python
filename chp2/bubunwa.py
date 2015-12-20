n = 4
a = [1, 2, 4, 7]
k = 13

# n = 4
# a = [1, 2, 4, 7]
# k = 15

def dfs(i, acc):
    if i == n: return acc == k

    if dfs(i + 1, acc): return True
    if dfs(i + 1, acc + a[i]): return True

    return False

if dfs(0, 0):
    print "Yes"
else:
    print "No"
