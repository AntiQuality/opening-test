import numpy as np
import matplotlib.pyplot as plt

# Sample dataset: square footage and corresponding house prices
square_feet = np.array([650, 700, 750, 800, 850, 900, 950, 1000])
prices = np.array([180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000])

# Perform linear regression using NumPy's polyfit
slope, intercept = np.polyfit(square_feet, prices, 1)

# Generate line of best fit for plotting
x_vals = np.linspace(square_feet.min(), square_feet.max(), 100)
y_vals = slope * x_vals + intercept

print(f"Slope: {slope:.2f} price per square foot")
print(f"Intercept: {intercept:.2f}")

# Predict price for a 1200 sq ft house
sqft_example = 1200
predicted_price = slope * sqft_example + intercept
print(f"Predicted price for {sqft_example} sq ft: ${predicted_price:,.2f}")

# Plotting
plt.scatter(square_feet, prices, label='Data Points')
plt.plot(x_vals, y_vals, color='red', label='Regression Line')
plt.xlabel('Square Feet')
plt.ylabel('Price ($)')
plt.title('House Prices vs. Square Footage')
plt.legend()
plt.tight_layout()
plt.savefig('house_price_regression.png')
plt.close()
