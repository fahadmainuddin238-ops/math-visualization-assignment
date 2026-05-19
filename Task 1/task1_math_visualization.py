import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-10, 10, 500)

# Functions
y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

# Create figure
plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='y = x', linestyle='-')
plt.plot(x, y2, label='y = x²', linestyle='--')
plt.plot(x, y3, label='y = sin(x)', linestyle='-.')
plt.plot(x, y4, label='y = e^(-0.1x)cos(x)', linestyle=':')

# Labels and title
plt.title("Mathematical Function Visualization")
plt.xlabel("x values")
plt.ylabel("y values")

plt.legend()
plt.grid(True)

# Save figure
plt.savefig("function_plot.png")

plt.show()