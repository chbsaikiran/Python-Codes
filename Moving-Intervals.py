import sys

input = sys.stdin.readline

N, K, F = map(int, input().split())

intervals = []
lengths = []

for _ in range(K):
    l, r = map(int, input().split())
    intervals.append((l, r))
    lengths.append(r - l + 1)

if F == 0:
    intervals.sort()
    prev_end = -10**18

    for l, r in intervals:
        if l < prev_end:
            print("Bad")
            sys.exit(0)
        prev_end = max(prev_end, r)

    print("Good")
    sys.exit(0)

lengths.sort()

cur = 1

for L in lengths:
    if cur + L - 1 > N:
        print("Bad")
        sys.exit(0)
    cur += L

print("Good")

