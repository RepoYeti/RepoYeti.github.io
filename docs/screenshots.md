# Screenshotting the page

The page's sections start at `opacity: 0` and are revealed by scroll-driven animations, so a
screenshot taken the ordinary way (an in-app browser pane, a plain headless capture) often comes
back as an empty band where a section should be. Measuring element boxes in JavaScript is not a
substitute: the numbers can all be right while the page looks broken. To see a change, take a
screenshot that forces the reveals to their finished state first.

## The tool

`shotpage.mjs` does that. It is not in this repo: it is a shared script kept in the owner's
claude-memory repo at `home/tools/shot/shotpage.mjs` (installed on each machine under the Claude
profile's `tools/shot/` folder). It needs Node and a system Chrome, and uses
`playwright-core`, so there is no browser download.

Before it captures a pixel it:

1. drives the system Chrome headless, so nothing depends on a window being visible;
2. emulates `prefers-reduced-motion`;
3. injects a stylesheet that forces every animation and transition to its finished state and
   un-hides the usual reveal patterns;
4. scrolls the whole document to trip any IntersectionObserver that survived step 3, then returns
   to the top;
5. waits for fonts, for every image to decode, and for layout to stop moving.

It exits non-zero when the capture cannot be trusted (a blank frame, an image that never decoded,
layout still moving), rather than quietly returning a dark rectangle.

## Usage

```sh
node shotpage.mjs index.html -o out.png                  # full page, from the local file
node shotpage.mjs https://repoyeti.com -o out.png        # full page, live
node shotpage.mjs index.html --sel "#pricing" -o out.png # one section
node shotpage.mjs index.html --each-section outdir/      # every <section>, one file each
node shotpage.mjs index.html --width 1400                # viewport width
node shotpage.mjs index.html --mobile -o mobile.png      # 390x844 phone viewport
```

`--keep-motion` skips the forced finished state, for when the animation itself is what you are
checking.

## Without the tool

Any headless browser works if it does the same things in the same order: reduced motion on,
animations and transitions forced to their end state, a full scroll to the bottom and back, then a
wait for fonts and images before capturing.
