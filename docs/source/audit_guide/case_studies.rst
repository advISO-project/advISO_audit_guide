============
Case Studies
============

Throughout this guide we make use of a series of case studies to illustrate how the modular audit structure can be applied in practice:

.. dropdown:: 🧪 Laboratory Procedure

   An audit assessing the process for preparing Illumina sequencing libraries from DNA.

.. dropdown:: 🧬 Bioinformatics QC Procedure

   An audit assessing the bioinformatics procedure for assessing the quality of Illumina sequencing reads prior to downstream analysis and reporting.

.. dropdown:: 🧬 Bioinformatics Analysis Pipeline

   An audit assessing the bioinformatics procedure for analysing Illumina sequencing reads to identify variants and generate a report for clinical interpretation.

.. dropdown:: 🌌 Galaxy Workflows

   An audit assessing the procedure for Galaxy workflow development, execution, and management.

.. dropdown:: 💻 Code Update & Review Procedure

   An audit assessing the procedure for updating bioinformatics pipelines and performing code review.

.. dropdown:: 🔧 Systems, Hardware, and Databases

   An audit assessing how procedures for logging, updating, and maintaining bioinformatics equipment, systems, hardware, and databases are implemented.

All of these case studies are loosely based on real procedures
used within ISO accredited laboratories.

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