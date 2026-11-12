# mlx-whisper

`tool:ml-explore/mlx-examples/whisper` - tool - <https://github.com/ml-explore/mlx-examples/tree/main/whisper>

Whisper speech recognition in MLX from Apple's MLX examples, installed as the mlx-whisper package with a CLI and a Python function.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: mlx_whisper, MLX Whisper

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the pip-installable way for an agent on a Mac to get a transcript file without compiling anything.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | captions, audio |
| cost | free-local |

Needs ffmpeg. The default model is whisper-tiny, which is too weak for captions; pass --model with a larger mlx-community checkpoint. Memory and speed figures are not in the README. Output formats beyond txt were not checked.

## Claims

1. It runs Whisper speech recognition in MLX.

   > Speech recognition with Whisper in MLX.

   Locator: whisper/README.md, opening line. Source: <https://github.com/ml-explore/mlx-examples/blob/main/whisper/README.md>, retrieved 2026-11-12.

2. The CLI picks the output format with -f and the model with --model.

   > Use `-f` to specify the output format and `--model` to specify the model.

   Locator: whisper/README.md, section Run > CLI. Source: <https://github.com/ml-explore/mlx-examples/blob/main/whisper/README.md>, retrieved 2026-11-12.

3. Without --model it uses the tiny model.

   > The default model is "mlx-community/whisper-tiny".

   Locator: whisper/README.md, section Run > API. Source: <https://github.com/ml-explore/mlx-examples/blob/main/whisper/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. mlx-examples whisper README against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `f73e9067d444d7aa247199ea0ae13e5243426bf82469ba08036685e8a966fcdd`
- Lane: local-models

## Observed

Nothing collected yet.

## Related

- alternative_to: [whisper.cpp](ggml-org__whisper.cpp.md)

## Referenced by

- [whisper.cpp](ggml-org__whisper.cpp.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
