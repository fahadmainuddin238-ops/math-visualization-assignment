import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-10, 10, 500)

# Mixed custom equation
# This equation combines cubic and cosine behavior
y = 0.02 * x**3 - 0.5 * x + np.cos(x)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(x, y)

plt.title("Custom Equation Visualization")
plt.xlabel("x values")
plt.ylabel("y values")

plt.grid(True)

# Save figure
plt.savefig("own_equation.png")

plt.show()