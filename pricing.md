# RepoYeti pricing

Machine-readable summary for agents and buyers. Plain-language answer: **RepoYeti 1.0.0 is free for purposes permitted by PolyForm Noncommercial 1.0.0.** Commercial use outside those permissions requires a separate license from LunarWerx Studios.

## Product cost

| Item | Cost | Notes |
|---|---|---|
| RepoYeti daemon + dashboard | $0 for permitted use | Source-available under PolyForm Noncommercial 1.0.0, copyright LunarWerx Studios. Consult the license for permitted purposes and organizational uses. |
| Account / sign-in | $0, optional | Core git management (repo grid, fetch, commit, push, history, diffs) is fully self-hosted and works offline with no account. "Sign in with Connections" is only needed for the remote tunnel and optional settings sync, and is off by default. |
| Source code | $0 | https://github.com/LunarWerxs/RepoYeti, PolyForm Noncommercial 1.0.0. Bundled file-type icons are from vscode-icons under a separate CC BY-SA license. |

Commercial licensing terms and pricing are arranged separately with LunarWerx Studios; no commercial price is quoted here.

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

v1.0.0, https://github.com/LunarWerxs/RepoYeti/releases

## Links

- Home: https://repoyeti.com/
- Full brief: https://repoyeti.com/llms-full.txt
- Source: https://github.com/LunarWerxs/RepoYeti
