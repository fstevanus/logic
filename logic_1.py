from util import print2d, create_array_2d_fill

# print("n = "),
# n = input()
# fill = input("fill with ")
n = 9
fill = "-"

print("logic 1")
a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = "*"

print2d(a, n)
print("")

print("logic 2")
a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            a[i][j] = "*"

print2d(a, n)
print("")

print("logic 3")
a = create_array_2d_fill(n, fill)
a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if i + j == n - 1 or i == j:
            a[i][j] = "*"

print2d(a, n)
print("")

print("logic 3")
a = create_array_2d_fill(n, fill)
a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if i == n/2 or j == n/2:
            a[i][j] = "*"

print2d(a, n)
print("")

print("logic 4")
a = create_array_2d_fill(n, fill)
a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if i == n-1 or j == n-1 or i == 0 or j == 0:
            a[i][j] = "*"

print2d(a, n)
print("")

print("logic 5")
a = create_array_2d_fill(n, fill)
a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if j <= n/2:
            if j + i == n/2:
                a[i][j] = "*"
                a[n-1-i][j] = "*"
                a[i][n-1-j] = "*"
      
print("logic 6")
a = create_array_2d_fill(n, fill)
print2d(a, n)
print("")

a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if i == n-1 or j == n-1 or i == 0 or j == 0 or i + j == n - 1 or i == j:
            a[i][j] = "*"

print2d(a, n)
print("")


a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if i == n/2 or j == n/2 or i + j == n - 1 or i == j:
            a[i][j] = "*"

print2d(a, n)
print("")

a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if i == n-1 or j == n-1 or i == 0 or j == 0 or i == n/2 or j == n/2 or i + j == n - 1 or i == j:
            a[i][j] = "*"

print2d(a, n)
print("")

a = create_array_2d_fill(n, fill)
for i in range(n):
    for j in range(n):
        if j <= n/2:
            if j + i == n/2:
                a[i][j] = "*"
                a[n-1-i][j] = "*"
                a[i][n-1-j] = "*"
                a[n-1-i][n-1-j] = "*"
        
        if i == n-1 or j == n-1 or i == 0 or j == 0 or i == n/2 or j == n/2 or i + j == n - 1 or i == j:
            a[i][j] = "*"
        
print2d(a, n)
print("")