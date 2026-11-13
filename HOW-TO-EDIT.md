# How to edit your website

This file is a guide for you. It does not appear on the website.

## What each file does

| File or folder | What it is |
|---|---|
| `_config.yml` | Your name, email, footer links and the top menu |
| `index.md` | Your home page (bio) |
| `cv.md` | Your CV page |
| `blog.md` | The list of blog posts. It updates itself, so you never need to edit it |
| `_posts/` | One file per blog post |
| `assets/images/` | Pictures, including your profile photo (`profile.jpg`) |
| `files/` | Downloadable files, such as `cv.pdf` |
| `assets/style.css` | Colours and fonts |
| `_layouts/` | The page design. Leave this alone unless you want to change the layout |
| `substack.html` | Sends anyone who visits the old Substack page to your Blog page. Leave it alone |
| `.pages.yml` | Settings for the optional visual editor (see the end of this guide) |

Every change you save on GitHub appears on your website after one or two minutes.

## First-time setup

1. Your repository on GitHub must be named `yourusername.github.io`.
2. If it already has old files you don't want, delete them first.
3. Open the repository on github.com, click **Add file**, then **Upload files**.
4. Unzip the folder on your computer, open it, select everything inside it and drag it onto the GitHub page. Drag the contents, not the folder itself.
   - On a Mac, the file `.pages.yml` is hidden. Press **Cmd + Shift + .** (full stop) in Finder to show it before selecting everything.
5. Click **Commit changes**.
6. Go to **Settings**, then **Pages**. Under "Build and deployment", choose **Deploy from a branch**, branch **main**, folder **/ (root)**, and save.
7. Visit `https://yourusername.github.io` after a couple of minutes.

## Change the text on a page

1. On github.com, open the file (for example `index.md` or `cv.md`).
2. Click the pencil icon at the top right of the file.
3. Edit the text. Do not touch the lines between the two `---` lines at the top unless you mean to.
4. Click **Commit changes** (green button), then **Commit changes** again.

## Write a new blog post

1. Open the `_posts` folder on github.com.
2. Click **Add file**, then **Create new file**.
3. Name the file with the date and a short title, joined by dashes, ending in `.md`:
   `2026-11-20-my-trip-to-montreal.md`
   The date must be written as year-month-day. It sets the post's date, and posts dated in the future won't appear until that day.
4. Paste this at the top, then write your post below it:

```
---
title: "My trip to Montreal"
description: "One sentence that appears on the blog list."
---

Your first paragraph goes here.
```

5. Click **Commit changes**.

To remove a post, open its file, click the three dots (**...**) at the top right and choose **Delete file**.

## Formatting cheat sheet

| You type | You get |
|---|---|
| `## Heading` | A section heading |
| `**bold**` | **bold** |
| `*italics*` | *italics* |
| `[link text](https://example.com)` | a link |
| `- item` | a bulleted list |
| `![description](/assets/images/photo.jpg)` | a picture |
| a blank line | a new paragraph |

## Add a picture

1. Open the `assets/images` folder, click **Add file**, then **Upload files**, and upload the picture.
2. In a page or post, write `![Description](/assets/images/the-file-name.jpg)`.

To change your profile photo, upload your own photo named `profile.jpg` into `assets/images`. GitHub will ask whether to replace the old one; say yes.

## Replace the CV PDF

Upload your CV into the `files` folder with the name `cv.pdf`. It replaces the placeholder, and the "Download my CV" link on the CV page will point to it.

## Change your name, email or the menu

Edit `_config.yml`. The comments in the file (lines starting with `#`) explain each setting. Keep the quotation marks and the spacing at the start of each line; this file is sensitive to indentation.

To add a new page (for example "Projects"): create `projects.md` in the main folder, starting with

```
---
title: Projects
permalink: /projects/
---
```

then add it to the `navigation` list in `_config.yml`:

```
  - name: "Projects"
    url: "/projects/"
```

## Substack and cross-posting

The bottom of the **Blog** page has a box where visitors can subscribe to your Substack by email. If you ever change your Substack address, edit the `substack_url` line in `_config.yml`.

If a post also appears somewhere else (Substack, LessWrong, the EA Forum), you can list those places at the top of the post, and the post will end with "Also published on ..." links:

```
---
title: "My post"
description: "One sentence for the blog list."
also_on:
  - name: "Substack"
    url: "https://theoshouse.substack.com/p/my-post"
  - name: "LessWrong"
    url: "https://www.lesswrong.com/posts/..."
---
```

## If something breaks

Click the **Actions** tab of your repository. A red X means the last change didn't build. Click it to see the error message. The usual causes are:

- a missing `---` line at the top of a page or post;
- a title containing a colon without quotation marks around it;
- a post filename without the `YYYY-MM-DD-` date at the start;
- wrong spacing in `_config.yml`.

Fix the file and commit again. Every earlier version of every file is kept in its **History**, so you can always go back.

## Optional: the visual editor

If you prefer a word-processor-style editor to editing files on GitHub:

1. Go to https://app.pagescms.org and sign in with GitHub.
2. Choose your `yourusername.github.io` repository.
3. You will see **Blog posts**, **About page**, **CV page** and **Site settings** in the menu. Click **Add an entry** under Blog posts to write a post; the file name and date are handled for you.

Saving in Pages CMS saves to GitHub in the same way, so you can switch between the two methods at any time.
