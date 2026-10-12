# -*- coding: utf-8 -*-
"""
home_page.py -- SG-ATLAS homepage hero.
"""

import streamlit as st

from nav_config import TOP_NAV_PAGES, tool_page, database_page
from shared_ui import (
    render_top_nav, render_crystal_background, render_protein_showcase,
    render_protein_carousel, render_chevrons, render_style_block,
    CAROUSEL_STRUCTURES,
)

if "sg_carousel_index" not in st.session_state:
    st.session_state["sg_carousel_index"] = 0


def _carousel_prev():
    st.session_state["sg_carousel_index"] = (
        st.session_state["sg_carousel_index"] - 1
    ) % len(CAROUSEL_STRUCTURES)


def _carousel_next():
    st.session_state["sg_carousel_index"] = (
        st.session_state["sg_carousel_index"] + 1
    ) % len(CAROUSEL_STRUCTURES)

# ---------------------------------------------------------------------------
# Hero-specific CSS 
# ---------------------------------------------------------------------------
render_style_block(
    """
    <style>
    [class*="st-key-sg_hero_outer"] {
        position: relative;
        z-index: 0;
        overflow: visible !important;
        min-height: 700px;
        padding-bottom: 2rem;
    }
    [class*="st-key-sg_hero_content"] {
        position: relative;
        z-index: 2;
        padding: 1.1rem 6% 0 6%;
    }
    [class*="st-key-sg_cta_primary"] [data-testid="stButton"] button,
    [class*="st-key-sg_cta_secondary"] [data-testid="stButton"] button {
        width: 100%;
    }
    @media (max-width: 640px) {
        [class*="st-key-sg_hero_outer"] { min-height: 0; }
    }

    [class*="st-key-sg_protein_row"] [data-testid="stHorizontalBlock"] {
        align-items: center !important;
        justify-content: center !important;
    }

    [class*="st-key-sg_left_content"] {
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 420px;
        box-sizing: border-box;
    }
    </style>
    """
)

render_top_nav(TOP_NAV_PAGES, active="Home")

with st.container(key="sg_hero_outer"):
    render_crystal_background()

    with st.container(key="sg_hero_content"):
        left_col, spacer_col, right_col = st.columns([1.3, 0.1, 1.1], vertical_alignment="top")

        with left_col:
            with st.container(key="sg_left_content"):
                
                _title_html = '''
                <div style="font-family: var(--font-display); color: var(--sg-navy); margin: 0rem 0 0rem 0;">
                    <span style="display: block; font-size: clamp(4rem, 5.5vw, 6.5rem); font-weight: 900; line-height: 1.05; -webkit-text-stroke: 2px #FFFFFF; text-shadow: 0px 0px 5px rgba(255,255,255,0.9);">SG</span>
                    <span style="display: block; font-size: clamp(4rem, 5.5vw, 6.5rem); font-weight: 900; line-height: 1.05; -webkit-text-stroke: 2px #FFFFFF; text-shadow: 0px 0px 5px rgba(255,255,255,0.9);">ATLAS</span>
                </div>
                '''
                render_style_block(_title_html)

                _subtitle_html = '''
                <p style="font-family: var(--font-body); font-style: italic; font-weight: 500; color: var(--sg-charcoal); font-size: clamp(1.2rem, 1.6vw, 1.5rem); margin-top: 1.4rem !important; margin-bottom: 1.5rem; white-space: nowrap;">An interpretive tool for Cryo-EM Structures</p>
                '''
                render_style_block(_subtitle_html)

                btn_col1, btn_col2 = st.columns([1, 1.3], gap="small")
                with btn_col1:
                    with st.container(key="sg_cta_primary"):
                        if st.button("Use Tool", key="cta_use_tool", use_container_width=True):
                            st.switch_page(tool_page)
                with btn_col2:
                    with st.container(key="sg_cta_secondary"):
                        if st.button("Discover Database", key="cta_discover_db", use_container_width=True):
                            st.switch_page(database_page)

        with right_col:
            with st.container(key="sg_protein_row"):
                chev_l, mol_col, chev_r = st.columns([0.14, 0.72, 0.14], gap="small")
                with chev_l:
                    render_chevrons("left", key="sg_chevron_left", on_click=_carousel_prev)
                with mol_col:
                    render_protein_carousel(
                        height=420,
                        start_index=st.session_state["sg_carousel_index"],
                    )
                with chev_r:
                    render_chevrons("right", key="sg_chevron_right", on_click=_carousel_next)
