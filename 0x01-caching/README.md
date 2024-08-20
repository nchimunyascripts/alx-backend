# Caching Algorithms Project

## Background Context

In this project, you will explore different caching algorithms, learning their mechanisms, benefits, and limitations. Caching is a fundamental concept in computer science, used to store copies of data in a system's memory for faster access. Understanding how different caching strategies work is essential for optimizing system performance.

## Resources

To gain a comprehensive understanding of caching algorithms, you should read or watch the following materials:

- **Cache Replacement Policies:**
  - [FIFO (First-In, First-Out)](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
  - [LIFO (Last-In, First-Out)](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
  - [LRU (Least Recently Used)](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
  - [MRU (Most Recently Used)](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
  - [LFU (Least Frequently Used)](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly, without needing to refer to external sources:

### General Concepts:
- **Caching System:**
  - What is a caching system?
  - What is its purpose?
  - What are its limitations?

### Cache Replacement Policies:
- **FIFO:** 
  - What does FIFO mean?
  - How is it implemented in caching?
- **LIFO:** 
  - What does LIFO mean?
  - How is it implemented in caching?
- **LRU:** 
  - What does LRU mean?
  - How is it implemented in caching?
- **MRU:** 
  - What does MRU mean?
  - How is it implemented in caching?
- **LFU:** 
  - What does LFU mean?
  - How is it implemented in caching?

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7).
- Each file should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, located at the root of the project folder, is mandatory.
- Your code must adhere to the `pycodestyle` style guide (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'` to check).
- All your classes should have documentation (use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'` to check).
- All your functions (inside and outside of a class) should have documentation (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'` or `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'` to check).
- Documentation should consist of real sentences that explain the purpose of the module, class, or method in detail (the length of the documentation will be verified).

## More Info

### Parent Class: `BaseCaching`

All your caching classes must inherit from the `BaseCaching` class, which is defined as follows:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

### Key Details

- **MAX_ITEMS:** The `BaseCaching` class defines a constant `MAX_ITEMS`, which is set to 4. This constant represents the maximum number of items that the cache can hold at any time.
  
- **`cache_data`:** The `cache_data` dictionary is where the data is stored in the caching system.

- **`print_cache`:** This method prints the current state of the cache, listing all keys and their corresponding values in sorted order.

- **`put`:** This method is intended to add an item to the cache. It must be implemented in your derived cache class, as the base class version raises a `NotImplementedError`.

- **`get`:** This method is intended to retrieve an item from the cache by its key. Like `put`, it must be implemented in your derived cache class, as the base class version raises a `NotImplementedError`.

## Tasks

### 0. Basic Dictionary

#### Objective
Create a class `BasicCache` that inherits from `BaseCaching` and implements a simple caching system without any limit on the number of items it can store.

#### Requirements

- **Use `self.cache_data`:** You must use the `self.cache_data` dictionary, which is inherited from the `BaseCaching` class.
- **No limit on the cache:** This caching system does not impose any limit on the number of items that can be stored.

#### Method Definitions

- **`def put(self, key, item):`**
  - Assign the `item` value to the `self.cache_data` dictionary with the given `key`.
  - If `key` or `item` is `None`, this method should do nothing.

- **`def get(self, key):`**
  - Return the value associated with the `key` in `self.cache_data`.
  - If `key` is `None` or if the `key` does not exist in `self.cache_data`, return `None`.

#### Example

```python
guillaume@ubuntu:~/0x01$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
```
### Repository

**GitHub repository:** `alx-backend`

**Directory:** `0x01-caching`

**File:** `0-basic_cache.py`

## 1. FIFO Caching

### Objective
Create a class `FIFOCache` that inherits from `BaseCaching` and implements a caching system using the FIFO (First-In, First-Out) algorithm.

### Requirements

- **Use `self.cache_data`:** You must use the `self.cache_data` dictionary, which is inherited from the `BaseCaching` class.
- **Overload `__init__` (optional):** If you choose to overload the `__init__` method, make sure to call the parent class's `__init__` method using `super().__init__()`.

### Method Definitions

- **`def put(self, key, item):`**
  - Assign the `item` value to the `self.cache_data` dictionary with the given `key`.
  - If `key` or `item` is `None`, this method should do nothing.
  - If the number of items in `self.cache_data` exceeds `BaseCaching.MAX_ITEMS` (which is 4):
    - Discard the first item that was added to the cache (following the FIFO algorithm).
    - Print `DISCARD:` followed by the key of the discarded item and a new line.

- **`def get(self, key):`**
  - Return the value associated with the `key` in `self.cache_data`.
  - If `key` is `None` or if the `key` does not exist in `self.cache_data`, return `None`.

### Example

```python
guillaume@ubuntu:~/0x01$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/0x01$ 
```
### Repository

**GitHub repository:** `alx-backend`

**Directory:** `0x01-caching`

**File:** `1-fifo_cache.py`

## 2. LIFO Caching

### Objective
Create a class `LIFOCache` that inherits from `BaseCaching` and implements a caching system using the LIFO (Last-In, First-Out) algorithm.

### Requirements

- **Use `self.cache_data`:** You must use the `self.cache_data` dictionary, which is inherited from the `BaseCaching` class.
- **Overload `__init__` (optional):** If you choose to overload the `__init__` method, make sure to call the parent class's `__init__` method using `super().__init__()`.

### Method Definitions

- **`def put(self, key, item):`**
  - Assign the `item` value to the `self.cache_data` dictionary with the given `key`.
  - If `key` or `item` is `None`, this method should do nothing.
  - If the number of items in `self.cache_data` exceeds `BaseCaching.MAX_ITEMS` (which is 4):
    - Discard the most recently added item in the cache (following the LIFO algorithm).
    - Print `DISCARD:` followed by the key of the discarded item and a new line.

- **`def get(self, key):`**
  - Return the value associated with the `key` in `self.cache_data`.
  - If `key` is `None` or if the `key` does not exist in `self.cache_data`, return `None`.

### Example

```python
guillaume@ubuntu:~/0x01$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/0x01$
```
### Repository

**GitHub repository:** `alx-backend`

**Directory:** `0x01-caching`

**File:** `2-lifo_cache.py`

## 3. LRU Caching

### Objective
Create a class `LRUCache` that inherits from `BaseCaching` and implements a caching system using the LRU (Least Recently Used) algorithm.

### Requirements

- **Use `self.cache_data`:** You must use the `self.cache_data` dictionary, which is inherited from the `BaseCaching` class.
- **Overload `__init__` (optional):** If you choose to overload the `__init__` method, make sure to call the parent class's `__init__` method using `super().__init__()`.

### Method Definitions

- **`def put(self, key, item):`**
  - Assign the `item` value to the `self.cache_data` dictionary with the given `key`.
  - If `key` or `item` is `None`, this method should do nothing.
  - If the number of items in `self.cache_data` exceeds `BaseCaching.MAX_ITEMS` (which is 4):
    - Discard the least recently used item in the cache (following the LRU algorithm).
    - Print `DISCARD:` followed by the key of the discarded item and a new line.

- **`def get(self, key):`**
  - Return the value associated with the `key` in `self.cache_data`.
  - If `key` is `None` or if the `key` does not exist in `self.cache_data`, return `None`.
  - The accessed key should be considered the most recently used.

### Example

```python
guillaume@ubuntu:~/0x01$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/0x01$
```
### Repository

**GitHub repository:** `alx-backend`

**Directory:** `0x01-caching`

**File:** `3-lru_cache.py`

## 4. MRU Caching

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - a dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):`, but don’t forget to call the parent init with `super().__init__()`.

### `def put(self, key, item):`
- Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
- If `key` or `item` is `None`, this method should not do anything.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
  - You must discard the most recently used item (MRU algorithm).
  - You must print `DISCARD:` with the key discarded, followed by a new line.

### `def get(self, key):`
- Must return the value in `self.cache_data` linked to `key`.
- If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

## Example

```python
guillaume@ubuntu:~/0x01$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
MRUCache = __import__('4-mru_cache').MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
```
### Repository

**GitHub repository:** `alx-backend`

**Directory:** `0x01-caching`

**File:** `4-mru_cache.py`

## 5. LFU Caching

#### Advanced

Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - a dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):`, but don’t forget to call the parent init with `super().__init__()`.

### `def put(self, key, item):`
- Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
- If `key` or `item` is `None`, this method should not do anything.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
  - You must discard the least frequently used item (LFU algorithm).
  - If you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used.
  - You must print `DISCARD:` with the key discarded, followed by a new line.

### `def get(self, key):`
- Must return the value in `self.cache_data` linked to `key`.
- If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

## Example

```python
guillaume@ubuntu:~/0x01$ cat 100-main.py
#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./100-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
```
### Repository

**GitHub repository:** `alx-backend`

**Directory:** `0x01-caching`

**File:** `100-lfu_cache.py`