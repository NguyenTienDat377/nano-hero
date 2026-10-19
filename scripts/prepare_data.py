"""Stream HuggingFaceFW/fineweb-edu (sample-10BT), tokenize, write uint16 shards.

Output: data/train_000.bin ..., data/val_000.bin, data/meta.json

TODO:
- load SmolLM2-135M tokenizer
- datasets.load_dataset(..., streaming=True)
- append EOS between documents
- write 100M-token train shards + one small val shard
"""
