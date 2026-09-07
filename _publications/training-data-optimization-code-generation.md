---
title: "On the Effectiveness of Training Data Optimization for LLM-based Code Generation: An Empirical Study"
collection: publications
permalink: /publication/training-data-optimization-code-generation
venue: "ACM Transactions on Software Engineering and Methodology (TOSEM)"
paperurl: "https://dl.acm.org/doi/10.1145/3844732"
year: 2026
uploaded_at: "2026-09-06"
is_full_paper: true
is_first_author: false
is_corresponding_author: false
authors:
  - name: "Shiqi Kuang"
  - name: "Zhao Tian"
  - name: "Tao Xiao"
  - name: "Dong Wang"
  - name: "Junjie Chen"
abstract: "Large language models (LLMs) have achieved remarkable progress in code generation, largely driven by the availability of high-quality code datasets for effective training. To further improve data quality, numerous training data optimization techniques have been proposed; however, their overall effectiveness has not been systematically evaluated. To bridge this gap, we conduct the first large-scale empirical study, examining five widely-used training data optimization techniques and their pairwise combinations for LLM-based code generation across three benchmarks and four LLMs. Our results show that data synthesis is the most effective technique for improving functional correctness and reducing code smells, although it performs relatively worse on code maintainability compared to data refactoring, cleaning, and selection. Regarding combinations, we find that most combinations do not further improve functional correctness but can effectively enhance code quality (code smells and maintainability). Among all combinations, data synthesis combined with data refactoring achieves the strongest overall performance. Furthermore, our fine-grained analysis reinforces these findings and provides deeper insights into how individual techniques and their combinations influence code generation effectiveness. Overall, this work represents a first step toward a systematic understanding of training data optimization and combination strategies, offering practical guidance for future research and deployment in LLM-based code generation."
---
