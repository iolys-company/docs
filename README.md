# iolys documentation

English user documentation for [iolys](https://getiolys.com/), built with DocFX and the iolys Iolite Sun palette. The generated site has a searchable header, left navigation, an on-page outline, and previous/next article links.

## Build and preview

Install the .NET 10 SDK. DocFX **2.81.0** is pinned in `dotnet-tools.json`; no global tool installation is needed.

```powershell
dotnet tool restore --configfile NuGet.Config
dotnet docfx docfx.json --warningsAsErrors
pwsh -File scripts/check-site.ps1
dotnet docfx serve _site --port 8080
```

Open <http://localhost:8080>. Rebuild after editing Markdown or the theme. Generated output is in `_site/` and is not committed. Node.js is not required to build or serve the site.

## Publish with GitHub Pages

1. Push this repository to `iolys-company/docs` on GitHub.
2. In **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source.
3. Configure `docs.getiolys.com` as the custom domain in GitHub Pages settings, with its DNS pointing to GitHub Pages.
4. Push to `main` or manually run the **Documentation** workflow.
5. Open <https://docs.getiolys.com/> after the deployment succeeds.

The workflow restores the pinned tool, builds with warnings treated as errors, validates generated links and assets, and deploys `_site`. Pull requests run build and validation only. Deployment uses GitHub's Pages artifact and environment; it does not require a personal access token or a `gh-pages` branch.

The canonical domain is `https://docs.getiolys.com/`. The theme emits an absolute `rel="canonical"` link for each documentation page using `build.globalMetadata._siteUrl` and its generated HTML path, including `index.html`, matching the sitemap. The 404 page remains `noindex`. Content, assets, navigation, and search use relative links so local previews and project subpaths still work. The error page is self-contained so it also works for missing nested URLs.

## Crawler and AI discovery files

DocFX copies `llm.txt`, `llms.txt`, and `robots.txt` into the generated site. The two LLM files contain the same overview and links to the documentation's Markdown sources on GitHub; keep them identical when updating the guides. `llms.txt` is the conventional filename for AI discovery, while `llm.txt` provides an alternate URL. The site check requires all three files and the sitemap.

`robots.txt` allows crawling and points to `https://docs.getiolys.com/sitemap.xml`. It is published at the [host root required by crawlers](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt): `https://docs.getiolys.com/robots.txt`. When changing the public URL, update `build.globalMetadata._siteUrl` and `build.sitemap.baseUrl` in `docfx.json`, the sitemap URL in `robots.txt`, the documentation URL in both LLM files, and the recovery link in `404.html`.

## Edit the documentation

| Path | Responsibility |
| --- | --- |
| `index.md` | Introduction and entry points |
| `guide/` | Installation and everyday workflows |
| `providers/` | Provider setup, capabilities, and limitations |
| `customization/` | Permissions, tools, skills, agents, and MCP |
| `reference/` | Tool catalog, shortcuts, and data handling |
| `navigation/toc.yml` | Article hierarchy and previous/next order |
| `templates/iolys/layout/_master.tmpl` | DocFX modern layout with canonical URLs and the shared Marketplace button |
| `templates/iolys/public/main.css` | Brand colors and responsive layout |
| `templates/iolys/public/main.js` | Theme defaults, search shortcut, and screenshot links |
| `assets/` | Local brand assets, product screenshots, and explanatory diagrams |

Add a Markdown page, include it in `navigation/toc.yml`, and link to its `.md` path. DocFX rewrites those links to HTML. Give each page a title, description, and one H1. Use relative asset paths, descriptive image alt text, and screenshots with demonstration data.

Place screenshots beside the steps they illustrate and follow each with a short italic caption. Name the provider when showing provider-specific controls, and identify illustrative models or account values. Reuse existing assets rather than duplicating them. Keep explanatory diagrams in `assets/diagrams/` and give each SVG an accessible title and description. Record new image sources in `SOURCES.md`.

The theme extends DocFX's `default` and `modern` templates. Its master layout copies the pinned modern template with a canonical link and a **Get iolys** button linking to the Visual Studio Marketplace. The button stays visible outside the collapsed mobile menu; the self-contained 404 page also includes that link. Recheck the layout override when upgrading DocFX. Search, mobile navigation, theme switching, code copying, the page outline, and article navigation remain DocFX features. Press **Ctrl+K** (or **Command+K**) to focus search; clicking an image opens a large preview over the article. Close it with **Escape**, the close button, or a click outside the image.

## Content provenance and maintenance

The initial content was adapted from the existing Markdown documentation in `vs_assistant`, especially `docs/marketing/Product Features.md`, the provider guides, tool guides, and workflow documents. Current UI labels and implementation were checked where source documents disagreed. Draft specifications are not treated as evidence that a feature has shipped.

See [SOURCES.md](SOURCES.md) for the topic-to-source map. This public documentation intentionally describes the product's user workflows rather than exposing the source repository's internal API or build architecture. The iolys repositories are not build dependencies: all site content and referenced images live here.

When updating, check provider capabilities and menus, avoid fixed model or pricing inventories, and recheck screenshots for personal information. Run the build and link check before publishing.

Implementation references: [DocFX template customization](https://dotnet.github.io/docfx/docs/template.html) and [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
