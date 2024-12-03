import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    np.random.seed()
    x = np.dot(np.random.rand(2, 2), np.random.randn(2, 100)).T

    x_mean = x - np.mean(x, axis=0)

    cov_matrix = np.cov(x_mean, rowvar=False)
    # print(cov_matrix)

    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    # print(eigenvalues, eigenvectors)
    x_pca = x_mean @ eigenvectors

    plt.scatter(x[:,0], x[:,1])
    plt.scatter(x_pca[:,0], x_pca[:,1], color='red')
    plt.quiver(0, 0, eigenvectors[0, 0], eigenvectors[1, 0], scale=3, label="PC1")
    plt.quiver(0, 0, eigenvectors[0, 1], eigenvectors[1, 1], scale=3, label="PC2")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()