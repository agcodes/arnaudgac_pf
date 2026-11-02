// Main JavaScript file for CV

document.addEventListener('DOMContentLoaded', function() {
    // Initialize HTMX
    htmx.logAll();
    
    // Log that the page loaded
    console.log('CV page loaded');
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add click handlers for experience cards
    document.querySelectorAll('.experience-card').forEach(card => {
        card.addEventListener('click', function() {
            // Toggle expanded state
            this.classList.toggle('expanded');
        });
    });
    
    // Animate stats on scroll
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-stats');
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.stats-number').forEach(stat => {
        statsObserver.observe(stat);
    });
    
    // Add HTMX indicators
    document.body.addEventListener('htmx:beforeRequest', function(evt) {
        const indicator = document.querySelector('.htmx-indicator');
        if (indicator) {
            indicator.style.display = 'block';
        }
    });
    
    document.body.addEventListener('htmx:afterRequest', function(evt) {
        const indicator = document.querySelector('.htmx-indicator');
        if (indicator) {
            indicator.style.display = 'none';
        }
    });
});

// HTMX config
htmx.config.globalViewTransitions = true;
