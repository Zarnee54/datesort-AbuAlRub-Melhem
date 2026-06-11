import csv


class SampleManager:

    def __init__(self):
        self.samples = []

    def load_samples(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            self.samples = list(reader)

    def add_sample(self, sample):
        self.samples.append(sample)

    def get_samples(self):
        return self.samples

    def get_statistics(self):
        stats = {
            "total": len(self.samples),
            "premium": 0,
            "standard": 0,
            "rejected": 0
        }

        for s in self.samples:
            grade = s.get("grade", "Unknown")

            if grade == "Premium":
                stats["premium"] += 1
            elif grade == "Standard":
                stats["standard"] += 1
            elif grade == "Rejected":
                stats["rejected"] += 1

        return stats

    def save_samples(self, filename):
        if not self.samples:
            return

        keys = self.samples[0].keys()

        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.samples)