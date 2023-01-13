from collections import defaultdict

testCases = int(input())

for idx in range(testCases):
    rows, cols = map(int, input().split())
    board = []

    for row in range(rows):
        temp = list(map(int, input().split()))
        board.append(temp)

    posIdx = defaultdict(int)
    negIdx = defaultdict(int)

    for r in range(rows):
        for c in range(cols):
            posIdx[r + c] += board[r][c]
            negIdx[r - c] += board[r][c]

    maxSum = 0

    for rIdx in range(rows):
        for cIdx in range(cols):
            total = (posIdx[rIdx + cIdx] + negIdx[rIdx - cIdx]) - board[rIdx][cIdx]

            maxSum = max(maxSum, total)

    print(maxSum)
