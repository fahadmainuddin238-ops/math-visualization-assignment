import numpy as np
import matplotlib.pyplot as plt

midterm = np.array([85, 72, 90, 66, 78,
                    92, 60, 74, 88, 95])

final = np.array([80, 70, 94, 68, 75,
                  90, 65, 72, 84, 96])

# Best-fit line
slope, intercept = np.polyfit(midterm, final, 1)

# Prediction line
predicted_final = slope * midterm + intercept

# Plot
plt.figure(figsize=(8, 6))

plt.scatter(midterm, final, label="Original Data")

plt.plot(midterm,
         predicted_final,
         label="Best-Fit Line")

plt.title("Midterm vs Final Prediction")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")

plt.legend()
plt.grid(True)

plt.savefig("score_prediction.png")

plt.show()

# Prediction examples
example_scores = [50, 75, 100]

print("Prediction Examples:\n")

for score in example_scores:
    predicted = slope * score + intercept
    print(f"Midterm {score} -> Predicted Final: {predicted:.2f}")