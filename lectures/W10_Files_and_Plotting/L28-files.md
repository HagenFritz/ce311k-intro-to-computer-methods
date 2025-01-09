# Working with Files in Python

### Getting a File Object
In Python, the `open()` command is used to interact with files by creating a file object. This file object allows you to read, write, or update the file.

```python
file_obj = open(filename_str, mode='r')
```

#### Modes
The `mode` specifies how the file will be used:
- **`r`**: Read only (default). The file must exist.
- **`w`**: Write. Creates a new file or overwrites an existing file.
- **`a`**: Append. Adds data to the end of the file without truncating it.

---

### Context Managers
Context managers ensure files are properly acquired and closed after their use. They are implemented using the `with` statement.
- Automatically closes the file, preventing resource leaks.
- No need to explicitly call `close()`.

```python
with open(filename_str, mode='r') as file_obj:
    # Perform file operations
    content = file_obj.read()
```

#### Key Points
- **`with`** starts the context manager block.
- **`as`** assigns the file object to a variable.
- The file object is **not accessible outside the block**.

---

### Reading Text Files

#### Methods
1. **`read()`**: Reads the entire file into a single string.
    ```python
    with open("example1.txt", mode='r') as f:
        content = f.read()
        print(content)
    ```
2. **`readlines()`**: Reads all lines and stores them in a list of strings.
    ```python
    with open("example2.txt", mode='r') as f:
        lines = f.readlines()
        print(lines)
    ```
3. **`readline()`**: Reads one line at a time and moves the pointer to the next line.
    ```python
    with open("example3.txt", mode='r') as f:
        line = f.readline()
        print(line)
    ```

#### Looping Through Lines
Using a `for` loop to iterate through lines in the file is memory-efficient, especially for large files, as it reads one line at a time.
- Avoids loading the entire file into memory (unlike `readlines()`).
- Automatically reads one line at a time.

```python
with open("example4.txt", mode='r') as f:
    for line in f:
        print(line.strip())  # Removes trailing newline characters
```

---

### Writing to Text Files
Python provides methods to write `str` data to files:
1. **`write()`**: Writes a single string to the file.
    ```python
    with open('example4.txt', 'w') as file:
        file.write("Hello, this is a new line.\n")
    ```
2. **`writelines()`**: Writes a list of strings to the file.
    ```python
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    with open('example5.txt', 'w') as file:
        file.writelines(lines)
    ```

#### Appending to a File
To add data to an existing file, use `write()` with `mode='a'`:
```python
with open('example5.txt', 'a') as file:
    file.write("This will be added to the file.\n")
```

---

### Reading CSV Files
CSV (Comma-Separated Values) files are plain text files for tabular data. Commas are the default delimiters but can vary (e.g., tabs or semicolons).

#### `csv` Module
In Python, to work with CSV files, you will need to import the `csv` module

```python
import csv
```

#### Reading CSV Files

##### Reading CSV with `csv.reader`
The `csv.reader` reads each row as a list of strings.

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

##### Skipping the Header Row
If the CSV file contains a header row, you can skip it using `next()`.

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        print(row)
```

##### Using a Custom Delimiter
If the CSV uses a delimiter other than a comma (e.g., a tab `\t`), specify it when creating the `reader` object.

```python
import csv

with open('data.tsv', 'r') as file:  # Example with a tab-separated file
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)
```

##### Reading into Dictionaries
The `csv.DictReader` reads rows as dictionaries, with the column headers as keys.

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

For a file `data.csv`:
```
Name,Age,City
Alice,30,New York
Bob,25,Chicago
```

The output will be:
```
{'Name': 'Alice', 'Age': '30', 'City': 'New York'}
{'Name': 'Bob', 'Age': '25', 'City': 'Chicago'}
```

---

### Writing CSV Files
The `csv` module provides methods for writing data to CSV files.

```python
import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Writes header
    writer.writerows([
        ['Alex', 30, 'New York City'],
        ['Victor', 31, 'Denver']
    ])
```

---

### Reading JSON Files
JSON (JavaScript Object Notation) is a lightweight format for storing structured data. It is similar to Python dictionaries.

#### Reading JSON
```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)  # Converts JSON into a Python dictionary
    print(data)
```

### Writing JSON Files
Python `dict` variables can be easily written to JSON files using `json.dump()`.

```python
import json

data = {
    "name": "Hagen",
    "age": 31,
    "city": "Austin"
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Writes data to JSON with indentation
```

---

### File Paths
File paths specify the location of a file.

#### Types:
1. **Absolute Paths**: Full path from the root directory.

     ```python
     with open("/Users/username/documents/example.txt", "r") as f:
         content = f.read()
     ```

2. **Relative Paths**: Starts from the current working directory.

     ```python
     with open("example.txt", "w") as f:
         f.write("Hello World")
     ```
