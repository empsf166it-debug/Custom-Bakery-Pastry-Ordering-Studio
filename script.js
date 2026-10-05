// Shared Logic for all pages
document.addEventListener('DOMContentLoaded', () => {
    // Initialize AOS Animation Library
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,
            once: true,
            offset: 50,
            easing: 'ease-out-cubic'
        });
    }

    // Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeToggleBtnMobile = document.getElementById('theme-toggle-mobile');
    const root = document.documentElement;
    
    function setTheme(isDark) {
        if (isDark) {
            root.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        } else {
            root.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        }
    }

    if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        setTheme(true);
    } else {
        setTheme(false);
    }

    const toggleTheme = () => setTheme(!root.classList.contains('dark'));
    if (themeToggleBtn) themeToggleBtn.addEventListener('click', toggleTheme);
    if (themeToggleBtnMobile) themeToggleBtnMobile.addEventListener('click', toggleTheme);

    // RTL Toggle
    const rtlToggleBtn = document.getElementById('rtl-toggle');
    const rtlToggleBtnMobile = document.getElementById('rtl-toggle-mobile');
    
    function setRTL(isRTL) {
        if (isRTL) {
            root.setAttribute('dir', 'rtl');
            localStorage.setItem('rtl', 'true');
        } else {
            root.setAttribute('dir', 'ltr');
            localStorage.setItem('rtl', 'false');
        }
    }

    if (localStorage.getItem('rtl') === 'true') {
        setRTL(true);
    }

    const toggleRTL = () => setRTL(root.getAttribute('dir') !== 'rtl');
    if (rtlToggleBtn) rtlToggleBtn.addEventListener('click', toggleRTL);
    if (rtlToggleBtnMobile) rtlToggleBtnMobile.addEventListener('click', toggleRTL);

    // Header Scroll Effect
    const header = document.getElementById('main-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('bg-white/90', 'dark:bg-brand-darkChoco/90', 'backdrop-blur-md', 'shadow-sm', 'py-3');
                header.classList.remove('bg-transparent', 'py-6');
            } else {
                header.classList.remove('bg-white/90', 'dark:bg-brand-darkChoco/90', 'backdrop-blur-md', 'shadow-sm', 'py-3');
                header.classList.add('bg-transparent', 'py-6');
            }
        });
    }

    // Mobile Menu
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMobileBtn = document.getElementById('close-mobile-menu');
    
    if (mobileBtn && mobileMenu) {
        mobileBtn.addEventListener('click', () => {
            const isRTL = root.getAttribute('dir') === 'rtl';
            const hideClass = isRTL ? '-translate-x-full' : 'translate-x-full';
            
            if (mobileMenu.classList.contains(hideClass)) {
                mobileMenu.classList.remove(hideClass);
                // Switch to 'X' close icon
                mobileBtn.innerHTML = '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>';
            } else {
                mobileMenu.classList.add(hideClass);
                // Switch back to hamburger icon
                mobileBtn.innerHTML = '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>';
            }
        });
    }

    // Magnetic Buttons
    document.querySelectorAll('.magnetic').forEach(btn => {
        btn.addEventListener('mousemove', e => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
        });
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = `translate(0px, 0px)`;
        });
    });

    // 3D Parallax effect on hover
    document.querySelectorAll('.parallax-container').forEach(container => {
        container.addEventListener('mousemove', e => {
            const el = container.querySelector('.parallax-element');
            if(el) {
                const rect = container.getBoundingClientRect();
                const x = (e.clientX - rect.left) / rect.width - 0.5;
                const y = (e.clientY - rect.top) / rect.height - 0.5;
                el.style.transform = `perspective(1000px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) scale(1.05)`;
            }
        });
        container.addEventListener('mouseleave', () => {
            const el = container.querySelector('.parallax-element');
            if(el) {
                el.style.transform = `perspective(1000px) rotateY(0deg) rotateX(0deg) scale(1)`;
            }
        });
    });

    // Menu Filtering
    const filterBtns = document.querySelectorAll('.filter-btn');
    const filterItems = document.querySelectorAll('.filter-item');

    if (filterBtns.length > 0 && filterItems.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active classes
                filterBtns.forEach(b => {
                    b.classList.remove('bg-[#C68E17]', 'text-white', 'border-[#C68E17]');
                    b.classList.add('bg-white', 'dark:bg-[#2A1300]', 'text-[#3E1C00]', 'dark:text-[#F5F5DC]', 'border-[#3E1C00]/10', 'dark:border-[#F5F5DC]/10');
                });
                
                // Add active to current
                btn.classList.add('bg-[#C68E17]', 'text-white', 'border-[#C68E17]');
                btn.classList.remove('bg-white', 'dark:bg-[#2A1300]', 'text-[#3E1C00]', 'dark:text-[#F5F5DC]', 'border-[#3E1C00]/10', 'dark:border-[#F5F5DC]/10');

                const filter = btn.getAttribute('data-filter');

                filterItems.forEach(item => {
                    if (filter === 'all' || item.getAttribute('data-category') === filter) {
                        item.style.display = ''; // Restore default flex/block layout
                        // Small animation pop
                        item.style.opacity = '0';
                        item.style.transform = 'scale(0.95)';
                        setTimeout(() => {
                            item.style.transition = 'all 0.5s ease';
                            item.style.opacity = '1';
                            item.style.transform = 'scale(1)';
                        }, 50);
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
    }

    // Highlight active mobile menu item
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const mobileLinks = document.querySelectorAll('#mobile-menu a');
    mobileLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.remove('text-[#3E1C00]', 'dark:text-[#F5F5DC]');
            link.classList.add('text-[#C68E17]', 'dark:text-[#C68E17]');
        }
    });
});
