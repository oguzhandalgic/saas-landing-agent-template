# SaaS Landing Agent Template
**AI-First Autonomous SaaS Landing Page Generation & Iteration Workflow**

![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)
![Tailwind](https://img.shields.io/badge/Tailwind-3.4-38bdf8?logo=tailwindcss)
![Claude 4.5 Opus](https://img.shields.io/badge/Claude-4.5%20Opus-9F70D1?logo=anthropic)
![CrewAI](https://img.shields.io/badge/CrewAI-0.67+-FF6B6B?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Template for fully/semi-autonomous generation, iteration and continuous improvement of high-converting SaaS landing pages 
using **Claude 4.5 Opus** + **CrewAI** multi-agent system.

Agents handle strategy → messaging → copy → structure → design → code → SEO → Git workflow.

## ✨ Core Features

- End-to-end AI pipeline: strategy → copy → structure → design → code → SEO
- Strict Git workflow (feature branches → documented PRs → auto-review → merge)
- Multiple output formats supported: Next.js + Tailwind, Astro, plain HTML+CSS+JS
- One-command preview deployment (Vercel / Netlify / Cloudflare Pages)
- Brand voice, target audience, competitors & pricing injected via docs/
- Reusable high-quality prompt templates (hero, features, pricing, testimonials, CTA)
- Visual feedback loop via screenshot analysis (optional future extension)

## 📁 Project Structure

```text
saas-landing-agent-template/
├── docs/                       # Product description, audience, competitors, tone, references
├── agents/                     # All specialized landing page agents
│   ├── base_agent.py
│   ├── strategist_agent.py     # Positioning, audience, messaging, funnel
│   ├── copywriter_agent.py     # Headlines, benefits, social proof, objections
│   ├── structure_agent.py      # Optimal section order & hierarchy
│   ├── design_agent.py         # Colors, typography, spacing, animations
│   ├── codegen_agent.py        # Generates HTML/CSS/JS or React/Next.js code
│   ├── seo_agent.py            # Meta, schema, alt texts, keywords
│   └── git_agent.py            # Branch → commit → PR → review → merge
├── prompts/                    # High-quality reusable prompt templates
│   ├── hero.prompt
│   ├── features.prompt
│   ├── pricing.prompt
│   ├── testimonials.prompt
│   └── cta.prompt
├── src/                        # Generated landing page source code
│   ├── app/                    # Next.js app router (or pages/)
│   ├── components/
│   ├── styles/
│   └── public/
├── status.json                 # Current phase, generation status, last preview url
├── status.lock
├── crew.py                     # Main orchestrator - runs the full pipeline
├── requirements.txt
├── tailwind.config.js          # (if using Tailwind)
├── next.config.js              # (if using Next.js)
├── vercel.json                 # Deployment configuration
└── README.md
```

## 🚀 Quick Start

1. Create new repo from this template
2. Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Set secrets
```bash
export ANTHROPIC_API_KEY=sk-ant-...
export GITHUB_TOKEN=ghp_...
```
4. Describe your SaaS product
- Create docs/01-product.md (most important step!)
- Include: product name, one-liner, target audience, main benefits, pricing, competitors
5. Initialize status
```bash
echo '{"phase":"ideation", "status":"ready", "preview_url":""}' > status.json
```
6. Generate your landing page
```bash
python crew.py
```
→ → Agents create strategy → copy → structure → design → code → PR → review → merge → preview deploy

## 🔥 Most Important Agents & Their Focus

| Agent              | Primary Focus                                                                 |
|--------------------|-------------------------------------------------------------------------------|
| strategist        | Audience understanding, positioning, core message, conversion funnel          |
| copywriter        | High-conversion copy: headlines, subheads, benefits, social proof, objections |
| structure         | Optimal section order, visual hierarchy, above-the-fold impact                |
| design            | Color palette, typography, spacing system, micro-animations, mobile-first     |
| codegen           | Clean, modern code (Next.js/Tailwind, Astro, or plain HTML+CSS+JS)            |
| seo               | Technical SEO, meta tags, schema.org, image alts, keyword optimization        |
| git               | Enforces branch → commit → documented PR → auto-review → merge                |

## 📌 Recommended Prompt Quality Tips

• Use very specific audience descriptions (age, job title, pain points, tech stack)
• Provide 3–5 strong competitor examples with URLs
• Define tone of voice explicitly (confident/playful/professional/friendly/...)
• Include pricing model early (helps structure agent decide pricing section)
• Add visual references (dribbble shots, existing landing pages)

## 🚀 Recommended Free Deployment Targets

| Platform          | Best For                          | Free Tier Notes                     |
|-------------------|-----------------------------------|-------------------------------------|
| Vercel            | Next.js / React                   | Excellent preview deploys           |
| Netlify           | Astro / static + forms            | Great developer experience          |
| Cloudflare Pages  | Speed + global CDN                | Unlimited bandwidth                 |

## License

MIT © 2025 [Your Name / Organization]

## Happy Building!

Let the agents create your next high-converting landing page! 🚀
