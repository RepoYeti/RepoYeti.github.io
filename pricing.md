# RepoYeti pricing

Machine-readable summary for agents and buyers. Plain-language answer: **RepoYeti is free for purposes permitted by PolyForm Noncommercial 1.0.0.** Commercial use outside those permissions requires a separate license from LunarWerx Studios.

## Product cost

| Item | Cost | Notes |
|---|---|---|
| RepoYeti daemon + dashboard, noncommercial use | $0 | Source-available under PolyForm Noncommercial 1.0.0, copyright LunarWerx Studios. Covers personal projects, learning, research and non-profits. Consult the license for its own definitions of permitted purposes and organizational uses. Every feature; nothing is time-limited or feature-gated. |
| RepoYeti commercial license | **US$79 per installation** | One license per machine running the daemon. The phones and browsers you read it on are not counted. Perpetual: the license does not expire. Includes 12 months of updates from purchase; after that the copy you have keeps working forever and new builds need a renewal. |
| Account / sign-in | $0, optional | Core git management (repo grid, fetch, commit, push, history, diffs) is fully self-hosted and works offline with no account. "Sign in with Connections" is only needed for the remote tunnel and optional settings sync, and is off by default. |
| Source code | $0 | https://github.com/LunarWerxs/RepoYeti, PolyForm Noncommercial 1.0.0. Bundled file-type icons are from vscode-icons under a separate CC BY-SA license. |

Buy a commercial license:
https://checkout.connections.icu/licence/3fd2c9a5-0806-428f-b0fd-4a1ff7898fcd

Checkout is handled by Connections, which is the name that appears on the receipt and the card
statement. Volume pricing for a team is available; ask on Discord (https://discord.gg/PsWpeNUzhk).

## Costs the user actually bears (bring-your-own)

RepoYeti itself never charges for these; any cost comes from a third-party service the user chooses to connect.

| Feature | What it needs | Who sets the price |
|---|---|---|
| AI Smart Commit | An API key for one of: Groq, OpenAI, Claude, Gemini, OpenRouter, or DeepSeek | The AI provider, not LunarWerx. Groq is the suggested default and has a free tier that covers typical use (about 30 seconds to set up). Usage beyond a provider's free tier is billed by that provider, at that provider's rates. RepoYeti does not mark it up or take a cut. |
| Remote access tunnel | `cloudflared`, installed separately | Cloudflare's free tunnel tier; no RepoYeti charge. |

## What "free" does not include

- Hardware and hosting: RepoYeti runs on hardware the user already owns (their own computer stays on for the daemon to be reachable).
- Any AI provider costs above that provider's free tier, if the user exceeds it.

## License

PolyForm Noncommercial 1.0.0, starting with RepoYeti 1.0.0. Earlier MIT grants remain in effect for earlier copies. Third-party components retain their own licenses. Full text: https://github.com/LunarWerxs/RepoYeti/blob/main/LICENSE

## Current version

v1.0.1, https://github.com/LunarWerxs/RepoYeti/releases

## Links

- Home: https://repoyeti.com/
- Full brief: https://repoyeti.com/llms-full.txt
- Source: https://github.com/LunarWerxs/RepoYeti
