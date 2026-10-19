"""Model tests (CPU-only, no data needed).

TODO:
- param count of v0 config == 134_518_848
- forward output shape == (B, T, vocab_size)
- causality: changing token t+1 must not change logits at positions <= t
"""
