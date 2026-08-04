---
title: "ThinkLog: Leveraging Reasoning for Log Statement Generation"
collection: publications
permalink: /publication/thinklog-leveraging-reasoning
venue: "The 26th International Conference on Software Quality, Reliability, and Security (QRS)"
track: "Short Paper"
paperurl: "https://arxiv.org/pdf/2607.11615"
year: 2026
uploaded_at: "2026-06-02"
is_full_paper: false
is_first_author: false
is_corresponding_author: false
authors:
  - name: "Kazuki Kusama"
  - name: "Honglin Shu"
  - name: "Masanari Kondo"
  - name: "Tao Xiao"
  - name: "Yasutaka Kamei"
abstract: "Runtime logs are an important source of information that supports software maintenance. To obtain useful logs, developers spend significant effort identifying appropriate log locations, assigning correct severity levels, and writing concise yet informative messages. Therefore, end-to-end automated log statement generation can help reduce this burden, and prior work has proposed many methods for this task. However, existing methods still exhibit limited accuracy. To address this problem, we propose ThinkLog, an LLM-based end-to-end log statement generation method. The core idea of ThinkLog is to incorporate reasoning that helps LLMs make decisions about log insertion, severity level assignment, and message generation, thereby improving log statement generation accuracy. ThinkLog injects reasoning into prompts as few-shot examples and guides LLMs to generate appropriate log statements. Evaluated on 9,619 Java methods extracted from public GitHub repositories, ThinkLog achieves 20.55% log statement generation accuracy, representing a 15.4% improvement over the best existing method. Moreover, these improvements were achieved at approximately 50% of the inference cost (USD) compared to the best existing method. These results show that leveraging reasoning is an effective and cost-efficient way to improve the accuracy of end-to-end log statement generation."
---
