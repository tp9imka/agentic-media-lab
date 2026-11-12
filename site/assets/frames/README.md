# Frames

Stills from one clip: [examples/clipcheck-fix-loop/results/before.mp4](../../../examples/clipcheck-fix-loop/results/before.mp4),
1920x1080, 30 fps, 600 frames. Each still is scaled to 640x360 JPEG. The home page shows them in
its evidence strip and next to each finding.

| File | Frame | Time | Use |
|---|---|---|---|
| `hf-f015.jpg` | 15 | 0.5 s | strip |
| `hf-f075.jpg` | 75 | 2.5 s | strip |
| `hf-f135.jpg` | 135 | 4.5 s | strip |
| `hf-f195.jpg` | 195 | 6.5 s | strip |
| `hf-f255.jpg` | 255 | 8.5 s | strip |
| `hf-f315.jpg` | 315 | 10.5 s | strip |
| `hf-f375.jpg` | 375 | 12.5 s | strip |
| `hf-f435.jpg` | 435 | 14.5 s | strip |
| `hf-f495.jpg` | 495 | 16.5 s | strip |
| `hf-f555.jpg` | 555 | 18.5 s | strip |
| `hf-d089.jpg` | 89 | 2.967 s | finding E1, empty frame |
| `hf-d239.jpg` | 239 | 7.967 s | finding E2, empty frame |
| `hf-d390.jpg` | 390 | 13.0 s | finding E3, empty frame |
| `hf-d420.jpg` | 420 | 14.0 s | finding W1, stray number |

The frame number is zero-based. This command reproduces `hf-d420.jpg` byte for byte with
ffmpeg 7.1.1 (checked on 2026-11-12); change `420` and the file name for any other row:

```sh
ffmpeg -i examples/clipcheck-fix-loop/results/before.mp4 -vf "select=eq(n\,420),scale=640:360" -frames:v 1 -q:v 3 site/assets/frames/hf-d420.jpg
```

Licence: rendered clips and images under `examples/**/results/` are CC BY 4.0, and these stills
are cut from one of them.
