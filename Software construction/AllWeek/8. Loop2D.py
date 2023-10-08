"""
Enter n: 5
    x 
   x x 
  x x x 
 x x x x 
x x x x x 
"""
# n = int(input("Enter n: "))

# for i in range(n):
#     spaces = " " * (n - i - 1)
#     x_chars = "x " * (i + 1)
#     print(spaces + x_chars)

def generate_chessboard_with_rook(row, col, size):
    for i in range(size):
        print("-" * (size * 4 + 1))
        for j in range(size):
            if i == row and j == col:
                print(f"| | | |R", end="")
            else:
                print("| | | | ", end="")
        print("|")

    print("-" * (size * 4 + 1))

row = int(input("Enter Rook's row position: "))
col = int(input("Enter Rook's column position: "))
size = 8  # You can adjust the size of the chessboard as needed
generate_chessboard_with_rook(row, col, size)
