# HGSI / CCD: conversational fine-tuning dataset + Lean 4 sketch

Training data and a small formalization based on Michael Aaron Russell's
October 2026 paper on **Human-Guided Super Intelligence (HGSI)** and the
**Collaborative Cognitive Dynamic (CCD)**.

## Links

- **Paper / archive (Zenodo):** [https://doi.org/10.5281/zenodo.23083737](https://doi.org/10.5281/zenodo.23083737)
- **Dataset on Hugging Face:** [PrimarchMI/hgsi-ccd-canonical](https://huggingface.co/datasets/PrimarchMI/hgsi-ccd-canonical)
- **ORCID iD:** [0009-0001-3360-6709](https://orcid.org/0009-0001-3360-6709)

## Contents

```
data/
  hgsi_ccd_conversations.jsonl        62 base conversations (3 multi-turn)
  hgsi_ccd_conversations_extra.jsonl  40 extra conversations (8 multi-turn): casual phrasing,
                                      misconception corrections, out-of-scope refusals, injection tests
  hgsi_all.jsonl                      merged + shuffled (seed 42), 102 rows
scripts/
  gen_base.py   regenerates the base file
  gen_extra.py  regenerates the extra file
  merge.py      builds hgsi_all.jsonl
lean/           Lean 4 sketch of the paper's definitions (see note below)
```

## Data format

One JSON object per line, chat format with `system`, `user`, and `assistant` roles:

```json
{"messages": [
  {"role": "system", "content": "..."},
  {"role": "user", "content": "..."},
  {"role": "assistant", "content": "..."}
]}
```

Load with Hugging Face `datasets`:

```python
from datasets import load_dataset
ds = load_dataset("json", data_files="data/hgsi_all.jsonl", split="train")
ds = ds.train_test_split(test_size=0.1, seed=42)
# ds.push_to_hub("PrimarchMI/hgsi-ccd-canonical")
```

Regenerate everything:

```bash
python3 scripts/gen_base.py && python3 scripts/gen_extra.py && python3 scripts/merge.py
```

## Notes on the data

- The answers are written from the paper's stated definitions. Where the paper does not
  say something (specific axioms, custodian qualification criteria, implementation
  details, empirical results), the rows say so instead of inventing an answer.
- It's a small dataset (~100 rows). It's enough to test a pipeline and teach tone and
  refusals, but not enough to reliably teach the content. Add paraphrased variants
  before relying on it.

## Lean 4

`lean/` contains a minimal formalization: the 4 to 8 axiom bound, the S₀→S₃ state chain,
the authorization rule (`M(τ)` ∧ qualified custodian ∧ recorded decision), and the theorem that
machine verification alone is not sufficient.

**Status: not yet compiled.** Check it before relying on it:

```bash
cd lean && lake build
```

If the pinned toolchain in `lean/lean-toolchain` doesn't suit your setup, change it to your
installed Lean 4 version.

## Citation

If you use this dataset, please cite the Zenodo record:
https://doi.org/10.5281/zenodo.23083737

## License

Choose and add a license before publishing. The dataset reflects the paper's content, so
confirm you have the author's permission to redistribute it.
