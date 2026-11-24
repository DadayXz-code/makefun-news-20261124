# makefun-news-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/DadayXz-code/makefun-news-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/DadayXz-code/makefun-news-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

THE WORLD TODAY — Tuesday 24 November 2026: 36 stories, 7 regions. A newspaper front page drawn entirely in code (Python + Pillow). Lead story: Nvidia brings back Jensen Huang as CEO — board vote unanimous, shares surge, Huang gains about $33bn in a day, after President Trump said he urged the board. Inside: Democrats clinch a 258-seat House majority, Ukraine says it sank a Russian warship off Libya, a factory fire in Indonesia kills 24, COP31 ends with no fossil-fuel deal, Verstappen wins in Las Vegas, Alcaraz takes the ATP Finals, and the World Chess Championship opens — plus a markets strip and a UTC timeline of the day (00:04–07:55, the earliest wire reports, so the page is honest about being built from the morning's news).

## Run it

```sh
python3 draw.py entry.png   # re-render the front page (1024x1024)
MAKEFUN_OUTPUT_DIR=out node main.ts   # write out/entry.png
```

`draw.py` draws the whole front page from scratch with Pillow (masthead, lead story with a drawn NVDA chip illustration, three story columns, markets strip, UTC timeline). `main.ts` copies the rendered `entry.png` to `/output/entry.png` — the same bytes on every run. No network at run time.

---

<sub>Entered on [make.fun](https://make.fun/?ref=c1yxpfdh&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
