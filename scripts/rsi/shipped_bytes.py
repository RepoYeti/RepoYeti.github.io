"""Bytes a visitor downloads: committed size at HEAD of the files the site serves. Prints shipped_bytes=<n> and html_bytes=<n>."""
import subprocess

SERVED = (".html", ".css", ".js", ".mjs", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico",
          ".woff", ".woff2", ".json", ".webmanifest", ".xml", ".txt")
EXTRA = ("pricing.md",)
SKIP_TOP = ("docs", "scripts")
listing = subprocess.run(["git", "ls-tree", "-r", "-l", "-z", "HEAD"], capture_output=True, check=True).stdout
total = 0
html = 0
for entry in listing.split(b"\0"):
    if not entry:
        continue
    meta, path = entry.decode("utf-8", "replace").split("\t", 1)
    size = meta.split()[3]
    parts = path.split("/")
    if size == "-" or any(p.startswith(".") for p in parts) or parts[0] in SKIP_TOP:
        continue
    if path.lower().endswith(SERVED) or path in EXTRA:
        total += int(size)
    if path == "index.html":
        html = int(size)
print(f"shipped_bytes={total}")
print(f"html_bytes={html}")
