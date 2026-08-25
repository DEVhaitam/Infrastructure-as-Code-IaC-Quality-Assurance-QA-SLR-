# Identify venues and time

Period (~ 10 years): 1 January 2015 to 29 July 2025 

Venues: We identified papers from well-known contributors (Rahman et. al., Dalla Palma et. al., Sokolowski et. al., Opdebeeck et. al.), plus venues from authors' expertise. About journals, we selected the top ones (Q1), but we enlarged the scope for conferences to catch more papers for the QGS. Ranks for journals are from [SCImago](https://www.scimagojr.com/) and for conferences, from [CORE2026](https://portal.core.edu.au/conf-ranks/). Note that we retained several venues in which the well-known contributors have published non-IaC work, as these venues remain suitable for IaC research. The search engine used for getting the papers of the different venues was google scholar.

## Journals (5)

- TSE: Transactions on Software Engineering                     (IEEE - Q1)
    * Sokolowski
    * Dalla Palm
    * Rahman
- JSS: Journal of Systems and Software                          (ScienceDirect - Q1)
    * Opdebeeck
- TOSEM: Transactions on Software Engineering and Methodology   (ACM - Q1)
    * Chiari
- EMSE: Empirical Software Engineering                          (Springer - Q1)
    * Authors' expertise
    * Rahman
- IST: Information and Software Technology (ScienceDirect - Q1)
    * Authors' expertise

## Conferences (18)

- ASE:      International Conference on Automated Software Engineering                                      (rank A*)
    * Authors' expertise
- FSE:      Foundations of Software Engineering                                                             (rank A*)
    * Authors' expertise
- ICSE:     International Conference on Software Engineering                                                (rank A*)
    * Sokolowski
    * Rahman
- PLDI: Programming Language Design and Implementation                                                      (rank A*)
    * Authors' expertise
- SANER:    International Conference on Software Analysis, Evolution and Reengineering                      (rank A)
    * Opdebeeck
- ICSME:    International Conference on Software Maintenance and Evolution                                  (rank A)
    * Opdebeeck
    * Dalla Palma
- ICSA: International Conference on Software Architecture                                                   (rank A)
    * Chiari
    * Sokolowski
- MSR:      Mining Software Repositories                                                                    (rank A)
    * Opdebeeck
    * Sokolowski
- ICST:     International Conference on Software Testing, Verification and Validation                       (rank A)
    * Authors' expertise
- Models: International Conference on Model-Driven Engineering Languages and Systems                        (rank A)
    * Authors' expertise
- TACAS: International Conference on Tools and Algorithms for the Construction and Analysis of Systems      (rank A)
    * Authors' expertise
- ICWS: International Conference on Web Services                                                            (rank A)
    * Authors' expertise
- SLE: International Conference on Software Language Engineering                                            (rank B)
    * Authors' expertise
- ICFEM: International Conference on Formal Engineering Methods                                             (rank C)
    * Authors' expertise
- SoCC: Symposium on Cloud Computing                                                                        (no rank)
    * Authors' expertise
- WIMS: Web Intelligence, Machine Intelligence and Semantics                                                (no rank)
    * Authors' expertise
- ESOCC: European Conference On Service-Oriented And Cloud Computing                                        (no rank)
    * Chiari
- ISSTA: International Symposium on Software Testing and Analysis                                           (rank A)
    * Saavedra
    * Sokolowski
---------------------

# Establish the quasi goldset (QGS)

## Manual search

- From MSR (10):
    * [1] Jiang & Adams, "Co-evolution of Infrastructure and Source Code — An Empirical Study" 2015, cited by 131
    * [2] Sharma, Fragkoulis & Spinellis, "Does Your Configuration Code Smell?" 2016, cited by 235
    * [3] Cito et al., "An Empirical Analysis of the Docker Container Ecosystem on GitHub" 2017, cited by 217
    * [4] Opdebeeck, Zerouali & De Roover, "Smelly Variables in Ansible Infrastructure Code: Detection, Prevalence, and Lifetime" 2022, cited by 44
    * [5] Opdebeeck, Zerouali & De Roover, "Control and Data Flow in Security Smell Detection for Infrastructure as Code: Is It Worth the Effort?", 2023, cited by 47
    * [6] Begoug et al., "Fine-Grained Just-In-Time Defect Prediction at the Block Level in Infrastructure-as-Code (IaC)" 2024, cited by 17
    * [7] Ksontini et al., "DRMiner: A Tool for Identifying and Analyzing Refactorings in Dockerfile" 2024, cited by 10
    * [8] Kosbar & Hamdaqa, "Smells-sus: Sustainability Smells in IaC" 2025, cited by 5
    * [9] Sobhani, Haque & Sharma, "It Works (only) on My Machine: A Study on Reproducibility Smells in Ansible Scripts" 2025, cited by 1
    * [10] Ksontini et al., "Refactoring for Dockerfile Quality: A Dive into Developer Practices and Automation Potential" 2025, cited by 11

- From ICSE (5):
    * [11] Rahman, Parnin & Williams, "The Seven Sins: Security Smells in Infrastructure as Code Scripts", 2019, cited by 306
    * [12] Rahman et al., "Gang of Eight: A Defect Taxonomy for Infrastructure as Code Scripts" 2020, cited by 88
    * [13] Sotiropoulos, Mitropoulos & Spinellis, "Practical Fault Detection in Puppet Programs" 2020, cited by 39
    * [14] Henkel et al., "Shipwright: A Human-in-the-Loop System for Dockerfile Repair" 2021, cited by 53
    * [15] Durieux, "Empirical Study of the Docker Smells Impact on the Image Size" 2024, cited by 23

- From ASE (4):
    * [16] Weiss, Guha & Brun, "Tortoise: Interactive System Configuration Repair" 2017, cited by 59
    * [17] Saavedra et al., "Polyglot Code Smell Detection for Infrastructure as Code with GLITCH" 2023, cited by 18
    * [18] Reis et al., "Leveraging Practitioners' Feedback to Improve a Security Linter" 2023, cited by 25
    * [19] Sahoo et al., "Ansible Lightspeed: A Code Generation Service for IT Automation" 2024, cited by 18

- From FSE (2):
    * [20] Sokolowski, "Infrastructure as Code for Dynamic Deployments" 2022, cited by 29
    * [21] Hassan et al., "State Reconciliation Defects in Infrastructure as Code" 2024, cited by 23

- From ICST (3):
    * [22] Rahman & Williams, "Characterizing Defective Configuration Scripts Used for Continuous Deployment" 2018, cited by 76
    * [23] Hassan & Rahman, "As Code Testing: Characterizing Test Quality in Open Source Ansible Development" 2022, cited by 29
    * [24] Cannavacciuolo & Mariani, "Smoke Testing of Cloud Systems" 2022, cited by 12

- From SANER (3):
    * [25] van der Bent et al., "How Good Is Your Puppet? An Empirically Defined and Validated Quality Model for Puppet" 2018, cited by 68
    * [26] Rahman & Sharma, "Lessons from Research to Practice on Writing Better Quality Puppet Scripts" 2022, cited by 6
    * [27] Bessghaier et al., "On the Prevalence, Co-occurrence, and Impact of Infrastructure-as-Code Smells" 2024, cited by 9

- From ICSME (3):
    * [28] Rosa, Scalabrino & Oliveto, "Assessing and Improving the Quality of Docker Artifacts" 2022, cited by 5
    * [29] Dalla Palma, Di Nucci & Tamburri, "Defuse: A Data Annotator and Model Builder for Software Defect Prediction" 2022, cited by 3
    * [30] Bui, Laukötter & Scandariato, "DockerCleaner: Automatic Repair of Security Smells in Dockerfiles" 2023, cited by 16

- From ISSTA (3):
    * [31] Xu, Gao & Wei, "An Empirical Study on Kubernetes Operator Bugs" 2024, cited by 23
    * [32] Saavedra, Ferreira & Mendes, "InfraFix: Technology-Agnostic Repair of Infrastructure as Code" 2025, cited by 5
    * [33] Coppa, Sokolowski & Salvaneschi, "Hybrid Fuzzing of Infrastructure as Code Programs (Short Paper)" 2025, cited by 1

- From TSE (3):
    * [34] Dalla Palma et al., "Within-Project Defect Prediction of Infrastructure-as-Code Using Product and Process Metrics" 2022, cited by 113
    * [35] Rahman & Parnin, "Detecting and Characterizing Propagation of Security Weaknesses in Puppet-Based Infrastructure Management" 2023, cited by 34
    * [36] Sokolowski, Spielmann & Salvaneschi, "Automated Infrastructure as Code Program Testing" 2024, cited by 32

- From TOSEM (4):
    * [37] Rahman et al., "Security Smells in Ansible and Chef Scripts: A Replication Study" 2021, cited by 115
    * [38] Rahman et al., "Security Misconfigurations in Open Source Kubernetes Manifests: An Empirical Study" 2023, cited by 147
    * [39] Zhou et al., "DRIVE: Dockerfile Rule Mining and Violation Detection" 2023, cited by 21
    * [40] Ntentos et al., "On the Understandability of Design-Level Security Practices in Infrastructure-as-Code Scripts and Deployment Architectures" 2024, cited by 8

- From EMSE (7): 
    * [41] Rahman, Farhana & Williams, "The 'As Code' Activities: Development Anti-patterns for Infrastructure as Code" 2020, cited by 58
    * [42] Borovits et al., "FindICI: Using Machine Learning to Detect Linguistic Inconsistencies Between Code and Natural Language Descriptions in Infrastructure-as-Code" 2022, cited by 29
    * [43] Rahman et al., "An Empirical Study of Task Infections in Ansible Scripts" 2023, cited by 8
    * [44] Eng, Hindle & Stroulia, "Patterns of Multi-Container Composition for Service Orchestration with Docker Compose" 2024, cited by 11
    * [45] Verdet et al., "Assessing the Adoption of Security Policies by Developers in Terraform Across Different Cloud Providers" 2025, cited by 15
    * [46] Minna, Massacci & Tuma, "Analyzing and Mitigating (with LLMs) the Security Misconfigurations of Helm Charts from Artifact Hub" 2025, cited by 24
    * [47] War et al., "Vulnerabilities in Infrastructure as Code: What, How Many, and Who?", 2025, cited by 14

- From JSS (2):
    * [48] Dalla Palma et al., "Toward a Catalog of Software Quality Metrics for Infrastructure Code" 2020, cited by 100
    * [49] Opdebeeck et al., "On the Practice of Semantic Versioning for Ansible Galaxy Roles: An Empirical Study and a Change Classification Model" 2021, cited by 24

- From SoCC (1):
    * [50] Automatically detecting risky scripts in infrastructure code
---------------------

## Additional papers

### From past SLRs (3)

- [51] J. Schwarz, A. Steffens, and H. Lichter, “Code smells in infrastructure as code,” in Proc. 11th Int. Conf. Qual. Inf. Commun. Technol., QUATIC’18. IEEE Comp. Soc., 2018, pp. 220–228. cited by 91
- [52] N. Borovits, I. Kumara, P. Krishnan, S. D. Palma, D. D. Nucci, F. Palomba, D. A. Tamburri, and W. van den Heuvel, “DeepIaC: deep learning-based linguistic anti-pattern detection in IaC,” in Proc. 4th Int. Workshop Mach. Learn. Techn. Softw. Qual. Eval., MaLTeSQuE’20. ACM, 2020, pp. 7–12. cited by 37
- [53] A. Brogi, A. Di Tommaso, and J. Soldani, “Sommelier: A tool for validating TOSCA application topologies,” in Proc. 5th Int. Conf. ModelDriven Eng. and Softw. Develop., MODELSWARD’17, ser. Commun. Comput. Inf. Sci., vol. 880. Springer, 2017, pp. 1–22. cited by 26

## Evaluating the search queries:

In the following, we refer several queries to score with our gold set. 
- Q1: Quality improvement centric:  *(“Infrastructure as Code” OR “IaC”) AND (“Quality assurance” or “Testing” OR “Verification” OR “linting” OR “Static Analysis” OR “Dynamic analysis”)*
- Q2: Issue centric:  *("Infrastructure as Code" OR "IaC") AND ("defects" OR "errors" OR "anti-patterns" OR "vulnerabilities" OR "code smells" OR "Quality issues" OR "bad practices" OR "Misconfiguration")*
- Q3: Survey oriented:  *("Infrastructure as Code" OR "IaC") AND ("taxonomy" OR "classification" OR "Categorization" OR "Survey")*
- Q4: Full merge (Q1+Q2): *("Infrastructure as Code" OR "IaC") AND ("defect" OR "bug" OR "smell" OR "anti-pattern" OR "vulnerability" OR "misconfiguration" OR "bad practice" OR "error" OR "fault" OR "testing" OR "analysis" OR "verification" OR "linting" OR "quality assurance" OR "static analysis" OR "validation")*
- Q5: SLR query:    *("Infrastructure as Code" OR "IaC") AND ("defect" OR "bug" OR "smell" OR "anti-pattern" OR "testing" OR "analysis" OR " verification")*

We excuted the search query across the 4 different databases, we got the following numbers:
- Q1 retrieved **3860** references
- Q2 retrieved **2304** references
- Q3 retrieved **1990** references
- Q4 retrieved **4361** references
- Q5 retrieved **2821** references

We used the scripts/check_goldset.py script to evaluate the different search queries against the gold set, and we got:
- Q1: **30/53**;**QSM:56%**; missing [3,8,9,10,15,16,19,24,25,27,28,29,30,31,32,34,42,43,46,47,49,52,53]
- Q2: **39/53**;**QSM:73%**; missing [8,9,10,15,16,19,23,24,25,28,30,31,35,53]
- Q3: **30/53**;**QSM:56%**; missing [2,3,5,9,10,11,13,15,16,19,22,23,24,25,26,27,28,29,30,31,33,34,53]
- Q4: **45/53**;**QSM:85%**; missing [15,16,24,25,28,30,31,53]
- Q5: **45/53**;**QSM:85%**; missing [15,16,24,25,28,30,31,53]
------------------------------------------------------------------------------------------------