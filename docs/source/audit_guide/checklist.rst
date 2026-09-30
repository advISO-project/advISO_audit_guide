===============================
Bioinformatics Audit Checklist
===============================
A checklist is a structured set of question used during an internal audit to check each area of a process is compliant by capturing evidence that supports it. It exists that the same areas of a process get checked with the same assessment each time, ensuring reproducibility.

When you are auditing a bioinformatics process, the checklist is usually applied to a randomly selected sample from a recent sequencing run from the audit period. This does not have to be every single sample or run, just enough to establish a representative picture of how the bioinformatics process handled a sample - that is to say whether the process conformed to the laboratory's own requirements and is effectively implemented and managed.

Checklists can be managed and archived on paper, a local spreadsheet, an electronic quality management system, or a reasonable alternative. Either way, it is advised to document where they are managed and backed up as this could be a single point of failure. It is important to mitigate the risk of losing a record of which checklist was used to perform a particular audit. 

If you already audit wet laboratory processes, the section headers below will likely be familiar and may correspond with headers that are present in an SOP associated with a process. This sets up the scope of the audit - what is the checklist aiming to evaluate?

.. dropdown:: 🧪 Laboratory Procedure

  1. **Pre-examination**: was the process for sample receipt and preparation followed correctly for a selected sample?
  
  2. **Examination procedures**: has the SOP been followed step-by-step for a selected sample?

  3. **Equipment**: is laboratory equipment calibrated, used, maintained/replaced correctly and functioning according to manufacturer's instructions? 

  4. **Kits and reagents**: is the stock of kits and reagents used for the test controlled?

  5. **Personnel**: are training and competency records for this process present and up to date for the staff member following the SOP?

  6. **Report**: is the final report correct and does it evidence the test was performed correctly within the agreed turnaround time (TAT)?

  7. **Quality assurance**: is there evidence of IQA and EQA for the test?

However, it is not immediately clear how each of these sections would translate into a bioinformatics equivalent. For example, "Kits and reagents" carries very little meaning in bioinformatics, as bioinformatics does not consume a physical, batch-tracked stock. Instead, it would likely not be fit for purpose to use a checklist exactly like the example above to assess the bioinformatics scope of an examination.

Rather than forcing bioinformatics checklists into headers that are not best designed for them, then, it is advised to work through each of these headers and ask for what it is assessing, decide whether that function exists in your own bioinformatics process, and if not, adapting it to be compatible with your bioinformatics scope. 

.. tip::
    Like a wet laboratory procedure, the bioinformatics equivalent of an audit checklist should be informed by the risks identified in the :doc:`/audit_guide/sample_journey`.

The checklist items for a bioinformatics equivalent are suggestions, and you may wish to add or remove items based on your own sample journey. You may find as you work through your own bioinformatics sample journey, you begin to sort risks into general categories that can be used to inform the checklist section headers. From there, you can start to think about questions which address checking those risks.

.. dropdown:: Pathogen X Case Study
    
    1. **Pre-examination**: whether the sample and its context are correctly identified and traceable before analysis begins
        a. **Example questions**
            i. Have you reviewed the previous audit to check for emerging patterns or trends?
            ii. What is the sample ID for this test?
    2. **Examination procedures**: whether the documented method for this test is current, validated, and being followed correctly.
        a. **Example questions**
            i. Are all SOPs used for this process within date of review?
            ii. Is a validation or verification report available for this test?
    3. **Personnel**: whether staff involved in testing this sample are trained, competent, and demonstrably aware of the relevant procedures
        a. **Example questions**
            i. Do staff involved in testing this sample have evidence of reading all relevant documentation?
            ii. Are training and competency records of staff who performed the test available and up to date?
    4. **Bioinformatics analysis**: whether the pipeline received the correct inputs and produced the expected outputs at each stage.
        a. **Example questions**
            i. Are the input sequencing files for this sample available and not corrupt?
            ii. Were expected outputs for the analysis sample generated at each stage of the bioinformatics workflow?
    5. **Databases**: whether reference databases are current, accessible, and any changes have been verified?
        a. **Example questions**
            i. Are any databases required for testing this sample accessible, back up, and up to date?
            ii. If there has been an updated in the last 12 months, was an appropriate verification performed?
    6. **Software**: whether tool versions are recorded and any updates have been proportionately verified
        a. **Example questions**
            i. For all tools used for testing this sample, is the version number stated?
            ii. If there has been an update in the last 12 months, was an appropriate verification performed?
    7. **Equipment**: whether IT hardware is functioning correctly, maintained, and covered by adequate support arrangements. If you have access to high performance computing, you may also want to think about additional risks like temperature breaches
        a. **Example questions**
            i. If the IT equipment used to perform this test has malfunctioned and been replaced in, has an inspection confirmed proper functioning?
            ii. Is there a warranty for IT equipment used to perform this test, and is it in date?
    8. **Data storage and archival**: whether files and logs are retained and stored according to an agreed, traceable procedure
        a. **Example questions**
            i. Is there an agreed procedure for how input and output files for this test are stored and archived?
            ii. Are log files outputted at each relevant stage of the bioinformatics process, and do they contain information for traceability, e.g. timestamps?
    9. **Quality assurance**: whether internal and external quality checks are defined, documented, and evidenced
        a. **Example questions**
            i. Is there evidence of EQA or interlaboratory exchange?
            ii. Are the IQA procedure, frequency, and pass/fail criteria included in an SOP? Is there evidence of recent IQA?
            iii. Are QC thresholds configured and documented to determine the pass/fail criteria of the sample?

.. tip:: 
    It is advised that proposed checklists are agreed upon by those who are responsible for quality management in your laboratory before proceeding further with the audit.