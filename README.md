# Personal Research Website

A clean, responsive personal research website built with Pelican static site generator and the Clean Blog theme.

## Technology Stack

- [Pelican](https://getpelican.com/) - Python-based static site generator
- [Clean Blog](https://github.com/gilsondev/pelican-clean-blog) - A simple and elegant theme

## Setup for Local Development

1. Clone the repository:
   ```
   git clone https://github.com/kvr06-ai/personal-website.git
   cd personal-website
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install pelican markdown
   pip install pelican.plugins.render_math  # For math rendering
   ```

4. Generate the site:
   ```
   pelican content -o output -s pelicanconf.py
   ```

5. Preview the site locally:
   ```
   cd output
   python -m http.server 8000
   ```

6. Open your browser and navigate to `http://localhost:8000`

## Site Structure

- `content/` - Contains all the content (pages, articles)
- `pelicanconf.py` - Main configuration file
- `publishconf.py` - Production configuration
- `themes/` - Contains the Clean Blog theme

## Deployment

The site can be deployed to various platforms like GitHub Pages, Netlify, or any web server that supports static sites.

## License

MIT 