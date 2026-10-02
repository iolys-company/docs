export default {
  defaultTheme: 'dark',
  iconLinks: [{ icon: 'github', href: 'https://github.com/iolys-company/docs', title: 'GitHub' }],
  start: () => {
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

    // Keep screenshots readable at full size with native browser navigation.
    document.querySelectorAll('article img').forEach(img => {
      img.loading = 'lazy';
      if (img.closest('a')) return;
      const link = document.createElement('a');
      link.href = img.src;
      link.className = 'screenshot-link';
      link.target = '_blank';
      link.rel = 'noopener';
      link.setAttribute('aria-label', `Open full-size image: ${img.alt}`);
      img.replaceWith(link);
      link.append(img);
    });
  }
};
