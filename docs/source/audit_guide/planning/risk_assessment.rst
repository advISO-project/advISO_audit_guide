===============
Risk Assessment
===============

The Focus on Risk
-------------------
The ISO 15189:2022 standard places risk management at the core of the quality management system. For laboratories bridging wet-lab and bioinformatics workflows, evaluating risks across the entire pipeline is essential before designing and conducting an audit.

Risk assessment acts as a triaging tool: it helps you audit high-impact failure points first rather than trying to cover everything at once.

.. note::
   **ISO 15189:2022 Clause Mapping**

   This section addresses the core risk-based thinking requirements outlined in:

   * **Clause 5.6 (Risk Management):** Mandates that laboratory management establish and maintain processes to identify risks to patient care and operational integrity.
   * **Clause 7.1 (General Process Requirements):** Requires risk assessment and mitigation across pre-examination, examination, and post-examination workflows (including bioinformatics pipelines).
   * **Clause 8.5 (Actions to Address Risks and Opportunities):** Requires integrated planning to integrate risk actions into the quality management system and evaluate their effectiveness.

Domain Risks: Wet Lab vs. Bioinformatics
-----------------------------------------
.. dropdown:: Wet-Lab Failure Modes

   * **Sample Swaps / Cross-Contamination:** Barcode index misalignment or physical contamination during library prep.
   * **Reagent / Assay Degradation:** Using expired flow cells, degraded enzymes, or uncalibrated pipettes causing run failures or dropouts.
   * **Inconsistent Input Data:** Variable DNA concentration/purity entering sequencing, impacting coverage uniformity.

.. dropdown:: Bioinformatics Failure Modes

   * **Uncontrolled Pipeline Code Changes:** A analyst making a "quick fix" directly on the production server without version control (e.g. git).
   * **Reference Database Stale Data:** Using outdated pathogen reference genomes, leading to missed variant or lineage assignments.
   * **Data Loss & Storage Issues:** Storage filling up mid-run or lack of backed-up FastQ/VCF files.

Risk Profiles by Architecture (What are you auditing?)
-------------------------------------------------------

The risk profile and necessary audit evidence depend heavily on the software platform being used:

* **In-House / Command-Line Pipelines (e.g., Nextflow, Snakemake, Bash):**
    * *Primary Risks:* Hardcoded paths, unpinned dependency versions, missing automated test suites, poor documentation.
    * *Audit Focus:* Git commit history, containerization (Docker/Singularity), workflow execution logs.

* **Galaxy Workflows (Local or Cloud):**
    * *Primary Risks:* Unlocked history workflows, tool version changes upon system updates, user permission management.
    * *Audit Focus:* Exported workflow JSON/GA files, tool version locking within Galaxy histories, user role access logs.

* **External / Commercial Platforms (SaaS / Black-Box Software):**
    * *Primary Risks:* Lack of transparency into algorithm changes, cloud vendor lock-in, local data residency compliance.
    * *Audit Focus:* Vendor verification/validation reports, SLA agreements, release notes review process.

* **Databases, Systems, & LIMS Integrations:**
    * *Primary Risks:* Manual data re-entry errors between sample accessioning and bioinformatics metadata files.
    * *Audit Focus:* API logs, automated barcode-to-sample linkage, data validation checks at ingestion.


Risk Prioritization Matrix
---------------------------

To decide how frequently or rigorously to audit a process, map identified risks using the matrix below:

+----------------+------------------------+------------------------+------------------------+
| Impact         | Low Likelihood         | Medium Likelihood      | High Likelihood        |
+================+========================+========================+========================+
| **Critical**   | **Medium Risk**        | **High Risk**          | **High Risk**          |
| (Patient harm) | (*Annual Audit*)       | (*Prioritize Audit*)   | (*Immediate Action*)   |
+----------------+------------------------+------------------------+------------------------+
| **Moderate**   | **Low Risk**           | **Medium Risk**        | **High Risk**          |
| (TAT delays)   | (*Spot Check*)         | (*Annual Audit*)       | (*Prioritize Audit*)   |
+----------------+------------------------+------------------------+------------------------+
| **Minor**      | **Low Risk**           | **Low Risk**           | **Medium Risk**        |
| (Minor typo)   | (*Self-Declare*)       | (*Spot Check*)         | (*Annual Audit*)       |
+----------------+------------------------+------------------------+------------------------+
Performing a risk assessment
-------------------

.. dropdown:: Top tips!
   :open:
   When thinking about risk assessment for bioinformatics processes, consider the following questions to help identify and prioritize risks:

   * What are the risks to patient safety?
   * What are the risks to turnaround times (TATs?)
   * What are the risks to data integrity?
   * What are the risks to data security?
