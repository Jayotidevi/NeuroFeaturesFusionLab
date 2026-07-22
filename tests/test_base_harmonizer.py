from neurofeaturefusion.core.base_dataset import BaseDataset
from neurofeaturefusion.core.base_harmonizer import BaseHarmonizer


class DummyDataset(BaseDataset):

    def __init__(self):
        super().__init__("dummy")
        self.samples = [1, 2, 3]

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        return self.samples[index]


class DummyHarmonizer(BaseHarmonizer):

    def harmonize(self, dataset):

        report = {
            "status": "completed",
            "samples_processed": len(dataset)
        }

        return self.update_metadata(dataset, report)


def test_base_harmonizer():

    dataset = DummyDataset()

    harmonizer = DummyHarmonizer("dummy_harmonizer")

    dataset = harmonizer.harmonize(dataset)

    assert "harmonization" in dataset.metadata

    assert dataset.metadata["harmonization"]["status"] == "completed"

    print("✓ BaseHarmonizer")


if __name__ == "__main__":
    test_base_harmonizer()
