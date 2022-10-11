# fs

def create_array_2d(n):
    return [[0] * n for a in range(n)]

def create_array_2d_ij(i, j):
    return [[0] * j for a in range(i)]

def create_array_2d_fill(n, fill):
    return [[fill] * n for a in range(n)]

def create_array_2d_fill_ij(i, j, fill):
    return [[fill] * j for a in range(i)]

def print2d(a, n):
    for i in range(n):
        result=""
        for j in range(n):
            result = result + a[i][j] + " "
        print(result)

def fibonanci(n):
    a = [0] * n
    for i in range(n):
        if i > 1:
            a[i] = a[i-1] + a[i-2]
        else:
            a[i] = 1
    return a

def fibonanci_start_with(start_with, n):
    a = [0] * n
    for i in range(n):
        if i > 1:
            a[i] = a[i-1] + a[i-2]
        else:
            a[i] = start_with
            if start_with == 0:
                start_with += 1
    return a

# fs