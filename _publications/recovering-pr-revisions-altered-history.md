---
title: "Recovering Revisions of Pull Requests with Altered History"
collection: publications
permalink: /publication/recovering-pr-revisions-altered-history
venue: "The 41st IEEE/ACM International Conference on Automated Software Engineering (ASE)"
paperurl: "https://rebels.cs.uwaterloo.ca/papers/ase2026_sun.pdf"
year: 2026
uploaded_at: "2026-08-04"
is_full_paper: true
is_first_author: false
is_corresponding_author: false
authors:
  - name: "Gengyi Sun"
  - name: "Georges Aaron Randrianaina"
  - name: "Tao Xiao"
  - name: "Yasutaka Kamei"
  - name: "Shane McIntosh"
abstract: "In pull-based development, Pull Requests (PRs) undergo peer review. To address review feedback, authors may force-push after amending, squashing, or rebasing commits. Such revisions can conflate PR-specific changes with updates on the base branch, hindering further review and introducing noise into PR-based datasets. In this paper, we empirically study 935,011 PRs from 1,445 well-maintained GitHub projects. We observe 568,218 force-push events in 242,624 PRs that span 1,366 projects. We denote the HEAD commits of the PR before and after force-pushing as a force-push pair, and observe that 210,837 pairs (37.1%) have a relationship that conflates PR changes with updates to the base branch. To systematically isolate PR-specific changes in such revisions, we propose AntiDiffamine - an ancestry-based approach that aligns commits on a common reference. AntiDiffamine can automatically deconflate 98.1% of the studied revisions, decreasing the diff size by one to three orders of magnitude. We also evaluate AntiDiffamine on fail-fix pairs, i.e., revisions that fix failing builds. A case study of Kubernetes reveals that 130 of 523 pairs have conflated diffs. Moreover, the fixing files identified when AntiDiffamine is applied overlap more with a human-labelled ground truth than when conflation is untreated or excluded. AntiDiffamine is a first attempt at addressing force-push-based diff conflation, which is having a real-world impact on practical and research workflows. To ease practical adoption, we provide a template GitHub Action, which scans PR updates for force-push events and applies AntiDiffamine to deconflate the diff."
---
