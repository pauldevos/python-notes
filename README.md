# mastering-python

### Books




### OOP
- [A Byte of Python](https://python.swaroopch.com/oop.html)
- [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [](https://medium.com/the-renaissance-developer/python-101-object-oriented-programming-part-1-7d5d06833f26)

- [OOP - Trying To Design A Good Class Structure)](https://stackoverflow.com/questions/39922553/oop-trying-to-design-a-good-class-structure)



### Virtual Environments


#### Make a project folder:
```mkdir myproject && cd myproject

# create a python env
pyvenv venv
# Put the venv in your .gitignore:
git init
echo 'venv' > .gitignore
```
Doing this keeps your virtual environment out of source control (Git).
```
# Activate the environment:
activate venv/bin/activate

# Install packages
pip install requests bs4

# Freeze the requirements:
pip freeze > requirements.txt

# Check requirements.txt into source control:
git add requirements.txt
```
