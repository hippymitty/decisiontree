import pandas as pd
import numpy as np
import pydot as pydot
# import matplotlib.pyplot as plt
import cv2
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# from scikit-learn import datasets
FEATURE_NAMES = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
print("loading data")
iris = load_iris()
X = pd.DataFrame(iris.data, columns = FEATURE_NAMES)
y = iris.target

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X,y)
print("initialising classifier")

from sklearn.tree import export_graphviz
export_graphviz(model, 'decisiontree.dot', feature_names = FEATURE_NAMES)
print("exporting graph")

(graph,) = pydot.graph_from_dot_file('decisiontree.dot')
graph.write_png('decisiontree.png')
print("converting dot to png")

img = cv2.imread('decisiontree.png')
plt.figure(figsize = (20, 20))
plt.imshow(img)