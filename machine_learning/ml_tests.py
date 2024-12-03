import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


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
    print(X.shape)
    Y = np.array(labels)

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    # print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    # knn = KNeighborsClassifier(n_neighbors=4)
    # knn.fit(x_train, y_train)
    # y_pred = knn.predict(x_test)
    # print(f"KNN Accuracy: {accuracy_score(y_test, y_pred)}")
    dtree = DecisionTreeClassifier(max_depth=5)
    dtree.fit(x_train, y_train)
    y_train_pred = dtree.predict(x_train)
    y_pred = dtree.predict(x_test)
    print(f"Decision Tree Train Accuracy: {accuracy_score(y_train, y_train_pred)}")
    print(f"Decision Tree Pred Accuracy: {accuracy_score(y_test, y_pred)}")
    # rforest = RandomForestClassifier(n_estimators=100, random_state=42)
    # rforest.fit(x_train, y_train)
    # y_train_pred = rforest.predict(x_train)
    # y_pred = rforest.predict(x_test)
    # print(f"RandomForest Train Accuracy: {accuracy_score(y_train, y_train_pred)}")
    # print(f"RandomForest Pred Accuracy: {accuracy_score(y_test, y_pred)}")
    plt.figure(figsize=(100, 100))
    tree.plot_tree(dtree, filled=True, feature_names=None, class_names=[str(i) for i in range(1, 41)], rounded=True)

    plt.show()


if __name__ == '__main__':
    main()
