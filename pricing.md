# RepoYeti pricing

Machine-readable summary for agents and buyers. Plain-language answer: **RepoYeti is free.**

## Product cost

| Item | Cost | Notes |
|---|---|---|
| RepoYeti daemon + dashboard | $0 | Free and open source, MIT license, copyright LunarWerx Studios. No purchase, subscription, trial limit, or seat count. |
| Account / sign-in | $0, optional | Core git management (repo grid, fetch, commit, push, history, diffs) is fully self-hosted and works offline with no account. "Sign in with Connections" is only needed for the remote tunnel and optional settings sync, and is off by default. |
| Source code | $0 | https://github.com/LunarWerxs/RepoYeti, MIT licensed. Bundled file-type icons are from vscode-icons under a separate CC BY-SA license. |

There is no paid tier, no usage cap, and no feature gated behind payment.

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

MIT. Full text: https://github.com/LunarWerxs/RepoYeti/blob/main/LICENSE

## Current version

v0.21.5, https://github.com/LunarWerxs/RepoYeti/releases

## Links

- Home: https://repoyeti.com/
- Full brief: https://repoyeti.com/llms-full.txt
- Source: https://github.com/LunarWerxs/RepoYeti
