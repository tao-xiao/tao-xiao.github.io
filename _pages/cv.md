---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Education

{% for edu in site.data.cv.education.en %}
* {{ edu.degree }}, {{ edu.institution }}, {{ edu.year }}
{% endfor %}

## Work Experience

{% for exp in site.data.cv.experience.en %}
* {{ exp.period }}: {{ exp.role }}
  * {{ exp.institution }}
  {% if exp.details %}* {{ exp.details }}{% endif %}
{% endfor %}

## Publications

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
