# Make a gold set

In the following, we refer several queries to score with our gold set. 
- SLR query:    *("Infrastructure as Code" OR "IaC") AND ("defect" OR "bug" OR "smell" OR "anti-pattern" OR "testing" OR "analysis" OR " verification")*
- 1st version:  *Quality improvement queries (e.g., ("Infrastructure as Code" OR "IaC") AND ("quality assurance" OR "testing" OR "verification" OR "linting"))*
- 2nd version:  *Issue-centric queries (e.g., ("Infrastructure as Code" OR "IaC") AND ("defects" OR "vulnerabilities" OR "misconfiguration" OR "bad practices" OR "errors" OR "antipatterns" OR "code smells"))*
- 3rd version:  *Survey-oriented queries (e.g., ("Infrastructure as Code" OR "IaC") AND ("survey" OR "taxonomy" OR "classification"))*
SLR final refers to the set of 70 final papers present in our SLR

## From close related surveys

### 21 References

[1] A. Rahman, C. Parnin, and L. A. Williams, “The seven sins: security smells in infrastructure as code scripts,” in Proc. 41st Int. Conf. Softw. Eng., ICSE’19. IEEE/ACM, 2019, pp. 164–175. **cited by 306**
[2] T. Sharma, M. Fragkoulis, and D. Spinellis, “Does your configuration code smell?” in Proc. 13th Int. Conf. Mining Softw. Repositories, MSR’16. ACM, 2016, pp. 189–200. **cited by 235**
[3] A. Rahman, M. R. Rahman, C. Parnin, and L. A. Williams, “Security smells in ansible and chef scripts: A replication study,” ACM Trans. Softw. Eng. Methodol., vol. 30, no. 1, pp. 3:1–3:31, 2021. **cited by 115**
[4] S. Dalla Palma, D. Di Nucci, F. Palomba, and D. A. Tamburri, “Within-project defect prediction of infrastructure-as-code using product and process metrics,” IEEE Trans. Softw. Eng., pp. 1–1, 2021, to appear. [Online]. Available: https://doi.org/10.1109/TSE.2021.3051492 **cited by 113**
[5] R. Shambaugh, A. Weiss, and A. Guha, “Rehearsal: a configuration verification tool for puppet,” in Proc. 37th ACM SIGPLAN Conf. Program. Lang. Des. Impl., PLDI’16. ACM, 2016, pp. 416–430. **cited by 109**
[6] J. Schwarz, A. Steffens, and H. Lichter, “Code smells in infrastructure as code,” in Proc. 11th Int. Conf. Qual. Inf. Commun. Technol., QUATIC’18. IEEE Comp. Soc., 2018, pp. 220–228. **cited by 91**
[7] A. Rahman, E. Farhana, C. Parnin, and L. A. Williams, “Gang of eight: a defect taxonomy for infrastructure as code scripts,” in Proc. 42nd Int. Conf. Softw. Eng., ICSE’20. ACM, 2020, pp. 752–764. **cited by 88**
[8] K. Jayaraman, N. Bjørner, G. Outhred, and C. Kaufman, “Automated analysis and debugging of network connectivity policies,” Microsoft, Tech. Rep. MSR-TR-2014-102, 2014. [Online]. Available: https://www.microsoft.com/en-us/research/publication/automated-analysis-and-debugging-of-network-connectivity-policies/ **cited by 86**
[9] A. Rahman and L. A. Williams, “Characterizing defective configuration scripts used for continuous deployment,” in Proc. 11th IEEE Int. Conf. Softw. Testing, Verification Validation, ICST’18. IEEE Comp. Soc., 2018, pp. 34–45. **cited by 76**
[10] A. Rahman and L. A. Williams, “Source code properties of defective infrastructure as code scripts,” Inf. Softw. Technol., vol. 112, pp. 148– 163, 2019. **cited by 75**
[11] N. Saavedra and J. F. Ferreira, “Glitch: Automated polyglot security smell detection in infrastructure as code,” 2022. [Online]. Available: https://arxiv.org/abs/2205.14371 **cited by 49**
[12] A. Brogi, A. Canciani, and J. Soldani, “Modelling and analysing cloud application management,” in Service Oriented and Cloud Computing, S. Dustdar, F. Leymann, and M. Villari, Eds. Cham: Springer International Publishing, 2015, pp. 19–33. **cited by 40**
[13] I. Kumara, Z. Vasileiou, G. Meditskos, D. A. Tamburri, W. van den Heuvel, A. Karakostas, S. Vrochidis, and I. Kompatsiaris, “Towards semantic detection of smells in cloud infrastructure code,” in Proc. 10th Int. Conf. Web Intell., Mining and Semantics, WIMS’20. ACM, 2020, pp. 63–67. **cited by 39**
[14] J. Lepiller, R. Piskac, M. Sch ̈af, and M. Santolucito, “Analyzing infrastructure as code to prevent intra-update sniping vulnerabilities,” in Proc. 27th Int. Conf. Tools Alg. for the Constr. and Anal. of Syst., TACAS’21, Part II, ser. LNCS, vol. 12652. Springer, 2021, pp. 105–123. **cited by 39**
[15] N. Borovits, I. Kumara, P. Krishnan, S. D. Palma, D. D. Nucci, F. Palomba, D. A. Tamburri, and W. van den Heuvel, “DeepIaC: deep learning-based linguistic anti-pattern detection in IaC,” in Proc. 4th Int. Workshop Mach. Learn. Techn. Softw. Qual. Eval., MaLTeSQuE’20. ACM, 2020, pp. 7–12. **cited by 37**
[16] T. Dai, A. A. Karve, G. Koper, and S. Zeng, “Automatically detecting risky scripts in infrastructure code,” in Proc. ACM Symp. Cloud Comput., SoCC’20. ACM, 2020, pp. 358–371. **cited by 31**
[17] M. M. Hassan and A. Rahman, “As code testing: Characterizing test quality in open source ansible development,” in 2022 IEEE Conference on Software Testing, Verification and Validation (ICST), 2022, pp. 208–219. **cited by 29**
[18] A. Brogi, A. Di Tommaso, and J. Soldani, “Sommelier: A tool for validating TOSCA application topologies,” in Proc. 5th Int. Conf. ModelDriven Eng. and Softw. Develop., MODELSWARD’17, ser. Commun. Comput. Inf. Sci., vol. 880. Springer, 2017, pp. 1–22. **cited by 26**
[19] W. Chareonsuk and W. Vatanawood, “Formal verification of cloud orchestration design with TOSCA and BPEL,” in Proc. 13th Int. Conf. Elect. Eng./Electron., Comput., Telecomm. Inf. Technol., ECTI-CON’16. IEEE, 2016, pp. 1–5. **cited by 16**
[20] H. Yoshida, K. Ogata, and K. Futatsugi, “Formalization and verification of declarative cloud orchestration,” in Proc. 17th Int. Conf. Formal Methods Softw. Eng., ICFEM’15, ser. LNCS, vol. 9407. Springer, 2015, pp. 33–49. **cited by 14**
[21] S. D. Palma, M. Mohammadi, D. D. Nucci, and D. A. Tamburri, “Singling the odd ones out: a novelty detection approach to find defects in infrastructure-as-code,” in Proc. 4th Int. Workshop Mach. Learn. Techn. Softw. Qual. Eval., MaLTeSQuE’20. ACM, 2020, pp. 31–36. **cited by 7**


### Score 

- SLR final:            14/21 ; missing [8,12,13,14,18,19,20] ; work cited with other reference: [9,11]
- SLR queries:          14/21; missing [8,12,13,14,18,19,20] 
- Query (1st version):  /21
- Query (2nd version):  /21
- Query (3rd version):  /21