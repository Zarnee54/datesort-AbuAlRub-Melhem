import matplotlib.pyplot as plt


class Visualizer:

    def plot_grade_distribution(self, samples):
        grades = {"Premium": 0, "Standard": 0, "Rejected": 0}

        for s in samples:
            grade = s.get("grade", "Unknown")
            if grade in grades:
                grades[grade] += 1

        plt.bar(grades.keys(), grades.values())
        plt.title("Grade Distribution")
        plt.xlabel("Grade")
        plt.ylabel("Count")
        plt.show()

    def plot_statistics(self, stats):
        labels = stats.keys()
        values = stats.values()

        plt.plot(list(labels), list(values), marker='o')
        plt.title("Sample Statistics")
        plt.xlabel("Category")
        plt.ylabel("Count")
        plt.show()