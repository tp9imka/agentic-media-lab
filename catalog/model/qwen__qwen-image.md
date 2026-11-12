# Qwen-Image

`model:qwen/qwen-image` - model - <https://huggingface.co/Qwen/Qwen-Image-2.1>

Alibaba Qwen's image generation and editing family. Version 2.1 (September 2026) is a 7.1B model with an 8B Qwen3-VL text encoder and transparent (RGBA) output.

Concepts: [Image models](../../docs/glossary.md#image-models), [Still images](../../docs/glossary.md#still-images), [Licences and territory](../../docs/glossary.md#licences-and-territory)

Also known as: Qwen-Image 2.1, Qwen Image 2.1, Qwen-Image-2.1

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It runs on a 64 GB Mac with published timings, but version 2.1 is licensed for research and evaluation only.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: low. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2i, i2i, edit |
| access | weights |
| apple_silicon | documented |
| licence_class | non-commercial |

Keep 2.1 output out of client or paid work unless Qwen grants a separate licence. For tests on a Mac, mflux-generate-qwen-2.1 with -q 8 lowers the 46 GB peak; mflux reports 27 GB peak at -q 8 on an M5 Max. The older 20B Qwen Image in mflux may have a different licence; not checked here.

## Claims

1. The licence defines non-commercial as research or evaluation only.

   > "Non-Commercial" shall mean for research or evaluation purposes only.

   Locator: Qwen-Image-2.1 LICENSE, section 1, definition i. Source: <https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE>, retrieved 2026-11-12.

2. On Apple Silicon mflux's bf16 path is the fastest and most accurate, measured on an M5 Max at about 1.5 s per step and 78 s for 40 steps at 1024x1024.

   > On Apple Silicon the bf16 default is both the fastest and the most accurate path (measured on M5 Max: ~1.5 s/step at 1024², ~78 s for a full 40-step generation

   Locator: mflux src/mflux/models/qwen21/README.md, base generation section. Source: <https://github.com/mflux-community/mflux/blob/main/src/mflux/models/qwen21/README.md>, retrieved 2026-11-12.

3. Peak memory is about 46 GB because the 17.5 GB text encoder stays resident, so mflux names 64 GB as the comfortable default.

   > Peak memory is ~46 GB (the Qwen3-VL text encoder, ~17.5 GB bf16, is never quantized and stays resident), so a 64 GB machine is the comfortable default; use `-q 8` when memory is tighter.

   Locator: mflux src/mflux/models/qwen21/README.md, base generation section. Source: <https://github.com/mflux-community/mflux/blob/main/src/mflux/models/qwen21/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Qwen-Image-2.1 LICENSE and mflux Qwen Image 2.1 README against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `30daee6b2099cad6ee217723d786e4873db97afaf9ddea27fcca054b92a67bb1`
- Lane: local-models

## Observed

Nothing collected yet.

## Related

- integrates_with: [MFLUX](../tool/mflux-community__mflux.md)
- alternative_to: [Z-Image](tongyi-mai__z-image.md)

## Referenced by

- [MFLUX](../tool/mflux-community__mflux.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
