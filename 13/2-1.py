data = [] # 초기 맵 리스트

data.append(list(map(int, 00)))
data.append(list(map(int, 00)))

def dfs(count):
    for i in range(2):
        for j in range(2):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

if __name__ == "__main__":
    dfs(0)