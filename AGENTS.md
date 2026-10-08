# Project Instructions

## Local Development & Testing

To preview the website locally, use the following commands:

1. **Install Dependencies**:
   ```bash
   bundle install
   ```

2. **Start Server**:
   ```bash
   bundle exec jekyll serve --livereload
   ```

### Troubleshooting Ruby 3.2+ / 4.0+ Compatibility

If you see an error like `undefined method 'tainted?' for an instance of String`, it means your Ruby version (>= 3.2) has removed methods that older Jekyll/Liquid versions depend on.

- **Solution**: I have added a compatibility patch in `_plugins/ruby_compatibility_patch.rb` and required it in the `Gemfile`.
- **Server address**: Visit `http://localhost:4000` to view the site.

## Data Consistency

- **Education & Experience**: Managed centrally in `_data/cv.yml`. This file feeds both the **About Me** (home) and **CV** pages.
- **Publications**: Managed as a collection in `_publications/`. Adding a new `.md` file there will automatically update the Publications page and the CV's publication list.
- **English/Chinese switch**: Every page renders both languages; the masthead button toggles which one is shown (always starts in English, the choice is not remembered). Wrap text in `class="i18n-en"` / `class="i18n-zh"` blocks (use `markdown="1"` on `<div>`s holding Markdown), or use `{% include i18n.html key="..." %}` with strings from `_data/locales.yml`. Page titles use `title_zh` in front matter; nav items use `title_zh` in `_data/navigation.yml`. When editing page content (e.g. `_pages/research.md`), update both languages.

## Research Page Organization

If the list of activities or grants grows too long:
- Use the **Jump to** navigation added at the top of `_pages/research.md`.
- Group entries by year or category using sub-headings.
