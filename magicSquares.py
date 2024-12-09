import sys
rows = []
for line in sys.stdin:
    rows.append(list(map(int, line.split())))
def isMagicSquare(rows):
    n = len(rows)
    sumOfSquare = 0
    for i, row in enumerate(rows):
        if 0 in row:
            zeroContainingRow = row
            zeroContainingIndex = i
            zeroIndex = row.index(0)
            break
    for i, row in enumerate(rows):
        if i != zeroContainingIndex:
            sumOfSquare = sum(row)
            break
    neededNum = sumOfSquare - sum(zeroContainingRow)
    zeroContainingRow[zeroIndex] = neededNum
    for row in rows:
        if sum(row) != sumOfSquare:
            print("Can't be magic")
            return
    for col in range(n):
        if sum(row[col] for row in rows) != sumOfSquare:
            print("Can't be magic")
            return
    if sum(rows[i][i] for i in range(n)) != sumOfSquare:
        print("Can't be magic")
        return
    if sum(rows[i][n - i - 1] for i in range(n)) != sumOfSquare:
        print("Can't be magic")
        return
    for row in rows:
        print(" ".join(map(str, row)))
isMagicSquare(rows)