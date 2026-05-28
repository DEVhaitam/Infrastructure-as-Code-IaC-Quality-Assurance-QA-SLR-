# Gold set creation and query validation

## Gold set construction:
We construct a gold set of 25 papers drawn from two independent sources:
- (A) Papers cited as foundational in prior IaC QA reviews (Chiari et al. 2022, Reddy Konala et al. 2023) — independent of our query because they were selected by other authors.
- (B) Academic expertise, by looking aspects that were missed in the previous surveys(not considering the dynamic aspect of IaC, or not covering the full IaC layers), as well as external checks about IaC QA.

### From close related surveys: 16 References

- [1] A. Rahman, C. Parnin, and L. A. Williams, “The seven sins: security smells in infrastructure as code scripts,” in Proc. 41st Int. Conf. Softw. Eng., ICSE’19. IEEE/ACM, 2019, pp. 164–175. **cited by 306**
- [2] T. Sharma, M. Fragkoulis, and D. Spinellis, “Does your configuration code smell?” in Proc. 13th Int. Conf. Mining Softw. Repositories, MSR’16. ACM, 2016, pp. 189–200. **cited by 235**
- [3] A. Rahman, M. R. Rahman, C. Parnin, and L. A. Williams, “Security smells in ansible and chef scripts: A replication study,” ACM Trans. Softw. Eng. Methodol., vol. 30, no. 1, pp. 3:1–3:31, 2021. **cited by 115**
- [4] S. Dalla Palma, D. Di Nucci, F. Palomba, and D. A. Tamburri, “Within-project defect prediction of infrastructure-as-code using product and process metrics,” IEEE Trans. Softw. Eng., pp. 1–1, 2021, to appear. [Online]. Available: https://doi.org/10.1109/TSE.2021.3051492 **cited by 113**
- [5] R. Shambaugh, A. Weiss, and A. Guha, “Rehearsal: a configuration verification tool for puppet,” in Proc. 37th ACM SIGPLAN Conf. Program. Lang. Des. Impl., PLDI’16. ACM, 2016, pp. 416–430. **cited by 109**
- [6] J. Schwarz, A. Steffens, and H. Lichter, “Code smells in infrastructure as code,” in Proc. 11th Int. Conf. Qual. Inf. Commun. Technol., QUATIC’18. IEEE Comp. Soc., 2018, pp. 220–228. **cited by 91**
- [7] A. Rahman, E. Farhana, C. Parnin, and L. A. Williams, “Gang of eight: a defect taxonomy for infrastructure as code scripts,” in Proc. 42nd Int. Conf. Softw. Eng., ICSE’20. ACM, 2020, pp. 752–764. **cited by 88**
- [8] A. Rahman and L. A. Williams, “Characterizing defective configuration scripts used for continuous deployment,” in Proc. 11th IEEE Int. Conf. Softw. Testing, Verification Validation, ICST’18. IEEE Comp. Soc., 2018, pp. 34–45. **cited by 76**
- [9] A. Rahman and L. A. Williams, “Source code properties of defective infrastructure as code scripts,” Inf. Softw. Technol., vol. 112, pp. 148– 163, 2019. **cited by 75**
- [10] N. Saavedra and J. F. Ferreira, “Glitch: Automated polyglot security smell detection in infrastructure as code,” 2022. [Online]. Available: https://arxiv.org/abs/2205.14371 **cited by 49**
- [11] I. Kumara, Z. Vasileiou, G. Meditskos, D. A. Tamburri, W. van den Heuvel, A. Karakostas, S. Vrochidis, and I. Kompatsiaris, “Towards semantic detection of smells in cloud infrastructure code,” in Proc. 10th Int. Conf. Web Intell., Mining and Semantics, WIMS’20. ACM, 2020, pp. 63–67. **cited by 39**
- [12] J. Lepiller, R. Piskac, M. Sch ̈af, and M. Santolucito, “Analyzing infrastructure as code to prevent intra-update sniping vulnerabilities,” in Proc. 27th Int. Conf. Tools Alg. for the Constr. and Anal. of Syst., TACAS’21, Part II, ser. LNCS, vol. 12652. Springer, 2021, pp. 105–123. **cited by 39**
- [13] N. Borovits, I. Kumara, P. Krishnan, S. D. Palma, D. D. Nucci, F. Palomba, D. A. Tamburri, and W. van den Heuvel, “DeepIaC: deep learning-based linguistic anti-pattern detection in IaC,” in Proc. 4th Int. Workshop Mach. Learn. Techn. Softw. Qual. Eval., MaLTeSQuE’20. ACM, 2020, pp. 7–12. **cited by 37**
- [14] T. Dai, A. A. Karve, G. Koper, and S. Zeng, “Automatically detecting risky scripts in infrastructure code,” in Proc. ACM Symp. Cloud Comput., SoCC’20. ACM, 2020, pp. 358–371. **cited by 31**
- [15] M. M. Hassan and A. Rahman, “As code testing: Characterizing test quality in open source ansible development,” in 2022 IEEE Conference on Software Testing, Verification and Validation (ICST), 2022, pp. 208–219. **cited by 29**
- [16] A. Brogi, A. Di Tommaso, and J. Soldani, “Sommelier: A tool for validating TOSCA application topologies,” in Proc. 5th Int. Conf. ModelDriven Eng. and Softw. Develop., MODELSWARD’17, ser. Commun. Comput. Inf. Sci., vol. 880. Springer, 2017, pp. 1–22. **cited by 26**

### From academic IaC expertise: 9 References
- [17] Akond Rahman, Shazibul Islam Shamim, Dibyendu Brinto Bose, and Rahul Pandita. 2023. "Security Misconfigurations in Open Source Kubernetes Manifests: An Empirical Study". **cited by 147**
- [18] Jiang, Yujuan, and Bram Adams. "Co-evolution of infrastructure and source code-an empirical study." 2015 IEEE/ACM 12th Working Conference on Mining Software Repositories. IEEE, 2015. **cited by 131**
- [19] Dalla Palma, Stefano, et al. "Toward a catalog of software quality metrics for infrastructure code." Journal of Systems and Software 170 (2020): 110726. **cited by 100**
- [20]Van der Bent, Eduard, et al. "How good is your puppet? an empirically defined and validated quality model for puppet." 2018 IEEE 25th international conference on software analysis, evolution and reengineering (SANER). IEEE, 2018. **cited by 68**
- [21] Opdebeeck, Ruben, Ahmed Zerouali, and Coen De Roover. "Control and data flow in security smell detection for infrastructure as code: Is it worth the effort?." 2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR). IEEE, 2023. **cited by 47**
- [22] R. Opdebeeck, A. Zerouali, C. De Roover, “Smelly variables in Ansible infrastructure code: Detection, prevalence, and lifetime”. Proceedings of the 19th International Conference on Mining Software Repositories. pp. 61-72. **cited by 44**
- [23] D. Sokolowski, D. Spielmann, G. Salvaneschi, “Automated infrastructure as code program testing”. 2024. IEEE Transactions on Software Engineering. **cited by 32**
- [24] Sokolowski, Daniel. "Infrastructure as code for dynamic deployments." Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering. 2022. **cited by 29**
- [25] Rahman, Akond. "Characteristics of defective infrastructure as code scripts in devops." Proceedings of the 40th International Conference on Software Engineering: Companion Proceeedings. 2018. **cited by 29**


## Evaluating the search queries:

In the following, we refer several queries to score with our gold set. 
- Q1: Quality improvement centric:  *(“Infrastructure as Code” OR “IaC”) AND (“Quality assurance” or “Testing” OR “Verification” OR “linting” OR “Static Analysis” OR “Dynamic analysis”)*
- Q2: Issue centric:  *("Infrastructure as Code" OR "IaC") AND ("defects" OR "errors" OR "anti-patterns" OR "vulnerabilities" OR "code smells" OR "Quality issues" OR "bad practices" OR "Misconfiguration")*
- Q3: Survey oriented:  *("Infrastructure as Code" OR "IaC") AND ("taxonomy" OR "classification" OR "Categorization" OR "Survey")*
- Q4: Full merge (Q1+Q2): *("Infrastructure as Code" OR "IaC") AND ("defect" OR "bug" OR "smell" OR "anti-pattern" OR "vulnerability" OR "misconfiguration" OR "bad practice" OR "error" OR "fault" OR "testing" OR "analysis" OR "verification" OR "linting" OR "quality assurance" OR "static analysis" OR "validation")*
- Q5: SLR query:    *("Infrastructure as Code" OR "IaC") AND ("defect" OR "bug" OR "smell" OR "anti-pattern" OR "testing" OR "analysis" OR " verification")*

We excuted the search query across the 4 different databases, we got the following numbers:
- Q1 retrieved **5974** references
- Q2 retrieved **2304** references
- Q3 retrieved **1990** references
- Q4 retrieved **4361** references
- Q5 retrieved **2821** references

We used the scripts/check_goldset.py script to evaluate the different search queries against the gold set, and we got:
- Q1: **18/25**; missing [4,5,9,11,13,16,20]
- Q2: **19/25**; missing [5,11,15,16,20,23]
- Q3: **12/25**; missing [1,2,4,5,6,8,11,12,15,16,20,21,23]
- Q4: **21/25**; missing [5,11,16,20]
- QF: **21/25** ; missing [5,11,16,20]
------------------------------------------------------------------------------------------------
