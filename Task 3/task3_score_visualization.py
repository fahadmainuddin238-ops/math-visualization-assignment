import numpy as np
import matplotlib.pyplot as plt

students = ["S1", "S2", "S3", "S4", "S5",
            "S6", "S7", "S8", "S9", "S10"]

midterm = np.array([85, 72, 90, 66, 78,
                    92, 60, 74, 88, 95])

final = np.array([80, 70, 94, 68, 75,
                  90, 65, 72, 84, 96])

# Total score calculation
total = 0.4 * midterm + 0.6 * final

# ==========================================
# Scatter Plot
# ==========================================

plt.figure(figsize=(8, 6))

plt.scatter(midterm, final)

plt.title("Midterm vs Final Scores")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")

plt.grid(True)

plt.savefig("score_scatter.png")

plt.close()

# ==========================================
# Histogram
# ==========================================

plt.figure(figsize=(8, 6))

plt.hist(total, bins=5)

plt.title("Distribution of Total Scores")
plt.xlabel("Total Score")
plt.ylabel("Frequency")

plt.grid(True)

plt.savefig("score_histogram.png")

plt.close()

# ==========================================
# Bar Chart
# ==========================================

plt.figure(figsize=(10, 6))

plt.bar(students, total)

plt.title("Student Total Scores")
plt.xlabel("Students")
plt.ylabel("Total Scores")

plt.grid(True)

plt.savefig("score_bar_chart.png")

plt.show()