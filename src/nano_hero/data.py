"""Read uint16 token shards with np.memmap and yield (x, y) batches.

TODO:
- ShardLoader(data_dir, split, batch_size, seq_len, seed)
- sample random windows of seq_len + 1 tokens; x = w[:-1], y = w[1:]
- convert to int64 torch tensors, pin memory, move to device
"""
