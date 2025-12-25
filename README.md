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

### 🚀 Quick Start in Google Antigravity

1. **Install Antigravity**  
   Download and install from [https://antigravity.google/download](https://antigravity.google/download)  
   (supports Windows, macOS, Linux)

2. **Create a new project**  
   Open Antigravity → **File** → **New Project**  
   Choose an empty folder or clone this repository directly into it

3. **Set Claude 4.5 Opus as primary model**  
   Go to **Settings** → **Models**  
   Select **Claude 4.5 Opus** and add your Anthropic API key

4. **Install recommended MCP servers**  
   Use the built-in marketplace (one-click install) or manual config for:  
   - Context retrieval (e.g. Context7 or Mem0)  
   - Task queue / manager  
   - Browser automation & control  
   - Vision / screenshot analysis (highly recommended for landing page review)

5. **Prepare your project docs (most important step!)**  
   Fill the `docs/` folder with key information:  
   - Create `docs/01-product.md`: product name, one-liner, core benefits, pricing  
   - Add `docs/02-audience.md`: target customer profile, pains, desires  
   - Include `docs/03-competitors.md`: 3–5 reference URLs + what you like/hate

6. **Start generating with Agent Manager**  
   Open **Agent Manager** view  
   Dispatch agents in this recommended order:  
   **Strategist** → **Copywriter** → **Structure** → **Design** → **Codegen** → **SEO** → **Browser** → **Reviewer**

7. **Review Artifacts**  
   Check the **Artifacts** tab for:  
   - Generated copy blocks  
   - Screenshots & browser recordings  
   - Code files & plans  
   → This is where you validate visual & conversion quality

8. **Version control & deploy**  
   Use Antigravity's built-in git tools or your `git_agent`:  
   → Commit changes → Create PR → Review → Merge  
   → Manually trigger preview deploy to Vercel / Netlify / Cloudflare Pages

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

### Pro Tips for Antigravity (Dec 2025)

- **Start small** — Generate only the hero section first to test the full pipeline quickly
- **Use Artifacts heavily** — Screenshots, browser recordings, and plans are gold for reviewing landing page quality
- **Keep browser control minimal** — Limit permissions to only necessary domains (strong security practice)
- **Save good agent configs** — Export and store successful agent profiles as templates in `.antigravity/agents.json`
- **Automate production deploys** — After merge, use git + Vercel/Netlify webhook for instant preview links
- **Review in Artifacts tab** — Always check visual output (screenshots/recordings) before approving code
- **Iterate fast** — Dispatch Reviewer agent after each major section to catch issues early

## License

MIT © 2025 [Your Name / Organization]

## Happy Building!

Let the agents create your next high-converting landing page on Antigravity! 🚀
