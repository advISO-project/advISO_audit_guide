.. _case_studies:

============
Case Studies
============

Throughout this guide we make use of a series of case studies to illustrate how the internal audit structure can be applied in practice to bioinformatics processes:

.. dropdown:: 🧬 Bioinformatics Analysis Pipeline

   An audit evaluating the bioinformatics procedure for analysing Illumina sequencing reads to identify variants and generate a report for clinical interpretation.

.. dropdown:: 🌌 Galaxy Workflows

   An audit evaluating the Galaxy workflow and management for analysing sequencing reads to produce a report for clinical interpretation.

.. dropdown:: 🧪 Laboratory Procedure

   An audit evaluating the procedure for preparing Illumina sequencing libraries from DNA.
  

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