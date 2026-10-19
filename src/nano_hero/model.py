"""NanoHero model: RMSNorm, RoPE, GQA attention (+QK-norm), SwiGLU, tied embeddings.

TODO:
- RMSNorm (compute in fp32, cast back)
- precompute RoPE cos/sin + apply_rope(q, k)
- Attention: GQA with F.scaled_dot_product_attention(is_causal=True)
- SwiGLU MLP
- Block (pre-norm, residual)
- NanoHero: embed -> blocks -> final norm -> lm_head (weight tied to embed)
- forward(idx, targets=None) -> (logits, loss)
"""
