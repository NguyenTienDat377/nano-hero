"""Build the optimizer.

v0: AdamW with two param groups:
- decay: 2D weights (linear layers, embedding)
- no decay: 1D params (norm gains)
v1: Muon for 2D hidden matrices gets added here.
"""
