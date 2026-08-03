---
title: "A Mutation-Guided Assessment of Acceleration Approaches for Continuous Integration: An Empirical Study of Yourbase"
collection: publications
permalink: /publication/mutation-guided-ci
venue: "21st IEEE International Conference on Mining Software Repositories (MSR)"
paperurl: "https://rebels.cs.uwaterloo.ca/papers/msr2024_zeng.pdf"
abstract: "Continuous Integration (CI) is a popular software development practice that quickly verifies updates to codebases. To cope with the ever-increasing demand for faster software releases, CI acceleration approaches have been proposed; however, adoption of CI acceleration is not without risks. For example, CI acceleration products may mislabel change sets (e.g., a build labeled as failing that passes in an unaccelerated setting or vice versa) or produce results that are inconsistent with an unaccelerated build (e.g., the underlying reasons for failure differ between (un)accelerated builds). These inconsistencies threaten the trustworthiness of CI acceleration products. In this paper, we propose an approach inspired by mutation testing to systematically evaluate the trustworthiness of CI acceleration. We apply our approach to YourBase, a program analysis-based CI acceleration product, and uncover issues that hinder its trustworthiness. First, we study how often the same build in accelerated and unaccelerated CI settings produce different mutation testing outcomes. We call mutants with different outcomes in the two settings “gap mutants”. Next, we study the code locations where gap mutants appear. Finally, we inspect gap mutants to understand why acceleration causes them to survive. Our analysis of ten open-source projects uncovers 2,237 gap mutants. We find that: (1) the gap mutants account for 0.11%–23.50% of the studied mutants; (2) 88.95% of gap mutants can be mapped to specific source code functions and classes using the dependency representation of the studied CI acceleration product; and (3) 69% of gap mutants survive CI acceleration due to deterministic reasons that can be classified into six fault patterns. Our results show that even deterministic CI acceleration solutions suffer from trustworthiness limitations, and highlight the ways in which trustworthiness could be pragmatically improved."
year: 2024
is_full_paper: true
is_first_author: false
is_corresponding_author: false
authors:
  - name: "Zhili Zeng"
  - name: "Tao Xiao"
  - name: "Maxime Lamothe"
  - name: "Hideaki Hata"
  - name: "Shane McIntosh"
---
