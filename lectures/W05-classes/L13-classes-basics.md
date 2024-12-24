# Classes
- A **class** serves as a blueprint for creating objects.
- Objects are **instances** of a class, and they **encapsulate**:
  - **Data** (attributes)
  - **Behaviors** (methods)
- Classes enable **reusable** and **modular** code.

```python
class CivilEngineer:
    def __init__(self, name, specialty):
        self.name = name  # Instance attribute
        self.specialty = specialty  # Instance attribute

    def introduce(self):  # Instance method
        return f"My name is {self.name}, and I specialize in {self.specialty}."
```

---

### Constructor Method
- A **constructor** is a special method used to initialize attributes of a newly created object.
- In Python, the constructor is defined as `__init__`.

```python
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
        self.attribute = value
```

- Constructor methods are **automatically called** when a new object is instantiated.
- The first parameter is always `self`, which refers to the object being created.

---

### More on `self`
- **`self`** is a convention in Python that refers to the instance of the class itself.
- It allows methods within the class to interact with a specific object (instance).
- `self` ensures that attributes and methods belong to the instance, not just a local variable.

#### Key Points
- All instance methods must include `self` as the first parameter.
- When you call a method on an object, Python automatically passes the instance as the first argument to the method.

---

### Creating an Object
- An object is an **instance** of a class.
- The constructor initializes the object when the class is called with arguments.

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Initialize name
        self.age = age    # Initialize age

# Creating objects
student1 = Student("Alice", 20)  # name is Alice, age is 20
student2 = Student("Bob", 22)    # name is Bob, age is 22
```

---

### Attributes and Methods
- **Attributes**: Variables associated with an object that hold its data.
- **Methods**: Functions defined inside a class that describe the behavior of the object.

```python
class Bridge:
    def __init__(self, length, material):
        self.length = length  # in meters
        self.material = material

    def get_description(self):
        return f"This is a {self.length}m bridge made of {self.material}."
```

```python
bridge = Bridge(500, "steel")
print(bridge.length)  # Output: 500
print(bridge.get_description())  # Output: This is a 500m bridge made of steel.
```
