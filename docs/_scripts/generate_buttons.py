"""Generate button images from button_base.png, guide_subtitle, and sidebar_color."""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SUBTITLE_COLOR = (23, 24, 23)

# Text placement as proportions of the base image dimensions.
# Button: region right of the divider where the guide name is drawn.
BUTTON_TEXT_TOP = 0.328
BUTTON_TEXT_BOTTOM = 0.676

# Website banner (16:9): region below the advISO logo for the guide name.
BANNER_TEXT_LEFT = 0.359
BANNER_TEXT_TOP = 0.586
BANNER_TEXT_RIGHT = 0.947
BANNER_TEXT_BOTTOM = 0.728

FONT_BOLD_CANDIDATES = [
    ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 0),
    ('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', 0),
    ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 0),
    ('/System/Library/Fonts/Helvetica.ttc', 1),                     # macOS Bold
    ('C:/Windows/Fonts/arialbd.ttf', 0),                            # Windows
]

FONT_BOLD_ITALIC_CANDIDATES = [
    ('/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf', 0),
    ('/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf', 0),
    ('/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf', 0),
    ('/System/Library/Fonts/Helvetica.ttc', 3),                     # macOS Bold Oblique
    ('C:/Windows/Fonts/arialbi.ttf', 0),                            # Windows
]


def _find_font(italic=False):
    candidates = FONT_BOLD_ITALIC_CANDIDATES if italic else FONT_BOLD_CANDIDATES
    for path, index in candidates:
        if os.path.exists(path):
            return path, index
    return None, 0


def _hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def _rounded_rect(size, radius, fill):
    """Create an RGBA image with a rounded rectangle."""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(0, 0), (size[0]-1, size[1]-1)], radius=radius, fill=fill)
    return img


def _fit_font(font_path, text, max_width, start_size, index=0, max_height=None):
    """Find the largest font size that fits text within max_width (and max_height if given)."""
    font_size = start_size
    font = ImageFont.truetype(font_path, font_size, index=index)
    while font_size > 10:
        bbox = font.getbbox(text)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        if tw <= max_width and (max_height is None or th <= max_height):
            return font
        font_size -= 2
        font = ImageFont.truetype(font_path, font_size, index=index)
    return font



def generate_button(subtitle, bg_color, docs_dir=None):
    """Generate a 1800x300 horizontal button image."""
    if docs_dir is None:
        docs_dir = Path(__file__).parent.parent
    else:
        docs_dir = Path(docs_dir)

    base_path = docs_dir / '_static' / 'base' / 'button_base.png'
    out_path = docs_dir / '_static' / 'brand' / 'button_horizontal.png'
    out_path.parent.mkdir(parents=True, exist_ok=True)

    bg_rgb = _hex_to_rgb(bg_color) if isinstance(bg_color, str) else bg_color

    width, height = 2100, 300
    padding_x = 15
    padding_y = 10
    corner_radius = 50

    canvas = _rounded_rect((width, height), corner_radius, (*bg_rgb, 255))

    base = Image.open(base_path).convert('RGBA')
    base_w, base_h = base.size

    # Scale base to fit canvas height, leaving extra room on the right for text
    inner_h = height - (padding_y * 2)
    scale = inner_h / base_h
    scaled_w = int(base_w * scale)
    scaled_h = inner_h
    logo = base.resize((scaled_w, scaled_h), Image.LANCZOS)
    logo_y = (height - scaled_h) // 2
    canvas.paste(logo, (padding_x, logo_y), logo)

    # Text height constraint from proportional constants
    text_area_h = int((BUTTON_TEXT_BOTTOM - BUTTON_TEXT_TOP) * base_h * scale)

    alpha = logo.split()[3]
    pixels = alpha.load()

    # Find divider and advISO right edge from the UNSCALED base (avoids anti-aliasing issues)
    base_alpha = base.split()[3]
    base_pixels = base_alpha.load()
    orig_divider_right = 0
    for x in range(base_w - 1, 0, -1):
        col_sum = sum(base_pixels[x, y] for y in range(base_h))
        if col_sum > 0:
            orig_divider_right = x
            break
    orig_divider_left = orig_divider_right
    for x in range(orig_divider_right, 0, -1):
        col_sum = sum(base_pixels[x, y] for y in range(base_h))
        if col_sum == 0:
            orig_divider_left = x + 1
            break
    orig_adviso_right = 0
    for x in range(orig_divider_left - 1, 0, -1):
        col_sum = sum(base_pixels[x, y] for y in range(base_h))
        if col_sum > 0:
            orig_adviso_right = x
            break
    # Mirror the advISO-to-divider gap on the right side (scaled)
    gap_left = int((orig_divider_left - orig_adviso_right) * scale)
    divider_right_scaled = int(orig_divider_right * scale)
    text_start_x = padding_x + divider_right_scaled + gap_left

    draw = ImageDraw.Draw(canvas)

    font_path, font_index = _find_font(italic=False)
    avail_w = width - padding_x - text_start_x
    if font_path:
        font = _fit_font(font_path, subtitle, avail_w, int(text_area_h * 1.2),
                         index=font_index, max_height=text_area_h)
    else:
        font = ImageFont.load_default()

    bbox = font.getbbox(subtitle)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = text_start_x
    # Find divider vertical centre
    divider_rows = [y for y in range(scaled_h) if pixels[divider_right_scaled, y] > 0]
    if divider_rows:
        divider_centre_y = logo_y + (divider_rows[0] + divider_rows[-1]) // 2
    else:
        divider_centre_y = height // 2
    text_y = divider_centre_y - text_h // 2 - bbox[1] + int(height * 0.05)
    draw.text((text_x, text_y), subtitle, fill=SUBTITLE_COLOR, font=font)

    canvas.save(out_path)
    return out_path


def generate_website_banner(subtitle, bg_color, docs_dir=None):
    """Generate a 16:9 website banner image."""
    if docs_dir is None:
        docs_dir = Path(__file__).parent.parent
    else:
        docs_dir = Path(docs_dir)

    base_path = docs_dir / '_static' / 'base' / 'logo_base_16x9.png'
    out_path = docs_dir / '_static' / 'brand' / 'button_website.png'
    out_path.parent.mkdir(parents=True, exist_ok=True)

    bg_rgb = _hex_to_rgb(bg_color) if isinstance(bg_color, str) else bg_color

    base = Image.open(base_path).convert('RGBA')
    base_w, base_h = base.size

    width = base_w
    height = base_h
    corner_radius = 40

    # Text placement from proportional constants
    box_left = int(BANNER_TEXT_LEFT * width)
    box_top = int(BANNER_TEXT_TOP * height)
    box_right = int(BANNER_TEXT_RIGHT * width)
    box_bottom = int(BANNER_TEXT_BOTTOM * height)

    canvas = _rounded_rect((width, height), corner_radius, (*bg_rgb, 255))
    canvas.paste(base, (0, 0), base)

    text_area_w = box_right - box_left
    text_area_h = box_bottom - box_top

    font_path, font_index = _find_font()
    if font_path:
        font = _fit_font(font_path, subtitle, text_area_w, int(text_area_h * 1.2),
                         index=font_index, max_height=text_area_h)
    else:
        font = ImageFont.load_default()

    bbox = font.getbbox(subtitle)
    draw = ImageDraw.Draw(canvas)
    text_x = box_left
    text_y = box_top + (text_area_h - (bbox[3] - bbox[1])) // 2 - bbox[1]
    draw.text((text_x, text_y), subtitle, fill=SUBTITLE_COLOR, font=font)

    canvas.save(out_path)
    return out_path


def generate_buttons(subtitle, bg_color, docs_dir=None):
    """Generate all button variants."""
    generate_button(subtitle, bg_color, docs_dir)
    generate_website_banner(subtitle, bg_color, docs_dir)


if __name__ == '__main__':
    from conf import guide_subtitle, sidebar_color
    generate_buttons(guide_subtitle, sidebar_color)
