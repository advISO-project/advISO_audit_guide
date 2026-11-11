# advISO Audit Guide

A practical guide to designing, implementing, and maintaining internal audits for bioinformatics processes under ISO 15189 accreditation. Built with the [advISO Guide Template](https://github.com/advISO-project/advISO_guide_template).

**Read the guide:** [adviso-audit-guide.readthedocs.io](https://adviso-audit-guide.readthedocs.io/en/latest/)

## Guide settings

The guide is configured via settings at the top of [`docs/conf.py`](docs/conf.py):

| Setting | Value |
|---|---|
| `guide_name` | `'advISO Audit Guide'` |
| `guide_subtitle` | `'Audit Guide'` |
| `sidebar_color` | `'#D97C5D'` |

## Project structure

```
docs/
├── conf.py                  # Guide settings and Sphinx configuration
├── index.md                 # Index page
├── intro.md                 # Introduction (edit this)
├── toc.md                   # Table of contents
├── requirements.txt         # Python dependencies for Read the Docs
│
├── pages/                   # Content pages
│   ├── audit_introduction.rst
│   ├── case_studies.rst
│   ├── checklist.rst
│   ├── choosing_audit_type.rst
│   ├── findings.rst
│   ├── performing_audits.rst
│   ├── review.rst
│   ├── sample_journey.rst
│   └── schedule.rst
│
├── _includes/               # Shared fragments
│   ├── guide_series.md
│   └── project_partners.md
│
├── _brand_assets/           # Brand assets page (hidden, accessible via direct URL)
│   └── brand_assets.md
│
├── _scripts/                # Build-time asset generation
│   ├── generate_logo.py
│   └── generate_buttons.py
│
├── _static/
│   ├── base/                # Template base images (do not modify)
│   │   ├── button_base.png
│   │   ├── logo_base.png
│   │   └── logo_base_16x9.png
│   ├── brand/               # Generated brand assets (gitignored)
│   │   ├── button_horizontal.png
│   │   └── button_website.png
│   ├── images/              # Content images
│   │   ├── logo.png         # Generated sidebar logo (gitignored)
│   │   ├── guide_series_button_horizontal.png
│   │   ├── partner_logos.png
│   │   └── *.svg
│   ├── custom.css           # Generated sidebar CSS (gitignored)
│   └── extra.css            # Audit-guide-specific styles (flip cards, etc.)
```

## Building locally

```bash
cd docs
pip install -r requirements.txt
make html
```

The built site will be in `docs/_build/html/`. Open `index.html` to preview.

## License

This project is licensed under CC BY-NC-SA 4.0. See [LICENSE.md](LICENSE.md) for details.
