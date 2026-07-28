==============
Audit Schedule
==============

An audit schedule converts risk assessment findings into a structured operational plan. ISO 15189:2022 requires internal audits to be planned based on process risk, clinical significance, and findings from previous audits.

High-risk processes must be audited more frequently than established, low-risk processes.

.. note::
   **ISO 15189:2022 Clause Mapping**

   * **Clause 8.5.2 (Actions to Address Risks):** Requires that actions taken to manage risks are proportional to the potential impact on patient care.
   * **Clause 8.8 (Internal Audits):** Mandates an audit programme where frequency and depth are determined by process importance, risk assessment outcomes, and historical audit performance.

---

Example Audit Cadence Mapping
-----------------------------

The table below illustrates how a laboratory might translate risk ratings into scheduled audit frequencies and event-driven triggers. Adjust these timeframes to reflect your laboratory's operational realities and institutional policies.

.. grid:: 1 1 3
   :gutter: 3

   .. grid-item-card:: 🟢 Low Risk
      :class-card: sd-bg-light sd-border-success

      **Baseline Cadence:** Annual

      **Triggers for Ad-Hoc Audit:** Major hardware migrations, operating system upgrades, or significant infrastructure shifts.

   .. grid-item-card:: 🟡 Medium Risk
      :class-card: sd-bg-light sd-border-warning

      **Baseline Cadence:** Bi-annual (Every 6 months)

      **Triggers for Ad-Hoc Audit:** Sub-tool updates, dependency shifts, or alterations to local/cloud storage pipelines.

   .. grid-item-card:: 🔴 High Risk
      :class-card: sd-bg-light sd-border-danger

      **Baseline Cadence:** Quarterly

      **Triggers for Ad-Hoc Audit:** Major code or pipeline version releases, unexplained run errors, or key staffing changes.

---

Scheduling Example across the Case Studies
------------------------------------------

Below are examples showing how a laboratory might translate risk outputs into a scheduled audit plan for the scenarios detailed in :doc:`Case Studies </audit_guide/case_studies>`.

.. dropdown:: 🧪 Laboratory Procedure

   * **Assigned Risk Level:** High Risk
   * **Example Cadence:** Quarterly
   * **Audit Focus:** Sample tracking, index entry verification, and physical contamination controls. 
   * **Scheduling Strategy:** Audit this procedure jointly with raw data demultiplexing to conduct a full vertical audit from physical tube to FASTQ file generation.

.. dropdown:: 🧬 Bioinformatics QC Procedure

   * **Assigned Risk Level:** Medium Risk
   * **Example Cadence:** Bi-annually
   * **Audit Focus:** Quality threshold settings, automated QC report generation, and data integrity checks following file transfer.
   * **Scheduling Strategy:** Review during routine mid-year system checks, or whenever new sequencing chemistry is introduced.

.. dropdown:: 🧬 Bioinformatics Analysis Procedure

   * **Assigned Risk Level:** High Risk
   * **Example Cadence:** Quarterly
   * **Audit Focus:** Variant caller parameter settings, reference genome integrity, database version control, and clinical report output consistency.
   * **Scheduling Strategy:** Require a targeted pre-release audit prior to deploying any new variant calling pipeline version into clinical production.

.. dropdown:: 🌌 Galaxy Training Procedure

   * **Assigned Risk Level:** Medium Risk
   * **Example Cadence:** Bi-annually
   * **Audit Focus:** Locked workflow configurations, user access permissions, history tracking, and staff training records.
   * **Scheduling Strategy:** Schedule regular bi-annual checks, with additional spot checks following major Galaxy system upgrades.

.. dropdown:: 💻 Code Update & Review Procedure

   * **Assigned Risk Level:** High Risk
   * **Example Cadence:** Quarterly
   * **Audit Focus:** Git commit logs, peer review sign-offs, container build definitions, and pipeline testing documentation.
   * **Scheduling Strategy:** Conduct quarterly reviews of code repositories alongside event-driven audits for all major software releases.

.. dropdown:: 🔧 Systems, Hardware, and Databases

   * **Assigned Risk Level:** Medium Risk
   * **Example Cadence:** Annually
   * **Audit Focus:** Disk space monitoring alerts, routine backup restoration tests, hardware maintenance logs, and database update records.
   * **Scheduling Strategy:** Schedule an annual infrastructure audit, with immediate ad-hoc audits triggered following hardware replacements or server migrations.

---

Non-Conformance Resolution Timelines
------------------------------------

When an audit identifies non-conformances, establish clear close-out timelines proportional to risk. The target timelines below represent common practice:

* **High Risk / Critical Non-Conformances:** Root cause analysis and corrective action should be implemented rapidly (e.g., within **30 days**). A targeted re-audit should follow (e.g., within **90 days**) to verify that the fix remains effective under routine conditions.
* **Medium or Low Risk Non-Conformances:** Corrective actions should be implemented within an agreed operational window (e.g., **60 to 90 days**), with verification occurring during the next scheduled routine audit.