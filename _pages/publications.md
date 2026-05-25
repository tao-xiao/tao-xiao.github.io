---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% if site.author.googlescholar %}
  <p>You can also find my articles on <a href="{{ site.author.googlescholar }}">my Google Scholar profile</a>.</p>
{% endif %}

{% include base_path %}

{% comment %}
  Filter buttons logic
{% endcomment %}
<div class="filters">
  <strong>Filter by (multi-select):</strong>
  <br>
  <button class="btn filter-btn" data-filter="first">First Author</button>
  <button class="btn filter-btn" data-filter="corresponding">Corresponding Author</button>
  <button class="btn filter-btn" data-filter="full">Full Paper</button>
  
  <button class="btn filter-btn-action" onclick="resetFilters()">
    Reset (First/Corresponding & Full)
  </button>
  
  <button class="btn filter-btn-action" onclick="showAll()">
    Show All
  </button>
</div>

<div id="publications-list">
{% for post in site.publications reversed %}
  <div class="publication-item" 
       data-first="{{ post.is_first_author | default: false }}" 
       data-corresponding="{{ post.is_corresponding_author | default: false }}"
       data-full="{{ post.is_full_paper | default: false }}">
    {% include archive-single.html %}
  </div>
{% endfor %}
</div>

<script>
let activeFilters = {
  first: false,
  corresponding: false,
  full: false
};

function updateVisibility() {
  const items = document.querySelectorAll('.publication-item');
  const hasActiveFilters = Object.values(activeFilters).some(v => v);
  
  items.forEach(item => {
    const isFirst = item.getAttribute('data-first') === 'true';
    const isCorresponding = item.getAttribute('data-corresponding') === 'true';
    const isFull = item.getAttribute('data-full') === 'true';

    if (!hasActiveFilters) {
      // Default: (First OR Corresponding) AND Full Paper
      item.style.display = ((isFirst || isCorresponding) && isFull) ? 'block' : 'none';
      return;
    }

    // Role Match Logic: (First OR Corresponding)
    let roleMatch = true;
    if (activeFilters.first || activeFilters.corresponding) {
      roleMatch = false;
      if (activeFilters.first && isFirst) roleMatch = true;
      if (activeFilters.corresponding && isCorresponding) roleMatch = true;
    }

    // Type Match Logic: AND Full Paper
    let typeMatch = true;
    if (activeFilters.full && !isFull) {
      typeMatch = false;
    }

    item.style.display = (roleMatch && typeMatch) ? 'block' : 'none';
  });
}

function showAll() {
  activeFilters = { first: false, corresponding: false, full: false };
  document.querySelectorAll('.filter-btn').forEach(b => {
    b.classList.remove('btn--selected');
    b.classList.add('btn--unselected');
  });
  document.querySelectorAll('.publication-item').forEach(item => item.style.display = 'block');
}

function resetFilters() {
  activeFilters = { first: false, corresponding: false, full: false };
  document.querySelectorAll('.filter-btn').forEach(b => {
    b.classList.remove('btn--selected');
    b.classList.add('btn--unselected');
  });
  updateVisibility();
}

document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.classList.add('btn--unselected');
  btn.addEventListener('click', () => {
    const filter = btn.getAttribute('data-filter');
    activeFilters[filter] = !activeFilters[filter];
    
    if (activeFilters[filter]) {
      btn.classList.add('btn--selected');
      btn.classList.remove('btn--unselected');
    } else {
      btn.classList.remove('btn--selected');
      btn.classList.add('btn--unselected');
    }
    updateVisibility();
  });
});

window.addEventListener('DOMContentLoaded', updateVisibility);
</script>

<style>
.filters {
  margin-bottom: 20px;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #eeeeee;
  border-radius: 4px;
}
.filter-btn, .filter-btn-action {
  margin-right: 8px;
  margin-bottom: 8px;
  cursor: pointer;
  border-radius: 4px;
  padding: 8px 16px;
  font-size: 0.9em;
  transition: all 0.2s ease;
  outline: none;
}
/* White style for unselected */
.btn--unselected {
  background-color: #ffffff !important;
  color: #333333 !important;
  border: 1px solid #cccccc !important;
  box-shadow: none !important;
}
/* Black style for selected */
.btn--selected {
  background-color: #000000 !important;
  color: #ffffff !important;
  border: 1px solid #000000 !important;
  box-shadow: none !important;
}
/* Action buttons (Reset/Show All) - strictly white background */
.filter-btn-action {
  background-color: #ffffff !important;
  color: #333333 !important;
  border: 1px solid #cccccc !important;
}
.filter-btn-action:hover {
  background-color: #f0f0f0 !important;
}
</style>
