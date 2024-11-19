import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def main() -> None:
    dataset = "../images/faces"
    images, labels = [], []

    for person_id in range(1, 41):
        person_folder = os.path.join(dataset, f"s{person_id}")
        for img_file in os.listdir(person_folder):
            img_path = os.path.join(person_folder, img_file)
            img = cv2.imread(img_path)
            img_resized = cv2.resize(img, (112, 92))
            images.append(img_resized.flatten())
            labels.append(person_id)

    X = np.array(images)
    Y = np.array(labels)

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    # print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    knn = KNeighborsClassifier(n_neighbors=4)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    print(f"KNN Accuracy: {accuracy_score(y_test, y_pred)}")

if __name__ == '__main__':
    main()
