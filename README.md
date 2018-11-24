# mastering-python

### Books
-----


- [The Hitchhikere's Guide to Python](https://docs.python-guide.org/)
- [Python-Textbook](https://python-textbok.readthedocs.io/en/1.0/index.html)
- [Tutorials Point](https://www.tutorialspoint.com/python)
- [Python by Programiz](https://www.programiz.com/python-programming/first-program)


### Writing Good Python Modules - Some Essential Python Libraries
- [The Hitchhiker's Guide to Packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/index.html)
- [The Hitchhiker's Guide to Structuring Your Project](https://docs.python-guide.org/writing/structure/)
- [setup.py](https://github.com/kennethreitz/setup.py)
- [attr](https://attrs.readthedocs.io/en/stable/)
  - [attr - The One Python Library Everyone Needs](https://glyph.twistedmatrix.com/2016/08/attrs.html)


### OOP
- [A Byte of Python](https://python.swaroopch.com/oop.html)
- [The Python Tutorial - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Tutorials Point - Objected Oriented Python](https://www.tutorialspoint.com/python/python_classes_objects.htm)
- [Python-Textbook](https://python-textbok.readthedocs.io/en/1.0/Object_Oriented_Programming.html)
- [Python by Programiz - OOP](https://www.programiz.com/python-programming/object-oriented-programming)
- [Object Oriented Design - Niko Wilbert](https://python.g-node.org/python-summerschool-2013/_media/wiki/oop/oo_design_2013.pdf)
- [Python 101 - Object Oriented Programming - Part 1](https://medium.com/the-renaissance-developer/python-101-object-oriented-programming-part-1-7d5d06833f26)
- [Improve Your Python: Python Classes and Object Oriented Programming](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
- [Raymond Hettinger - Python's Class Development Toolkit](https://www.youtube.com/watch?v=HTLu2DFOdTg)
- [OOP - Trying To Design A Good Class Structure)](https://stackoverflow.com/questions/39922553/oop-trying-to-design-a-good-class-structure)

### Design Patterns
- [A Collection of Design Patterns in Python](https://github.com/faif/python-patterns)
- [Toptal - Python Design Patterns](https://www.toptal.com/python/python-design-patterns)




### Data Analysis Libraries

#### Data Visualization
- [ipyvolume](https://github.com/maartenbreddels/ipyvolume) - 3d plotting for Python in the Jupyter notebook based on IPython widgets using WebGL
- [Dash](https://dash.plot.ly/) - Written on top of Flask, Plotly.js, and React.js, Dash can be used for highly custom user interfaces in Python
- [Chartify](https://github.com/spotify/chartify/) - Same interface for plots with a goal to make it easy to use Bokeh plots.
- [bqplot](https://github.com/bloomberg/bqplot) - 2-D plotting library for Project Jupyter
- [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) - A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.
- [pythreejs](https://github.com/jupyter-widgets/pythreejs) - 
A Python / ThreeJS bridge utilizing the Jupyter widget infrastructure.
- [gmaps](https://jupyter-gmaps.readthedocs.io/en/stable/tutorial.html) - Google Maps For Jupyter Notebooks
- [vaex](https://vaex.io/) - Lazy Out-of-Core DataFrames for Python. Visualize a billion rows per second on a single computer.
- [ipywebrtc](https://github.com/maartenbreddels/ipywebrtc) - WebRTC for Jupyter notebook/lab
- [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html) - Interactive Widgets for the Jupyter Notebook
- [itk-jupyter-widgets](https://github.com/InsightSoftwareConsortium/itk-jupyter-widgets) - Interactive Jupyter widgets to visualize images in 2D and 3D.


#### Time Series
- [Prophet](https://facebook.github.io/prophet/) - A Facebook Time Series Analysis library
- [PyFlux](https://pyflux.readthedocs.io/en/latest/index.html) - Time series analysis library with flexible range of modelling and inference options.

#### NLP/Text Manipulation
- [FlashText](https://flashtext.readthedocs.io/en/latest/) - This module can be used to replace keywords in sentences or extract keywords from sentences.
- [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy) - Fuzzy string matching in Python

#### Others
- [wget](https://bitbucket.org/techtonik/python-wget/src) - free utility for non-interactive downloading files from the web
- [pendulum](https://github.com/sdispater/pendulum) - Python datetime manipulation made easy

#### Repeatable Python Workflows in Notebooks
- [Building a Repeatable Data Analysis Process with Jupyter Notebooks](http://pbpython.com/notebook-process.html)

#### Deep Learning Tools
- [Pyro](http://pyro.ai/examples/) - Pyro is a flexible, scalable deep probabilistic programming library built on PyTorch

### Virtual Environments

Creating Your First Project & Virtual Environment

```
# Create a directory and enter into it
mkdir myproject && cd myproject

# create a python env
pyvenv venv

# Put the venv in your .gitignore:
git init
echo 'venv' > .gitignore
```
Doing this keeps your virtual environment out of source control (Git).
```
# Activate the environment:
source venv/bin/activate

# Install packages
pip install requests bs4

# Freeze the requirements:
pip freeze > requirements.txt

# Check requirements.txt into source control:
git add requirements.txt
```
