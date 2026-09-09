# RepoYeti site

> Landing page for RepoYeti, a phone git dashboard that refuses force-push, reset --hard, and rebase by design.

<!-- odin:about HAND-OWNED above the GENERATED marker. Edit freely; `odin codex about --ingest` carries it back into Odin's Codex. -->

## What it is

The marketing and landing site for RepoYeti, a self-hosted remote git manager that runs as a daemon on your desktop and serves a dashboard to your phone. The site introduces the product, showcases its core features (repo dashboard, git-graph history, Monaco diffs, Smart Commit), explains its safety guardrails, and hosts an FAQ. Deployed to GitHub Pages at repoyeti.com.

## Things not to forget

_The intricacies worth remembering: the gotchas, the half-built parts, the decisions whose
reason lives nowhere else. Odin never overwrites this section._

- The safety section is not a list of missing features but a deliberate design stance - the copy frames leaving out force-push, reset --hard, rebase, and non-fast-forward merges as the whole point of a phone git client, so a request to 'add' one of these to the product is a philosophy change, not a feature request. anchors: `index.html:461`
- Smart Commit is bring-your-own-key across six providers (Groq, OpenAI, Claude, Gemini, OpenRouter, DeepSeek) and the copy is explicit that the key and the code only ever reach the model the user picked, never a RepoYeti server - that phrasing is load-bearing and should not be loosened when this section is edited. anchors: `index.html:527`
- The ARGUS analytics pixel's privacy behavior is spelled out in a source comment, not just prose: it honors DNT and Sec-GPC, is grant-by-default only outside the EU/EEA/UK/CH (stamped per-visitor at the edge), and skips localhost so local previews cannot inflate pageview counts. anchors: `index.html:221`
- robots.txt names AI answer-engine and training bots one by one (ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, MistralAI-User, GPTBot, ClaudeBot, etc.) instead of relying on a wildcard rule, with an inline comment explaining that an explicit allow survives being told otherwise later - it is paired with llms.txt, llms-full.txt, and a machine-readable pricing.md aimed at agents rather than human readers. anchors: `robots.txt:1`
- There is no build step at all: index.html is the entire site (markup, copy, and CSS together), so editing and pushing main is the full deploy pipeline, and CNAME plus .nojekyll are both load-bearing for GitHub Pages (CNAME routes the repoyeti.com custom domain, .nojekyll stops Jekyll from reprocessing the raw HTML). anchors: `CNAME:1`
- The 'Running it' section is also where the real tech stack is disclosed publicly (Bun, bun:sqlite, Hono, simple-git, Vue 3 + Tailwind PWA) and states the daemon tunnels the local server out and requires signing in with Connections to reach it from a phone - useful context if this copy ever needs to change alongside the actual product. anchors: `index.html:566`
- Two improvements are recorded as wanted but not yet built: a copy-to-clipboard button for the terminal install commands, and replacing the prose-only alternatives comparison with a visual feature matrix - neither exists in the current markup. anchors: `index.html:572`

<!-- odin:about GENERATED BEGIN - rewritten by `odin codex about --publish`; edit the Codex, not this -->

## What Odin knows about this project

Everything from here down is generated from this project's Codex dossier
(`codex/projects/repoyeti-github-io.md` in the Odin clone) and is **rewritten on every publish** -
edit the dossier, not this block. Everything ABOVE the marker is yours.

### At a glance

- **Ships as:** static site - GitHub Pages (RepoYeti/RepoYeti.github.io repo, served from main branch at custom domain repoyeti.com)
- **Live at:** https://repoyeti.com
- **Entry points:** `site_root`
- **Deploys via:** github-pages
- **Domain:** git, remote-git, mobile-first, self-hosted-dashboard, safety-by-constraint, PWA, marketing-site
- **Remote:** https://github.com/RepoYeti/RepoYeti.github.io.git

### Architecture

- `index.html` - the entire site: hero, sections for each feature, navigation, FAQ, comparison, footer; inline CSS, no build step
- `shots/` - screenshot images for git-graph and Monaco diff features, displayed in responsive mobile/desktop versions
- `favicon.svg` - site mark and browser tab icon
- `docs/` - documentation folder (README explaining no build, edit and push workflow)
- `CNAME` - custom domain config (repoyeti.com)
- `.nojekyll` - signal to GitHub Pages to skip Jekyll processing and serve files as-is

### Features

10 recorded - 10 shipped, 0 partial, 0 planned. Each `path:line` is where the feature is DEFINED, checked by `odin codex check`.

**Shipped**

- **Hero and product overview** - Introductory section with headline 'Push a hotfix from your phone', lede explaining RepoYeti as a daemon + phone dashboard, CTA linking to GitHub, and animated demo GIF showing the product in use. - `index.html:420`
- **Live repo dashboard showcase** - Section explaining the repo grid feature: fetch all repos at once, live updates as you commit elsewhere, pin and hide repos, automatic git identity per repo. Cards layout describing each capability. - `index.html:511`
- **Git-graph history browser** - Section with real product screenshots (mobile and desktop) showing the commit-graph view with branching lanes, merges, and uncommitted changes at the top. Explains it's the actual git log drawn out, not a flat list. - `index.html:489`
- **Monaco diff viewer with editing** - Section showcasing the Monaco editor integration with syntax highlighting, proper diffs against HEAD, folded context. Explains users can edit and save typos directly from the phone. - `index.html:500`
- **Smart Commit AI feature** - Section explaining AI-powered commit splitting: reads messy diffs and suggests clean commit boundaries. Describes bring-your-own-key model (Groq, OpenAI, Claude, Gemini, OpenRouter, DeepSeek). Emphasizes keys stay in the daemon. - `index.html:527`
- **Safety guardrails and constraints** - Section titled 'An app that can push git from your phone should scare you' listing what the app explicitly will NOT do: no force-push, no reset --hard, no rebase, no non-fast-forward merges, automatic identity, no keys leaving the daemon. Explains the philosophy of leaving dangerous operations off a phone. - `index.html:461`
- **FAQ and comparison** - Comprehensive FAQ answering key questions (does code leave your computer, what AI providers work, is it open source, how to use from phone, is it free). Comparison section explaining differences from GitHub Mobile (no working tree), Working Copy (no cloning), and SSH clients (no dangerous commands). - `index.html:582`, `index.html:599`
- **AI answer-engine allow-list & agent content bundle** - robots.txt explicitly allow-lists AI search/answer bots (ChatGPT-User, Claude-SearchBot/Claude-User, PerplexityBot, MistralAI-User, DuckAssistBot) and AI training crawlers (GPTBot, ClaudeBot, anthropic-ai, CCBot, Bytespider, etc.) by name with inline rationale, paired with llms.txt, llms-full.txt, and a machine-readable pricing.md written for agents/buyers rather than human readers. Entirely missing from the spec's architecture, features and domain lists. - `robots.txt:7`, `llms.txt:1`, `pricing.md:1`
- **Site analytics pixel (ARGUS)** - First-party ARGUS pageview-tracking pixel (analytics.connections.icu) loaded from <head>, honoring Do Not Track / Sec-GPC and skipping localhost. Was described only in notes/mistagged onto an unrelated feature, never given its own entry or anchor. - `index.html:221`
- **How to run it (installation walkthrough)** - Dedicated section walking a visitor through installing and starting the daemon (repoyeti add-root, repoyeti start), naming supported platforms (macOS/Linux/Windows) and the tech stack (Bun, bun:sqlite, Hono, simple-git, Vue 3 + Tailwind PWA). A distinct site section with no feature entry. - `index.html:566`

### Where to add a new one

- **edit an existing section (hero, feature showcase, FAQ)** - edit the HTML section in index.html (markup and copy are together), test locally by opening the file in a browser, commit and push to main anchors: `index.html:419`
- **add a new full-page section** - add a new <section id='...'> block following the pattern (kicker, h2, sec-grid with rail + body), add styles to the <style> block, link from the nav if it's top-level anchors: `index.html:32`, `index.html:403`
- **replace or add screenshots** - add PNG/GIF files to shots/ folder, reference them in the HTML <img src='shots/...'> tags with alt text, commit and push anchors: `index.html:493`

### Gaps and wants

_Withheld: this repository is public, and the gap list is not published outside the private index._
_Read it with `python odin.py codex brief repoyeti-github-io` in the Odin clone._

---

_Generated by `odin codex about --publish repoyeti-github-io` on 2026-09-09 from a Codex dossier stamped 2026-09-04. Regenerate after the product moves; `odin codex about` reports drift._
<!-- odin:about GENERATED END sha=c8ca99d00f27 -->
