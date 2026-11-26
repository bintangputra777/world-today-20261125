# Dossier — make.fun bounty "Sum up 25 November's world news in one image"

## Bounty (verified 26 Nov 2026, ~07:55 WIB)

- Bounty: **Sum up 25 November's world news in one image** — https://make.fun/bounty/news-image-20261125
- Slug: `news-image-20261125` · Prize: **$100, 50 places paid** (1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each), USDC on Solana. (The task body's $250 figure is stale for this edition — the live board lists $100, same as the 24 Nov edition.)
- Deadline: **Friday 27 Nov 2026, 07:00 WIB** (2026-11-27T00:00:00Z).
- Judging: an AI judge that can see images compares entries two at a time; the image itself must show the day's news (the judge has no news feed).
- Same format as the accepted 19–24 Nov entries (world-today-20261119 … world-today-20261124); this build reuses their verified render pipeline.

## The image — five stories (checked 26 Nov against Just Security Early Edition 25 Nov, OneTurn, Open Chronicle, Reuters/BusinessWorld, all dated 25 Nov 2026)

1. **HORMUZ — Two tankers hit mines in Strait of Hormuz.** Iran's IRGC says two oil tankers struck naval mines and caught fire in the strait, raising fears for global energy shipping.
2. **TARIFFS — US proposes tariffs on 14 economies.** Washington plans new tariffs on 14 trading partners, including China, the EU and India, after a probe into excess factory capacity.
3. **MARKETS — Wall Street slides 2.2% on AI doubts.** The S&P 500 falls 2.2% and the Nikkei 2.8% as AI-spending doubts deepen; Brent crude rises 1.1% to $89.73 after Gulf attacks.
4. **HUAWEI — Huawei convicted in US criminal trial.** A Brooklyn jury convicts Huawei on 10 of 12 counts, including bank fraud, wire fraud and conspiracy to steal trade secrets.
5. **SPACE — China flies Pakistan's first astronaut.** Shenzhou-24 docks with the Tiangong station carrying Pakistan's first astronaut — the first foreign guest aboard China's station.

Design: same newspaper front-page style as the earlier entries — navy masthead "THE WORLD TODAY / WEDNESDAY · 25 NOVEMBER 2026", five numbered colour-tagged rows, footer citing major news outlets. Rendered in code with Python/PIL (`scripts/render.py`) — no AI image generator.

## Program

`main.ts` copies `assets/entry.png` to `/output/entry.png` — deterministic, no network. Verified locally: two runs byte-identical and equal to the source asset.
