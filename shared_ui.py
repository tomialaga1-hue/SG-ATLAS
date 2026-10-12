# -*- coding: utf-8 -*-
"""
shared_ui.py -- design tokens + reusable UI pieces shared by every page of
the SG-ATLAS site (homepage, tool, database, about).
"""

import os
import base64
import streamlit as st

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------
COLORS = {
    "bg": "#FFFFFF",
    "navy": "#1A385E",
    "navy_dark": "#122C49",
    "crystal_gray": "#ADADAD",
    "btn_primary": "#75C6FB",
    "btn_primary_hover": "#58B4EE",
    "btn_secondary_bg": "#D3D3CE",
    "btn_secondary_border": "#B9B9B2",
    "btn_secondary_text": "#8B8B84",
    "btn_secondary_text_hover": "#5B5B54",
    "charcoal": "#2E2F2F",
}

FONT_DISPLAY = "'Chakra Petch', 'Poppins', sans-serif"
FONT_BODY = "'Poppins', sans-serif"
FONT_MONO = "'Space Mono', 'Courier New', monospace"

GOOGLE_FONTS_IMPORT = (
    "https://fonts.googleapis.com/css2?"
    "family=Poppins:wght@400;500;600;700;800;900&"
    "family=Chakra+Petch:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&"
    "family=Space+Mono:wght@400;700&display=swap"
)


def render_style_block(css: str):
    """Safely inject a pure <style>...</style> block."""
    collapsed = "\n".join(line for line in css.splitlines() if line.strip())
    st.markdown(collapsed, unsafe_allow_html=True)


def inject_global_css():
    """Fonts + base styling shared by every page."""
    render_style_block(
        f"""
        <style>
        @import url('{GOOGLE_FONTS_IMPORT}');

        :root {{
            --sg-bg: {COLORS['bg']};
            --sg-navy: {COLORS['navy']};
            --sg-navy-dark: {COLORS['navy_dark']};
            --sg-crystal-gray: {COLORS['crystal_gray']};
            --sg-btn-primary: {COLORS['btn_primary']};
            --sg-btn-primary-hover: {COLORS['btn_primary_hover']};
            --sg-btn-secondary-bg: {COLORS['btn_secondary_bg']};
            --sg-btn-secondary-border: {COLORS['btn_secondary_border']};
            --sg-btn-secondary-text: {COLORS['btn_secondary_text']};
            --sg-btn-secondary-text-hover: {COLORS['btn_secondary_text_hover']};
            --sg-charcoal: {COLORS['charcoal']};
            --font-display: {FONT_DISPLAY};
            --font-body: {FONT_BODY};
            --font-mono: {FONT_MONO};
        }}

        html, body, [class*="css"] {{
            font-family: var(--font-body);
        }}

        /* Completely hide horizontal and vertical scrollbars visually */
        ::-webkit-scrollbar {{
            display: none !important;
            width: 0px !important;
            height: 0px !important;
            background: transparent !important;
        }}
        * {{
            -ms-overflow-style: none !important;
            scrollbar-width: none !important;
        }}
        
        /* THE NUCLEAR SCROLL LOCK */
        html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {{
            overflow: hidden !important;
            width: 100vw !important;
            height: 100vh !important;
            max-width: 100vw !important;
            max-height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            overscroll-behavior: none !important;
        }}

        /* 
         * WIDENED APP CONTAINER
         */
        .block-container {{
            padding-top: 0 !important;
            padding-bottom: 2rem;
            max-width: 1400px; 
        }}

        #MainMenu, footer {{
            background: transparent;
        }}

        header[data-testid="stHeader"] {{
            background: transparent;
            z-index: 1 !important;
        }}

        /* ---- Top nav bar ------------------- */
        [class*="st-key-sg_nav_wrap"] {{
            position: relative;
            z-index: 999;
            padding: 1.6rem 2% 1rem 2%;
        }}
        
        [class*="st-key-sg_nav_wrap"] [data-testid="stButton"] button,
        [class*="st-key-sg_nav_wrap"] [data-testid^="stBaseButton"],
        [class*="st-key-sg_nav_wrap"] button {{
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            color: var(--sg-charcoal) !important;
            font-family: var(--font-mono) !important;
            font-weight: 700 !important;
            letter-spacing: 0.8em !important; 
            font-size: clamp(1.4rem, 1.8vw, 1.7rem) !important;
            text-transform: uppercase !important;
            padding: 0.35rem 0.2rem !important;
            border-radius: 0 !important;
            transition: opacity 0.15s ease, transform 0.15s ease;
        }}
        [class*="st-key-sg_nav_wrap"] [data-testid="stButton"] button:hover,
        [class*="st-key-sg_nav_wrap"] [data-testid^="stBaseButton"]:hover,
        [class*="st-key-sg_nav_wrap"] button:hover {{
            opacity: 0.6;
            transform: translateY(-1px);
        }}
        [class*="st-key-sg_nav_wrap"] [data-testid="stButton"] button:focus-visible,
        [class*="st-key-sg_nav_wrap"] [data-testid^="stBaseButton"]:focus-visible,
        [class*="st-key-sg_nav_wrap"] button:focus-visible {{
            outline: 3px solid var(--sg-btn-primary);
            outline-offset: 3px;
        }}

        /* ---- Hero CTA pill buttons ------------------------ */
        [class*="st-key-sg_cta_primary"] [data-testid="stButton"] button,
        [class*="st-key-sg_cta_primary"] [data-testid^="stBaseButton"],
        [class*="st-key-sg_cta_primary"] button {{
            background: var(--sg-btn-primary) !important;
            color: #FFFFFF !important;
            border: 3px solid var(--sg-charcoal) !important;
            border-radius: 999px !important;
            padding: 1.2rem 3rem !important; 
            font-family: var(--font-display) !important;
            font-weight: 700 !important;
            font-size: clamp(1.2rem, 1.5vw, 1.6rem) !important; 
            box-shadow: 6px 6px 0px var(--sg-charcoal) !important;
            transition: background 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
        }}
        [class*="st-key-sg_cta_primary"] [data-testid="stButton"] button:hover,
        [class*="st-key-sg_cta_primary"] [data-testid^="stBaseButton"]:hover,
        [class*="st-key-sg_cta_primary"] button:hover {{
            background: var(--sg-btn-primary-hover) !important;
            transform: translate(-3px, -3px);
            box-shadow: 9px 9px 0px var(--sg-charcoal) !important;
        }}
        [class*="st-key-sg_cta_secondary"] [data-testid="stButton"] button,
        [class*="st-key-sg_cta_secondary"] [data-testid^="stBaseButton"],
        [class*="st-key-sg_cta_secondary"] button {{
            background: var(--sg-btn-secondary-bg) !important;
            color: var(--sg-charcoal) !important;
            border: 3px solid var(--sg-charcoal) !important;
            border-radius: 999px !important;
            padding: 1.2rem 3rem !important; 
            font-family: var(--font-display) !important;
            font-weight: 700 !important;
            font-size: clamp(1.2rem, 1.5vw, 1.6rem) !important; 
            box-shadow: 6px 6px 0px var(--sg-charcoal) !important;
            transition: color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
        }}
        [class*="st-key-sg_cta_secondary"] [data-testid="stButton"] button:hover,
        [class*="st-key-sg_cta_secondary"] [data-testid^="stBaseButton"]:hover,
        [class*="st-key-sg_cta_secondary"] button:hover {{
            color: var(--sg-charcoal) !important;
            transform: translate(-3px, -3px);
            box-shadow: 9px 9px 0px var(--sg-charcoal) !important;
        }}
        
        [class*="st-key-sg_nav_wrap"] [data-testid="stButton"] button:active,
        [class*="st-key-sg_nav_wrap"] [data-testid^="stBaseButton"]:active,
        [class*="st-key-sg_nav_wrap"] button:active {{
            transform: translateY(0);
        }}
        [class*="st-key-sg_cta_primary"] [data-testid="stButton"] button:active,
        [class*="st-key-sg_cta_primary"] [data-testid^="stBaseButton"]:active,
        [class*="st-key-sg_cta_primary"] button:active {{
            transform: translate(0, 0);
            box-shadow: 2px 2px 0px var(--sg-charcoal) !important;
        }}
        [class*="st-key-sg_cta_secondary"] [data-testid="stButton"] button:active,
        [class*="st-key-sg_cta_secondary"] [data-testid^="stBaseButton"]:active,
        [class*="st-key-sg_cta_secondary"] button:active {{
            transform: translate(0, 0);
            box-shadow: 2px 2px 0px var(--sg-charcoal) !important;
        }}

        /* ---- Generic page shell for non-hero pages --------- */
        .sg-page-title {{
            font-family: var(--font-display);
            font-weight: 900;
            color: var(--sg-navy);
            line-height: 1.1;
            font-size: clamp(4.5rem, 9vw + 2rem, 10rem);
            margin: 0.4rem 0 0.4rem 0;
        }}
        .sg-page-subtitle {{
            font-family: var(--font-body);
            color: var(--sg-charcoal);
            opacity: 0.85;
            font-size: clamp(1.2rem, 1.5vw + 0.85rem, 1.6rem); 
            margin-bottom: 2rem;
        }}
        .sg-mono-label {{
            font-family: var(--font-mono);
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: var(--sg-navy);
        }}

        /* SVGs changed to position: fixed so they physically cannot overflow the page */
        .sg-crystal-layer {{
            position: fixed !important; 
            pointer-events: none;
            opacity: 0.38;
            z-index: -1;
        }}
        .sg-crystal-layer svg {{
            width: 100%;
            height: auto !important; 
            display: block;
        }}
        </style>
        """
    )


def render_top_nav(pages, active=None):
    with st.container(key="sg_nav_wrap"):
        cols = st.columns(len(pages))
        for col, (label, target) in zip(cols, pages.items()):
            with col:
                if st.button(label.upper(), key=f"nav_{label}", use_container_width=True):
                    st.switch_page(target)


_CRYSTAL_FILES = ["crystal_1.svg", "crystal_2.svg", "crystal_3.svg", "crystal_4.svg"]


_CRYSTAL_LAYOUT = {
    1: {"svg_index": 0, "top": "-5vh", "left": "-2vw", "width": "65vw", "height": "auto",
        "z": -2, "anim": "sgFloatA 20s ease-in-out infinite", "origin": "center"},
    2: {"svg_index": 1, "top": "-8vh", "left": "-18vw", "width": "45vw", "height": "auto",
        "z": -1, "anim": "sgFloatB 18s ease-in-out infinite", "origin": "center"},
    3: {"svg_index": 2, "bottom": "-65vh", "left": "-5vw", "width": "85vw", "height": "auto",
        "z": -1, "anim": "sgFloatC 21s ease-in-out infinite", "origin": "center"},
    4: {"svg_index": 3, "top": "-22vh", "right": "-22vw", "width": "45vw", "height": "auto",
        "z": -1, "anim": "sgFloatD 19s ease-in-out infinite", "origin": "center"},
    5: {"svg_index": 0, "bottom": "-50vh", "right": "-45vw", "width": "75vw", "height": "auto",
        "z": -1, "anim": "sgFloatE 24s ease-in-out infinite", "origin": "center"},
    6: {"svg_index": 3, "bottom": "-20vh", "left": "-20vw", "width": "45vw", "height": "auto",
        "z": -1, "anim": "sgFloatF 22s ease-in-out infinite", "origin": "center"},
}


@st.cache_data(show_spinner=False)
def _load_crystal_svgs():
    svgs = []
    for fname in _CRYSTAL_FILES:
        path = os.path.join(ASSETS_DIR, fname)
        try:
            with open(path, "r", encoding="utf-8") as f:
                svgs.append(f.read())
        except FileNotFoundError:
            svgs.append(None)
    return svgs


def render_crystal_background():
    svgs = _load_crystal_svgs()
    if not any(svgs):
        return
        
    html_parts = []
    for i, cfg in _CRYSTAL_LAYOUT.items():
        svg_index = cfg.get("svg_index", (i - 1) % len(svgs))
        svg = svgs[svg_index]
        
        if svg is None:
            continue
            
        offsets = "".join(
            f"{prop}:{cfg[prop]};" for prop in ("top", "right", "bottom", "left") if prop in cfg
        )
        style = (
            "position:fixed; pointer-events:none; opacity:0.38; "
            f"z-index:{cfg['z']}; width:{cfg['width']}; height:{cfg['height']}; "
            f"{offsets} animation:{cfg['anim']}; transform-origin:{cfg['origin']};"
        )
        html_parts.append(
            f'<div class="sg-crystal-layer sg-crystal-{i}" style="{style}">'
            f'<div style="width:100%; height:auto !important; display:block;">{svg}</div></div>'
        )

    keyframes = """
    <style>
    @keyframes sgFloatA { 0% { transform: rotate(55deg) translate(0px, 0px); } 50% { transform: rotate(55deg) translate(8px, -12px); } 100% { transform: rotate(55deg) translate(0px, 0px); } }
    @keyframes sgFloatB { 0% { transform: rotate(25deg) translate(0px, 0px); } 50% { transform: rotate(25deg) translate(-6px, 8px); } 100% { transform: rotate(25deg) translate(0px, 0px); } }
    @keyframes sgFloatC { 0% { transform: rotate(70deg) translate(0px, 0px); } 50% { transform: rotate(70deg) translate(-10px, 10px); } 100% { transform: rotate(70deg) translate(0px, 0px); } }
    @keyframes sgFloatD { 0% { transform: rotate(-45deg) translate(0px, 0px); } 50% { transform: rotate(-45deg) translate(8px, 12px); } 100% { transform: rotate(-45deg) translate(0px, 0px); } }
    @keyframes sgFloatE { 0% { transform: rotate(-25deg) translate(0px, 0px); } 50% { transform: rotate(-25deg) translate(-7px, -9px); } 100% { transform: rotate(-25deg) translate(0px, 0px); } }
    @keyframes sgFloatF { 0% { transform: rotate(-10deg) translate(0px, 0px); } 50% { transform: rotate(-10deg) translate(8px, -5px); } 100% { transform: rotate(-10deg) translate(0px, 0px); } }
    @media (prefers-reduced-motion: reduce) {
        .sg-crystal-layer { animation: none !important; }
    }
    </style>
    """
    render_style_block(keyframes + "".join(html_parts))


def render_protein_showcase(pdb_id="6XYO", height=200):
    dot_colors = ["#E63946", "#2A6FB0", "#3FA34D", "#F2A93B", "#7C5CBF", "#3FA34D", "#E63946", "#2A6FB0"]
    points = [(20, 70), (55, 40), (90, 65), (125, 35), (160, 60), (195, 30), (225, 55), (255, 40)]
    branch_offsets = [(-14, 26), (16, -24), (-16, 26), (14, -26), (-14, 26), (16, -24), (-14, 24), (14, -22)]

    circles = []
    lines = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#B9B9B9" stroke-width="3"/>')
    for i, (x, y) in enumerate(points):
        bx, by = branch_offsets[i]
        lines.append(f'<line x1="{x}" y1="{y}" x2="{x+bx}" y2="{y+by}" stroke="#B9B9B9" stroke-width="3"/>')
        circles.append(f'<circle cx="{x+bx}" cy="{y+by}" r="7" fill="{dot_colors[(i+3) % len(dot_colors)]}"/>')
        circles.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{dot_colors[i % len(dot_colors)]}"/>')

    svg = f"""
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; height:{height}px;">
      <svg viewBox="0 0 275 100" style="width:100%; max-width:340px; height:auto; overflow:visible;">
        <ellipse cx="140" cy="95" rx="95" ry="9" fill="#000000" opacity="0.06"/>
        {''.join(lines)}
        {''.join(circles)}
      </svg>
      <div class="sg-mono-label" style="margin-top: 40px; font-size: clamp(1.4rem, 2vw, 1.8rem); font-weight:400; letter-spacing: 0.4em;">
        {pdb_id}
      </div>
    </div>
    """
    render_style_block(svg)


def render_chevrons(direction="left", key=None, on_click=None, container_height=420, arrow_top=160):
    flip_transform = "scaleX(-1)" if direction == "right" else "none"

    polyline_svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 40">'
        '<polyline points="20,2 4,20 20,38" fill="none" '
        'stroke="%23ADADAD" stroke-width="2.4" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>'
    )

    if key is None or on_click is None:
        svg = f"""
        <div style="display:flex; align-items:center; justify-content:center; min-height: {container_height}px; width: 100%; transform:{flip_transform};">
          <svg viewBox="0 0 24 40" style="width: 20px; height: auto;">
            <polyline points="20,2 4,20 20,38" 
                      fill="none" 
                      stroke="var(--sg-crystal-gray)" 
                      stroke-width="2" 
                      stroke-linecap="round" 
                      stroke-linejoin="round"/>
          </svg>
        </div>
        """
        render_style_block(svg)
        return False

    wrap_key = f"{key}_wrap"
    render_style_block(
        f"""
        <style>
        [class*="st-key-{wrap_key}"] {{
            position: relative;
            min-height: {container_height}px !important;
            width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
            display: block !important;
        }}
        [class*="st-key-{wrap_key}"] [data-testid="stElementContainer"] {{
            position: absolute !important;
            top: {arrow_top}px !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            width: 64px !important;
            height: 120px !important;
            padding: 0 !important;
            margin: 0 !important;
        }}
        [class*="st-key-{wrap_key}"] [data-testid="stButton"] {{
            width: 100% !important;
            height: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }}
        [class*="st-key-{wrap_key}"] [data-testid="stButton"] button,
        [class*="st-key-{wrap_key}"] [data-testid^="stBaseButton"] {{
            background-color: transparent !important;
            background-image: url('data:image/svg+xml;utf8,{polyline_svg}') !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            background-size: 36px 60px !important; 
            border: none !important;
            box-shadow: none !important;
            width: 100% !important;
            height: 100% !important;
            min-width: 64px !important;
            min-height: 64px !important;
            padding: 0 !important;
            margin: 0 !important;
            transform: {flip_transform} !important;
            transition: opacity 0.15s ease;
        }}
        [class*="st-key-{wrap_key}"] [data-testid="stButton"] button p,
        [class*="st-key-{wrap_key}"] [data-testid^="stBaseButton"] p {{
            display: none;
        }}
        [class*="st-key-{wrap_key}"] [data-testid="stButton"] button:hover,
        [class*="st-key-{wrap_key}"] [data-testid^="stBaseButton"]:hover {{
            opacity: 0.55;
        }}
        [class*="st-key-{wrap_key}"] [data-testid="stButton"] button:focus:not(:focus-visible) {{
            box-shadow: none !important;
        }}
        </style>
        """
    )

    with st.container(key=wrap_key):
        clicked = st.button(
            direction,
            key=key,
        )

    if clicked:
        on_click()

    return clicked


CAROUSEL_STRUCTURES = [
    {"id": "6CU7", "label": "Rod Polymorph", "color": "#E63946"},
    {"id": "6CU8", "label": "Twister Polymorph", "color": "#1D3557"},
    {"id": "6XYO", "label": "MSA Type I", "color": "#2A9D8F"},
    {"id": "8A9L", "label": "Lewy Fold (PD / DLB)", "color": "#F4A261"},
    {"id": "6PES", "label": "H50Q Wide Fibril", "color": "#6A4C93"},
    {"id": "6UFR", "label": "E46K Fibril", "color": "#457B9D"},
    {"id": "7E0F", "label": "G51D Fibril", "color": "#B08968"},
]

CAROUSEL_AUTO_MS = 7000  


def render_protein_carousel(height=420, start_index=0, auto_ms=CAROUSEL_AUTO_MS):
    n = len(CAROUSEL_STRUCTURES)
    start_index = start_index % n
    structures_json = _structures_to_js_array(CAROUSEL_STRUCTURES)
    label_images_json = _label_images_to_js_object()

    html = f"""
    <html>
    <head>
    <meta charset="utf-8">
    <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&display=swap');

      html, body {{
        margin: 0; padding: 0; width: 100%; height: 100%;
        background: #FFFFFF; overflow: hidden;
        font-family: 'Poppins', -apple-system, sans-serif;
      }}
      #sg-car-root {{
        width: 100%; height: 100%;
        background: #FFFFFF;
        display: flex; flex-direction: column;
        align-items: center; justify-content: flex-start;
        box-sizing: border-box;
      }}
      #sg-car-viewer {{
        width: 320px; height: 320px; flex: 0 0 320px;
        position: relative;
        background: #FFFFFF;
        transition: opacity 0.3s ease;
      }}
      #sg-car-viewer.sg-fading {{ opacity: 0; }}
      #sg-car-viewer canvas {{
        background: #FFFFFF !important;
      }}
      
      /* Robust Flexbox Center Crop */
      #sg-car-label {{
        flex: 0 0 auto; 
        padding-top: 0.5rem;
        width: 100%; 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center;
        transition: opacity 0.3s ease;
      }}
      #sg-car-label.sg-fading {{ opacity: 0; }}
      
      #sg-car-code-img-wrapper {{
        width: 100%;
        height: 55px; /* Safely hides the top/bottom vertical white space */
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #FFFFFF;
      }}
      #sg-car-code-img {{
        width: 480px; /* Scales the 1920x1080 canvas down. Flexbox perfectly centers it. */
        height: auto;
        flex-shrink: 0; /* Prevents the image from being squished */
        max-width: none !important;
      }}
      
      #sg-car-name {{
        font-family: 'Chakra Petch', 'Poppins', sans-serif; 
        font-weight: 600;
        font-size: 1.3rem; 
        color: #2E2F2F; opacity: 0.85; 
        margin: 0.5rem 0 0 0;
        letter-spacing: 0.02em; 
        text-align: center;
      }}
      
      #sg-car-dots {{
        display: flex; gap: 8px; justify-content: center;
        margin-top: 0.75rem; padding-bottom: 4px;
      }}
      .sg-car-dot {{
        width: 7px; height: 7px; border-radius: 50%; background: #D3D3CE;
        transition: background 0.2s ease, transform 0.2s ease;
      }}
      .sg-car-dot.sg-active {{ background: #75C6FB; transform: scale(1.35); }}
    </style>
    </head>
    <body>
    <div id="sg-car-root">
      <div id="sg-car-viewer"></div>
      <div id="sg-car-label">
        <div id="sg-car-code-img-wrapper">
          <img id="sg-car-code-img" src="" alt="" />
        </div>
        <p id="sg-car-name">&mdash;</p>
        <div id="sg-car-dots"></div>
      </div>
    </div>
    <script>
    (function () {{
      "use strict";
      const STRUCTURES = {structures_json};
      const LABEL_IMAGES = {label_images_json};
      const AUTO_MS = {auto_ms};
      const FADE_MS = 300;
      let currentIndex = {start_index};
      let viewer = null;
      let timer = null;
      const cache = {{}};

      const viewerEl = document.getElementById("sg-car-viewer");
      const labelEl = document.getElementById("sg-car-label");
      const codeImgEl = document.getElementById("sg-car-code-img");
      const nameEl = document.getElementById("sg-car-name");
      const dotsEl = document.getElementById("sg-car-dots");

      function buildDots() {{
        dotsEl.innerHTML = "";
        STRUCTURES.forEach(function (_, i) {{
          const d = document.createElement("div");
          d.className = "sg-car-dot" + (i === currentIndex ? " sg-active" : "");
          dotsEl.appendChild(d);
        }});
      }}
      function updateDots() {{
        const dots = dotsEl.querySelectorAll(".sg-car-dot");
        dots.forEach(function (d, i) {{ d.classList.toggle("sg-active", i === currentIndex); }});
      }}

      function fetchStructure(pdbId) {{
        if (cache[pdbId]) return Promise.resolve(cache[pdbId]);
        const url = "https://files.rcsb.org/download/" + pdbId.toUpperCase() + ".pdb";
        return fetch(url).then(function (r) {{
          if (!r.ok) throw new Error("fetch failed: " + pdbId);
          return r.text();
        }}).then(function (t) {{ cache[pdbId] = t; return t; }});
      }}

      function setCodeImage(pdbId) {{
        const b64 = LABEL_IMAGES[pdbId.toUpperCase()];
        if (b64) {{
          codeImgEl.src = "data:image/png;base64," + b64;
          codeImgEl.alt = pdbId.toUpperCase();
        }} else {{
          codeImgEl.removeAttribute("src");
          codeImgEl.alt = pdbId.toUpperCase();
        }}
      }}

      function show(index, animate) {{
        const entry = STRUCTURES[index];
        function paint() {{
          fetchStructure(entry.id).then(function (pdbText) {{
            viewer.clear();
            viewer.addModel(pdbText, "pdb");
            viewer.setStyle({{}}, {{ cartoon: {{ color: entry.color }} }});
            viewer.setBackgroundColor("white");
            viewer.zoomTo();
            viewer.spin(true, 1);
            viewer.render();
            setCodeImage(entry.id);
            nameEl.textContent = entry.label;
            updateDots();
          }}).catch(function (err) {{
            console.error(err);
            setCodeImage(entry.id);
            nameEl.textContent = "(failed to load)";
          }}).finally(function () {{
            viewerEl.classList.remove("sg-fading");
            labelEl.classList.remove("sg-fading");
          }});
        }}
        if (animate) {{
          viewerEl.classList.add("sg-fading");
          labelEl.classList.add("sg-fading");
          setTimeout(paint, FADE_MS);
        }} else {{
          paint();
        }}
      }}

      function advance() {{
        currentIndex = (currentIndex + 1) % STRUCTURES.length;
        show(currentIndex, true);
      }}

      function restartTimer() {{
        if (timer) clearInterval(timer);
        timer = setInterval(advance, AUTO_MS);
      }}

      function init() {{
        viewer = $3Dmol.createViewer(viewerEl, {{ backgroundColor: "white" }});
        buildDots();
        show(currentIndex, false);
        restartTimer();
      }}

      window.addEventListener("load", init);
      document.addEventListener("visibilitychange", function () {{
        if (document.hidden) {{ if (timer) clearInterval(timer); }}
        else {{ restartTimer(); }}
      }});
    }})();
    </script>
    </body>
    </html>
    """
    st.components.v1.html(html, height=height, scrolling=False)


def _structures_to_js_array(structures):
    items = []
    for s in structures:
        items.append(
            '{id:"%s",label:"%s",color:"%s"}' % (s["id"], s["label"], s["color"])
        )
    return "[" + ",".join(items) + "]"


def _label_images_to_js_object():
    items = []
    for s in CAROUSEL_STRUCTURES:
        pdb_id = s["id"]
        b64 = ""
        path = os.path.join(ASSETS_DIR, f"{pdb_id}.png")
        try:
            with open(path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
        except Exception:
            pass
        
        if b64:
            items.append('"%s":"%s"' % (pdb_id, b64))
    return "{" + ",".join(items) + "}"
