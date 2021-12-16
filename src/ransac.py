import numpy as np

def ransac(x, y, z, roll, pitch, yaw,
           data, U, eta_0,  k_max=100, t=2.0):
    k = 0
    I_max = 0
    n_sample = 3 # サンプル数
    num_inlier = 300
    while k < k_max:
        ### データ長さに対して n_sample 個のインデックスを取得 ###
        theta_k = np.random.choice(len(data), n_sample, replace=False)
        # ### モデルの ###
        # x_set = x[theta_k]
        # y_set = y[theta_k]
        # z_set = z[theta_k]
        # roll_set = roll[theta_k]
        # pitch_set = pitch[theta_k]
        # yaw_set = yaw[theta_k]

        S = []
        for theta in theta_k:
            S.append([x[theta], y[theta], z[theta], roll[theta], pitch[theta], yaw[theta]])

        a1, a2, a3, a4, a5, a6, observe_val = gauss_j(S, len(data))

        err = 0.3
        cnt = 0
        for x, y, z, roll, pitch, yaw in data:
            get_val = a1*x + a2*y + a3*z + a4*roll + a5*pitch + a6*yaw
            if err > abs(get_val - observe_val):
                cnt += 1
                if cnt >= num_inlier:
                    cnt = num_inlier


### ガウス・ジョルダン法による方程式の解算出 ###
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
                    
    for i in range(k+1):
        print(S[i][k+1])
