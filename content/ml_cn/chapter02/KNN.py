import numpy as np
from collections import Counter


class KNN:
    def __init__(self, train_x, train_y, n, distance_fn=None):
        self.__train_x = train_x
        self.__train_y = train_y
        self.__n = n
        self.__distance_fn = distance_fn if distance_fn else self.__cosine_distance

    def __euc_distance(self, X1, X2):
        return np.sqrt((X1 - X2) * (X1 - X2).T)

    def __cosine_distance(self, X1, X2):
        return - X1 * X2.T / (np.sqrt(X1 * X1.T) * np.sqrt(X2 * X2.T))

    def predict(self, X):
        distances = np.array(np.zeros(len(self.__train_x)))
        for i in range(len(self.__train_x)):
            distances[i] = self.__distance_fn(self.__train_x[i], X)
        distances_sorted_indexes = np.argsort(distances)

        n_labels = []
        for idx in distances_sorted_indexes[:self.__n]:
            n_labels.append(self.__train_y[idx])

        print(distances, distances_sorted_indexes, n_labels_count)

        return Counter(n_labels_count).most_common(1)[0]


def test_knn():
    train_x = np.mat([[1, 1], [1, 2], [2, 1], [1, 4], [0, 4], [7, 8], [8, 9], [8, 8], [6, 9], [9, 6]])
    train_y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    knn = KNN(train_x, train_y, 5)
    print(knn.predict(np.mat([0, 2])))
