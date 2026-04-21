This file contains the list of intermediate values for classifying the quality issues and the supprot techniques.

## Quality issues:
1. **Structural Quality**
    
    **Definition:**
    Issues related to the overall architecture, organization, and modular design of IaC code. This category encompasses how well the code is structured in terms of abstraction levels, component relationships, and architectural patterns.
    
    **Scope:**
    Covers abstraction mechanisms, modularity principles, code organization patterns, and architectural anti-patterns that affect the maintainability and comprehensibility of infrastructure definitions.
    1. 1. Abstraction Issues:
    - Multifaceted abstraction
    - Unnecessary abstraction
    - Imperative abstraction
    - Missing abstraction

    1. 2. Modularity & Organization
    - Insufficient modularization
    - Broken hierarchy
    - Unstructured module
    - Weakened modularity
    - Deficient encapsulation
    - Monolithic infrastructur
    
    1. 3. Code Structure
    - Dense structure
    - Long statement/resource
    - Complex expression (from a structral POV)
    - Depth of nested blocks
    - Dynamic blocks
2. **Syntactic & Linguistic Quality**
    
    **Definition:** 
    Issues related to the proper use of language constructs, syntax correctness, naming conventions, and linguistic consistency within IaC scripts. This category focuses on the correctness and readability of the code.
    
    **Scope:**
    Includes syntax errors, formatting inconsistencies, naming convention violations, and language-specific construct misuse that can be detected through lexical and syntactic analysis.
    
    2. 1. Naming & Conventions
    - Inconsistent naming convention
    - Linguistic anti-pattern (name-body inconsistency)
    2. 2. Syntax & Formatting
    - Improper alignment
    - Improper quote usage
    - YAML syntax issues
    - Quoting issues
    - Misplaced attribute
    2. 3. Language Constructs
    - Invalid property value
    - Deprecated statement/keywords/modules
    - Incomplete tasks/conditional (missing blocks, statements like then, if…)
    - Missing default case
3. **Security**
    
    **Definition:** Vulnerabilities, weaknesses, and security anti-patterns that could lead to unauthorized access, data breaches, or compromised infrastructure. This category addresses security-critical aspects of infrastructure configuration.
    
    **Scope:** Encompasses authentication flaws, authorization issues, secret management problems, network security misconfigurations, and cryptographic weaknesses detectable in IaC code.
    
    3. 1. **Authentication & Authorization**
    - Admin by default
    - Empty password
    - Insufficient access control
    - RBAC violations
    - Unnecessary privileges
    3. 2. **Secrets Management**
    - Hard-coded secrets
    - Hard-coded values
    - Compromised sensitive data
    - Hardcoded secrets in containers
    3. 3. **Network Security**
    - Invalid IP address binding
    - Unrestricted IP address
    - Use of HTTP without TLS/SSL
    - Unencrypted pod-to-pod traffic
    - Exposed services
    3. 4. **Cryptography & Integrity**
    - Use of weak cryptography algorithms
    - No integrity check
    - Suspicious comments

4. **Operational Quality**
**Definition:** Issues affecting the reliability, consistency, and predictable behavior of infrastructure deployment and management. This category focuses on operational aspects that impact system stability and repeatability.
**Scope:** Covers idempotency violations, state management issues, error handling, and dependency-related problems that affect operational reliability.
    
    4. 1. **Idempotency & State Management**
    - Non-idempotence
    - State management issues
    - Configuration drift
    - Unconditional override
    4. 2. **Error Handling & Reliability**
    - Missing error handling
    - Silent failure
    - Non-deterministic errors
    - Incomplete tasks (failures that can happen in run time)
    4. 3. **Dependencies & Integration**
    - Over-constrained dependencies
    - Dependency management
    - Integration issues
    - Module execution failures
    - Service connections
    - API interactions
    - External module integration
    - Inter-component communication
    4. 4. **Network**

5. **Performance & Resource Management**

    **Definition:** Issues related to inefficient resource utilization, scalability limitations, and performance bottlenecks in infrastructure configurations. This category addresses cost optimization and system performance aspects.

    **Scope:** Includes resource over-provisioning, scaling misconfigurations, lifecycle management issues, and performance anti-patterns that lead to inefficient resource usage.
    
    5. 1. **Resource Optimization**
    - Over-provisioning resources
    - Expensive instance/storage types
    - Missing resource limits/requests
    - Unoptimized data transfers
    5. 2. **Scalability**
    - Lack of auto-scaling
    - Performance bottlenecks
    - Inventory management issues
    5. 3. **Lifecycle Management**
    - Ignoring resource lifecycles
    - Object storage lifecycle rules
    - Spot instances management

6. **Maintainability & Documentation**

    **Definition:** Issues that hinder code maintenance, evolution, and knowledge transfer. This category focuses on factors that affect the long-term sustainability and collaborative development of IaC projects.

    **Scope:** Encompasses documentation quality, code readability, version control practices, compatibility management, and code reusability patterns.
   
    6. 1. **Code Readability**
    - Poor documentation
    - Inconsistent formatting
    - Complex expressions (from human comprehension POV)
    - Too many variables
    6. 2. **Version Control & Compatibility**
    - Version control issues
    - Compatibility problems
    - Deprecation handling
    - Ansible versions conflicts
    6. 3. **Code Reusability**
    - Code duplication
    - Unnecessary operations (set_fact, include_vars)
    - Violation of DRY principle

7. **Data & Variable Management**
    
    **Definition:** Issues related to the handling, organization, and management of data values, variables, and parameters within IaC scripts. This category addresses how data is defined, stored, accessed, and utilized throughout the infrastructure definition.
    
    **Scope:** Covers data handling patterns, variable management practices, parameter passing, conditional logic, and the proper separation of data from code logic.
    
    7. 1. **Configuration Data**
    - Hardcoded values (or security)
    - Separation of config from code
    7. 2. **Variable Management**
    - Unguarded variables
    - Undefined variables
    - Variable scope issues
    7. 3. **Template handling**
    - Template handling

8. **Control Flow & Logic**
    
    **Definition:** Issues related to the logical structure, program flow, and functional correctness of IaC scripts. This category focuses on the algorithmic and logical aspects of infrastructure definitions.
    
    **Scope:** Includes control flow patterns, function usage, logical operations, and integration logic that can be statically analyzed for correctness and best practices.
    
    8. 1. **Program Flow**
    - Control flow issues
    - Conditional execution logic
    - Loop constructs
    - Execution dependencies
    8. 2. **Function & Method Logic**
    - Deprecated functions
    - Function call patterns
    - Lookup operations
    - Function parameter handling

9. **Domain-Specific Issues**
    
    **Definition:** Issues specific to particular infrastructure domains, cloud providers, or technology stacks. This category captures specialized knowledge and best practices for specific IaC contexts.
    
    **Scope:** Encompasses container orchestration issues, cloud provider-specific anti-patterns, and technology-specific configuration problems that require domain expertise to identify.
    
    9. 1. **Container & Orchestration**
    - Improper pod security contexts
    - Container image specifications
    - Kubernetes networking policies
    - Probes and health checks
    9. 2. **Cloud Provider Specific**
    - AWS-specific antipatterns
    - Expensive cloud resources
    - Cloud service misconfigurations
    9. 3. **Infrastructure Components**
    - Load balancer setup
    - Networking configurations
    - Serverless configurations
    - Storage configurations

## Techniques:
Some techniques instances that we used for classifying the support techniques used in the literrature:
1. **Rule-Based and Pattern-Matching Approaches**
- Regular Expressions - RegX
- Rule-based checks
- Pattern Matching
- Pattern Algorithms
- Visitor Pattern
2. **Graph-Based Analyses**
- AST Traversal
- Control Flow Graph
- Data Dependecy Graph - DDG
- Program Dependncy Graph - PDG
- Resource Graph - RG
3. **Formal Methods**
- SMT solvers
4. **Statistical and Learning-Based Methods**
- Machine Learning - ML
- Statistical Learners
- Deep Learning - DL
- LLMs
- RAG
- NLP
5. **Testing Methods**
- Tests