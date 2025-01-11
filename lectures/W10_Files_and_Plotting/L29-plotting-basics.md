# Basics of Plotting with Matplotlib

### Importing Matplotlib
To use Matplotlib for plotting, you typically import its `pyplot` module under the alias `plt`:

```python
import matplotlib.pyplot as plt
```

This provides access to functions for creating and customizing plots.

---

### Creating Figures
A **figure** is the top-level container for all elements of a plot (axes, titles, legends, etc.).

- **`plt.figure()`**: Creates a new figure or activates an existing one.
- **Importance**:
  - Separates different plots, especially when working with multiple figures.
  - Prevents plots from overlapping or overwriting.
- **Optional Parameters**:
  - `figsize=(width, height)`: Sets the size of the figure in inches.
  - `dpi`: Sets the resolution (dots per inch).

```python
plt.figure(figsize=(8, 6), dpi=100)  # Creates a figure of size 8x6 inches at 100 DPI
```

---

### Displaying and Closing Figures
- **`plt.show()`**: Renders and displays the figure. Essential when working in scripts or IDEs.
- **`plt.close()`**: Closes a figure to free memory and prevent overlap.

```python
plt.figure()
plt.plot([1, 2, 3], [4, 5, 6])  # Simple plot
plt.title("Example Plot")
plt.show()                      # Display the figure
plt.close()                     # Close the figure
```

---

### Basic Plotting Functions

#### Line Plot (`plt.plot`)
- Displays data points connected by a line.
- Commonly used for trends or time series.

```python
plt.plot([1, 2, 3], [4, 5, 6])  # X and Y values
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
```

#### Bar Chart (`plt.bar`)
- Displays categorical data using rectangular bars
- Useful for comparisons

```python
# Sales of products in units
products = ['Product A', 'Product B', 'Product C']
sales = [150, 200, 120]

# Create a bar chart
plt.figure(2)
plt.bar(products, sales, color='skyblue')  # Add color
plt.title("Sales by Product")              # Add a title
plt.xlabel("Products")                     # Label the x-axis
plt.ylabel("Units Sold")                   # Label the y-axis
plt.show()                                 # Display the plot
plt.close(2)
```

3. **Scatter Plot (`plt.scatter`)**
   - Plots individual data points.
   - Ideal for showing relationships between two variables.

   ```python
   x = [1, 2, 3, 4, 5]
   y = [5, 4, 3, 2, 1]
   plt.scatter(x, y, color='blue', s=50, edgecolor='black')  # Custom color, size, and edge
   plt.title("Scatter Plot Example")
   plt.xlabel("X-axis")
   plt.ylabel("Y-axis")
   ```

---

#### **5. Enhancing Plots with Related Functions**
1. **Titles and Labels**:
   - `plt.title()`: Sets the plot title.
   - `plt.xlabel()`, `plt.ylabel()`: Label the X and Y axes.

   Example:
   ```python
   plt.title("Example Plot")
   plt.xlabel("X-axis Label")
   plt.ylabel("Y-axis Label")
   ```

2. **Grid Lines**:
   - `plt.grid(True)`: Adds grid lines to improve readability.

   Example:
   ```python
   plt.grid(linestyle='--', alpha=0.7)
   ```

3. **Legends**:
   - `plt.legend()`: Adds a legend to the plot.

   Example:
   ```python
   plt.plot([1, 2, 3], [4, 5, 6], label="Line A")
   plt.plot([1, 2, 3], [6, 5, 4], label="Line B")
   plt.legend()
   ```

4. **Colors, Markers, and Line Styles**:
   - `color`: Changes the color of the plot.
   - `marker`: Adds markers at data points.
   - `linestyle`: Customizes the line style.

   Example:
   ```python
   plt.plot([1, 2, 3], [4, 5, 6], color='red', marker='o', linestyle='--')
   ```

5. **Saving Figures**:
   - `plt.savefig('filename.png')`: Saves the figure to a file.

   Example:
   ```python
   plt.savefig('plot.png', dpi=300)  # Save with high resolution
   ```

---

#### **6. Common Customization Techniques**
1. **Multiple Plots in One Figure**:
   - Use `plt.subplot()` or `plt.subplots()` to create multiple plots.

   Example:
   ```python
   fig, axs = plt.subplots(1, 2, figsize=(10, 5))
   axs[0].plot([1, 2, 3], [4, 5, 6])
   axs[0].set_title("Plot 1")
   axs[1].bar(['A', 'B', 'C'], [5, 7, 3])
   axs[1].set_title("Plot 2")
   plt.tight_layout()  # Adjusts layout to prevent overlap
   plt.show()
   ```

2. **Setting Axes Limits**:
   - `plt.xlim()`, `plt.ylim()`: Set limits for the X and Y axes.

   Example:
   ```python
   plt.xlim(0, 10)
   plt.ylim(0, 20)
   ```

---

### **Summary**
1. Import `matplotlib.pyplot` as `plt`.
2. Use `plt.figure()` to create or manage figures.
3. Plot data using functions like `plt.plot`, `plt.bar`, and `plt.scatter`.
4. Enhance plots with titles, labels, grids, legends, and more.
5. Always call `plt.show()` to render plots and `plt.close()` to free resources.

This structure provides a solid foundation for working with Matplotlib. Let me know if you’d like more examples or advanced customizations!
