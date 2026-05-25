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

<div class="filters" style="margin-bottom: 20px; background: #ffffff; padding: 15px; border: 1px solid #eeeeee; border-radius: 4px;">
  <strong>Filter by (multi-select):</strong>
  <br>
  <button id="btn-first" class="filter-btn-custom" onclick="toggleFilter('first')">First Author</button>
  <button id="btn-corresponding" class="filter-btn-custom" onclick="toggleFilter('corresponding')">Corresponding Author</button>
  <button id="btn-full" class="filter-btn-custom" onclick="toggleFilter('full')">Full Paper</button>
  
  <button class="filter-btn-action" onclick="resetFilters()">Reset (First/Corresponding & Full)</button>
  <button class="filter-btn-action" onclick="showAll()">Show All</button>
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
(function() {
  var activeFilters = { first: false, corresponding: false, full: false };

  var style = document.createElement('style');
  style.innerHTML = [
    '.filter-btn-custom, .filter-btn-action {',
    '  margin-right: 8px !important;',
    '  margin-bottom: 8px !important;',
    '  cursor: pointer !important;',
    '  border-radius: 4px !important;',
    '  padding: 8px 16px !important;',
    '  font-size: 0.9em !important;',
    '  transition: all 0.2s ease !important;',
    '  display: inline-block !important;',
    '  font-family: sans-serif !important;',
    '  text-decoration: none !important;',
    '  line-height: 1.5 !important;',
    '}',
    '.btn-unselected {',
    '  background-color: #ffffff !important;',
    '  color: #333333 !important;',
    '  border: 1px solid #cccccc !important;',
    '  box-shadow: none !important;',
    '}',
    '.btn-selected {',
    '  background-color: #000000 !important;',
    '  color: #ffffff !important;',
    '  border: 1px solid #000000 !important;',
    '  box-shadow: none !important;',
    '}',
    '.filter-btn-action {',
    '  background-color: #ffffff !important;',
    '  color: #333333 !important;',
    '  border: 1px solid #cccccc !important;',
    '}'
  ].join('\\n');
  document.head.appendChild(style);

  function updateVisibility() {
    var items = document.querySelectorAll('.publication-item');
    var hasActiveFilters = false;
    for (var key in activeFilters) { if (activeFilters[key]) hasActiveFilters = true; }
    
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var isFirst = item.getAttribute('data-first') === 'true';
      var isCorresponding = item.getAttribute('data-corresponding') === 'true';
      var isFull = item.getAttribute('data-full') === 'true';

      if (!hasActiveFilters) {
        var shouldShow = ((isFirst || isCorresponding) && isFull);
        item.style.display = shouldShow ? 'block' : 'none';
      } else {
        var roleMatch = true;
        if (activeFilters.first || activeFilters.corresponding) {
          roleMatch = false;
          if (activeFilters.first && isFirst) roleMatch = true;
          if (activeFilters.corresponding && isCorresponding) roleMatch = true;
        }
        var typeMatch = true;
        if (activeFilters.full && !isFull) typeMatch = false;
        item.style.display = (roleMatch && typeMatch) ? 'block' : 'none';
      }
    }
  }

  function updateButtonStyles() {
    var keys = ['first', 'corresponding', 'full'];
    for (var i = 0; i < keys.length; i++) {
      var f = keys[i];
      var btn = document.getElementById('btn-' + f);
      if (btn) {
        btn.className = 'filter-btn-custom ' + (activeFilters[f] ? 'btn-selected' : 'btn-unselected');
      }
    }
  }

  window.toggleFilter = function(f) {
    activeFilters[f] = !activeFilters[f];
    updateButtonStyles();
    updateVisibility();
  };

  window.showAll = function() {
    for (var key in activeFilters) { activeFilters[key] = false; }
    updateButtonStyles();
    var items = document.querySelectorAll('.publication-item');
    for (var i = 0; i < items.length; i++) { items[i].style.display = 'block'; }
  };

  window.resetFilters = function() {
    for (var key in activeFilters) { activeFilters[key] = false; }
    updateButtonStyles();
    updateVisibility();
  };

  function ready(fn) {
    if (document.readyState !== 'loading') { fn(); } 
    else { document.addEventListener('DOMContentLoaded', fn); }
  }

  ready(function() {
    updateButtonStyles();
    updateVisibility();
  });
})();
</script>
