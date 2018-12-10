# mastering-python

### Good Overviews of Python (Online or Paper)
-----


- [The Hitchhikere's Guide to Python](https://docs.python-guide.org/)
- [Python-Textbook](https://python-textbok.readthedocs.io/en/1.0/index.html)
- [Tutorials Point](https://www.tutorialspoint.com/python)
- [Python by Programiz](https://www.programiz.com/python-programming/first-program)

- 2nd Tier (haven't tried these yet)
- [Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)
- [Berkeley Python Bootcamp](https://www.youtube.com/watch?v=P5BHTrluu1M&list=PLKW2Azk23ZtSeBcvJi0JnL7PapedOvwz9&index=1)
- [Python Deliberate Practice](https://github.com/robert8138/python-deliberate-practice)
- [Effective Python](https://www.amazon.com/Effective-Python-Specific-Software-Development/dp/0134034287) - [code](https://github.com/bslatkin/effectivepython)
- [Python Tips & Tutorials - Sebastian Raschka](https://github.com/rasbt/python_reference#-python-tips-and-tutorials)

- [Free Python ebooks](https://pythonbooks.revolunet.com/)

### Python Projects, OOP, and Building your own Modules
-------

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
- [Python Patterns](https://github.com/faif/python-patterns) - A collection of design patterns/idioms in Python
- [10 Common Software Architectural Patterns in a nutshell](https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-nutshell-a0b47a1e9013)







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


