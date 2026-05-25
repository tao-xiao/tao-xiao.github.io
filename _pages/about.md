---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hello and welcome to my website! I’m Tao Xiao, an Assistant Professor at Kyushu University, Japan. I’m part of the [POSL (Principles of Software engineering and programming Languages) Lab](https://posl.ait.kyushu-u.ac.jp/en/).

My research focuses on enhancing software development through both traditional methods and advanced technologies.

Research Interests
======
{% for interest in site.data.cv.interests.en %}
* **{{ interest.title }}:** {{ interest.desc }}
{% endfor %}

Education Background
======
{% for edu in site.data.cv.education.en %}
* {{ edu.degree }}, {{ edu.institution }}, {{ edu.year }}
{% endfor %}

For more info
------
More info, please contact me
```
xiao[AT]ait[DOT]kyushu-u[DOT]ac[DOT]jp
```
