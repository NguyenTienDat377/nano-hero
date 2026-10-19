"""Training entrypoint.

Usage: python scripts/train.py configs/smoke.json

TODO:
- load config, set seed, build model / optimizer / loaders
- loop: grad accumulation under bf16 autocast, clip, step, set LR
- every eval_every: val loss; log to runs/<name>/metrics.jsonl
- log tok/s and torch.cuda.max_memory_allocated()
- every ckpt_every: save checkpoint
"""
