==============
Audit Schedule
==============

Mapping your sample journey surfaces where **risk** sits in your
bioinformatics processes. This page turns that **mapping exercise** into a
practical and documented **action plan**: which bioinformatics processes are
prioritised for audit, and how often they are audited.

Under ISO 15189:2022, internal audits are planned according to the **level
of risk** associated with a process, together with any **previous findings**,
compliments and complaints, and any **major changes** to processes that have
perhaps warranted a recent validation.

In a typical audit cycle (e.g. a financial year), this schedule is **not
fixed**. It being **flexible** means it can be **responsive** to risks
changing as bioinformatics processes themselves change.

If your laboratory **already has an audit schedule** for wet laboratory
processes, you may choose to integrate audits for bioinformatics into this.
However, where a risk you identified is specific to a
bioinformatics process, it may call for its own audit frequency, as it can
be more responsive to how a bioinformatics process evolves, with respect to
the overall end-to-end process that includes both wet laboratory and
bioinformatics processes.

The frequency bands below are one example of mapping risk level to audit
frequency, which can be **adjusted to fit** a specific bioinformatics
laboratory's needs and capacity.

.. grid:: 1 1 3 3
   :gutter: 2

   .. grid-item-card:: Low Risk 🟢
      :class-header: sd-bg-success sd-text-white sd-font-weight-bold

      **Audit Frequency:** Annual

   .. grid-item-card:: Medium Risk 🟡
      :class-header: sd-bg-warning sd-text-dark sd-font-weight-bold

      **Audit Frequency:** Every 6 months

   .. grid-item-card:: High Risk 🔴
      :class-header: sd-bg-danger sd-text-white sd-font-weight-bold

      **Audit Frequency:** Every 3 months


The Pathogen X Sample Journey
-------------------------------
Continuing the Pathogen X example from the sample journey page, here are
two worked examples showing how the risks identified there can translate
into a scheduled frequency.

**The Pathogen X analysis pipeline**

*Process:* The bioinformatics analysis pipeline used for Pathogen X,
from quality control through to the report sent to the requesting
clinician.

*Risk level:* High 🔴

*Reasoning:* This pipeline's output directly informs a clinical report
used in patient care. Mapping the sample journey for this pipeline
surfaced two risks: the pipeline depends on a reference database that
could update independently of the pipeline's own code, and it is not
currently possible to establish which code version produced a specific
result after the fact.

*Resulting frequency:* Every 3 months, so that a reference database update
or an unreviewed code change is unlikely to go more than one audit cycle
without being caught.

Vertical audit.

**The code update and review procedure**

*Process:* The procedure governing how code changes are reviewed before
deployment, including changes to the Pathogen X pipeline.

*Risk level:* Medium 🟡

*Reasoning:* This procedure is not specific to the Pathogen X pipeline,
but a gap in it is what makes the code-versioning risk above possible in
the first place. Mapping identified that code changes are not currently
required to go through a documented review step before deployment.

*Resulting frequency:* Every 6 months, reflecting its reach across
pipelines, with a review triggered early if an audit of the Pathogen X
pipeline uncovers a code-related issue tracing back to this procedure.

Horizontal audit. 


Multiple pipelines may share the same code update and review procedure, so auditing it less frequently than the Pathogen X pipeline itself is appropriate. If a code-related issue is uncovered in the Pathogen X pipeline audit, it may trigger an early review of the code update and review procedure 





Applying this to your own processes
--------------------------------------

The two worked examples above show the reasoning for one process-specific
risk and one that cuts across pipelines. The dropdowns below extend that
reasoning to other areas you may have mapped on the sample journey page.
Not all six will necessarily apply, and some may turn out to be low risk.

.. dropdown:: 🧪 Laboratory Procedure

   *Since the last audit of this procedure, has anything changed that would justify a different frequency — new instrumentation, a revised SOP, a change in sample volume?*

.. dropdown:: 🧬 Bioinformatics QC Procedure

   *How often does a QC threshold or parameter actually change? Does your current frequency match how often that happens?*

.. dropdown:: 🧬 Bioinformatics Analysis Pipeline

   *If this pipeline is updated more often than it is audited, what risk does that gap leave uncovered?*

.. dropdown:: 🌌 Galaxy Workflows

   *If a workflow or tool version changes, does that trigger a review on its own, or only at the next scheduled audit?*

.. dropdown:: 💻 Code Update & Review Procedure

   *Does this procedure's audit frequency reflect how often code actually changes, or how often the laboratory happens to audit?*

.. dropdown:: 🔧 Systems, Hardware, and Databases

   *Which of these changes quietly enough that a scheduled audit might be the only way you would find out?*


Once you have a frequency for each process, the next step is to define
what an audit against that schedule actually checks (see
:doc:`Checklist <checklist>`).
