// Entry for the make.fun bounty "Sum up 25 November's world news in one image"
// (news-image-20261125).
//
// The program writes the pre-rendered summary image held in this repository
// (assets/entry.png, 1024x1024 PNG) to /output/entry.png. It is the simplest
// program the brief allows: a deterministic copy of an image the repository
// holds. No network, no randomness, no environment input — every run writes
// the same bytes.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot: string = dirname(fileURLToPath(import.meta.url));
const source: string = join(repoRoot, "assets", "entry.png");
const output: string = "/output/entry.png";

mkdirSync(dirname(output), { recursive: true });
copyFileSync(source, output);
