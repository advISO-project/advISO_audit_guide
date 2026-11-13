# Configuration file for the Sphinx documentation builder.
import os
import sys
from datetime import date

#
# ============================================================================
# GUIDE SETTINGS — edit these to configure your guide
# ============================================================================

guide_name = 'advISO Audit Guide'
author = 'advISO Team'
copyright = f'{author} & contributors'
release = '0.2'
version = '0.2.0'

under_development = True

guide_subtitle = 'Audit Guide'

sidebar_color = '#C7602E'

github_repo = 'https://github.com/advISO-project/advISO_audit_guide'

html_logo = '_static/images/logo.png'


# ============================================================================
# Everything below here is Sphinx plumbing — you shouldn't need to change it.
# ============================================================================

project = guide_name

exclude_patterns = [
    '_build',
    '_scripts',
    '_includes',
    'intro.md',
    'toc.md',
]

# -- Extensions --------------------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx_design',
    'sphinx_tabs.tabs',
]

# -- MyST (Markdown) configuration ------------------------------------------

myst_enable_extensions = [
    'colon_fence',
    'substitution',
]

today_fmt = "%Y-%m-%d"

myst_substitutions = {
    'guide_name': guide_name,
    'guide_subtitle': guide_subtitle,
    'sidebar_color': sidebar_color,
    'release': release,
    'version': version,
    'github_repo': github_repo,
    'github_issues_link': f'[GitHub repository]({github_repo}/issues)',
    'today_date': date.today().strftime(today_fmt),
}

# -- RST configuration (for .rst content pages) -----------------------------

numfig = True

rst_epilog = f"""

.. |release| replace:: {release}
.. |version| replace:: {version}
"""

# -- Intersphinx -------------------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
templates_path = ['_templates']

html_css_files = [
    'custom.css',
    'extra.css',
]

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'collapse_navigation': False,
    'navigation_depth': 3,
}

# -- EPUB output -------------------------------------------------------------

epub_show_urls = 'footnote'

# -- Build-time asset generation ---------------------------------------------

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '_scripts'))
from generate_logo import generate_logo
from generate_buttons import generate_buttons
from generate_contributors import generate_contributors
generate_logo(guide_subtitle)
generate_buttons(guide_subtitle, sidebar_color)
generate_contributors(github_repo)

_css_path = os.path.join(os.path.dirname(__file__), '_static', 'custom.css')
with open(_css_path, 'w') as _f:
    _f.write(f""".wy-side-nav-search,
.wy-nav-top {{
    background: {sidebar_color};
}}

.guide-button {{
  border-radius: 12px;
  box-shadow: 0 2px 6px rgba(0,0,0,.15);
  transition: transform .15s, box-shadow .15s;
}}
.guide-button:hover {{
  transform: translateY(-3px);
  box-shadow: 0 6px 14px rgba(0,0,0,.25);
}}
""")

_settings_path = os.path.join(os.path.dirname(__file__), '_brand_assets', '_settings.html')
with open(_settings_path, 'w') as _f:
    _f.write(f'<p>Current settings: subtitle <strong>"{guide_subtitle}"</strong>, colour <span style="display:inline-block;width:14px;height:14px;background:{sidebar_color};border-radius:3px;vertical-align:middle;margin-right:4px;border:1px solid #ccc;"></span><strong>{sidebar_color}</strong>.</p>')

# -- Custom config values ----------------------------------------------------

def setup(app):
    app.add_config_value('under_development', False, 'env')
