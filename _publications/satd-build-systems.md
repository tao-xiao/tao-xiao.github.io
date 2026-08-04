---
title: "Characterizing and Mitigating Self-Admitted Technical Debt in Build Systems"
collection: publications
permalink: /publication/satd-build-systems
venue: "IEEE Transactions on Software Engineering (TSE)"
paperurl: "http://tao-xiao.github.io/files/SATD_TSE_2021.pdf"
abstract: "Technical Debt is a metaphor used to describe the situation in which long-term software artifact quality is traded for short-term goals in software projects. In recent years, the concept of self-admitted technical debt (SATD) was proposed, which focuses on debt that is intentionally introduced and described by developers. Although prior work has made important observations about admitted technical debt in source code, little is known about SATD in build systems. In this paper, we set out to better understand the characteristics of SATD in build systems. To do so, through a qualitative analysis of 500 SATD comments in the Maven build system of 291 projects, we characterize SATD by location and rationale (reason and purpose). Our results show that limitations in tools and libraries, and complexities of dependency management are the most frequent causes, accounting for 50% and 24% of the comments. We also find that developers often document SATD as issues to be fixed later. As a first step towards the automatic detection of SATD rationale, we train classifiers to detect the two most frequently occurring reasons and the four most frequently occurring purposes of SATD in the content of comments in Maven build systems. The classifier performance is promising, achieving an F1-score of 0.71–0.79. Finally, within 16 identified ‘ready-to-be-addressed’ SATD instances, the three SATD submitted by pull requests and the five SATD submitted by issue reports were resolved after developers were made aware. Our work presents the first step towards understanding technical debt in build systems and opens up avenues for future work, such as tool support to track and manage SATD backlogs."
year: 2021
uploaded_at: "2021-12-01"
is_full_paper: true
is_first_author: true
is_corresponding_author: true
authors:
  - name: "Tao Xiao"
  - name: "Dong Wang"
  - name: "Shane Mcintosh"
  - name: "Hideaki Hata"
  - name: "Raula Gaikovina Kula"
  - name: "Takashi Ishio"
  - name: "Kenichi Matsumoto"
---
