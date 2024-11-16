# 🔢Linear Regression Application💻

## Table of Contents📑
1. [Introduction](#introduction)
2. [Mathematical Background](#mathematical-background)
3. [Tasks](#tasks)
4. [Implementation Details](#implementation-details)

---

## Introduction🎯
In this laboratory, we will implement linear regression using the least squares method. The goal is to find a linear relationship between points in a dataset by minimizing the sum of squared errors.

## Mathematical Background📐
Given n points (x₁, y₁), (x₂, y₂),..., (xₙ, yₙ), we want to determine a linear relationship where y can be expressed as a function of x:

```
y = a + b⋅x
```

The error for each point (xᵢ, yᵢ) is:
```
eᵢ = yᵢ - (a + b⋅xᵢ)
```

The total error function Q(a,b) is defined as:
```
Q(a,b) = Σ eᵢ² = Σ (yᵢ - a - b⋅xᵢ)²
```

The minimum values for this function are obtained using:
```
b = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
a = ȳ - b⋅x̄
```

Where x̄ = (x₁ + x₂ + ... + xₙ)/n and ȳ = (y₁ + y₂ + ... + yₙ)/n represent the arithmetic means of the x and y coordinates of the given points.

---

## Tasks📝
1. Manually create several images containing scattered points that show a correlation (at least one image with ascending correlation and one with descending correlation)
2. Using Python, determine the coordinates (xᵢ, yᵢ) of the points from the images
3. Calculate and display the values of a, b and Q(a,b) according to the formulas above
4. Draw the trend line on the images using a different color

---

## Implementation Details💻
- Use Python for implementation
- Image processing libraries may be used for point detection
- Visualization should include both the original points and the calculated trend line
- The trend line should be clearly visible in a contrasting color