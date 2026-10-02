export default {
  defaultTheme: 'dark',
  iconLinks: [{ icon: 'github', href: 'https://github.com/iolys-company/docs', title: 'GitHub' }],
  start: () => {
    // Match the public site's wordmark: the compass replaces the "o".
    const brand = document.querySelector('.navbar-brand');
    const logo = brand?.querySelector('#logo');
    if (logo) {
      const letters = ['i', 'lys'].map(text => {
        const span = document.createElement('span');
        span.textContent = text;
        span.setAttribute('aria-hidden', 'true');
        return span;
      });
      logo.alt = '';
      brand.setAttribute('aria-label', 'iolys documentation home');
      brand.replaceChildren(letters[0], logo, letters[1]);
    }

    document.querySelector('meta[name="loc:inThisArticle"]')?.setAttribute('content', 'On this page');
    const article = document.querySelector('article');
    if (article) {
      article.id = 'main-content';
      article.tabIndex = -1;
      const skip = document.createElement('a');
      skip.className = 'skip-link';
      skip.href = '#main-content';
      skip.textContent = 'Skip to content';
      document.body.prepend(skip);
    }

    const search = document.getElementById('search-query');
    if (search) {
      search.placeholder = 'Search documentation';
      search.setAttribute('aria-keyshortcuts', 'Control+k Meta+k');
      document.addEventListener('keydown', event => {
        if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
          event.preventDefault();
          const panel = document.getElementById('navpanel');
          if (panel && !panel.classList.contains('show') && window.innerWidth < 768) {
            document.querySelector('[data-bs-target="#navpanel"]')?.click();
          }
          search.focus();
        }
      });
    }

    // Keep screenshots readable without leaving the article.
    const viewer = document.createElement('dialog');
    viewer.className = 'image-viewer';
    viewer.setAttribute('aria-label', 'Full-size image');
    const close = document.createElement('button');
    close.type = 'button';
    close.className = 'image-viewer-close';
    close.textContent = '×';
    close.setAttribute('aria-label', 'Close image');
    close.autofocus = true;
    const preview = document.createElement('img');
    viewer.append(close, preview);
    document.body.append(viewer);
    close.addEventListener('click', () => viewer.close());
    viewer.addEventListener('click', event => {
      if (event.target === viewer) viewer.close();
    });
    viewer.addEventListener('close', () => {
      document.documentElement.classList.remove('image-viewer-open');
      preview.removeAttribute('src');
    });

    document.querySelectorAll('article img').forEach(img => {
      img.loading = 'lazy';
      if (img.closest('a')) return;
      const link = document.createElement('a');
      link.href = img.src;
      link.className = 'screenshot-link';
      link.target = '_blank';
      link.rel = 'noopener';
      link.setAttribute('aria-label', `Open full-size image: ${img.alt}`);
      link.setAttribute('aria-haspopup', 'dialog');
      link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
        event.preventDefault();
        preview.src = img.currentSrc || img.src;
        preview.alt = img.alt;
        viewer.showModal();
        document.documentElement.classList.add('image-viewer-open');
      });
      img.replaceWith(link);
      link.append(img);
    });
  }
};
