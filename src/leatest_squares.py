import numpy as np

def main():
    x, y = [], []
    
    n = 5 # データ数
    print("フィッティングさせる方程式の次元数を入力してください")
    k = int(input()) # 次元数

    S = np.zeros((k+1, k+2))
    T = np.zeros((k+1, 1))

    print("データを入力してください")
    for i in range(n):
        print("x_{}=".format(i), end="")
        x.append(float(input()))
        print("y_{}=".format(i), end="")
        y.append(float(input()))
    
    for i in range(k+1):
        for j in range(k+1):
            S[i][j] = sum([xs**(i+j) for xs in x])
        S[i][k+1] = sum([yt*(xt**i) for xt in x for yt in y])
    # for i in range(k+1):
    #     T[i][0] = sum([yt*(xt**i) for xt in x for yt in y])
    print(S)

    a = gauss_j(S, k)
    
def gauss_j(S, k):
    for n in range(k+1):
        pivot = S[n][n]
        for i in range(k+2):
            S[n][i] /= pivot

        for i in range(k+1):
            if i != n:
                d = S[i][n]
                for j in range(k+2):
                    S[i][j] -= d * S[n][j]

    print(S)
    for i in range(k+1):
        print(S[i][k+1])

main()