---
permalink: /
title: "About"
excerpt: "Tao Xiao is an Assistant Professor at Kyushu University researching AI for Software Engineering, Mining Software Repositories, CI/CD, and Code Review."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am an Assistant Professor at Kyushu University, Japan, and a member of the [POSL (Principles of Software Engineering and Programming Languages) Lab](https://posl.ait.kyushu-u.ac.jp/en/).

My research focuses on AI-assisted software engineering, particularly how large language models can support code review, software repository analysis, and continuous integration and deployment.

## Research Interests

{% for interest in site.data.cv.interests.en %}
* **{{ interest.title }}:** {{ interest.desc }}
{% endfor %}

## Selected Publications

{% for post in site.publications reversed %}
  {% if post.selected %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

[View all publications]({{ "/publications/" | relative_url }})

## Education Background

{% for edu in site.data.cv.education.en %}
* {{ edu.degree }}, {{ edu.institution }}, {{ edu.year }}
{% endfor %}

## Contact

For inquiries, please contact me at:

```
xiao[AT]ait[DOT]kyushu-u[DOT]ac[DOT]jp
```
