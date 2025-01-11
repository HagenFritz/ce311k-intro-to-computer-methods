# Advanced Classes Topics

### Encapsulation
- **Encapsulation** restricts access to some components of an object, protecting data from being accidentally modified.
- Attributes can be made **private** by prefixing their names with double underscores (`__`).

```python
class Pipeline:
    def __init__(self, length, diameter):
        self.__length = length  # Private attribute
        self.__diameter = diameter  # Private attribute

    def get_flow_rate(self):
        return 3.14 * (self.__diameter / 2) ** 2 * self.__length
```

```python
pipe = Pipeline(200, 0.5)
print(pipe.get_flow_rate())  # Output: 39.25
print(pipe.__length)  # AttributeError: 'Pipeline' object has no attribute '__length'
```

#### Key Points
1. Private attributes cannot be accessed directly but can be accessed using methods.
2. Encapsulation ensures controlled access to sensitive data through getter and setter methods.

---

### Inheritance
- **Inheritance** allows a class (child) to derive attributes and methods from another class (parent).
- The parent class provides generic functionality, and the child class specializes or extends it.

```python
class Engineer:
    def __init__(self, name):
        self.name = name

class StructuralEngineer(Engineer):
    def __init__(self, name, expertise):
        super().__init__(name)  # Call parent class constructor
        self.expertise = expertise

    def introduce(self):
        return f"I am {self.name}, specializing in {self.expertise}."
```

```python
struct_eng = StructuralEngineer("Alice", "Bridge Design")
print(struct_eng.introduce())  # Output: I am Alice, specializing in Bridge Design.
```

#### Key Points
1. The `super()` function allows calling methods of the parent class.
2. Inheritance promotes code reuse and modular design.

---

### More on `super()`
- `super()` is a built-in function that allows you to call methods from a parent class in a child class.
- It avoids rewriting shared logic in the parent class.

```python
class Engineer:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "Hello, " + self.name

class StructuralEngineer(Engineer):
    def __init__(self, name, expertise):
        super().__init__(name)  # Call parent class constructor
        self.__expertise = expertise  # Private attribute

    def show_expertise(self):
        return super().describe() + ". Your expertise: " + self.__expertise
```

```python
eng = StructuralEngineer("Bob", "Structural Analysis")
print(eng.show_expertise())  # Output: Hello, Bob. Your expertise: Structural Analysis.
```

#### Key Points
- **Avoid Redundancy**: `super()` prevents repeating code in the parent class.
- **Access Parent Methods**: Child classes can enhance or modify the functionality of parent methods.

---

### Polymorphism
- **Polymorphism** enables different objects to use the same method name but perform different actions depending on their class.
- This is achieved through **method overriding** in child classes.

```python
class Engineer:
    def describe(self):
        return "I am an engineer."

class StructuralEngineer(Engineer):
    def describe(self):
        return "I am a structural engineer specializing in bridges."

class EnvironmentalEngineer(Engineer):
    def describe(self):
        return "I am an environmental engineer specializing in sustainability."
```

```python
eng1 = Engineer()
eng2 = StructuralEngineer()
eng3 = EnvironmentalEngineer()

print(eng1.describe())  # Output: I am an engineer.
print(eng2.describe())  # Output: I am a structural engineer specializing in bridges.
print(eng3.describe())  # Output: I am an environmental engineer specializing in sustainability.
```

#### Key Points
1. **Dynamic Behavior**: Different classes can define their own implementation of the same method.
2. **Code Generalization**: Enables writing code that works with multiple types of objects.
