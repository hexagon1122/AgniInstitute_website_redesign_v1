# Agni Institute website

Static redesign of [agniinstitute.org](https://agniinstitute.org) for Agni Institute, a 501(c)(3) nonprofit. The Institute is a volunteer community for Agni Yoga study, meditation training, and research into consciousness. Programs are offered free of charge.

## Repository layout

- `_build/` holds the Python static-site generator and the assets it copies into the site: `build.py`, `landing.py`, `pages.py`, `footer.html`, `styles.css`, `bios.json`, `_redirects`, `robots.txt`, favicons, and `assets/`.
- `_publish/` is the generated static site. It includes the HTML pages, styles, images, redirects, and `_publish/AYBooks/` (the Agni Yoga books as PDF and ePub).

## Rebuild

From the repository root:

```bash
python3 _build/build.py
```

The script writes `_publish/`. It removes the existing `_publish` directory, regenerates the HTML, and copies the book files from `/workspace/agni/AYBooks`. This repository already contains the finished `_publish` directory, including those books, and that copy is what gets deployed.

## Deploy

`_publish` is committed, so the host serves those files directly.

### Netlify

`netlify.toml` sets the publish directory to `_publish` and leaves the build command empty. In the Netlify site settings, use the same values:

- Publish directory: `_publish`
- Build command: empty

Turn on form detection in the Netlify site settings. The contact form in `contact.html` is a Netlify Form protected by reCAPTCHA (`data-netlify="true"` and `data-netlify-recaptcha="true"`). With form detection on, Netlify registers the form at deploy time and serves the reCAPTCHA widget.

Attach `agniinstitute.org` (and `www.agniinstitute.org` if you use it). Redirects in `_publish/_redirects` send `www` to the apex domain and map the old Drupal paths onto the new pages.
