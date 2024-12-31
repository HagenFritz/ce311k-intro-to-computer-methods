# Classes
- A **class** serves as a blueprint for creating objects.
- Objects are **instances** of a class, and they **encapsulate**:
  - **Data** (attributes)
  - **Behaviors** (methods)
- Classes enable **reusable** and **modular** code, making it easier to organize and scale programs.

```python
class CivilEngineer:
    def __init__(self, name, specialty):
        self.name = name  # Instance attribute
        self.specialty = specialty  # Instance attribute

    def introduce(self):  # Instance method
        return f"My name is {self.name}, and I specialize in {self.specialty}."

# Creating an object (instance) of the class
engineer = CivilEngineer("Alice", "Structural Engineering")
print(engineer.introduce())
```

---

### Benefits of Classes
1. **Modularity**: Breaks down large programs into smaller, logical pieces.
2. **Reusability**: Reuse classes across multiple projects or within a project.
3. **Encapsulation**: Groups related data and behavior together, making code easier to maintain.
4. **Abstraction**: Hides implementation details while exposing only the essential functionalities.

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

#### Constructor with Default Values
You can provide **default values** for constructor parameters, making them optional during object creation.

```python
class Car:
    def __init__(self, make, model, year=2023):  # year has a default value
        self.make = make
        self.model = model
        self.year = year

# Creating objects
car1 = Car("Toyota", "Camry")  # Uses default year
car2 = Car("Honda", "Civic", 2022)  # Overrides default year

print(car1.year)  # Output: 2023
print(car2.year)  # Output: 2022
```

---

### More on `self`

- **`self`** is a convention in Python that refers to the instance of the class itself.
- It allows methods within the class to interact with a specific object (instance).
- `self` ensures that attributes and methods belong to the instance, not just a local variable.

#### Understanding `self` Through an Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def introduce(self):  # Instance method
        return f"I am {self.name}, and I am {self.age} years old."

# Creating two instances of the class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.introduce())  # Output: I am Alice, and I am 20 years old.
print(student2.introduce())  # Output: I am Bob, and I am 22 years old.
```

#### Key Points
- `self` is automatically passed as the first argument when calling a method.
- Different instances maintain **separate copies** of their attributes.

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

---

### Class vs. Instance Attributes
- **Instance Attributes**: Defined within `__init__` and unique to each object.
- **Class Attributes**: Shared across all instances of the class.

```python
class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):
        return Circle.pi * self.radius ** 2
```

```python
circle1 = Circle(5)
circle2 = Circle(10)

print(circle1.area())  # Output: 78.53975
print(circle2.area())  # Output: 314.159
```
