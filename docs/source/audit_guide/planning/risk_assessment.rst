=================
Risk Assessment
=================

ISO 15189:2022 places risk management at the core of the quality management system. Evaluating risks across the entire pipeline is essential before designing and conducting an audit.

Risk assessment acts as a triaging tool. It helps prioritize high-impact failure points first rather than attempting to audit every process with equal depth. Vertical audits are particularly useful for demonstrating end-to-end traceability, identifying bottlenecks, and uncovering hidden risks in the process, which auditors and accreditation bodies will want to see evidenced.

.. note::
   **ISO 15189:2022 Clause Mapping**

   * **Clause 5.6 (Risk Management):** Requires laboratory management to establish, maintain, and evaluate processes to identify and manage risks to patient care.
   * **Clause 7.1 (General Requirements):** Mandates risk assessment across pre-examination, examination, and post-examination stages, including digital and computational workflows.
   * **Clause 8.5 (Actions to Address Risks and Opportunities):** Requires integrating risk mitigations into the quality system and evaluating their ongoing effectiveness.

---

Selecting a Risk Assessment Framework
--------------------------------------

There is no single "correct" way to structure a risk matrix. Accreditation assessors look for evidence that your laboratory systematically identifies, evaluates, and mitigates risk—not that you adhere to a specific grid design. 

Laboratories should adopt or adapt a risk assessment tool that aligns with their local clinical governance, institutional policy, or relevant risk standards (such as ISO 14971 for medical devices/software). 

The matrix below is provided purely as an **illustrative example** to demonstrate how severity and likelihood can be combined to guide audit planning.

Example Risk Categorization Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. grid:: 1 2 3
   :gutter: 3

   .. grid-item-card:: 🟢 Low Risk
      :class-card: sd-bg-light sd-border-success

      **Characteristics:** Minor operational impact (e.g., logging typos, minor internal documentation delays) with low likelihood.

      **Audit Action:** Spot-check during routine cycles or address via periodic self-declaration.

   .. grid-item-card:: 🟡 Medium Risk
      :class-card: sd-bg-light sd-border-warning

      **Characteristics:** Moderate impact (e.g., re-analysis required, turnaround time delays) or minor issues with high likelihood.

      **Audit Action:** Schedule for routine periodic audit (e.g., annually or bi-annually).

   .. grid-item-card:: 🔴 High Risk
      :class-card: sd-bg-light sd-border-danger

      **Characteristics:** Critical impact on diagnostic accuracy or patient care (e.g., false variant call, sample mix-up) or frequent failure modes.

      **Audit Action:** Prioritize for immediate vertical audit and close monitoring.

---

Example Matrix Structure
^^^^^^^^^^^^^^^^^^^^^^^^

If your institution uses a traditional two-dimensional matrix, your evaluation might look similar to this model:

+--------------------+------------------------+------------------------+------------------------+
| Impact Severity    | Low Likelihood         | Medium Likelihood      | High Likelihood        |
+====================+========================+========================+========================+
| **Critical**       | **Medium Risk**        | **High Risk**          | **High Risk**          |
| *(Patient harm)*   |                        |                        |                        |
+--------------------+------------------------+------------------------+------------------------+
| **Moderate**       | **Low Risk**           | **Medium Risk**        | **High Risk**          |
| *(Delay / re-run)* |                        |                        |                        |
+--------------------+------------------------+------------------------+------------------------+
| **Minor**          | **Low Risk**           | **Low Risk**           | **Medium Risk**        |
| *(Minor log error)*|                        |                        |                        |
+--------------------+------------------------+------------------------+------------------------+

---

Risk Assessing the Case Studies
-------------------------------

Below are examples of how risk assessment principles can be applied to each procedure listed in :doc:`Case Studies </audit_guide/case_studies>`. These examples illustrate the thought process assessors expect to see evidenced.

.. dropdown:: 🧪 Laboratory Procedure

   **Process Scope:** Preparation of Illumina sequencing libraries from DNA.

   * **Identified Risks:**
     
     * Sample swaps or index misalignment during manual plate setup.
     * Reagent degradation or pipette calibration errors leading to low library yield.
     * Cross-contamination between high-concentration and low-concentration samples.

   * **Example Evaluation:**
     
     * *Impact:* High (Sample swaps lead to incorrect patient results).
     * *Likelihood:* Medium (Depends on level of manual handling vs. liquid handling automation).
     * *Overall Risk Level:* **High Risk**

.. dropdown:: 🧬 Bioinformatics QC Procedure

   **Process Scope:** Assessing the quality of Illumina sequencing reads (FASTQ files) prior to downstream analysis.

   * **Identified Risks:**
     
     * Undetected adapter contamination or phred score degradation passing filtering.
     * Incorrect quality score encoding (Phred+33 vs Phred+64) in custom scripts.
     * Corrupted FASTQ files during transfer from sequencer to storage server.

   * **Example Evaluation:**
     
     * *Impact:* Moderate (Low-quality reads can lead to failed variant calling or re-analysis delays).
     * *Likelihood:* Medium (Data transfer steps and multi-vendor instruments introduce variations).
     * *Overall Risk Level:* **Medium Risk**

.. dropdown:: 🧬 Bioinformatics Analysis Procedure

   **Process Scope:** Analyzing Illumina sequencing reads to identify variants and generate reports for clinical interpretation.

   * **Identified Risks:**
     
     * Reference genome version mismatches between analysis pipeline steps.
     * Unvalidated parameter changes in variant calling algorithms.
     * Stale database versions for pathogen strain or resistance marker identification.

   * **Example Evaluation:**
     
     * *Impact:* Critical (Directly impacts diagnostic accuracy and patient treatment decisions).
     * *Likelihood:* Medium (Complex command-line parameters or frequent database updates).
     * *Overall Risk Level:* **High Risk**

.. dropdown:: 🌌 Galaxy Training Procedure

   **Process Scope:** Workflow development, execution, and user management within a Galaxy environment.

   * **Identified Risks:**
     
     * Analysts modifying tool parameters inside active histories without updating the master workflow.
     * Automatic tool updates altering underlying execution parameters.
     * Shared user credentials or improper permission settings on shared histories.

   * **Example Evaluation:**
     
     * *Impact:* Moderate (Loss of reproducibility across diagnostic runs).
     * *Likelihood:* Medium (Multiple users accessing the same instance).
     * *Overall Risk Level:* **Medium Risk**

.. dropdown:: 💻 Code Update & Review Procedure

   **Process Scope:** Updating bioinformatics pipelines, scripts, and conducting code review.

   * **Identified Risks:**
     
     * Direct edits made to production scripts without version control (Git).
     * Lack of peer code review prior to deploying software updates.
     * Unpinned software dependencies pulling updated packages automatically.

   * **Example Evaluation:**
     
     * *Impact:* High (Unintended side effects can break downstream analysis across all samples).
     * *Likelihood:* High (If formal change-control procedures are not strictly enforced).
     * *Overall Risk Level:* **High Risk**

.. dropdown:: 🔧 Systems, Hardware, and Databases

   **Process Scope:** Logging, updating, and maintaining bioinformatics equipment, systems, hardware, and databases.

   * **Identified Risks:**
     
     * Storage capacity limits reached during an active sequencing run.
     * Lack of routine off-site or secondary backups for raw sequencing data.
     * Unmonitored hardware failure or system outages.

   * **Example Evaluation:**
     
     * *Impact:* High (Permanent loss of primary diagnostic data or extended service downtime).
     * *Likelihood:* Low (If monitoring and infrastructure checks are established).
     * *Overall Risk Level:* **Medium Risk**

---

Exercise: Risk Assess Your Own Workflows
----------------------------------------

When evaluating internal procedures using your facility's chosen risk framework:

1. **Define the Procedure:** Name the process and clearly establish its boundaries (inputs and outputs).
2. **List Potential Failure Points:** Identify failure modes across hardware, software, user actions, and data transfer.
3. **Assign Risk Ratings:** Apply your institution’s severity and likelihood criteria.
4. **Determine Audit Priority:** Focus vertical audits on high-risk steps where failure directly impacts patient care or diagnostic integrity.