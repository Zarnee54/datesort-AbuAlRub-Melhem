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
        rules = self.varieties[variety]
        if weight >= rules["premium_weight"] and size >= rules["premium_size"]:
            return "Premium"
        elif weight >= rules["standard_weight"] and size >= rules["standard_size"]:
            return "Standard"
        else:
            return "Rejected"

      
    

    def classify_samples(self, samples):
        pass

    def get_available_varieties(self):
        return list(self.varieties.keys())