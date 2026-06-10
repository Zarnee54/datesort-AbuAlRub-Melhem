import json
import csv


class SampleDataCreator:

    def create_varieties(self):
        varieties = {
            "Medjool": {
                "premium_weight": 24,
                "premium_size": 5.0,
                "standard_weight": 18,
                "standard_size": 4.0
            }
        }

        with open("varieties.json", "w") as file:
            json.dump(varieties, file, indent=4)

    def create_samples(self):
        samples = [
            ["sample_id", "variety", "weight", "size", "color"],
            [1, "Medjool", 26, 5.3, "Dark Brown"]
        ]

        with open("samples.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(samples)


if __name__ == "__main__":
    creator = SampleDataCreator()
    creator.create_varieties()
    creator.create_samples()