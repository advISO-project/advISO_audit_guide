.. _case_studies:

============
Case Studies
============

Throughout this guide we make use of a series of case studies to illustrate how the modular audit structure can be applied in practice:

.. dropdown:: 🧪 Laboratory Procedure

   An audit assessing the procedure for preparing Illumina sequencing libraries from DNA.

.. dropdown:: 🧬 Bioinformatics Analysis Pipeline

   An audit assessing the bioinformatics procedure for analysing Illumina sequencing reads to identify variants and generate a report for clinical interpretation.

.. dropdown:: 🌌 Galaxy Workflows

   An audit assessing the procedure for Galaxy workflow development, execution, and management.


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