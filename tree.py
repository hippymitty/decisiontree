from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from IPython.display import Image  
from sklearn import tree
import pydotplus

iris = datasets.load_iris()
X = iris.data
y = iris.target
# Create decision tree classifer object
clf = DecisionTreeClassifier(random_state=0)
print("data loaded, training started")

model = clf.fit(X, y)
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=iris.feature_names,  
                                class_names=iris.target_names)
print("trainging complete")


graph = pydotplus.graph_from_dot_data(dot_data)  
# Show graph
Image(graph.create_png())
# # Create PDF
# graph.write_pdf("tree.pdf")
graph.write_png("tree.png")