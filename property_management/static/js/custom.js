document.addEventListener("DOMContentLoaded", () => {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const content = document.getElementById('content');
    const navbarCollapse = document.getElementById('navbarNav');
    const overlay = document.createElement('div');

    // Create and append overlay
    overlay.className = 'collapse-overlay';
    document.body.appendChild(overlay);

    // Toggle blur and overlay
    navbarToggler.addEventListener('click', () => {
        const isCollapsed = navbarCollapse.classList.contains('show');
        if (isCollapsed) {
            content.classList.remove('blurred-content');
            overlay.classList.remove('show');
        } else {
            content.classList.add('blurred-content');
            overlay.classList.add('show');
        }
    });

    // Close navbar on overlay click
    overlay.addEventListener('click', () => {
        navbarToggler.click();
    });
});
