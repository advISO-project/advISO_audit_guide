===============================================
Introducing Audits for Bioinformatics Teams
===============================================
Wet laboratory audits work well because a wet laboratory procedure is usually anchored to one thing: a single documented SOP that a trained member of staff follows step by step. Checking compliance means checking that the SOP was followed, and the evidence - signed forms, reagent lot numbers, instrument logs - is usually stable once it is created.

Bioinformatics work does not anchor the same way. A single process might be implemented across several interacting scripts, a Galaxy workflow, and one or more pipelines, any of which can be updated independently of the others. And unlike a reagent, which stays exactly as it was once used, a bioinformatics pipeline's dependencies - a reference database, a container image, a third-party tool - can change *after* a result has already been produced, silently altering what that pipeline would now do to the same input. A wet-laboratory approach build around "was the SOP followed" has no natural way to ask that second question.

THis is the specific problem this guide addresses: not that bioinformatics needs different accreditation standards, but that auditing well needs different approaches, which is where the distinctions below come in.


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
 
This guide follows the same cycle any audit does — planning, execution,
analysis of findings, and review and closure — with each stage adapted
for bioinformatics work rather than performed as if it were a wet laboratory
audit carried out on a different subject.
 
The next step is mapping where your own bioinformatics team's
responsibility sits within the wider examination process, and where the
risks are within it.

