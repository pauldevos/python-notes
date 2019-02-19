# mastering-python

## Intermediate Level Overviews of Python

- [Python Tips Docs](http://book.pythontips.com/en/latest/)
- [Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)
- [Berkeley Python Bootcamp](https://www.youtube.com/watch?v=P5BHTrluu1M&list=PLKW2Azk23ZtSeBcvJi0JnL7PapedOvwz9&index=1)
- [Effective Python](https://www.amazon.com/Effective-Python-Specific-Software-Development/dp/0134034287) - [code](https://github.com/bslatkin/effectivepython)


## Writing Python Modules - Some Essential Python Libraries

- [The Hitchhiker's Guide to Packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/index.html)
- [The Hitchhiker's Guide to Structuring Your Project](https://docs.python-guide.org/writing/structure/)
- [setup.py](https://github.com/kennethreitz/setup.py)
- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/)
- [Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)



## OOP

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

## Building RESTful APIs
- [Creating Web APIs with Python and Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
- [Using Elasticsearch with Python and Flask](https://dev.to/aligoren/using-elasticsearch-with-python-and-flask-2i0e)


## Design Patterns

- [A Collection of Design Patterns in Python](https://github.com/faif/python-patterns)
- [Toptal - Python Design Patterns](https://www.toptal.com/python/python-design-patterns)
- [Python Patterns](https://github.com/faif/python-patterns) - A collection of design patterns/idioms in Python
- [10 Common Software Architectural Patterns in a nutshell](https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-nutshell-a0b47a1e9013)


## Building RESTful API Wrappers
- [Designing a RESTful API with Python and Flask - Miguel Grinberg](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [How To Use Web APIs in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3)
- [Building and Documenting Python REST APIs With Flask and Connexion](https://realpython.com/flask-connexion-rest-api/)
- [API Integration in Python](https://realpython.com/api-integration-in-python/)
- [How to Use Restful Web APIs in Python](https://code.tutsplus.com/articles/how-to-use-restful-web-apis-in-python--cms-29493)

## Algorithms in Python
- [The Algorithms](https://github.com/TheAlgorithms/Python)

## Virtual Environments

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


