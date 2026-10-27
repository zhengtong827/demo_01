
# 计算两点欧氏距离
import math
import numpy as np

def euclidean_distance_np(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    return np.linalg.norm(p1 - p2)

if __name__ == '__main__':
    p1=(1,2)
    p2=(4,6)
    print(euclidean_distance_np(p1, p2))

