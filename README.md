# repoyeti.com

The marketing/landing site for **RepoYeti** — a self-hosted, system-wide remote git manager
(a background daemon + mobile PWA that lets you run git from your phone, safely).

[![Discord](https://img.shields.io/badge/Discord-join_the_community-5865F2?logo=discord&logoColor=white)](https://discord.gg/PsWpeNUzhk)

- **Live:** https://repoyeti.com
- **Hosting:** GitHub Pages (this repo, `RepoYeti/RepoYeti.github.io`), served from `main` at the root.
- **Domain:** `repoyeti.com` (custom domain in `CNAME`), DNS on Cloudflare pointing the apex + `www`
  at GitHub Pages. `app.repoyeti.com` is a **separate** record (the daemon's own tunnel) and is not
  touched by this site.

## What's here

A single static page, no build step.

- `index.html`: the whole page. Inline CSS; the Inter font is self-hosted (see `fonts/`); two small
  inline scripts (the Connections analytics pixel loader, which skips localhost, and the dismissible
  notice's localStorage memory) plus JSON-LD structured data.
- `fonts/`: the two Inter `wght` subsets (latin, latin-ext) taken from
  `@fontsource-variable/inter`, served from this origin so no third-party stylesheet sits in the
  render path. Replace them by copying the matching files out of that package.
- `favicon.svg` — the mark.
- `CNAME` — the custom domain GitHub Pages serves.
- `.nojekyll` — skip Jekyll processing (we serve the file as-is).

## Editing

Edit `index.html` and push to `main`. GitHub Pages redeploys automatically.
