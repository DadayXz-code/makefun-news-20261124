// THE WORLD TODAY — 24 November 2026 news front page.
// Copies the pre-rendered entry.png (drawn from scratch by draw.py,
// a Pillow program that lays out the masthead, lead story, 35 more
// stories, a markets strip and a UTC timeline) to the output
// directory. Deterministic: the same bytes every run. No network.
import { copyFileSync, mkdirSync, readdirSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

// Create the output directory and clear only its contents — never
// remove the directory itself.
mkdirSync(outDir, { recursive: true });
for (const name of readdirSync(outDir)) {
  rmSync(join(outDir, name), { recursive: true, force: true });
}

copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
