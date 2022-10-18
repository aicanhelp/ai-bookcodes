import sys
import os
import time
import numpy as np
import scipy.spatial.distance as dist


class Test_Distance:
    def test_distance1(self):
        # Euc distance
        vector1 = np.mat([1, 2, 3])
        vector2 = np.mat([4, 7, 5])
        print(np.sqrt((vector1 - vector2) * (vector1 - vector2).T))

        # cosine distance
        Lv1 = np.sqrt(vector1 * vector1.T)
        Lv2 = np.sqrt(vector2 * vector2.T)
        cosV12 = vector1 * vector2.T / (Lv1 * Lv2)
        print(cosV12)

    def test_distance_cosine(self):
        Vector1 = np.array([1, 1, 0, 1, 0, 1, 0, 0, 1])
        Vector2 = np.array([0, 1, 1, 0, 0, 0, 1, 1, 1])
        matV = np.mat([Vector1, Vector2])
        print(matV, dist.pdist(matV), dist.cdist(matV, matV, 'cosine'))

    def test_distance_manha(self):
        Vector1 = np.array([1, 3, 0, 1, 0, 1, 0, 0, 1])
        Vector2 = np.array([0, 1, 1, 0, 0, 0, 1, 5, 1])
        print("Manhatan distance: ", np.sum(np.abs(Vector1 - Vector2)))
        print("Chebe distance: ", np.abs(Vector1 - Vector2).max())

    def test_L2(self):
        v = np.mat([1, 2, 3])
        l2_0 = np.sqrt(np.sum(np.power(v, 2)))
        l2_1 = np.sqrt(v * v.T)
        l2_2 = np.linalg.norm(v)
        print("L2 or Euc: %d, %d, %d" % (l2_0, l2_1, l2_2))

    def test_hanming(self):
        Vector1 = np.array([1, 3, 0, 1, 0, 1, 0, 0, 1])
        Vector2 = np.array([0, 1, 1, 0, 0, 0, 1, 5, 1])
        mat = np.mat([Vector1, Vector2])
        nonzero = np.nonzero(mat[0] - mat[1])
        print("nonzero: %s, shape: %d" % (nonzero, np.shape(nonzero[1])[0]))

    def test_distance_jaccard(self):
        Vector1 = np.array([1, 1, 0, 1, 0, 1, 0, 0, 1])
        Vector2 = np.array([0, 1, 1, 0, 0, 0, 1, 1, 1])
        matV = np.mat([Vector1, Vector2])
        print(matV, dist.pdist(matV), dist.cdist(matV, matV, 'jaccard'))


class Test_Linag:
    A = np.mat([[1, 2, 4, 5, 7, ], [9, 12, 11, 8, 2, ], [6, 4, 3, 2, 1, ], [9, 1, 3, 4, 5], [0, 2, 3, 4, 1]])

    def test_det(self):
        print("方阵的行列式 det(A):", np.linalg.det(self.A))
        print("矩阵的逆 inv(A):", np.linalg.inv(self.A))
        print("矩阵的对称: ", self.A.T)
        print("矩阵的秩:", np.linalg.matrix_rank(self.A))
        # 可逆矩阵求解
        b = [1, 0, 1, 0, 1]
        S = np.linalg.solve(self.A, np.transpose(b))
        print(S)


class Test_prob:
    featuremat = np.mat([[88.5, 96.8, 104.1, 111.3, 117.7, 124.0, 130.0, 135.4, 140.2, 145.3, 151.9, 159.5, 165.9,
                          169.8, 171.6, 172.3, 172.7],
                         [12.54, 14.65, 16.64, 18.98, 21.26, 24.06, 27.33, 30.46, 33.74, 37.69, 42.49, 48.08, 53.37,
                          57.08, 59.35, 60.68, 61.40]])

    def test_correcof(self):
        # 计算均值
        mv1 = np.mean(self.featuremat[0])
        mv2 = np.mean(self.featuremat[1])
        # 计算两列标准差
        dv1 = np.std(self.featuremat[0])
        dv2 = np.std(self.featuremat[1])

        corref = np.mean(np.multiply(self.featuremat[0] - mv1, self.featuremat[1] - mv2)) / (dv1 * dv2)
        print("corref1:", corref)

        # cal by lib
        print("corref2:", np.corrcoef(self.featuremat))

        print("cov: ", np.cov(self.featuremat))
        # 计算马氏距离
        covinv = np.linalg.inv(np.cov(self.featuremat))
        print("covinv: ", covinv)
        tp = self.featuremat.T[0] - self.featuremat.T[1]
        distma = np.sqrt(np.dot(np.dot(tp, covinv), tp.T))
        print("distma:", distma)
