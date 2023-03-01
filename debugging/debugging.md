# Debugging

#### To figure out which module is busing used in a given program

```python
import a_module
print(a_module.__file__)

# Will actually give you the path to the .pyc file that was loaded, at least on Mac OS X.

# another option
import os
path = os.path.abspath(a_module.__file__)
# or
path = os.path.dirname(a_module.__file__)

```


### Another way

outside of virtualenv - provides the path of global site-packages,
insidue a virtualenv - provides the virtualenv's site-packages
...is this one-liner:
```python

python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"

# Formatted for readability (rather than use as a one-liner), that looks like the following:
from distutils.sysconfig import get_python_lib
print(get_python_lib())
```