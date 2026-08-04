---
title: "Quantifying and Characterizing Clones of Self-Admitted Technical Debt in Build Systems"
collection: publications
permalink: /publication/satd-clones
venue: "Empirical Software Engineering (ESE)"
paperurl: "https://arxiv.org/pdf/2402.08920.pdf"
abstract: "Self-Admitted Technical Debt (SATD) annotates development decisions that intentionally exchange long-term software artifact quality for short-term goals. Recent work explores the existence of SATD clones (duplicate or near duplicate SATD comments) in source code. Cloning of SATD in build systems (e.g., CMake and Maven) may propagate suboptimal design choices, threatening qualities of the build system that stakeholders rely upon (e.g., maintainability, reliability, repeatability). Hence, we conduct a large-scale study on 50,608 SATD comments extracted from Autotools, CMake, Maven, and Ant build systems to investigate the prevalence of SATD clones and to characterize their incidences. We observe that: (i) prior work suggests that 41–65% of SATD comments in source code are clones, but in our studied build system context, the rates range from 62% to 95%, suggesting that SATD clones are a more prevalent phenomenon in build systems than in source code; (ii) statements surrounding SATD clones are highly similar, with 76% of occurrences having similarity scores greater than 0.8; (iii) a quarter of SATD clones are introduced by the author of the original SATD statements; and (iv) among the most commonly cloned SATD comments, external factors (e.g., platform and tool configuration) are the most frequent locations, limitations in tools and libraries are the most frequent causes, and developers often copy SATD comments that describe issues to be fixed later. Our work presents the first step toward systematically understanding SATD clones in build systems and opens up avenues for future work, such as distinguishing different SATD clone behavior, as well as designing an automated recommendation system for repaying SATD effectively based on resolved clones."
year: 2024
uploaded_at: "2024-02-01"
is_full_paper: true
is_first_author: true
is_corresponding_author: true
authors:
  - name: "Tao Xiao"
  - name: "Zhili Zeng"
  - name: "Dong Wang"
  - name: "Hideaki Hata"
  - name: "Shane McIntosh"
  - name: "Kenichi Matsumoto"
---
