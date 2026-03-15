# 📊 Regression & Predictive Models

## 🔁 What Is Regression?

Regression models the relationship between one or more input variables and a numeric output.

### 💡 Why Use Regression?
- Estimate missing values based on known patterns  
- Predict future outcomes using historical data  
- Understand how different inputs affect results  

### ⚠️ Key Terms  
- **Interpolation**: Predicting *within* known data range  
- **Extrapolation**: Predicting *beyond* known range  
- **Underfitting**: Too simple to capture trends  
- **Overfitting**: Too complex, captures noise  
- **Multicollinearity**: Input variables are too similar

## 🧮 Linear Regression with NumPy

Use NumPy to fit and evaluate a basic linear model.

```python
import numpy as np

m, b = np.polyfit(x, y, 1)
y_pred = np.polyval([m, b], x_val)
```

- `np.polyfit(x, y, deg)` fits a polynomial  
- `np.polyval(coeffs, x)` evaluates it

## 📈 Polynomial Regression

When the relationship is **nonlinear**, increase the degree:

```python
coeffs = np.polyfit(x, y, deg=2)
y_pred = np.polyval(coeffs, x_vals)
```

- Degree 2 fits a curve (quadratic)  
- Use `np.linspace()` to create smooth `x` values for plotting  
- Avoid high degrees → may lead to **overfitting**

## 🔢 Multiple Linear Regression

Like linear regression, but with **more input variables**.

```python
from sklearn.linear_model import LinearRegression

X = [[x1, x2], [x1, x2], ...]  # 2D list of inputs
y = [output1, output2, ...]    # target values

model = LinearRegression()
model.fit(X, y)
model.predict([[new_x1, new_x2]])
```

✅ Supports any number of numeric input features.

## 🤖 Advanced Predictive Models

### 🌳 Decision Tree
- Works like a flowchart
- Splits data based on decision rules

### 🌲 Random Forest
- Builds many decision trees and **averages** results
- More stable and accurate than a single tree

### 👥 K-Nearest Neighbors (KNN)
- Predicts based on **similar past inputs**
- No explicit model; based on **distance to other points**

## 🔧 Using `scikit-learn`

All models follow a similar structure:

```python
from sklearn.model import ModelType  # e.g., LinearRegression, RandomForestRegressor

model = ModelType()
model.fit(X, y)
model.predict([[input1, input2]])
```

✅ Supports linear models, trees, forests, and more  
✅ Works with **lists of lists** or NumPy arrays