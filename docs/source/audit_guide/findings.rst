Resolving audit findings
========================
Let's say that when you performed the most recent audit for Pathogen X, you discovered that there was no evidence that there is an SOP for detailing how the bioinformatics method worked, despite there being an expectation that one existed. 
This would have been recorded as Non-Compliant. Any non-conformities like this should be corrected without undue delay, following a process like the one outlined below to ensure the correction happens:

[figure with flow diagram of impact assessment - Root-cause analysis - Correction - Effectiveness check - Lessons learned - Closing the audit ]


Impact assessment
------------------
Firstly, think through the impact of this non-conformity to assess its severity. Questions worth asking yourself might include:
*	Did this mean a step in the bioinformatics pipeline was performed incorrectly, or without a documented basis?
*	Could that have had a detrimental impact on a patient?
*	Was the missing information available somewhere else instead?
*	Does this need to be escalated or reported elsewhere?
*	For how long has this non-conformity existed?

.. danger::
    If there is any possibility that a non-conformity identified through an interal audit could have detrimentally impacted patient results, it is strongly advised to escalate it immediately through the reporting pathway that is most appropriate for your organisation. This guide cannot tell you what that pathway is; make sure you are aware of your own policy in advance of needed it. 

Record some details about the non-conformity, including the discovery date, a severity level, and where it took place. Severity might range from a Recommendation (an observation or suggestion for improvement, where nothing has actually failed), through to a scale like Minor, Major, or Critical, depending on how serious the consequence is and how directly it touches patient results.
Then, you might want to think through the impact and origin of the non-conformity. Impact and origin are two different lenses on the same non-conformity, and both are worth thinking through, in whatever language fits your operational context. Impact is about consequence: what could go wrong, or has gone wrong, because of this? It might tough on patient safety, data protection, service continuity, or how effectively your quality management system is working as a whole. Meanwhile, origin is about where in your bioinformatics sample journey did this arise? It might sit with documentation, equipment integrity and maintenance, personnel, data storage and archival, etc. Naming this helps you (and whoever reviews the audit later), spot if the same kind of issue keeps recurring from the same source. 

Immediate action
^^^^^^^^^^^^^^^^^
Before turning to why the non-conformity happened, consider whether any action needs to be taken immediately to limit ongoing harm. This is different from fixing the underlying problem; it is about stopping the immediate risk. For example, this could mean pausing a pipeline that is still processing samples with an out-of-date reference database or flagging affected results to stakeholders, so they are not relied upon while the issue is investigated. 

Not every non-conformity will need this step. In our Pathogen X example, the missing SOP was not actively causing harm at the point of discovery, so no immediate action was required beyond what has already been covered in impact assessment. Where immediate action is needed, record what was done, when, and by whom.

Root-cause analysis
--------------------
Root-cause analysis identifies the reason why the non-conformity occurred, not just what happened. A useful rule of thumb for root-cause analysis to ask “why” about 3-5 times, backtracking until you reach something you can act upon. 
A root-cause analysis has been outlined for the non-conformity we identified for Pathogen X. Click on the cards below to reveal each step of the root-cause analysis.

.. grid:: 1 1 1 1
   :gutter: 2

   .. grid-item-card:: Step 1: SOP Availability
      :class-card: sd-border-primary

      **Why?** Why was there not an SOP outlining the bioinformatics process?
      ^^^
      **Finding:** There was an SOP, but it was accidentally deleted.

   .. grid-item-card:: Step 2: File Deletion
      :class-card: sd-border-primary

      **Why?** Why was the SOP accidentally deleted?
      ^^^
      **Finding:** A staff member was tidying directory files and moved it to the Recycle Bin.

   .. grid-item-card:: Step 3: Recovery Failure
      :class-card: sd-border-primary

      **Why?** Why was it permanently lost rather than restored?
      ^^^
      **Finding:** The Recycle Bin was already emptied, and no backup copy existed.

   .. grid-item-card:: Step 4: Governance Gap
      :class-card: sd-border-warning

      **Why?** Why was there no backup or version-controlled copy?
      ^^^
      **Finding:** Document control relied on a single working copy on a shared drive.

   .. grid-item-card:: Step 5: Root Cause
      :class-card: sd-border-danger

      **Why?** Why did document control not include digital backups for this scope?
      ^^^
      **Finding:** This scope was overlooked when bioinformatics was integrated into the QMS.


Correction
-----------
With the root cause identified, ask yourself: what would actually resolve this and stop it from reoccurring? In this case, that would likely mean introducing a backup or version-control requirement for bioinformatics SOPs and other controlled digital documents, in addition to retrieving or rewriting the missing SOP itself. 

Some corrective actions are quick to implement; others are not. If a fix would take significant staff time or resources, for example resolving a software bug, the corrective action can be a documented plan for how it will be fixed and how it is prioritised against other work, rather than the fix itself. 

Effectiveness check
-------------------
For each non-conformity identified, also plan an effectiveness check. This is where you agree a timeframe (with the person responsible for verifying the audit) within which to check progress on the corrective action. What counts as reasonable will depend on your operational context; it may not be realistic to expect resolution within a short space of time, particularly if the fix falls outside your team's direct control.

Within the agreed timeframe, document the status of the corrective action, including any mitigating circumstances if progress has been delayed. 

Lessons learned
----------------
Once the action has been corrected, record any lessons learned about what to do differently in future to prevent the issue from recurring. This might be about the specific fix, or something broader about how similar issues could be caught sooner next time. 

Closing the audit
------------------
Once impact, immediate action (where relevant), root cause, and corrective action, and lessons learned are documented, liaise with those responsible for closing audits (e.g. quality management teams) to confirm there is an approved action for each non-compliance, and schedule a review of the audit. Once the effectiveness check is also complete, the audit can be signed off by someone with relevant authority, along with feedback on the quality of the audit itself.

Non-conformities should be reviewed by those responsible for quality management, both to ensure they close within a reasonable timeframe, and to watch for patterns emerging over time. 

