---
permalink: /
title: "About"
title_zh: "个人简介"
excerpt: "Tao Xiao is an Assistant Professor at Kyushu University researching AI for Software Engineering, Mining Software Repositories, CI/CD, and Code Review."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="i18n-en" lang="en" markdown="1">

I am an Assistant Professor at Kyushu University, Japan, and a member of the [POSL (Principles of Software Engineering and Programming Languages) Lab](https://posl.ait.kyushu-u.ac.jp/en/).

My research focuses on AI-assisted software engineering, particularly how large language models can support code review, software repository analysis, and continuous integration and deployment.

</div>
<div class="i18n-zh" lang="zh" markdown="1">

我是日本九州大学助理教授，隶属于 [POSL（软件工程与编程语言原理）实验室](https://posl.ait.kyushu-u.ac.jp/en/)。

我的研究方向是 AI 辅助软件工程，重点关注大语言模型如何支持代码审查、软件仓库分析以及持续集成与交付。

</div>

## {% include i18n.html key="research_interests" %}

<div class="i18n-en" lang="en" markdown="1">
{% for interest in site.data.cv.interests.en %}
* **{{ interest.title }}:** {{ interest.desc }}
{% endfor %}
</div>
<div class="i18n-zh" lang="zh" markdown="1">
{% for interest in site.data.cv.interests.zh %}
* **{{ interest.title }}：** {{ interest.desc }}
{% endfor %}
</div>

## {% include i18n.html key="selected_publications" %}

{% assign sorted_publications = site.publications | sort: "uploaded_at" | reverse %}
{% for post in sorted_publications %}
  {% if post.selected %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

[{% include i18n.html key="view_all_publications" %}]({{ "/publications/" | relative_url }})

## {% include i18n.html key="education" %}

<div class="i18n-en" lang="en" markdown="1">
{% for edu in site.data.cv.education.en %}
* {{ edu.degree }}, {{ edu.institution }}, {{ edu.year }}
{% endfor %}
</div>
<div class="i18n-zh" lang="zh" markdown="1">
{% for edu in site.data.cv.education.zh %}
* {{ edu.degree }}，{{ edu.institution }}，{{ edu.year }}
{% endfor %}
</div>

## {% include i18n.html key="contact" %}

{% include i18n.html key="contact_text" %}

```
xiao[AT]ait[DOT]kyushu-u[DOT]ac[DOT]jp
```
