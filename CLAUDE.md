# Notes for Claude

This is Theo's personal website, a Jekyll site published by GitHub Pages from `main`. Theo is not technical: explain things in plain language, write in Canadian English, and avoid em-dashes and emojis. `HOW-TO-EDIT.md` is Theo's own guide; keep it up to date when you change how the site works.

## Publishing a blog post from a Google Doc

Theo writes drafts in Google Docs and sends Claude the link. Each time:

1. Read the doc with the Google Docs connector. Keep Theo's wording; only fix formatting.
2. Convert it to Markdown in `_posts/YYYY-MM-DD-short-title.md` (today's date unless Theo gives one), with front matter `title` and a one-sentence `description`. Put images in `assets/images/` and link them.
3. Build the site locally with Jekyll to check it, then open a pull request and give Theo the link to merge. The post goes live a minute or two after merging.
4. Ask Theo whether to also publish it on Substack, LessWrong and/or the EA Forum. Claude can't post to those sites (they need Theo signed in). For each site Theo picks, give a version ready to paste into that site's editor, ending with a line like "Originally published on [my website](link to the post)".
5. When Theo sends the links of the cross-posts, add them to the post's front matter so the post ends with "Also published on ..." links:

```
also_on:
  - name: "Substack"
    url: "https://theoshouse.substack.com/p/..."
```

## Substack

Substack blocks automated requests from GitHub and from Claude's servers, so posts can't be fetched automatically. To import old Substack posts, Theo downloads an export from Substack (Settings, Export) and uploads the zip. The site only links to Substack (`substack_url` in `_config.yml`); `/substack/` redirects to `/blog/`.
