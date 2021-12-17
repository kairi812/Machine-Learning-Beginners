'''
Create date : 2021/12/16.
Update      : 2021/12/17.
Writer      : Nishimura Kairi
'''

import numpy as np

def ransac(x, y, z, roll, pitch, yaw, data, k_max=100):
    k = 0
    n_sample = 3 # サンプル数
    num_inlier = 100 # インライア数の設定 -> 更新処理かける
    while k < k_max:
        ### データ長さに対して n_sample 個のインデックスを取得 ###
        theta_k = np.random.choice(len(x), n_sample, replace=False)

        ### 平面の方程式算出 ###
        p_t, q_t, r_t, d_t= calc_plane_equation(x, y, z, theta_k)
        p_r, q_r, r_r, d_r = calc_plane_equation(roll, pitch, yaw, theta_k)

        ### 全ての点に対してフィットしているか探索 ###
        err = 0.3
        cnt = 0
        inlier_points = []
        for x, y, z, roll, pitch, yaw in x, y, z, roll, pitch, yaw:
            ### 並進・回転の観測値を取得 ###
            observe_val_t = calc_observe_val(x, y, z, p_t, q_t, r_t, d_t)
            observe_val_r = calc_observe_val(roll, pitch, yaw, p_r, q_r, r_r, d_r)
            ### 閾値判断 ###
            if err > abs(observe_val_t) and err > abs(observe_val_r):
                inlier_points.append([x, y, z, roll, pitch, yaw])
                cnt += 1
                ### カウント数が設定したインライア数を超えている場合は更新 ###
                if cnt >= num_inlier:
                    num_inlier = cnt
                    best_inlier_points = inlier_points

        ### インライアが多いサンプリング点を返す ###
        return best_inlier_points

### 平面の係数算出関数 ###
def calc_plane_equation(x, y, z, theta_k):
        x0, y0, z0 = x[theta_k[0]], y[theta_k[0]], y[theta_k[0]]
        x1, y1, z1 = y[theta_k[1]], y[theta_k[1]], y[theta_k[1]]
        x2, y2, z2 = z[theta_k[2]], z[theta_k[2]], z[theta_k[2]]
        ### 外積計算 ###
        p = (y1-y0)*(z2-z0) - (z1-z0)*(y2-y0)
        q = (z1-z0)*(x2-x0) - (x1-x0)*(z2-z0)
        r = (x1-x0)*(y2-y0) - (y1-y0)*(x2-x0)

        d = -p*x0 - q*y0 - r*z0 # 平面の方程式

        return p, q, r, d

### 観測値算出関数 ###
def calc_observe_val(x, y, z, p, q, r, d):
    observe_val = p * x + q * y + r * z + d
    return observe_val
