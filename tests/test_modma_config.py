from neurofeaturefusion.datasets.modma.config import MODMAConfig


def test_modma_config():
    config = MODMAConfig("data/MODMA")

    assert config.validate() is True