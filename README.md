# pyPropertyTest
This is a test of how to define set only variable and get only variable in Python.

## usage
If you define get only variable.
```python
class Test:
    def __init__(self):
        self.__get_only = "get_only"

    @property
    def get_only(self):
        return self.__get_only
```

If you define set only variable.
```python

class Test:
    def __init__(self):
        self.__set_only = "set_only"
```


If you define gettable and settable  variable.

```python
class Test:
    def __init__(self):
        self.__get_and_set = "get_and_set"

    @property
    def get_and_set(self):
        return self.__get_and_set
    @get_and_set.setter
    def get_and_set(self, get_and_set):
        self.__get_and_set = get_and_set
```

or

```python
class Test:
    def __init__(self):
        self.another_get_and_set = "another_get_and_set"
```
