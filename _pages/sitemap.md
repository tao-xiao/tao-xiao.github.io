---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of the pages and publications on this site. An [XML version]({{ base_path }}/sitemap.xml) is also available for search engines.

<h2>Pages</h2>
{% for post in site.pages %}
  {% if post.title %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2>Publications</h2>
{% assign sorted_publications = site.publications | sort: "uploaded_at" | reverse %}
{% for post in sorted_publications %}
  {% include archive-single.html %}
{% endfor %}
