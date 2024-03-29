s = list(map(int, input().split()))
n = s[0]
k = s[1]
m = s[2]
all_kids = int(n * 2 / k) + 1 * int((n * 2 % k) != 0) + 1 * int(n * 2 <= k)
print(all_kids * m)
