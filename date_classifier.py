import json


class DateClassifier:

    def __init__(self):
        self.varieties = {}

    def load_varieties(self, filename):
        with open(filename, "r") as file:
            self.varieties = json.load(file)

    def classify_sample(self, variety, weight, size):
            if variety not in self.varieties:
                return "Unknown"
            self.last_result = {
            "variety": variety,
            "weight": weight,
            "size": size
            }
            return "Pending"

    

    def classify_samples(self, samples):
        pass

    def get_available_varieties(self):
        return list(self.varieties.keys())