import pandas as pd
import re

# Get input and output file paths
input_excel = "resources/iso_terms.xlsx"
input_intro = "resources/glossary_intro.txt"
output_rst = "docs/source/glossary.rst"

# Define color mapping for ontology prefixes
ontology_colors = {
    "mesh": "primary",
    "NCIT": "danger",
    "OBI": "success",
    "SIO": "warning",
    "OBCS": "info",
    "default": "secondary"
}

# Function to create safe anchor names
def make_anchor(term):
    return re.sub(r'[^a-z0-9_]', '', term.lower().replace(" ", "_"))

# Load glossary intro text
with open(input_intro) as intro_file:
    intro_text = intro_file.read()

# Load Excel file
df = pd.read_excel(input_excel)

# Create output RST file
with open(output_rst, "w") as f:
    f.write("Glossary of ISO terms\n")
    f.write("=====================\n\n")
    f.write(intro_text + "\n\n")
    f.write("----\n\n")

    # Insert search box
    f.write(".. raw:: html\n\n")
    f.write('   <input type="text" id="glossarySearch" placeholder="Search glossary..." style="width: 100%; padding: 8px; margin-bottom: 16px; font-size: 1em;">\n\n')

    # Process each term in the DataFrame
    for _, row in df.iterrows():
        term = str(row.get("Term", "")).strip()
        if not term or term.lower() == "nan":
            continue

        anchor = make_anchor(term)
        definition = str(row.get("Definition", "")).strip()
        example = str(row.get("Example usage", "")).strip()
        bio_def = str(row.get("Bioinformatics translation", "")).strip()
        bio_example = str(row.get("Bioinformatics example sentence", "")).strip()
        ontology_refs = str(row.get("Ontological reference(s)", "")).strip()
        ontology_links = str(row.get("Link to reference", "")).strip()

        f.write(f".. _{anchor}:\n\n")
        f.write(f".. dropdown:: {term}\n\n")
        f.write(f"   {definition}\n\n")

        if example and example.lower() != "nan":
            f.write(f"   **Example usage:**  \n   *“{example}”*\n\n")

        if bio_def and bio_def.lower() != "nan":
            f.write(f"   .. admonition:: **💻 Bioinformatics translation**\n      :class: tip\n\n")
            f.write(f"      {bio_def}\n\n")
            if bio_example and bio_example.lower() != "nan":
                f.write(f"      **Example usage:**  \n      *“{bio_example}”*\n\n")

        if (
            ontology_refs
            and ontology_links
            and ontology_refs.lower() != "nan"
            and ontology_links.lower() != "nan"
        ):
            ref_items = [r.strip() for r in ontology_refs.split("|")]
            link_items = [l.strip() for l in ontology_links.split("|")]

            if len(ref_items) == len(link_items) and all(ref_items) and all(link_items):
                f.write("   **Ontological references:**\n\n")
                f.write("   .. raw:: html\n\n")
                f.write("      ")
                for ref, link in zip(ref_items, link_items):
                    if "[" in ref and "]" in ref:
                        label = ref.split("[")[0].strip()
                        ont_def = ref.split("[")[1].strip(" ]")
                        prefix = label.split(":")[0].strip()
                        color = ontology_colors.get(prefix, ontology_colors["default"])
                        html = f'<a class="sd-badge sd-bg-{color} sd-text-white" href="{link}" title="{ont_def}">{label}</a>'
                        f.write(f"{html} ")
                f.write("\n\n")

    # Inject JavaScript for live filtering, auto-close, and auto-open on anchor
    f.write(".. raw:: html\n\n")
    f.write("""   <script>
     // Live search filter
     document.getElementById('glossarySearch').addEventListener('input', function () {
       const query = this.value.toLowerCase();
       const dropdowns = document.querySelectorAll('details');
       dropdowns.forEach(drop => {
         const summary = drop.querySelector('summary');
         if (summary && summary.textContent.toLowerCase().includes(query)) {
           drop.style.display = '';
         } else {
           drop.style.display = 'none';
         }
       });
     });

     // Auto-close other dropdowns when one opens
     document.querySelectorAll('details').forEach((el) => {
       el.addEventListener('toggle', function () {
         if (el.open) {
           document.querySelectorAll('details').forEach((other) => {
             if (other !== el) {
               other.removeAttribute('open');
             }
           });
         }
       });
     });

     // Auto-open dropdown if linked via anchor
     window.addEventListener('DOMContentLoaded', () => {
       const hash = window.location.hash;
       if (hash) {
         const anchor = document.querySelector(hash);
         if (anchor && anchor.nextElementSibling && anchor.nextElementSibling.tagName === 'DETAILS') {
           anchor.nextElementSibling.setAttribute('open', '');
           anchor.scrollIntoView({ behavior: 'smooth' });
         }
       }
     });
   </script>\n""")
