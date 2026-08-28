===============================================
Sample Journey
===============================================

Before designing your audits, it might be useful to map out the *sample journey* - the path a sample takes from initial raw input to final output. This exercise can help pinpoint key steps, identify risks, and decide which audit type (vertical, horizontal, or cross-audit) best fits each stage of the bioinformatics process. It also helps to focus audit efforts on areas of highest risk and importance.

If you already audit wet-lab processes, you may be familiar with the pre-examination, examination, and post-examination framework in ISO 15189. That framework describes the test as a whole, from requesting user to reporting user. In bioinformatics, the sample journey may be different as it may not cover that whole. So the more useful question to ask is: where does your bioinformatics team's scope begin and end within that whole test? And where are the risks


.. image:: ../images/sample_journey.svg
   :alt: Sample Journey Diagram
   :align: center
   :width: 600px

*Figure 1: Diagram illustrating the principal idea of the sample journey, forming the axis for auditing bioinformatics procedures and processes.*


Examples of mapping the sample journey to bioinformatics processes
-------------------------------------------------------------------
Have a go at mapping the sample journey for your own bioinformatics processes.

Once you have mapped out these journeys, match the key steps to the appropriate audit type (vertical, horizontal, or cross-audit). Doing this ensures all critical areas are covered, reveals where risks or gaps hide, and helps you determine how often each step needs to be audited based on its risk level.


.. dropdown:: 🧪 Laboratory Procedure

   Map the laboratory procedure for processing samples from initial receipt to final reporting. This could include identifying risks at the pre-examination, examination, and post-examination stages. 

.. dropdown:: 🧬 Bioinformatics QC Procedure

   Map the bioinformatics quality control procedures for processing samples from raw input to final output. This could include quality scores, read trimming, 

.. dropdown:: 🧬 Bioinformatics Analysis Pipeline

   Map the bioinformatics analysis pipeline(s) for processing samples from raw input to final input. This could include identifying risks at each stage of the pipeline, such as assembly, variant calling, annotation, phylogenetic analysis, and reporting. 

   You may identify that you have some pipelines that are more critical than others, and therefore require more frequent audits. For example, a pipeline that is used for clinical decision-making may require more frequent audits than a pipeline used for research purposes.

.. dropdown:: 🌌 Galaxy Workflows

   Map the Galaxy workflows for processing samples from raw input to final output. This could include identifying risks at each stage of the workflow, such as data import, quality control, analysis, and reporting.

.. dropdown:: 💻 Code Update & Review Procedure

   Map the code update and review procedures for processing samples from raw input to final output. This could include identifying risks at each stage of the code update and review process, such as version control, code review, testing, and deployment.

.. dropdown:: 🔧 Systems, Hardware, and Databases

   Map the systems, hardware, and databases used for processing samples from raw input to final output. This could include identifying risks at each stage of the process, such as data storage, backup, and recovery, as well as database management, versioning, and security.


----------------


.. raw:: html

   <script>
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
   </script>