import numpy as np

def main():
    x, y = [], []
    
    n = 2 # データ数
    print("フィッティングさせる方程式の次元数を入力してください")
    k = int(input()) # 次元数

    S = np.zeros((k+1, k+1))
    T = np.zeros((k+1, 1))

    print("データを入力してください")
    for i in range(n):
        x.append(float(input()))
        y.append(float(input()))
    
    for i in range(k+1):
        for j in range(k+1):
            S[i][j] = sum([xs**(i+j) for xs in x])
    
    for i in range(k+1):
        T[i][0] = sum([yt*(xt**i) for xt in x for yt in y])

    a = gauss_j(S, T, k)
    
def gauss_j(S, T, k):
    for k in range(k):
        pivot = S[k][k]
        for i in range(k+1):
            S[k][i] = S[k][i] / pivot

        for i in range(k):
            if i != k:
                d = S[i][k]
                for j in range(k+1):
                    S[i][j] = S[i][j] - d * S[k][j]

    for i in range(k):
        print(S[i][k])

main()