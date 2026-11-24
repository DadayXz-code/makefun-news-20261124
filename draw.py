#!/usr/bin/env python3
"""Draw THE WORLD TODAY — front page summing up world news of
Tuesday 24 November 2026. Pure Pillow, no network, deterministic.
Writes entry.png (1024x1024) next to this file, or to argv[1]."""
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (22, 22, 22)
RED = (178, 34, 34)
BLUE = (28, 68, 128)
GREY = (96, 92, 84)
LIGHT = (232, 226, 212)
RULE = (180, 172, 156)

FDIR = "/usr/share/fonts/truetype/dejavu/"
SERIF = FDIR + "DejaVuSerif.ttf"
SERIF_B = FDIR + "DejaVuSerif-Bold.ttf"
SANS = FDIR + "DejaVuSans.ttf"
SANS_B = FDIR + "DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(d, y, text, fnt, fill=INK, x0=0, x1=W):
    w = d.textlength(text, font=fnt)
    d.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)


# ---------------------------------------------------------------- stories
# (region, tag colour, title, summary) — every story reported 24 Nov 2026.
LEAD_TITLE = "NVIDIA BRINGS BACK HUANG AS CEO"
LEAD_DEK = ("Nvidia's board unanimously reinstates Jensen Huang as chief "
            "executive — less than two weeks after he resigned — after "
            "President Trump said he personally persuaded the board. "
            "Shares surge and Huang gains about $33bn in a day, while "
            "lawmakers of both parties criticise the move.")
LEAD_FACTS = ["Board vote: unanimous", "Huang +$33bn in a day",
              "Nvidia peak value: ~$5.8tn"]

COL_A = [
    ("NORTH AMERICA", BLUE),
    ("US", "Democrats clinch House majority",
     "At least 258 seats, the largest majority since 1992."),
    ("US", "States sue Musk firms over Grok",
     "Oregon, Virginia sue over 'spicy mode' deepfakes."),
    ("US", "Trump blames Democrats for rout",
     "President blames opposition after a $1tn rout."),
    ("US", "Congressman to quit after inquiry",
     "Rep. Jimmy Gomez to resign after misconduct findings."),
    ("US", "Trump halts toxic blast in Iowa",
     "Army plan to detonate explosives is postponed."),
    ("LATIN AMERICA", BLUE),
    ("BRAZIL", "Brazil lifts inflation forecasts",
     "Markets lift inflation, dollar forecasts for 2026–27."),
    ("WORLD", BLUE),
    ("CLIMATE", "COP31 ends with no fossil-fuel deal",
     "Antalya talks collapse with no fossil-fuel deal."),
    ("ENERGY", "Oil slides about 3%",
     "Crude falls on higher supply and a Libyan reopening."),
    ("SPORT", BLUE),
    ("F1", "Verstappen wins Las Vegas GP",
     "Verstappen takes another win in Las Vegas."),
    ("TENNIS", "Alcaraz wins maiden ATP Finals",
     "Beats Zverev in Turin for a first ATP Finals title."),
    ("CHESS", "World title match opens in Geneva",
     "Gukesh defends his crown against Sindarov in Geneva."),
    ("FOOTBALL", "Women's World Cup hosts set",
     "US to co-host 2031; UK gets the 2035 Women's World Cup."),
]

COL_B = [
    ("EUROPE", BLUE),
    ("EU", "EU unveils 22nd Russia sanctions",
     "New package targets banks, crypto and Russian athletes."),
    ("FINLAND", "Russian ship burns after drone hit",
     "Cargo ship Sparta II burns in the Gulf of Finland."),
    ("PORTUGAL", "Thousands march in Lisbon",
     "Crowds march in Lisbon against the cost of living."),
    ("BELGIUM", "National strike shuts transport",
     "Airports, transport stop in a strike over austerity."),
    ("GERMANY", "Bomb threats hit schools",
     "Schools in Germany and Denmark hit by device alerts."),
    ("NATO", "NATO vows space defence",
     "Alliance pledges space defence after satellite report."),
    ("ARMENIA", "New charter drops Karabakh claim",
     "Draft constitution drops the Nagorno-Karabakh claim."),
    ("MIDDLE EAST", BLUE),
    ("LIBYA", "Ukraine says it sank Russian warship",
     "Kyiv claims a Benghazi strike sank a Russian corvette."),
    ("GAZA", "Israeli strike kills at least 3",
     "Strike near a Khan Younis police post kills three."),
    ("GAZA", "Four nations urge Gaza aid access",
     "Four nations urge Israel to open Gaza aid access."),
    ("GULF", "Iran eyed in ship cyberattacks",
     "US probes Iran's suspected role in tanker cyberattacks."),
    ("SYRIA", "Landmine kills five children",
     "Blast in the north-west kills five children."),
]

COL_C = [
    ("ASIA-PACIFIC", BLUE),
    ("INDONESIA", "Factory fire kills 24, 30 missing",
     "Blaze at a Banten candy factory kills 24; 30 missing."),
    ("INDIA", "India and Nepal open rail link",
     "Modi and Nepal's PM open the Saryu-Kamala Express."),
    ("CRICKET", "India-New Zealand Test drawn",
     "Wellington Test drawn; Pant's 128 sets a record."),
    ("CHINA", "China sets 2030 welfare targets",
     "Beijing sets 2030 goals for elderly care and childcare."),
    ("KOREA", "Seoul reshuffles top posts",
     "President names a new foreign minister and intel chief."),
    ("BANGLADESH", "Dhaka vows to arrest Hasina",
     "Dhaka vows to arrest ex-PM Hasina if she returns."),
    ("THAILAND", "Bangkok curbs mining chemicals",
     "Bangkok curbs mining chemicals over river pollution."),
    ("INDIA", "Sensex drops 1,484 points",
     "Shares fall 1.77% to 82,435; Nifty down 451."),
    ("AFRICA", BLUE),
    ("SENEGAL", "Migrant boat capsizes",
     "Boat sinks off Senegal; dozens of migrants missing."),
    ("S. AFRICA", "Mass shootings kill 17",
     "Seventeen killed in mass shootings across the country."),
    ("SOMALIA", "Somalia sinks into crisis",
     "Corruption and power struggles deepen the crisis."),
]

TIMELINE = [
    ("00:04", "Iran ship attacks hit record"),
    ("00:10", "Landmine kills 5 children"),
    ("00:15", "Oil falls ~3% on Libya reopening"),
    ("00:41", "Libya rejects foreign battleground"),
    ("02:36", "Four nations urge Gaza aid"),
    ("05:48", "Wall Street rebounds"),
    ("07:55", "Nvidia value tops Germany's GDP"),
]


def section_header(d, y, x, w, text):
    f = font(SANS_B, 12)
    d.rectangle([x, y, x + w, y + 18], fill=INK)
    d.text((x + 8, y + 2), text, font=f, fill=PAPER)
    return y + 23


def story_block(d, x, y, w, tag, title, summary):
    """Draw one compact story; return height used."""
    tag_f = font(SANS_B, 10)
    t_f = font(SANS_B, 12)
    s_f = font(SANS, 11)
    tag_w = d.textlength(tag, font=tag_f) + 10
    d.rectangle([x, y, x + tag_w, y + 14], fill=RED)
    d.text((x + 5, y + 2), tag, font=tag_f, fill=(255, 255, 255))
    tx = x + tag_w + 7
    tlines = wrap(d, title, t_f, w - (tx - x))
    ty = y - 1
    for ln in tlines[:2]:
        d.text((tx, ty), ln, font=t_f, fill=INK)
        ty += 15
    slines = wrap(d, summary, s_f, w)
    sy = max(y + 16, ty + 2)
    for ln in slines[:2]:
        d.text((x, sy), ln, font=s_f, fill=(52, 52, 48))
        sy += 13
    return max(ty, sy) + 4 - y


def draw_column(d, x, y, w, items, bottom):
    for it in items:
        if len(it) == 2:
            y = section_header(d, y, x, w, it[0])
        else:
            tag, title, summary = it
            used = story_block(d, x, y, w, tag, title, summary)
            y += used
        if y > bottom - 20:
            print(f"OVERFLOW in column x={x}: y={y} > {bottom}", file=sys.stderr)
    return y


def draw_lead_art(d, x, y, w, h):
    """Drawn illustration: chip, rising chart, NVDA ticker."""
    d.rectangle([x, y, x + w, y + h], fill=(16, 32, 54))
    d.rectangle([x, y, x + w, y + h], outline=(255, 255, 255), width=2)
    # chip
    cx, cy, cw, chh = x + 28, y + 30, 96, 96
    d.rectangle([cx, cy, cx + cw, cy + chh], fill=(34, 120, 90))
    d.rectangle([cx + 18, cy + 18, cx + cw - 18, cy + chh - 18],
                outline=(255, 255, 255), width=2)
    d.text((cx + 30, cy + 38), "NVDA", font=font(SANS_B, 20), fill=(255, 255, 255))
    for i in range(3):
        d.line([cx + 22 + i * 26, cy - 12, cx + 22 + i * 26, cy],
               fill=(255, 255, 255), width=3)
        d.line([cx + 22 + i * 26, cy + chh, cx + 22 + i * 26, cy + chh + 12],
               fill=(255, 255, 255), width=3)
    # rising chart
    pts = [(x + 150, y + h - 42), (x + 185, y + h - 66), (x + 215, y + h - 58),
           (x + 250, y + h - 84), (x + 285, y + h - 108)]
    d.line(pts, fill=(118, 200, 90), width=5, joint="curve")
    d.polygon([(x + 285, y + h - 108), (x + 300, y + h - 108),
               (x + 300, y + h - 92)], fill=(118, 200, 90))
    d.text((x + 150, y + 26), "+$33bn", font=font(SANS_B, 30),
           fill=(118, 200, 90))
    d.text((x + 150, y + 62), "in a single day", font=font(SANS, 14),
           fill=(220, 220, 220))
    d.text((x + 28, y + h - 26), "SHARES SURGE AS HUANG RETURNS",
           font=font(SANS_B, 12), fill=(255, 255, 255))


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead
    d.rectangle([0, 0, W, 8], fill=RED)
    draw_centered(d, 16, "THE WORLD TODAY", font(SERIF_B, 62))
    d.line([28, 92, W - 28, 92], fill=INK, width=2)
    draw_centered(d, 98, "TUESDAY 24 NOVEMBER 2026  •  36 STORIES  •  7 REGIONS",
                  font(SANS_B, 15))
    d.line([28, 122, W - 28, 122], fill=INK, width=1)

    # ---- lead story
    lx, ly, lw = 28, 134, 620
    d.text((lx, ly), "LEAD STORY — TECHNOLOGY", font=font(SANS_B, 12), fill=RED)
    lead_size = 34
    while d.textlength(LEAD_TITLE, font=font(SERIF_B, lead_size)) > lw:
        lead_size -= 1
    d.text((lx, ly + 20), LEAD_TITLE, font=font(SERIF_B, lead_size), fill=INK)
    dek_f = font(SERIF, 16)
    dl = wrap(d, LEAD_DEK, dek_f, lw)
    yy = ly + 70
    for ln in dl[:5]:
        d.text((lx, yy), ln, font=dek_f, fill=INK)
        yy += 21
    facts = "  •  ".join(LEAD_FACTS)
    d.text((lx, yy + 4), facts, font=font(SANS_B, 11), fill=GREY)
    draw_lead_art(d, 668, 134, 328, 168)

    d.line([28, 316, W - 28, 316], fill=RULE, width=1)

    # ---- three-column grid
    col_w = 312
    xs = [28, 356, 684]
    cols = [COL_A, COL_B, COL_C]
    grid_top, grid_bottom = 324, 928
    ends = []
    for x, items in zip(xs, cols):
        ends.append(draw_column(d, x, grid_top, col_w, items, grid_bottom))
    for x in (348, 676):
        d.line([x, grid_top, x, grid_bottom], fill=RULE, width=1)

    # ---- markets strip, placed below the longest column if it fits
    my = max(ends) + 8
    if my + 26 <= 930:
        d.line([28, my, W - 28, my], fill=RULE, width=1)
        d.text((28, my + 6), "MARKETS", font=font(SANS_B, 11), fill=RED)
        d.text((108, my + 6),
               "Sensex 82,435 (−1.77%)  •  Nifty 25,350 (−451)  •  "
               "Stoxx 600 630.24 (+0.73%)  •  Nasdaq surges  •  "
               "Oil −3%  •  Nvidia peak ~$5.8tn",
               font=font(SANS, 11), fill=INK)
    print("column ends:", ends, "markets y:", my, file=sys.stderr)

    # ---- timeline
    d.line([28, 936, W - 28, 936], fill=INK, width=2)
    d.text((28, 942), "THE DAY IN UTC — AS REPORTED", font=font(SANS_B, 12), fill=RED)
    ty = 964
    d.line([48, ty + 5, W - 48, ty + 5], fill=GREY, width=2)
    n = len(TIMELINE)
    for i, (t, label) in enumerate(TIMELINE):
        cx = 60 + i * (W - 120) // (n - 1)
        d.ellipse([cx - 5, ty, cx + 5, ty + 10], fill=RED)
        tf = font(SANS_B, 11)
        tw = d.textlength(t, font=tf)
        d.text((cx - tw / 2, ty + 14), t, font=tf, fill=INK)
        lf = font(SANS, 8)
        lw_ = d.textlength(label, font=lf)
        lx2 = max(28, min(cx - lw_ / 2, W - 28 - lw_))
        d.text((lx2, ty + 28), label, font=lf, fill=GREY)

    # ---- footer
    d.line([28, 1010, W - 28, 1010], fill=RULE, width=1)
    draw_centered(d, 1014, "All stories first reported on 24 November 2026  •  "
                  "Compiled from wire reports  •  Times UTC",
                  font(SANS, 10), fill=GREY)

    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} {img.size}")


if __name__ == "__main__":
    main()
