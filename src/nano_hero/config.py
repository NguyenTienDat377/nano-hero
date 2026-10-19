"""ModelConfig and TrainConfig dataclasses, loaded from a JSON file.

TODO:
- @dataclass ModelConfig (fields match configs/*.json "model")
- @dataclass TrainConfig (fields match configs/*.json "train")
- load_config(path) -> (ModelConfig, TrainConfig)
- validate: d_model % n_head == 0, n_head % n_kv_head == 0
"""
