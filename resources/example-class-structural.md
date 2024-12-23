# Example Class: Structural Component
This file provides an example Python class related to structural engineering. The various components of this class are detailed below the code definition.

```python
# Base Class: StructuralComponent
class StructuralComponent:
    def __init__(self, name, material, length):
        self.name = name
        self.material = material
        self.__length = length  # Private attribute

    def get_length(self):
        return self.__length

    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Length must be positive.")

    def describe(self):
        return f"{self.name} made of {self.material}, length: {self.__length} meters"

# Subclass: Beam
class Beam(StructuralComponent):
    def __init__(self, name, material, length, load_capacity):
        super().__init__(name, material, length)  # Initialize base class
        self.load_capacity = load_capacity  # Additional attribute

    def describe(self):
        return f"{self.name} made of {self.material}, length: {self.get_length()} meters, capacity: {self.load_capacity} tons"

# Subclass: Column
class Column(StructuralComponent):
    def __init__(self, name, material, length, axial_load):
        super().__init__(name, material, length)
        self.axial_load = axial_load  # Additional attribute

    def describe(self):
        return f"{self.name} made of {self.material}, length: {self.get_length()} meters, axial load: {self.axial_load} tons"
```

---

### Base Class: `StructuralComponent`
The `StructuralComponent` class serves as the base class. It contains:
- **Attributes**
  - `name` (public): Name of the component.
  - `material` (public): Material used in the component.
  - `__length` (private): Length of the component in meters.
- **Encapsulation**
  - Private `__length` attribute is accessed via `get_length()` and `set_length()` methods, ensuring only valid lengths are assigned.
- **Methods**
  - `describe()`: Returns a string description of the component.

#### Example
```python
component = StructuralComponent("Generic Component", "Steel", 5.0)
print(component.describe())  # Output: Generic Component made of Steel, length: 5.0 meters
```

---

### Encapsulation in `StructuralComponent`
Encapsulation is demonstrated with the `__length` attribute:
- **Getter Method (`get_length`)**: Provides controlled read access to the length.
- **Setter Method (`set_length`)**: Ensures only positive values can be assigned.

#### Examples

**Valid Use**
```python
component = StructuralComponent("Beam", "Concrete", 10.0)
component.set_length(15.0)
print(component.get_length())  # Output: 15.0
```
**Invalid Use**: If a negative value is provided
```python
component.set_length(-5)  # Raises ValueError: Length must be positive.
```

---

### Subclass: `Beam`
The `Beam` class extends `StructuralComponent` and introduces:
- **Attribute**
  - `load_capacity`: Maximum load capacity of the beam in tons.
- **Method Override** (Polymorphism)
  - Overrides `describe()` to include load capacity in the description.

#### Example
```python
beam = Beam("Main Beam", "Steel", 12.0, 500)
print(beam.describe())  # Output: Main Beam made of Steel, length: 12.0 meters, capacity: 500 tons
```

---

### Subclass: `Column`
The `Column` class also extends `StructuralComponent` and introduces:
- **Attribute**
  - `axial_load`: Axial load supported by the column in tons.
- **Method Override** (Polymorphism)
  - Overrides `describe()` to include axial load in the description.

#### Example
```python
column = Column("Support Column", "Concrete", 8.0, 300)
print(column.describe())  # Output: Support Column made of Concrete, length: 8.0 meters, axial load: 300 tons
```

---

### Summary
This example demonstrates:
1. **Basic Class Design**: Using `StructuralComponent` to represent common attributes and methods.
2. **Encapsulation**: Protecting the `__length` attribute with getters and setters.
3. **Inheritance**: Creating specialized subclasses `Beam` and `Column` that build upon the base class.
4. **Polymorphism**: Treating different structural components uniformly via the base class.

