import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


def load_faces(directory, image_size=(92, 112)):
    images = []
    for subdir in sorted(os.listdir(directory)):
        subdir = os.path.join(directory, subdir)
        if os.path.isdir(subdir):
            for filename in sorted(os.listdir(subdir)):
                filepath = os.path.join(subdir, filename)
                img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    img_resized = cv2.resize(img, image_size)
                    images.append(img_resized)
    return np.array(images)


def compute_eigenfaces(images, num_components=10):
    n_samples, h, w = images.shape
    flattened = images.reshape(n_samples, -1)

    mean_faces = np.mean(flattened, axis=0)
    centered_data = flattened - mean_faces

    covariance_matrix = np.dot(centered_data, centered_data.T)

    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, sorted_indices]

    eigenfaces = np.dot(centered_data.T, eigenvectors)

    eigenfaces = eigenfaces[:, :num_components]
    eigenfaces /= np.linalg.norm(eigenfaces, axis=0)

    return mean_faces, eigenfaces, (h, w)


def display_eigenfaces(mean_face, eigenfaces, image_shape):
    h, w = image_shape
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 6, 1)
    plt.title("Mean Face")
    plt.imshow(mean_face.reshape(h, w), cmap="gray")
    plt.axis('off')

    for i in range(eigenfaces.shape[1]):
        plt.subplot(2, 6, i + 2)
        plt.title(f"Eigenface {i + 1}")
        plt.imshow(eigenfaces[:, i].reshape(h, w), cmap="gray")
        plt.axis('off')
    plt.tight_layout()
    plt.show()


def main() -> None:
    images = load_faces("../images/faces")

    mean_face, eigenfaces, image_shape = compute_eigenfaces(images)

    display_eigenfaces(mean_face, eigenfaces, image_shape)


if __name__ == '__main__':
    main()