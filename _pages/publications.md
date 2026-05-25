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
  <button class="btn filter-btn btn--unselected" data-filter="first">First Author</button>
  <button class="btn filter-btn btn--unselected" data-filter="corresponding">Corresponding Author</button>
  <button class="btn filter-btn btn--unselected" data-filter="full">Full Paper</button>
  
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
// We use a self-executing function to avoid global namespace pollution
(function() {
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
        // Default behavior: (First OR Corresponding) AND Full Paper
        const shouldShow = ((isFirst || isCorresponding) && isFull);
        item.style.display = shouldShow ? 'block' : 'none';
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

  // Global functions attached to window for HTML onclick attributes
  window.showAll = function() {
    activeFilters = { first: false, corresponding: false, full: false };
    document.querySelectorAll('.filter-btn').forEach(b => {
      b.classList.remove('btn--selected');
      b.classList.add('btn--unselected');
    });
    document.querySelectorAll('.publication-item').forEach(item => item.style.display = 'block');
  };

  window.resetFilters = function() {
    activeFilters = { first: false, corresponding: false, full: false };
    document.querySelectorAll('.filter-btn').forEach(b => {
      b.classList.remove('btn--selected');
      b.classList.add('btn--unselected');
    });
    updateVisibility();
  };

  function init() {
    document.querySelectorAll('.filter-btn').forEach(btn => {
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

    // Apply initial default view
    updateVisibility();
  }

  // Execute immediately if DOM ready, otherwise wait
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>

<style>
/* Increase specificity with body prefix to override theme defaults */
body .filters {
  margin-bottom: 20px;
  background: #ffffff !important;
  padding: 15px;
  border: 1px solid #eeeeee;
  border-radius: 4px;
}
body .filter-btn, body .filter-btn-action {
  margin-right: 8px;
  margin-bottom: 8px;
  cursor: pointer;
  border-radius: 4px;
  padding: 8px 16px;
  font-size: 0.9em;
  transition: all 0.2s ease;
  outline: none;
  display: inline-block;
}
/* White style for unselected - strictly enforced */
body .btn--unselected {
  background-color: #ffffff !important;
  color: #333333 !important;
  border: 1px solid #cccccc !important;
  box-shadow: none !important;
}
/* Black style for selected - strictly enforced */
body .btn--selected {
  background-color: #000000 !important;
  color: #ffffff !important;
  border: 1px solid #000000 !important;
  box-shadow: none !important;
}
/* Action buttons (Reset/Show All) - strictly white background */
body .filter-btn-action {
  background-color: #ffffff !important;
  color: #333333 !important;
  border: 1px solid #cccccc !important;
}
body .filter-btn-action:hover {
  background-color: #f0f0f0 !important;
}
</style>
