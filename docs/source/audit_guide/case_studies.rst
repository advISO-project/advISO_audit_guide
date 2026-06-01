Case studies
============

Throughout this guide we make use of a series of case studies to illustrate how the modular SOP structure can be applied in practice:

.. dropdown:: 🧬 Bioinformatics QC Procedure

   A bioinformatics procedure for assessing the quality of Illumina sequencing reads prior to downstream analysis and reporting.

.. dropdown:: 🧪 Laboratory Procedure

   A laboratory procedure detailing the process for preparing Illumina sequencing libraries from DNA.

.. dropdown:: 👩‍🔬 Staff Training Procedure

   A procedure for planning, delivering, and documenting staff training activities.

.. dropdown:: 🌌 Galaxy Training Procedure
  
   A procedure for delivering standardized training on the Galaxy platform, covering workflow development, execution, and management.

.. dropdown:: 💻 Code Update & Review Procedure

   A procedure outlining best practices for updating bioinformatics pipelines and performing code review.

.. dropdown:: ✅ Verification Procedure

   A standard operating procedure for perfoming verification of bioinformatics pipelines prior to rollout.

All of these case studies are loosely based on real procedures used within ISO accredited laboratories.

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