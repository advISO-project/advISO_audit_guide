# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'advISO'
copyright = 'advISO 2026'
author = 'Amy Gaskin, advISO Team'

release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------

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


# -- Custom substitutions ---------------------------------------------------
# Ensure leading newline so it doesn't merge with the end of rst files
rst_epilog = f"""

.. |release| replace:: {release}
.. |version| replace:: {version}
"""

today_fmt = "%Y-%m-%d"

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = [ 
    'custom.css',
]

html_logo = '_static/adviso_logo.png'

html_theme_options = {
    'logo_only': True,  
    'display_version': False,
    'collapse_navigation': False,
    "navigation_depth": 3,
}

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'