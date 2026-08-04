---
name: academic-page-manager
description: Manage and update this personal academic page. Handles adding publications, updating CV data, and running local development tests. Use when the user wants to add new research content or fix site issues.
---

# Academic Page Manager

This skill helps you manage and update your academic website efficiently.

## Core Mandate: Verification & Learning
**IMPORTANT**: After making ANY code change, content update, or bug fix:
1. Run `bundle exec jekyll serve --livereload`.
2. Access `http://localhost:4000/` and navigate to the affected page(s).
3. **Check against the "Verification Checklist" below.**
4. Confirm UI layout, styling, and functionality.
5. **Update this Skill**: If a new problem was solved, append it to the "Verification Checklist" (merge with similar items if applicable).
6. Report the verification results to the user.

## Verification Checklist (Lessons Learned)
- **Ruby & Environment**: Ensure `csv`, `webrick`, etc., are in `Gemfile` for Ruby 3.4+. Maintain the `tainted?` patch for Ruby 3.2+ compatibility.
- **Data Integrity**: Validate YAML syntax (indentation, colons). Ensure `abstract` is a single line and properly quoted.
- **Publication Metadata**: Verify exact author order, author-name capitalization, branded title casing, publication year convention, and URLs against the publisher, conference, or current paper record.
- **Markdown Rendering**: Always leave blank lines around HTML blocks (e.g., `<div>`) to prevent Markdown layout collapse.
- **UI/UX Consistency**: 
    - Verify high-contrast button colors (Selected: Black, Unselected: White).
    - Ensure publication filter button classes, JavaScript filter state, visible results, and the "Showing X of Y publications" counter agree on initial load and after Reset/Show All.
    - Homepage selected publications must be controlled by `selected: true` in publication front matter; verify that only the intended papers appear.
    - **Author Styling (Tao Xiao Only)**:
        - Highlight: Light red background (`#ffcccc`) via `<span>`.
        - First Author: Bold (`<strong>`).
        - Corresponding Author: Underline (`<u>`).
        - Rule: These styles apply ONLY to "Tao Xiao". Other authors are plain text.
    - **Paper Tracks**: For non-full papers (`is_full_paper: false`), display the `track` (default: "Short Paper") in parentheses after the venue.
    - **PDF Placeholders**: If `paperurl` is missing, display `[pdf (placeholder)]` linked to `#`.
    - Ensure no extra spaces before commas in author lists.
    - Check navigation menu alignment (menu items should stay on one line).
- **Routing**: Ensure Home page (`/`) and all permalinks do not return 404.
- **Publication Slugs & Ordering**: Keep publication filenames and permalinks date-free (for example, `paper-title.md` and `/publication/paper-title`). Sort publication lists by the internal `uploaded_at` front-matter field in descending order. Never render `uploaded_at` in the visible publication UI.
- **SEO & Template Hygiene**: Ensure site description, Open Graph image, and Person `sameAs` profiles are populated. Verify `sitemap.xml` contains no template/demo pages and every favicon/manifest asset referenced by the generated HTML exists.
- **Typos & Formatting**: Scan for obvious spelling errors or redundant punctuation (e.g., `, ,`). **DO NOT** fix automatically; report them to the user for confirmation.

## Core Workflows

### 1. Adding a New Publication
Create a new file in `_publications/` with the date-free naming `title-slug.md`.
```yaml
---
title: "Full Paper Title"
collection: publications
permalink: /publication/title-slug
year: YYYY
uploaded_at: "YYYY-MM-DD"
venue: "Conference or Journal Name"
paperurl: "URL to PDF"
is_full_paper: true/false
is_first_author: true/false
is_corresponding_author: true/false
authors:
  - name: "Tao Xiao"
abstract: "One-line abstract text without newlines."
---
```

### 2. Updating CV or Education
Information for both the **About Me** page and the **CV** page is centralized in `_data/cv.yml`.
Modify `_data/cv.yml` to update:
- Education background
- Work experience

### 3. Local Development & Testing
To preview the site locally:
```bash
bundle exec jekyll serve --livereload
```
If you encounter `tainted?` method errors (due to Ruby 3.2+), ensure `_plugins/ruby_compatibility_patch.rb` is required in the `Gemfile`.

## Technical Maintenance
- **Navigation**: Controlled by `_data/navigation.yml`.
- **Default Filter**: The Publications page defaults to `(First/Corresponding Author) AND Full Paper`.
