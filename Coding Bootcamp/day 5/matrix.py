
import random
row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))

grid = [[random.randint(1, 100) for _ in range(col)] for _ in range(row)]
for i in grid:
    for element in i:
        print(f"{element:3}", end=" ")
    print()

outer_sum = 0
inner_sum = 0

for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            outer_sum += grid[i][j]
        else:
            inner_sum += grid[i][j]
            
    if outer_sum == inner_sum:
        print("Outer and inner sums are equal.")
        for row in grid:
            print(row)
        print(f"\nOuter Layer Sum: {outer_sum}")
        print(f"Inner Layer Sum: {inner_sum}")
        break

print(f"Sum of outer elements: {outer_sum}")
print(f"Sum of inner elements: {inner_sum}")
