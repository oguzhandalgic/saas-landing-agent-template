# SaaS Landing Antigravity Template
**AI-First Autonomous SaaS Landing Page Generation & Iteration on Google Antigravity**

![Antigravity](https://img.shields.io/badge/Google-Antigravity-4285F4?logo=google)
![Claude 4.5 Opus](https://img.shields.io/badge/Claude-4.5%20Opus-9F70D1?logo=anthropic)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

Template optimized for **Google Antigravity** (public preview, Dec 2025) to build high-converting SaaS landing pages 
using Claude 4.5 Opus + multi-agent system + MCP integrations.

Leverage Agent Manager, Artifacts, browser control, git integration, and one-click MCP servers.

## ✨ Core Features

- Agent-first workflow inside Google Antigravity (no heavy Python orchestration needed)
- Native Claude 4.5 Opus support + full Anthropic API integration
- Artifacts: screenshots, browser recordings, plans — perfect for landing page review
- One-click MCP marketplace (context retrieval, task queue, browser control, vision)
- Built-in git support + optional git_agent for branch/PR/merge flow
- Persistent local project folder — no session timeouts
- Parallel agent execution via Agent Manager (strategist, copywriter, design, codegen, seo, etc.)

## 📁 Recommended Project Structure

```text
saas-landing-antigravity-template/
├── docs/                        # Product brief, audience, competitors, tone, visual refs
│   ├── 01-product.md
│   ├── 02-audience.md
│   ├── 03-competitors.md
│   └── 04-visual-references.md
├── prompts/                     # Reusable prompt templates (used by agents)
│   ├── hero.txt
│   ├── features.txt
│   ├── pricing.txt
│   ├── testimonials.txt
│   ├── cta.txt
│   └── seo-meta.txt
├── src/                         # Generated landing page code (any stack)
│   ├── index.html               # or app/page.tsx, Astro pages, etc.
│   ├── styles/
│   ├── components/
│   └── public/
├── .antigravity/                # Antigravity-specific config (optional but recommended)
│   ├── agents.json              # Pre-configured agent profiles
│   └── mcps.json                # Preferred MCP servers
├── README.md
├── .gitignore
└── requirements.txt             # Only needed if running Python scripts outside Antigravity
```

## 🚀 Quick Start in Google Antigravity

1. Install Antigravity
Download from https://antigravity.google/download (Windows/macOS/Linux)
2. Create new project
Open Antigravity → File → New Project → Choose folder or clone this repo
3. Set primary model
Settings → Models → Select Claude 4.5 Opus (add your Anthropic API key)
4. Install MCP servers
Use the marketplace (one-click) or manual config for: context retrieval, task queue, browser control, vision
5. Fill docs/ folder
Most important: create docs/01-product.md with product name, one-liner, benefits, audience, pricing
6. Start generating
Open Agent Manager → dispatch agents in order: Strategist → Copywriter → Structure → Design → Codegen → SEO → Browser → Reviewer
7. Review Artifacts
Check screenshots, browser recordings, generated copy & code in Artifacts tab
8. Version & deploy
Use built-in git or git_agent → commit → PR → merge → manual deploy to Vercel/Netlify
## 🔥 Key Agents & Their Focus

| Agent | Primary Focus | Recommended MCPs |
| --- | --- | --- |
| Strategist | Audience, positioning, messaging, funnel | Context retrieval |
| Copywriter | High-conversion headlines, benefits, social proof | None required |
| Structure | Optimal section order & hierarchy | Context retrieval |
| Design | Colors, typography, spacing, animations | Vision / Design MCP |
| Codegen | HTML/Tailwind/Next.js/Astro code generation | None required |
| SEO | Meta tags, schema.org, alt texts, keywords | Context retrieval |
| Browser | Open preview, take screenshots, record interaction | Browser control MCP |
| Reviewer | Critique conversion, design, copy & suggest fixes | Vision + Context |

## Recommended MCP Servers (install via Antigravity marketplace)

- Context retrieval (Context7, Mem0, or vector store)
- Task queue / manager
- Browser automation & control
- Vision / screenshot analysis
- Optional: Tailwind Design MCP, screenshot-to-code

## Pro Tips for Antigravity (Dec 2025)

• Start small: generate only hero section first
• Use Artifacts heavily — screenshots & recordings are gold
• Keep browser control permissions minimal (security)
• Save good agent configurations as templates in .antigravity/agents.json
• For production deploys: use git + Vercel/Netlify webhook after merge

## License

MIT © 2025 [Your Name / Organization]

## Happy Building!

Let the agents create your next high-converting landing page on Antigravity! 🚀
