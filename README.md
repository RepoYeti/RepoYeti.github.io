# repoyeti.com

The marketing/landing site for **RepoYeti** — a self-hosted, system-wide remote git manager
(a background daemon + mobile PWA that lets you run git from your phone, safely).

- **Live:** https://repoyeti.com
- **Hosting:** GitHub Pages (this repo, `RepoYeti/RepoYeti.github.io`), served from `main` at the root.
- **Domain:** `repoyeti.com` (custom domain in `CNAME`), DNS on Cloudflare pointing the apex + `www`
  at GitHub Pages. `app.repoyeti.com` is a **separate** record (the daemon's own tunnel) and is not
  touched by this site.

## What's here

A single, self-contained static page — no build step.

- `index.html` — the whole page (inline CSS, no JS, no external assets/fonts).
- `favicon.svg` — the mark.
- `CNAME` — the custom domain GitHub Pages serves.
- `.nojekyll` — skip Jekyll processing (we serve the file as-is).

## Editing

Edit `index.html` and push to `main`. GitHub Pages redeploys automatically.
