from date_classifier import DateClassifier
from sample_manager import SampleManager
from visualizer import Visualizer


def main():
    classifier = DateClassifier()
    manager = SampleManager()
    visualizer = Visualizer()

    classifier.load_varieties("varieties.json")

    manager.load_samples("samples.csv")

    samples = manager.get_samples()

    classified = classifier.classify_samples(samples)

    stats = manager.get_statistics()

    visualizer.plot_grade_distribution(classified)
    visualizer.plot_statistics(stats)


if name == "__main__":
    main()