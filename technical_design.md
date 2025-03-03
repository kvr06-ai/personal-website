# Technical Design Document: Personal Research Website and Blog

## 1. Project Overview
This document outlines the technical design for a personal website and blog to establish your online presence as a scientist with nearly a decade of experience in the tech industry, including four years at Amazon developing statistical and time series forecasting models. The website will emphasize your research interests in applying deep reinforcement learning (DRL) to multi-agent systems, game-theoretic principles (e.g., mechanism design), and neuroeconomic principles (e.g., neural and computational decision-making). It will feature a professional homepage with links to your CV and Medium profile, a blog for technical articles, interactive demos, an about page, and a publications page.

## 2. Objectives
Showcase Expertise: Highlight your professional background and research in DRL, game theory, and neuroeconomics.

Engage Visitors: Provide technical articles and interactive demos to demonstrate complex concepts.

Professional Accessibility: Ensure easy access to your CV and Medium profile.

Future-Proofing: Design a scalable and maintainable platform for ongoing content updates.

## 3. Functional Requirements
### 3.1 Homepage
Introduction Section:
Brief bio: "Scientist with nearly a decade in tech, including four years at Amazon building forecasting models impacting billions in revenue."

Summary of research interests: DRL for multi-agent systems, game theory, neuroeconomics.

External Links:
Prominent link to your CV (PDF or static page).

Link to your Medium profile for additional technical writings.

Content Previews:
Display links to the latest blog posts.

Showcase featured interactive demos.

Navigation Menu:
Links to Homepage, Blog, Demos, About, Publications, CV, and Medium.

### 3.2 Blog
Article Listings:
Display post titles, summaries, publication dates, and categories/tags (e.g., "DRL," "Game Theory").

Individual Post Pages:
Full article content with support for:
LaTeX-rendered mathematical equations.

Syntax-highlighted code snippets (e.g., Python, Julia).

Embedded images or diagrams.

Organization:
Categories or tags for filtering content.

Search:
Basic search functionality for blog posts.

### 3.3 Demos
Gallery Layout:
List of interactive demonstrations with titles and descriptions.

Interactivity:
Embed demos allowing users to manipulate parameters and view results (e.g., RL simulations, game-theoretic models).

Technical Support:
Compatibility with JavaScript-based or WebAssembly-based implementations.

### 3.4 About
Detailed Summary:
Expanded bio covering your Amazon experience and research goals.

Contact:
Include a contact form or email link.

### 3.5 Publications
Publication List:
Entries with paper titles, co-authors, venues, and links (PDFs or DOIs).

Layout:
Clean, academic-style formatting.

### 3.6 CV
Delivery Method:
Option 1: Link to a downloadable PDF.

Option 2: Static page with CV content.

Recommendation:
Use a PDF link for simplicity and professionalism.

### 3.7 Medium Profile
External Linking:
Direct link to your Medium profile, opening in a new tab.

Accessibility:
Featured on the homepage and navigation menu.

## 4. Non-Functional Requirements
### 4.1 Performance
Load Speed:
Target page load times under 2 seconds.

Optimization:
Minimize JS/CSS payloads and optimize images.

### 4.2 Accessibility
Standards:
Comply with WCAG 2.1 guidelines (e.g., alt text, keyboard navigation).

Design:
High-contrast colors and legible typography.

### 4.3 Security
Encryption:
Enforce HTTPS for all connections.

Dependencies:
Limit and vet third-party scripts.

### 4.4 Scalability
Content Growth:
Support adding new blog posts, demos, and publications without structural changes.

Modularity:
Use a modular architecture for extensibility.

### 4.5 Responsiveness
Device Compatibility:
Fully responsive design for desktop, tablet, and mobile.

### 4.6 Search Engine Optimization (SEO)
Metadata:
Include meta tags for titles, descriptions, and keywords.

Structure:
Generate a sitemap for indexing.

## 5. Technical Architecture
### 5.1 Static Site Generator
Tool: Pelican
Rationale: Python-based, Markdown support, extensible, aligns with your technical expertise.

Capabilities: Generates static HTML from Markdown, supports LaTeX and plugins.

### 5.2 Frontend
Core Technologies:
HTML for structure.

CSS for styling.

JavaScript for interactivity.

Libraries:
p5.js: Lightweight animations and simulations.

Plotly: Interactive plots and visualizations.

D3.js: Optional for advanced data-driven graphics.

### 5.3 Mathematical Rendering
Tool: KaTeX or MathJax
Purpose: Efficiently render LaTeX equations in blog posts and demos.

### 5.4 Version Control
System: Git
Hosting: GitHub repository for source code management.

### 5.5 Hosting
Platform: Netlify or GitHub Pages
Benefits: Free static site hosting, HTTPS, CDN support, auto-deployment from GitHub.

### 5.6 Domain
Custom Domain: 
Specification: Configure a domain (e.g., yourname.com) for branding.

## 6. Design Decisions
### 6.1 Content Management
Format: Markdown files for blog posts and static pages.

Directory Structure:
content/blog/: Blog articles.

content/pages/: Static pages (homepage, about, etc.).

content/demos/: Demo pages with embedded scripts.

static/: Assets (CSS, JS, images, CV PDF).

### 6.2 Interactive Demos
Implementation: JavaScript libraries or WebAssembly (e.g., Pyodide for Python).

Fallback: Static images or text descriptions if interactivity fails.

### 6.3 CV and Medium Integration
Placement: Prominent buttons/links on homepage, repeated in navigation menu.

CV Hosting: PDF stored in static/ directory.

Medium Link: Configured as an external URL in site settings.

### 6.4 Search Functionality
Approach: Use Pelican plugin (e.g., tipue_search) or external service (e.g., Algolia).

### 6.5 Analytics
Tool: Privacy-focused option like Plausible or Fathom.

Purpose: Track usage without invasive data collection.

### 6.6 Styling
Theme: Minimalistic, professional Pelican theme (e.g., Flex).

Customization: Custom CSS for branding and accessibility tweaks.

### 7. User Experience (UX) Considerations
Navigation: Clear, consistent menu across all pages.

Readability: Minimum 16px font size, adequate spacing for technical content.

Demo Guidance: Include brief instructions or tooltips for interactivity.

Feedback: Loading indicators for demos or dynamic content.

### 8. Maintenance and Updates
Content Addition: New blog posts/demos added via Markdown files in respective directories.

CV Updates: Replace PDF in static/ directory.

Medium Link: Update configuration if profile URL changes.

### 9. Testing and Quality Assurance
Scope:
Cross-browser compatibility (Chrome, Firefox, Safari, Edge).

Accessibility checks (e.g., Lighthouse audit).

Performance benchmarks (e.g., image compression, minified assets).

### 10. Deployment
Process: Continuous deployment via Netlify/GitHub Pages from GitHub.

Domain Setup: DNS configuration for custom domain with HTTPS.

### 11. Future Enhancements
Comments: Lightweight system (e.g., utterances) for blog interaction.

Newsletter: Subscription form for updates.

Multilingual: Support additional languages if desired.

