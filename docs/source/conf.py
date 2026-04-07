# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'advISO'
copyright = 'advISO 2026'
author = 'Amy Gaskin, advISO Team'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_design',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Custom substitutions --------------------------------
rst_epilog = f"""
.. |release| replace:: {release}
.. |version| replace:: {version}
"""

# Use dynamic date for |today|
today_fmt = "%Y-%m-%d"

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Path for static files (e.g., CSS, JavaScript)
html_static_path = ['_static']

# Load custom CSS
html_css_files = [ 
    'custom.css',
]

# Path to the advISO logo
html_logo = '_static/advISO_logo.png'

html_theme_options = {
    'logo_only': True,  
    'display_version': False,  
}
# -- Options for EPUB output
epub_show_urls = 'footnote'
