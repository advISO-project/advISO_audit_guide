Resolving Audit Findings
========================
Let's say that when you performed the most recent audit for Pathogen X, you discovered that there was no evidence that there is an SOP for detailing how the bioinformatics method worked, despite there being an expectation that one existed. 

This would have been recorded as Non-Compliant. Any non-conformities like this should be corrected without undue delay, following a process like the one outlined below to ensure the correction happens:

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 6px; margin: 30px auto; max-width: 1050px;">

     <!-- Step 1 -->
     <div style="background: #ffffff; border: 2px solid #648FFF; border-radius: 8px; padding: 10px 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04); flex: 1 1 120px; max-width: 150px; min-width: 110px; box-sizing: border-box;">
       <p style="margin: 0; font-size: 0.84em; font-weight: 600; color: #2c3e50;">⚠️ Impact Assessment</p>
     </div>

     <!-- Arrow 1 -> 2 -->
     <div style="color: #648FFF; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
       <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
     </div>

     <!-- Step 2 -->
     <div style="background: #ffffff; border: 2px solid #648FFF; border-radius: 8px; padding: 10px 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04); flex: 1 1 120px; max-width: 150px; min-width: 110px; box-sizing: border-box;">
       <p style="margin: 0; font-size: 0.84em; font-weight: 600; color: #2c3e50;">🔍 Root-Cause Analysis</p>
     </div>

     <!-- Arrow 2 -> 3 -->
     <div style="color: #648FFF; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
       <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
     </div>

     <!-- Step 3 -->
     <div style="background: #ffffff; border: 2px solid #648FFF; border-radius: 8px; padding: 10px 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04); flex: 1 1 120px; max-width: 150px; min-width: 110px; box-sizing: border-box;">
       <p style="margin: 0; font-size: 0.84em; font-weight: 600; color: #2c3e50;">🛠️ Corrective Action</p>
     </div>

     <!-- Arrow 3 -> 4 -->
     <div style="color: #648FFF; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
       <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
     </div>

     <!-- Step 4 -->
     <div style="background: #ffffff; border: 2px solid #648FFF; border-radius: 8px; padding: 10px 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04); flex: 1 1 120px; max-width: 150px; min-width: 110px; box-sizing: border-box;">
       <p style="margin: 0; font-size: 0.84em; font-weight: 600; color: #2c3e50;">⏱️ Effectiveness Check</p>
     </div>

     <!-- Arrow 4 -> 5 -->
     <div style="color: #648FFF; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
       <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
     </div>

     <!-- Step 5 -->
     <div style="background: #ffffff; border: 2px solid #648FFF; border-radius: 8px; padding: 10px 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04); flex: 1 1 120px; max-width: 150px; min-width: 110px; box-sizing: border-box;">
       <p style="margin: 0; font-size: 0.84em; font-weight: 600; color: #2c3e50;">📚 Lessons Learned</p>
     </div>

     <!-- Arrow 5 -> 6 -->
     <div style="color: #D97C5D; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
       <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
     </div>

     <!-- Step 6 -->
     <div style="background: #fef4f0; border: 2px solid #D97C5D; border-radius: 8px; padding: 10px 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04); flex: 1 1 120px; max-width: 150px; min-width: 110px; box-sizing: border-box;">
       <p style="margin: 0; font-size: 0.84em; font-weight: 600; color: #2c3e50;">🏁 Closing the Audit</p>
     </div>

   </div>


Impact assessment
------------------

.. card:: 💡 Think through the impact of this non-conformity to assess its severity. Some questions you may consider at this stage could include:
   :class-card: sd-border-success sd-shadow-md
   :class-header: sd-bg-success sd-text-white sd-font-weight-bold

   * Did this non-conformity mean a step in the bioinformatics pipeline was performed incorrectly, or without a documented basis?
   *	Could that have had a detrimental impact on a patient?
   *	Was the missing information available somewhere else instead?
   *	Does this need to be escalated or reported elsewhere?
   *	For how long has this non-conformity existed?


.. warning::
    If there is **any** possibility that a non-conformity identified through an interal audit could have detrimentally impacted patient results, it is strongly advised to escalate it immediately through the reporting pathway that is most appropriate for your organisation. This guide cannot tell you what that pathway is; make sure you are aware of your own policy in advance of needed it. 

Record some details about the non-conformity, including the discovery date, where it took place, and an initial severity level. Severity typically ranges from a Recommendation (an observation or suggestion for improvement where nothing has actually failed) through to Minor, Major, or Critical, depending on the seriousness of the issue.

To understand the true weight of the non-conformity, it helps to explore it through two different lenses: **impact** and **origin**. 

**Impact** is about consequence: what could go wrong, or has already gone wrong, because of this? Consider how the issue touches upon patient safety, data protection, service continuity, or the overall effectiveness of your quality management system. 

Meanwhile, **origin** is about *where* in your bioinformatics sample journey the issue arose - whether it sits with documentation, equipment integrity and maintenance, personnel, or data storage and archival. Naming the origin helps you (and anyone reviewing the audit later) spot if the same kind of issue keeps recurring from a familiar source.

Immediate action
^^^^^^^^^^^^^^^^^
Before turning to why the non-conformity happened, consider whether any action needs to be taken immediately to limit ongoing harm. This is different from fixing the underlying problem; it is about stopping the immediate risk. For example, this could mean pausing a pipeline that is still processing samples with an out-of-date reference database or flagging affected results to stakeholders, so they are not relied upon while the issue is investigated. 

Not every non-conformity will need this step. In our Pathogen X example, the missing SOP was not actively causing harm at the point of discovery, so no immediate action was required beyond what has already been covered in impact assessment. Where immediate action is needed, record what was done, when, and by whom.

Root-cause analysis
--------------------
Root-cause analysis identifies the reason why the non-conformity occurred, not just what happened. A useful rule of thumb for root-cause analysis to ask “why” about 3-5 times, backtracking until you reach something you can act upon. 

A root-cause analysis for the non-conformity we identified for Pathogen X is outlined below. 

.. raw:: html

   <!-- Problem Statement / Audit Finding Banner -->
   <div style="background-color: #fef4f0; border-left: 6px solid #D97C5D; padding: 16px 20px; border-radius: 6px; margin: 20px auto 10px auto; max-width: 450px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); box-sizing: border-box;">
     <p style="margin: 0 0 4px 0; color: #D97C5D; font-size: 1.0em; font-weight: bold; letter-spacing: 0.05em;">
       🤔 Problem Statement (i.e. Non-Compliant Finding)
     </p>
     <p style="margin: 0; font-size: 1.05em; color: #2c3e50; font-weight: 600;">
       During an internal audit of a bioinformatics process, the required Bioinformatics SOP was missing from the designated repository.
     </p>
   </div>

   <p style="text-align: center; margin-bottom: 20px;"><em>Click or tap any card below to flip it and trace the investigation down to the root cause by asking "why":</em></p>

   <!-- Vertical Flow Container -->
   <div class="flip-card-container" style="display: flex; flex-direction: column; align-items: center; gap: 0;">

     <!-- Arrow from Banner to Card 1 -->
     <div style="display: flex; justify-content: center; align-items: center; height: 36px; color: #D97C5D;">
       <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
     </div>

     <!-- Card 1 -->
     <div class="flip-card" onclick="this.classList.toggle('is-flipped')">
       <div class="flip-card-inner">
         <div class="flip-card-front">
           <p style="font-size: 0.8em; opacity: 0.9; margin-bottom: 8px;">WHY #1</p>
           <p>🔍 Where did the required SOP go?</p>
         </div>
         <div class="flip-card-back">
           <p>A staff member accidentally moved the file to the Recycle Bin while organising folders, and it was emptied before anyone noticed, permanently deleting the record.</p>
         </div>
       </div>
     </div>

     <!-- Arrow 1 -> 2 -->
     <div style="display: flex; justify-content: center; align-items: center; height: 36px; color: #648FFF;">
       <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
     </div>

     <!-- Card 2 -->
     <div class="flip-card" onclick="this.classList.toggle('is-flipped')">
       <div class="flip-card-inner">
         <div class="flip-card-front">
           <p style="font-size: 0.8em; opacity: 0.9; margin-bottom: 8px;">WHY #2</p>
           <p>❓ Why was the file able to be permanently deleted?</p>
         </div>
         <div class="flip-card-back">
           <p>The document was stored in a standard shared folder where every employee had unrestricted edit and delete permissions.</p>
         </div>
       </div>
     </div>

     <!-- Arrow 2 -> 3 -->
     <div style="display: flex; justify-content: center; align-items: center; height: 36px; color: #648FFF;">
       <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
     </div>

     <!-- Card 3 -->
     <div class="flip-card" onclick="this.classList.toggle('is-flipped')">
       <div class="flip-card-inner">
         <div class="flip-card-front">
           <p style="font-size: 0.8em; opacity: 0.9; margin-bottom: 8px;">WHY #3</p>
           <p>❓ Why were those permissions unrestricted?</p>
         </div>
         <div class="flip-card-back">
           <p>Standard document protection controls, such as delete-protection and automated daily backups, were never configured for this specific drive.</p>
         </div>
       </div>
     </div>

     <!-- Arrow 3 -> 4 -->
     <div style="display: flex; justify-content: center; align-items: center; height: 36px; color: #648FFF;">
       <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
     </div>

     <!-- Card 4 -->
     <div class="flip-card" onclick="this.classList.toggle('is-flipped')">
       <div class="flip-card-inner">
         <div class="flip-card-front">
           <p style="font-size: 0.8em; opacity: 0.9; margin-bottom: 8px;">WHY #4</p>
           <p>❓ Why were these document protection controls missed?</p>
         </div>
         <div class="flip-card-back">
           <p>When the bioinformatics team and processes were added to the quality framework, the IT workspace security checklist was omitted.</p>
         </div>
       </div>
     </div>

     <!-- Arrow 4 -> 5 -->
     <div style="display: flex; justify-content: center; align-items: center; height: 36px; color: #D97C5D;">
       <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
     </div>

     <!-- Card 5 -->
     <div class="flip-card" onclick="this.classList.toggle('is-flipped')">
       <div class="flip-card-inner">
         <div class="flip-card-front" style="background-color: #D97C5D; border-color: #D97C5D;">
           <p style="font-size: 0.8em; opacity: 0.9; margin-bottom: 8px;">ROOT CAUSE</p>
           <p>🎯 What is the systemic issue?</p>
         </div>
         <div class="flip-card-back" style="border-color: #D97C5D;">
           <p>The formal onboarding process for integrating new teams or domains into the organisation's system does not mandate verifying digital folder security and backup configurations.</p>
         </div>
       </div>
     </div>

   </div>

Corrective Action
-------------------
With the root cause identified, ask yourself: what would actually resolve this and stop it from recurring? In this case, that means addressing both the immediate symptom, i.e. retrieving or rewriting the missing SOP itself, and the systemic issue. Practically, this looks like updating the team onboarding and system-integration process so that any new domain bringing in digital documents must verify that folder permissions, delete protection, and automated backups are properly configured from day one.

Some corrective actions are quick to implement; others are not. If a fix would take significant staff time or resources, for example, a complex software bug that requires extensive testing, the corrective action can be a documented plan for how it will be fixed and how it is prioritised against other work, rather than the fix itself. 

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

