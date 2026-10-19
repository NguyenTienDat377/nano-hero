# Nano-Hero

From-scratch pre-training of a 135M-parameter Llama-style model on a single RTX 3060 Ti.

## Status: v0 (in progress)

v0 goal: a 100M-token run with AdamW, with **measured** tok/s, peak VRAM and validation loss.
Numbers below are filled in only after they are measured.

| Metric | Value |
| --- | --- |
| Throughput (tok/s) | TBD |
| Peak VRAM (GB) | TBD |
| Final val loss | TBD |

## Quickstart

```bash
pip install -e ".[dev]"
pytest
python scripts/prepare_data.py
python scripts/train.py configs/smoke.json
python scripts/train.py configs/v0_135m.json
```
