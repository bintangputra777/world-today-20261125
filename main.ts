// Entry for the make.fun bounty "Sum up 25 November's world news in one image"
// (news-image-20261125).
//
// The entry ships its picture as a file in this repository: assets/entry.png,
// a 1024x1024 PNG drawn in code by scripts/render.py. Running this program
// copies that file to /output/entry.png. No network access, no randomness,
// no environment input — every run writes the same bytes as the last one.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot: string = dirname(fileURLToPath(import.meta.url));
const sourceImage: string = join(repoRoot, "assets", "entry.png");
const destination: string = "/output/entry.png";

mkdirSync(dirname(destination), { recursive: true });
copyFileSync(sourceImage, destination);
