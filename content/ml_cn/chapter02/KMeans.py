import numpy as np

class KMeans:
    def __init__(self, dataset, k):
        self.__dataset = dataset
        self.__k = k

    def __euc_distance(self, X1, X2):
        return np.sqrt((X1 - X2) * (X1 - X2).T)

    def __cosine_distance(self, X1, X2):
        return - X1 * X2.T / (np.sqrt(X1 * X1.T) * np.sqrt(X2 * X2.T))

    def __rand_centers(self, dataset, k):
        n = np.shape(dataset)[1]
        cluster_centers = np.mat(np.zeros((k, n)))

        for col in range(n):
            min_col = np.min(dataset[:, col])
            max_col = np.max(dataset[:, col])
            cluster_centers[:, col] = np.mat(min_col + float(max_col - min_col) * np.random.rand(k, 1))
        return cluster_centers

    def train(self):
        m = np.shape(self.__dataset)[0]
        cluster_distances = np.mat(np.zeros(m, 2))
        cluster_centers = self.__rand_centers(self.__dataset, self.__k)

        flag = True
        while flag:
            flag = False
            for i in range(m):
                distance_list = [self.__euc_distance(cluster_centers[j], self.__dataset[i]) for j in range(self.__k)]
                min_distance = np.min(distance_list)
                min_index = distance_list.index(min_distance)
                if cluster_distances[i, 0] != min_index:
                    flag = True

                cluster_distances[i, :] = min_index, min_distance

            for i in range(self.__k):
                # 从ClustDist的第一列中筛选出等于cent值的行下标
                dInx = np.nonzero(cluster_distances[:, 0].A == i)[0]
                # 从dataSet中提取行下标==dInx构成一个新数据集
                p_in_cluster = self.__dataset[dInx]
                # 计算p_in_cluster各列的均值: mean(ptsInClust, axis=0):axis=0 按列计算
                cluster_centers[i, :] = np.mean(p_in_cluster, axis=0)

        return cluster_centers
