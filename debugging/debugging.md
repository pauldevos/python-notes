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
