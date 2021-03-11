# Decision Tree examples
Two different python files, both with the same output however two different approaches to the solution, depending on the data.
Each of these will produce a PNG file with the same name as the file, either decisiontree or tree

### How it works
Purpose of this repo is to run sample data to split into categories using a decision tree

### Packages to pre-install
Anaconda packages,
pandas,
numpy,
pydot,
scikitlean (sklearn),
matplotlib,
opencv-python,
IPython,
pydotplus

### How to use
Run the python files, and install any packages that show as 'module not found'. Once completed the print lines in the files will indicate if there's any errors, and at which point, otherwise it will produce the dot & PNG file



### Errors/installs
If youre running on jupyter notebooks you may encounter a graphviz error. To resolve, run:
`! conda install python-graphviz`

For Mac with the same or similar error, please run:
`brew install graphviz`
`pip install -U pydotplus`