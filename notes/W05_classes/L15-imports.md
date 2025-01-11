# Imports: Modules, Packages, and Libraries

1. **Module**
   - A single file containing Python code.
   - Includes functions, classes, variables, and runnable statements.

2. **Package**
   - A collection of related modules grouped in a directory.
   - Represents a higher-level organization of functionality.

3. **Library**
   - A collection of modules and packages providing pre-built functionality for a specific purpose.
   - Usually shared for general use.

---

### Why Use Imports?
Using imports promotes:
  - **Code Organization**: Modularizing code for readability.
  - **Reusability**: Avoid rewriting common functions or classes.
  - **Simplification**: Use existing libraries to save development time.

#### **The `import` Statement**
The `import` statement allows external code to be used in a program.

```python
import math  # Import the math module
print(math.sqrt(16))  # Output: 4.0
```

#### Importing Specific Components
Instead of importing the entire module, specific components (like functions or classes) can be imported.

```python
from module_name import specific_function, another_function
```

```python
from math import sqrt, pi
print(sqrt(16))  # Access directly, Output: 4.0
print(pi)  # Output: 3.141592653589793
```

#### Importing a Module with an Alias
Modules can be imported under a different name (alias) to simplify usage.

```python
import numpy as np  # Import numpy as np
array = np.array([1, 2, 3])
print(array)
```

#### Wildcard Import (`*`)
Using `*` imports everything from a module.

```python
from module_name import *
```

❗**Caution**: Avoid using wildcard imports to prevent conflicts between similarly named variables or functions in different modules.

---

### Module Search Path
When importing a module, Python searches for it in the following order:
1. Current working directory.
2. Directories in the `PYTHONPATH` environment variable.
3. Default system paths, such as the `site-packages` directory.

#### Viewing the Search Path
```python
import sys
print(sys.path)
```

---

### Package Managers
- Tools for installing, upgrading, and managing libraries.
- Examples include:
  - Python: `pip`, `conda`
  - JavaScript: `npm`, `yarn`
  - Ruby: `gem`

#### Installing Packages
```bash
pip install package_name
```

---

### **Built-In Libraries**
Python includes several built-in libraries for general-purpose tasks:

1. **`math`**: Advanced arithmetic, trigonometry, logarithms, etc.
2. **`datetime`**: Manipulating dates and times.
3. **`os`**: Interacting with the operating system (e.g., file paths).
4. **`sys`**: Accessing system-specific parameters (e.g., command-line arguments).
5. **`re`**: Handling regular expressions for pattern matching.

---

### Libraries for Data and File Handling
1. **`csv`**:  Reading and writing CSV files.
2. **`json`**: Parsing JSON data.
3. **`openpyxl`**: Working with Excel files.
4. **`sqlite3`**: Managing SQL-based databases.

---

### Libraries for Data Analysis and Visualization
1. **`pandas`**: Manipulating structured data with DataFrames.
2. **`numpy`**: Numerical computations and array operations.
3. **`matplotlib`**: Creating visualizations and plots.
4. **`seaborn`**: High-level statistical visualizations.
5. **`scipy`**: Advanced scientific computations.

---

### Web Scraping Tools
1. **`requests`**: Sending HTTP requests to web servers.
2. **`beautifulsoup4`**: Parsing and extracting HTML/XML data.
3. **`selenium`**: Automating browsers for web scraping.
