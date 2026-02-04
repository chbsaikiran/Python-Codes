def can_stack(blocks):
    left = 0
    right = len(blocks) - 1
    last = float('inf')  # size of the previously placed cube

    while left <= right:
        if blocks[left] <= last and blocks[right] <= last:
            # pick the larger one to keep future options open
            if blocks[left] >= blocks[right]:
                last = blocks[left]
                left += 1
            else:
                last = blocks[right]
                right -= 1
        elif blocks[left] <= last:
            last = blocks[left]
            left += 1
        elif blocks[right] <= last:
            last = blocks[right]
            right -= 1
        else:
            return "No"

    return "Yes"


# -------- Main --------
T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    blocks = list(map(int, input().split()))
    print(can_stack(blocks))

