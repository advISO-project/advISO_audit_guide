===============================
Bioinformatics Audit Schedule
===============================
.. tip::
   If you have quality management team who is responsible for putting the audit schedule together for a department, the following approach may help integrate bioinformatics into the remit and ensure audits for bioinformatics are compliant.


Mapping the :doc:`/audit_guide/sample_journey` clarifies key risk areas within bioinformatics processes. This section explores how that sample journey exercise can inform a practical, documented **schedule** to support your team as you evaluate how to prioritise bioinformatics processes for audit and how frequently to review them.

Under `ISO 15189 <https://www.iso.org/standard/76677.html>`_, internal audit scheduling considers the risk profile associated with a process, alongside any historical findings, feedback, complaints, recent updates, or the maturity of the implemented process.  

While wet laboratory assays and instruments generally change on more predictable cycles, bioinformatics software, pipelines, or analyses often evolve differently, meaning risk profiles can shift more dynamically. 

A more adaptable approach to auditing for bioinformatics allows teams to adjust audit scope as processes change, while still maintaining a consistent schedule for review. Some laboratories may find it helpful to maintain a dedicated audit schedule for bioinformatics processes, while others may choose to integrate bioinformatics into a broader laboratory audit schedule.

Defining the number of years in an audit schedule (or cycle) will depend on where you are in your accreditation journey, risk assessment, and resource constraints. 

In this example, we will use an audit schedule which lasts for 2 years at a time before review.  

The frequency bands outlined below offer one model of how a laboratory might align bioinformatics risk levels with audit frequency. They are intended as a practical reference that teams can adapt based on their own operational context.
 

.. grid:: 1 1 3 3
   :gutter: 2

   .. grid-item-card:: Low Risk 🟢
      :class-header: sd-bg-success sd-text-white sd-font-weight-bold

      **Audit Frequency:** Every 2 years (within a 2-year audit schedule)

   .. grid-item-card:: Medium Risk 🟡
      :class-header: sd-bg-warning sd-text-dark sd-font-weight-bold

      **Audit Frequency:** Every 1 year (within a 2-year audit schedule)

   .. grid-item-card:: High Risk 🔴
      :class-header: sd-bg-danger sd-text-white sd-font-weight-bold

      **Audit Frequency:** Every 6 months (within a 2-year audit schedule)


.. tip::
   A useful rule of thumb is to prioritise processes higher if they impact patients and/or have been deployed recently, as these are factors that carry higher risk.


------------------------------
The Pathogen X Sample Journey 
------------------------------
Consider the sample journey of a hypothetical pathogen, Pathogen X. The worked examples below illustrate how a team might translate risks identified from the Pathogen X sample journey into a practical audit **schedule**. 

.. note::
   The Pathogen X sample journey revealed that the output contributes to **clinical decision making.**


.. container:: flip-card-container

   .. container:: flip-card

      .. container:: flip-card-inner
         
         Test

      .. container:: flip-card-back

         Test

   






**Sequence Receipt**
There is an SOP within review date which outlines the process for transferring sequence data to the start of the bioinformatics workflow.

**Assembly**
The genome assembly tool is set up to run with liberal parameters as a trade-off between accuracy and memory constraints to prevent the computer from crashing and causing undue delay to results. 

**Variant Calling**
The version of a variant-calling tool is controlled in a Docker container and any major updates to the variant-calling tools are reviewed and the pipeline is verified before the production pipeline itself is updated with the new version of the tool.

**Results QC**
The QC thresholds to determine the pass/fail criteria of a consensus sequence are configured and documented in an SOP. 


**Data Storage and Archival**
The FASTQs used to analyse a sample are deleted permanently after each sequencing run is processed through the bioinformatics analysis to save on space. 


You may then decide that the bioinformatics process for Pathogen X is high risk based on the fact the output affects patients, there is no way to trace a result back to FASTQs, and it was deployed into production less than 6 months ago. Therefore, you may consider auditing this process once every 6 months within a 2-year schedule and then decrease this frequency after the first cycle (i.e. 2 years) once the process has matured. 

The schedule can be recorded in something as straightforward as a spreadsheet, so long as it is shared and agreed upon with relevant parties with responsibility for managing quality e.g. a quality management team. Where possible, the schedule should also be backed up and version controlled to decrease the risk of losing the record. 


.. tip::
   Audits can be intrusive to business, so bear this in mind when deciding the practicalities of audit frequency.

.. raw:: html

   <script>
     // Toggle flip state on click
     document.addEventListener('DOMContentLoaded', () => {
       document.querySelectorAll('.flip-card').forEach((card) => {
         card.addEventListener('click', () => {
           card.classList.toggle('is-flipped');
         });
       });
     });
     </script>