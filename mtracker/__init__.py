def f(x: int):
    if x != -1:
        x += 1
    return x
def sapper(arr: list, mini: list):
    for x, y in mini:
        arr[x][y] = -1
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                arr[x+i][y+j] = f(arr[x+i][y+j])
    return arr
n, m, k = map(int, input('Введите размер поля и кол-во мин (x y n): ').split())
n += 2
m += 2
mini = [[int(input()) for c in range(2)] for k in range(k)]
arr = [[0 for j in range(m)] for i in range(n)]
arr = sapper(arr, mini)
for i in range(1, n-1):
    print(*arr[i][1:m-1])
