#!/usr/bin/env python3
"""Render 012 AI Payment cards."""
from PIL import Image, ImageDraw, ImageFont
import os

W = 1800
MARGIN = 60
BG  = (18, 18, 24)
ACC = (255, 120, 50)
WH  = (255, 255, 255)
GR  = (138, 138, 154)
DIM = (106, 106, 122)

def find_font(size, bold=False):
    candidates = [
        f"/usr/share/fonts/opentype/noto/NotoSansCJK-{'Bold' if bold else 'Regular'}.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                continue
    return ImageFont.load_default()

FONT_TITLE = find_font(36, True)
FONT_H3 = find_font(26, True)
FONT_BODY = find_font(20)
FONT_SMALL = find_font(17)
FONT_MINI = find_font(15)

def wrap_cjk(draw, text, max_width, font):
    lines = []
    current = ""
    for ch in text:
        test = current + ch
        if draw.textlength(test, font=font) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines

# ============================================================
# Card 1: 48h Timeline
# ============================================================
def render_timeline():
    events = [
        ("06-02", "腾讯港股 +10.46%",
         "微信 AI 智能体内测消息引爆，市值 +4000 亿港元"),
        ("06-08", "小程序开发者接入",
         "京东 / 美团 / 滴滴 / 得物百米冲刺接入内测"),
        ("06-16", "三线齐发·决战日",
         "蚂蚁阿宝上线 + 银联 APOP 落地 + 京东 ClawTip"),
        ("06-17 14:02", "微信 AI 专属卡正式上线",
         "Mac WorkBuddy 5.1.1，首批接入美团餐饮团购"),
    ]

    avail_w = W - 2 * MARGIN
    tmp = Image.new("RGB", (1, 1))
    tmp_d = ImageDraw.Draw(tmp)

    h = MARGIN + 50 + 20
    h += 3 + 30
    for date, title, desc in events:
        h += 34 + 28 + 20
    h += MARGIN + 30

    H = h
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    y = MARGIN
    draw.text((MARGIN, y), "48h 窗口：从港股 +4000 亿到三线齐发", fill=ACC, font=FONT_TITLE)
    y += 70
    draw.rectangle([MARGIN, y, MARGIN + 60, y + 3], fill=ACC)
    y += 30

    for date, title, desc in events:
        draw.text((MARGIN, y), date, fill=ACC, font=FONT_H3)
        dw = int(draw.textlength(date, font=FONT_H3))
        draw.text((MARGIN + dw + 20, y + 2), title, fill=WH, font=FONT_BODY)
        y += 36
        draw.text((MARGIN + dw + 20, y), desc, fill=GR, font=FONT_SMALL)
        y += 30

    draw.text((MARGIN, H - MARGIN - 20),
              "数据窗口：2026-06-02 ~ 2026-06-17 18:30 CST",
              fill=DIM, font=FONT_MINI)

    out = "/home/zhang/china-ai-frontline/assets/drafts/012/timeline-48h.png"
    img.save(out, "PNG")
    print(f"Timeline saved: {out} ({W}x{H})")

# ============================================================
# Card 2: Three Routes Framework
# ============================================================
def render_routes():
    routes = [
        ("微信 AI 专属卡",
         "账户层安全",
         ["给 AI 一张子卡，充值上限 = AI 能花的最大值",
          "主账隔离，每笔交易手机端二次确认"],
         "做在花钱之前"),
        ("蚂蚁阿宝 + Token Pay",
         "赔付层信任",
         ["全端 AI 化，3 亿笔积累，Token Pay 按调用计费",
          "你敢付，我敢赔"],
         "做在花钱之后"),
        ("银联 APOP 协议",
         "协议层中立",
         ["四方模式，19 家伙伴，4600 万境外商户",
          "不做产品，做所有 AI 都能接的底层协议"],
         "做在所有人之侧"),
    ]

    COL_W = 520
    GAP = 50
    CARD_W = 2 * MARGIN + 3 * COL_W + 2 * GAP
    avail_h_per = 260

    H = MARGIN + 50 + 30 + avail_h_per + MARGIN + 40
    img = Image.new("RGB", (CARD_W, H), BG)
    draw = ImageDraw.Draw(img)

    y = MARGIN
    draw.text((MARGIN, y), "三条路线，三个答案，同一道题", fill=ACC, font=FONT_TITLE)
    y += 60
    draw.text((MARGIN, y), "AI 帮你花钱的时候，信任从哪里来？", fill=GR, font=FONT_BODY)
    y += 20
    draw.rectangle([MARGIN, y, MARGIN + 80, y + 3], fill=ACC)
    y += 30

    for i, (name, layer, desc_lines, tagline) in enumerate(routes):
        x = MARGIN + i * (COL_W + GAP)
        card_y = y
        card_h = avail_h_per

        # Card bg
        draw.rectangle([x, card_y, x + COL_W, card_y + card_h],
                       fill=(30, 30, 38), outline=(50, 50, 60), width=1)

        # Layer tag badge
        tag_x = x + 18
        tag_y = card_y + 16
        tw = int(draw.textlength(layer, font=FONT_SMALL)) + 30
        draw.rectangle([tag_x, tag_y, tag_x + tw, tag_y + 26], fill=ACC)
        draw.text((tag_x + 15, tag_y + 4), layer, fill=BG, font=FONT_SMALL)

        # Name
        ny = tag_y + 38
        draw.text((x + 18, ny), name, fill=WH, font=FONT_H3)

        # Description
        dy = ny + 38
        for dl in desc_lines:
            draw.text((x + 18, dy), dl, fill=GR, font=FONT_SMALL)
            dy += 26

        # Tagline
        ty = card_y + card_h - 36
        draw.text((x + 18, ty), tagline, fill=ACC, font=FONT_SMALL)

    draw.text((MARGIN, H - MARGIN - 20),
              "微信把安全做在花钱之前，蚂蚁做在花钱之后，银联做在所有人之侧",
              fill=DIM, font=FONT_MINI)

    out = "/home/zhang/china-ai-frontline/assets/drafts/012/routes-framework.png"
    img.save(out, "PNG")
    print(f"Routes saved: {out} ({CARD_W}x{H})")

if __name__ == "__main__":
    render_timeline()
    render_routes()
