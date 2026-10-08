---
layout: archive
title: "CV"
title_zh: "个人简历"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## {% include i18n.html key="education_short" %}

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

## {% include i18n.html key="work_experience" %}

<div class="i18n-en" lang="en" markdown="1">
{% for exp in site.data.cv.experience.en %}
* {{ exp.period }}: {{ exp.role }}
  * {{ exp.institution }}
  {% if exp.details %}* {{ exp.details }}{% endif %}
{% endfor %}
</div>
<div class="i18n-zh" lang="zh" markdown="1">
{% for exp in site.data.cv.experience.zh %}
* {{ exp.period }}：{{ exp.role }}
  * {{ exp.institution }}
  {% if exp.details %}* {{ exp.details }}{% endif %}
{% endfor %}
</div>

## {% include i18n.html key="publications" %}

  {% assign sorted_publications = site.publications | sort: "uploaded_at" | reverse %}
  <ul>{% for post in sorted_publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
