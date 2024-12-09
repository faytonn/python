def count_tile_positions(N, M, board):
    h_count = 0
    v_count = 0

    for row in board:
        count = 0
        for cell in row:
            if cell == 0:
                count += 1
            else:
                if count >= N:
                    h_count += (count - N + 1)
                count = 0
        if count >= N:
            h_count += (count - N + 1)

    for col in range(M):
        count = 0
        for row in range(M):
            if board[row][col] == 0:
                count += 1
            else:
                if count >= N:
                    v_count += (count - N + 1)
                count = 0
        if count >= N:
            v_count += (count - N + 1)

    return h_count + v_count

def main():
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0

    if idx >= len(data):
        return

    N = int(data[idx])
    idx += 1

    while idx < len(data):
        if idx >= len(data):
            break
        M = int(data[idx])
        idx += 1
        if M == 0:
            break
        board = []
        for _ in range(M):
            row = []
            for _ in range(M):
                if idx >= len(data):
                    row.append(1) 
                else:
                    num = int(data[idx])
                    row.append(num)
                    idx += 1
            board.append(row)
        total = count_tile_positions(N, M, board)
        print(total)

if __name__ == "__main__":
    main()
