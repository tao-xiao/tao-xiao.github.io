---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% if site.author.googlescholar %}
  <p>You can also find an up-to-date publication list on <a href="{{ site.author.googlescholar }}">my Google Scholar profile</a>.</p>
{% endif %}

{% include base_path %}

<div class="filters-container">
  <strong style="display: block; margin-bottom: 10px;">Filter by (multi-select):</strong>
  <div class="button-group">
    <button id="btn-first" class="btn-modern selected" onclick="toggleFilter('first')">First Author</button>
    <button id="btn-corresponding" class="btn-modern selected" onclick="toggleFilter('corresponding')">Corresponding Author</button>
    <button id="btn-full" class="btn-modern selected" onclick="toggleFilter('full')">Full Paper</button>
  </div>
  <div class="button-group-actions" style="margin-top: 10px;">
    <button class="btn-action-modern" onclick="resetFilters()">Reset (First/Corresponding & Full)</button>
    <button class="btn-action-modern" onclick="showAll()">Show All</button>
  </div>
  <p id="publication-count" aria-live="polite" style="margin: 10px 0 0;"></p>
</div>

<div id="publications-list">
{% assign sorted_publications = site.publications | sort: "uploaded_at" | reverse %}
{% for post in sorted_publications %}
  <div class="publication-item" 
       data-first="{{ post.is_first_author | default: false }}" 
       data-corresponding="{{ post.is_corresponding_author | default: false }}"
       data-full="{{ post.is_full_paper | default: false }}">
    {% include archive-single.html %}
  </div>
{% endfor %}
</div>

<style>
  /* Base Modern Button Styles */
  .btn-modern, .btn-action-modern {
    display: inline-block;
    padding: 0.5rem 1.2rem;
    margin-right: 8px;
    margin-bottom: 8px;
    font-size: 0.85em;
    font-weight: 600;
    line-height: 1.5;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    cursor: pointer;
    user-select: none;
    border: 1px solid #dbdbdb;
    border-radius: 4px;
    transition: all 0.2s ease-in-out;
    font-family: -apple-system, BlinkMacSystemFont, "Roboto", "Segoe UI", Helvetica, Arial, sans-serif;
  }

  /* Unselected: Pure White Background */
  .btn-modern.unselected {
    background-color: #ffffff !important;
    color: #333333 !important;
    border-color: #dddddd !important;
    box-shadow: none !important;
  }

  /* Selected: Pure Black Background */
  .btn-modern.selected {
    background-color: #000000 !important;
    color: #ffffff !important;
    border-color: #000000 !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
  }

  /* Hover states */
  .btn-modern:hover {
    opacity: 0.85;
  }

  /* Reset/Show All: Light and Clean */
  .btn-action-modern {
    background-color: #f8f9fa !important;
    color: #495057 !important;
    border-color: #e9ecef !important;
  }
  .btn-action-modern:hover {
    background-color: #e2e6ea !important;
  }

  .filters-container {
    margin-bottom: 30px;
    padding: 20px;
    background: #fafafa;
    border-radius: 6px;
    border: 1px solid #f1f1f1;
  }
</style>

<script>
(function() {
  var activeFilters = { first: true, corresponding: true, full: true };

  function updateVisibility() {
    var items = document.querySelectorAll('.publication-item');
    var hasActiveFilters = false;
    var visibleCount = 0;
    for (var key in activeFilters) { if (activeFilters[key]) hasActiveFilters = true; }
    
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var isFirst = item.getAttribute('data-first') === 'true';
      var isCorresponding = item.getAttribute('data-corresponding') === 'true';
      var isFull = item.getAttribute('data-full') === 'true';

      if (!hasActiveFilters) {
        item.style.display = 'block';
        visibleCount++;
      } else {
        var roleMatch = true;
        if (activeFilters.first || activeFilters.corresponding) {
          roleMatch = false;
          if (activeFilters.first && isFirst) roleMatch = true;
          if (activeFilters.corresponding && isCorresponding) roleMatch = true;
        }
        var typeMatch = true;
        if (activeFilters.full && !isFull) typeMatch = false;
        var shouldShow = roleMatch && typeMatch;
        item.style.display = shouldShow ? 'block' : 'none';
        if (shouldShow) visibleCount++;
      }
    }

    var count = document.getElementById('publication-count');
    if (count) count.textContent = 'Showing ' + visibleCount + ' of ' + items.length + ' publications';
  }

  function updateButtonStyles() {
    ['first', 'corresponding', 'full'].forEach(function(f) {
      var btn = document.getElementById('btn-' + f);
      if (btn) {
        if (activeFilters[f]) {
          btn.classList.add('selected');
          btn.classList.remove('unselected');
        } else {
          btn.classList.add('unselected');
          btn.classList.remove('selected');
        }
      }
    });
  }

  window.toggleFilter = function(f) {
    activeFilters[f] = !activeFilters[f];
    updateButtonStyles();
    updateVisibility();
  };

  window.showAll = function() {
    for (var key in activeFilters) { activeFilters[key] = false; }
    updateButtonStyles();
    updateVisibility();
  };

  window.resetFilters = function() {
    activeFilters.first = true;
    activeFilters.corresponding = true;
    activeFilters.full = true;
    updateButtonStyles();
    updateVisibility();
  };

  if (document.readyState !== 'loading') {
    updateButtonStyles();
    updateVisibility();
  } else {
    document.addEventListener('DOMContentLoaded', function() {
      updateButtonStyles();
      updateVisibility();
    });
  }
})();
</script>
