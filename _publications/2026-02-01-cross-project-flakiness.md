---
title: "Cross-Project Flakiness: A Case Study of the OpenStack Ecosystem"
collection: publications
permalink: /publication/2026-02-01-cross-project-flakiness
venue: "IEEE Transactions on Software Engineering (TSE)"
paperurl: "https://arxiv.org/pdf/2602.09311"
abstract: "Automated regression testing is a cornerstone of modern software development, often contributing directly to code review and Continuous Integration (CI). Yet some tests suffer from flakiness, where their outcomes vary non-deterministically. Flakiness erodes developer trust in test results, wastes computational resources, and undermines CI reliability. While prior research has examined test flakiness within individual projects, its broader ecosystem-wide impact remains largely unexplored. In this paper, we present an empirical study of test flakiness in the OpenStack ecosystem, which focuses on (1) cross-project flakiness, where flaky tests impact multiple projects, and (2) inconsistent flakiness, where a test exhibits flakiness in some projects but remains stable in others. By analyzing 649 OpenStack projects, we identify 1,535 cross-project flaky tests and 1,105 inconsistently flaky tests. We find that cross-project flakiness affects 55% of OpenStack projects and significantly increases both review time and computational costs. Surprisingly, 70% of unit tests exhibit cross-project flakiness, challenging the assumption that unit tests are inherently insulated from issues that span modules like integration and system-level tests. Through qualitative analysis, we observe that race conditions in CI, inconsistent build configurations, and dependency mismatches are the primary causes of inconsistent flakiness. These findings underline the need for better coordination across complex ecosystems, standardized CI configurations, and improved test isolation strategies."
year: 2026
is_full_paper: true
is_first_author: true
is_corresponding_author: false
authors:
  - name: "Tao Xiao"
  - name: "Dong Wang"
  - name: "Shane McIntosh"
  - name: "Hideaki Hata"
  - name: "Yasutaka Kamei"
---

