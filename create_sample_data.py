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
            },
            "Ajwa": {
                "premium_weight": 18,
                "premium_size": 3.5,
                "standard_weight": 14,
                "standard_size": 3.0
            },
            "Deglet Noor": {
                "premium_weight": 15,
                "premium_size": 3.8,
                "standard_weight": 12,
                "standard_size": 3.0
            }
        }

        with open("varieties.json", "w") as file:
            json.dump(varieties, file, indent=4)

    def create_samples(self):
        samples = [
            ["sample_id", "variety", "weight", "size", "color"],
            [1, "Medjool", 26, 5.3, "Dark Brown"],
            [2, "Medjool", 20, 4.1, "Brown"],
            [3, "Ajwa", 19, 3.6, "Black"],
            [4, "Ajwa", 13, 2.9, "Dark Brown"],
            [5, "Deglet Noor", 16, 4.0, "Golden"],
            [6, "Deglet Noor", 11, 2.8, "Yellow"]
        ]

        with open("samples.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(samples)


if __name__ == "__main__":
    creator = SampleDataCreator()
    creator.create_varieties()
    creator.create_samples()
    print("Dataset files created successfully.")