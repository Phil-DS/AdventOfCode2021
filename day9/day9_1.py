from day9_data import data

cnt = 0
for i,row in enumerate(data):
    for j,n in enumerate(row):
        if i != 0 and data[i-1][j] <= n:
            continue
        if j != 0 and data[i][j-1] <= n:
            continue
        if i != 99 and data[i+1][j] <= n:
            continue
        if j != 99 and data[i][j+1] <= n:
            continue
        cnt += 1 + n

print(cnt)
            