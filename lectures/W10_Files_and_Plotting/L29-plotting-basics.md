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

#### Histogram (`plt.hist`)
- Visualizes the distribution of numerical data.
- Groups data into intervals (bins) and displays the frequency of data points in each bin.
- Ideal for understanding data distributions or identifying patterns.

```python
# Tensile strength values (in MPa)
tensile_strength = [250, 260, 255, 270, 275]

# Create a histogram
plt.figure(3)
plt.hist(tensile_strength, bins=5, edgecolor='black')  # Specify bins and add edges for clarity
plt.title("Distribution of Tensile Strength in Tested Materials")  # Add a title
plt.xlabel("Tensile Strength (MPa)")  # Label the x-axis
plt.ylabel("Frequency")  # Label the y-axis
plt.grid(axis='y')  # Add gridlines along the y-axis
plt.show()  # Display the histogram
plt.close(3)  # Close the figure
```

#### Scatter Plot (`plt.scatter`)
- Plots individual data points.
- Ideal for showing relationships between two variables.

```python
# Load vs. Deflection in a beam test
load = [0, 10, 20, 30, 40, 50]  # (kN)
deflection = [0, 1.2, 2.5, 3.9, 5.1, 6.3]  # (mm)

# Create a scatter plot
plt.figure()
plt.scatter(load, deflection, s=80, color='blue')
plt.title("Load vs. Deflection in a Beam Test")
plt.xlabel("Load (kN)")
plt.ylabel("Deflection (mm)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
plt.close()
```

#### Pie Chart (`plt.pie`)
- Visualizes proportions of a whole.
- Displays data as slices of a circle, with each slice representing a category's contribution.
- Ideal for showing percentage-based data distributions.

```python
# Energy source distribution
labels = ['Coal', 'Solar', 'Wind']
sizes = [60, 25, 15]  # Percent contribution of each energy source

# Create a pie chart
plt.figure()
plt.pie(sizes, labels=labels, colors=['grey', 'gold', 'lightblue'], autopct='%1.1f%%', startangle=90)  # Add percentages and start angle for better readability
plt.title("Energy Source Distribution")  # Add a title
plt.show()  # Display the pie chart
plt.close()  # Close the figure
```

---

### Enhancing Plots with Related Functions
1. **Titles and Labels**:
   - `plt.title()`: Sets the plot title.
   - `plt.xlabel()`, `plt.ylabel()`: Label the X and Y axes.

   ```python
   plt.title("Example Plot")
   plt.xlabel("X-axis Label")
   plt.ylabel("Y-axis Label")
   ```

2. **Grid Lines** (`plt.grid(True))`: Adds grid lines to improve readability.

   ```python
   plt.grid(linestyle='--', alpha=0.7)
   ```

3. **Legends** (`plt.legend()`): Adds a legend to the plot.

   ```python
   plt.plot([1, 2, 3], [4, 5, 6], label="Line A")
   plt.plot([1, 2, 3], [6, 5, 4], label="Line B")
   plt.legend()
   ```

4. **Colors, Markers, and Line Styles**:
   - `color`: Changes the color of the plot.
   - `marker`: Adds markers at data points.
   - `linestyle`: Customizes the line style.

   ```python
   plt.plot([1, 2, 3], [4, 5, 6], color='red', marker='o', linestyle='--')
   ```

5. **Saving Figures** (`plt.savefig('filename.png')`): Saves the figure to a file.

   ```python
   plt.savefig('plot.png', dpi=300)  # Save with high resolution
   ```

7. **Setting Axes Limits** (`plt.xlim()`, `plt.ylim()`): Set limits for the X and Y axes.

   ```python
   plt.xlim(0, 10)
   plt.ylim(0, 20)
   ```
