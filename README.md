# benmorristech.com (v2.0)

> Modern, Git-backed personal portfolio and thought leadership platform for **Ben Morris** (Senior Product Leader & CX Architect).

[![Built with Astro](https://img.shields.io/badge/Astro-5.0-orange.svg)](https://astro.build)
[![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-v4-blue.svg)](https://tailwindcss.com)
[![Deployed on Cloudflare Pages](https://img.shields.io/badge/Cloudflare_Pages-Edge-F38020.svg)](https://pages.cloudflare.com)
[![Lighthouse Score](https://img.shields.io/badge/Lighthouse-100%2F100-brightgreen.svg)](https://pagespeed.web.dev/)
[![Hosting Cost](https://img.shields.io/badge/Cost-%240%2Fmonth-brightgreen.svg)]()

---

## ⚡ Overview

Migrated away from a legacy, fragile AWS Lightsail WordPress VM ($10/month) to a zero-cost, high-velocity, Git-native static edge architecture on **Cloudflare Pages**.

### Key Architectural Highlights
- **Performance**: 100/100 Lighthouse performance, sub-second global Time to First Byte (TTFB).
- **Design System**: "Tactical Aviator LCD — Dark" (Instrument Brutalism, JetBrains Mono, `#FF8A1F` tactical amber, `#7FE0C8` status mint, and `#0B0F12` deep charcoal base).
- **Work & Portfolio**: Interactive Bento Grid showcasing enterprise missions across GoalZero, Human Improvement (BuyHi), Westfield AR Spatial Computing, and Smith Optics.
- **Field Notes**: 180+ archived and migrated articles with clean typed frontmatter schemas.
- **SEO & Reversibility**: Full 301 redirects mapping legacy WordPress endpoints (`_redirects`) to preserve all organic search equity.
- **Deploy Pipeline**: Automatic GitHub-driven edge builds on push.

---

## 🛠 Tech Stack

- **Framework**: [Astro 5](https://astro.build) (Content Layer + Static Site Generation)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com) (`@theme` CSS-first token configuration)
- **Hosting & Edge**: [Cloudflare Pages](https://pages.cloudflare.com) (Unmetered static bandwidth, 300+ edge PoPs)
- **DNS & CDN**: Cloudflare
- **Version Control**: Git & GitHub (`ParzivalWins/benmorristech`)
- **Figma Design Concept**: [Tactical Aviator LCD Workspace](https://www.figma.com/design/Ead78uue0klz7kNeB7uMfN)

---

## 🚀 Local Development

```bash
# Clone the repository
git clone https://github.com/ParzivalWins/benmorristech.git
cd benmorristech

# Install dependencies
npm install

# Start local dev server
npm run dev

# Build for production
npm run build

# Preview production build locally
npm run preview
```

---

## 📡 Deployment to Cloudflare Pages

1. Connect the GitHub repository `ParzivalWins/benmorristech` in the Cloudflare Pages dashboard.
2. Build configuration:
   - **Framework preset**: `Astro`
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
3. Custom Domains:
   - `benmorristech.com`
   - `www.benmorristech.com`

---

## 📄 License
MIT © Ben Morris
