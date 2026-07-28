==================================================
Introduction to audits for bioinformatics teams
===================================================

:ref:`Internal audits <internal_audits>` are systematic, independent evaluations of an organisation's processes, procedures, and systems to ensure compliance with established standards and identify areas for improvement. Internal audits play a crucial role in maintaining quality management systems and achieving accreditation under standards such as ISO 15189 and ISO 17025.

Audits can be structured in different ways depending on what you want to check. The three approaches below are not mutually exclusive and a well-designed audit programme will usually draw on all three at different times, acoording to the specific needs of the laboratory and the processes being audited.

.. dropdown:: ↕️ Vertical audit

    A vertical audit follows a single item, sample, or dataset through every stage of a process, end to end, checking that each step is compliant before moving to the next. It trades breadth for depth: you learn a great deal about one specific case, but nothing directly about how consistently the process is followed elsewhere.

    In bioinformatics, a vertical audit should be used for tracing a single sample or dataset from the first input e.g., raw sequencing output through the bioinformatics process to the final result or report. This would be applicable to both in-house bioinformatics pipelines and externally sourced bioinformatics services, where the laboratory is responsible for the quality of the final result.

    Vertical audits are particularly useful for demonstrating end-to-end traceability, identifying bottlenecks, and uncovering hidden risks in the process, which auditors and accreditation bodies will want to see evidenced.   

.. dropdown:: ↔️ Horizontal audit 

    A horizontal audit does the opposite to a vertical audit. It takes a single step of a process and checks how consistently it is applied across multiple services, if a laboratory has more than one service. It trades depth for breadth: you learn how consistent a specific practice is, but not necessarily whether the process as a whole works end to end. 

    In bioinformatics, a horizontal audit should check that a specific control, such as version control, software version pinning / containerisation, or reference database version pinning, is applied consistently across all bioinformatics pipelines / workflows, not just for one. 

.. dropdown:: 👥 Cross-audit
    
    A cross-audit is performed by someone independent of the team or process being audited, rather than someone reviewing their own work. This independence is what gives the findings credibility. 

    Note: a key limitation to bioinformatics cross-audits is finding other bioinformatics teams with relevant domain-specific knowledge and experience to perform the cross-audit, as they will need to be independent of the team being audited. This is particularly challenging for small laboratories with only one bioinformatics team, where it may be necessary to seek external auditors from other laboratories or organisations.