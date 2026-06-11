import json
import csv


class SampleDataCreator:

    def generate_varieties(self):
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
            },
            "Sukkari": {
                "premium_weight": 22,
                "premium_size": 4.8,
                "standard_weight": 17,
                "standard_size": 3.8
            }  
        }

        with open("varieties.json", "w", encoding="utf-8") as file:
            json.dump(varieties, file, indent=4)

    def generate_samples(self):
        samples = [
            ["sample_id", "variety", "weight", "size", "color"],
            [1, "Medjool", 26, 5.3, "Dark Brown"],
            [2, "Medjool", 20, 4.1, "Brown"],
            [3, "Ajwa", 19, 3.6, "Black"],
            [4, "Ajwa", 13, 2.9, "Dark Brown"],
            [5, "Deglet Noor", 16, 4.0, "Golden"],
            [6, "Deglet Noor", 11, 2.8, "Yellow"],
            [7, "Sukkari", 23, 4.9, "Golden Brown"],
            [8, "Sukkari", 18, 3.9, "Light Brown"]
        ]

        with open("samples.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(samples)


if __name__ == "__main__":
    creator = SampleDataCreator()
    creator.generate_varieties()
    creator.generate_samples()
    print("Dataset files created successfully: varieties.json & samples.csv")
