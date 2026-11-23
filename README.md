# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/kuni29/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/kuni29/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image that sums up the world news of Monday 23 November 2026, drawn as a newspaper front page in a graphic-recording style: a large central visual for the day's biggest story — Ukraine's sea drones sinking a Russian warship docked at Benghazi, taking the war 2,400 km from home waters — a labelled atlas strip marking where the day happened (Mexico City, Washington, Copenhagen, Kyiv, Benghazi, Khartoum, Seoul, Tokyo), a "how today connects" arrow flow from the AI rout to Monday's market bounce and from the Libya strike to the Sharara oilfield shutdown, two more hero stories (markets bounce after the worst week since 2020: Nasdaq futures +3.0%, S&P +2.2%, gold $3,620; Democrats' biggest House majority in decades), three mid stories (Russian strikes kill 11 in the Kyiv region; Denmark says Russia plotted to kill a rapper in Copenhagen; Europe and Japan reach Mercury) and 24 one-line briefs from every region, 30 stories in all, each colour-coded by category with a legend. Every story was first reported on 23 November 2026. The picture is designed in `design.html` with hand-drawn inline SVG illustrations and rendered to `entry.png` by `render.mjs` (headless Chrome), so every word is typeset, not generated: no garbled text. `main.py` delivers the image bytes to the output directory, unchanged on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024×1024 PNG, under the 1 MiB cap).

---
<sub>Entered on [make.fun](https://make.fun/?ref=sjptyjw4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
