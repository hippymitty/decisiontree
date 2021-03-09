# Load libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from IPython.display import Image  
from sklearn import tree
import pydotplus
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
# Create decision tree classifer object
clf = DecisionTreeClassifier(random_state=0)
print("loaded, starting training")
# Train model
model = clf.fit(X, y)
# Create DOT data
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=iris.feature_names,  
                                class_names=iris.target_names)
print("trainging done")
# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data)  

# Show graph
Image(graph.create_png())

# # Create PDF
# graph.write_pdf("tree.pdf")

# Create PNG
graph.write_png("tree.png")