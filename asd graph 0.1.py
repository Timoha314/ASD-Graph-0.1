with open('input.txt', 'r') as file:
    n,m = map(int, file.readline().split())
    matrix = [[0] * n for _ in range(n)]
    for i in range(m):
        u,v = map(int, file.readline().split())
        matrix[u-1][v-1]=1
        matrix[v-1][u-1] = 1

with open('output.txt', 'w') as output_file:
    for row in matrix:
        output_file.write(' '.join(map(str, row)) + '\n')