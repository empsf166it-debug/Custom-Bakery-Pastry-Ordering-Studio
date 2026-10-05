import os

header_html = """
<header id="main-header" class="fixed w-full z-50 transition-all duration-300 py-6 bg-transparent">
  <div class="container mx-auto px-6 flex justify-between items-center">
    <a href="index.html" class="flex items-center gap-3 group z-50">
      <div class="w-10 h-10 bg-[#D4AF37] rounded-full flex items-center justify-center transform group-hover:rotate-180 transition-transform duration-700">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 21h18M5 21V8l4 3 3-6 3 6 4-3v13"></path></svg>
      </div>
      <span class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] group-hover:text-[#C68E17] transition-colors">Maison Dorée</span>
    </a>
    
    <nav class="hidden xl:flex items-center gap-6">
      <a href="index.html" class="text-sm font-medium hover:text-[#C68E17] transition-colors relative after:absolute after:bottom-0 after:left-0 after:h-0.5 after:w-0 after:bg-[#C68E17] hover:after:w-full after:transition-all {active_home}">Home</a>
      <a href="studio.html" class="text-sm font-medium hover:text-[#C68E17] transition-colors relative after:absolute after:bottom-0 after:left-0 after:h-0.5 after:w-0 after:bg-[#C68E17] hover:after:w-full after:transition-all {active_studio}">Custom Cake Studio</a>
      <a href="menu.html" class="text-sm font-medium hover:text-[#C68E17] transition-colors relative after:absolute after:bottom-0 after:left-0 after:h-0.5 after:w-0 after:bg-[#C68E17] hover:after:w-full after:transition-all {active_menu}">Menu & Pastries</a>
      <a href="order.html" class="text-sm font-medium hover:text-[#C68E17] transition-colors relative after:absolute after:bottom-0 after:left-0 after:h-0.5 after:w-0 after:bg-[#C68E17] hover:after:w-full after:transition-all {active_order}">Order & Delivery</a>
      <a href="about.html" class="text-sm font-medium hover:text-[#C68E17] transition-colors relative after:absolute after:bottom-0 after:left-0 after:h-0.5 after:w-0 after:bg-[#C68E17] hover:after:w-full after:transition-all {active_about}">About Bakery</a>
      <a href="contact.html" class="text-sm font-medium hover:text-[#C68E17] transition-colors relative after:absolute after:bottom-0 after:left-0 after:h-0.5 after:w-0 after:bg-[#C68E17] hover:after:w-full after:transition-all {active_contact}">Contact</a>
      <a href="dashboard.html" class="text-sm font-medium hover:text-[#C68E17] transition-colors relative after:absolute after:bottom-0 after:left-0 after:h-0.5 after:w-0 after:bg-[#C68E17] hover:after:w-full after:transition-all {active_dashboard}">Dashboard</a>
    </nav>
    
    <div class="hidden xl:flex items-center gap-4">
      <button id="theme-toggle" class="p-2 rounded-full hover:bg-black/5 dark:hover:bg-white/10 transition-colors" title="Toggle Theme">
        <svg class="w-5 h-5 hidden dark:block" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
        <svg class="w-5 h-5 block dark:hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
      </button>

      <a href="login.html" class="magnetic px-6 py-2.5 bg-[#3E1C00] dark:bg-[#F5F5DC] text-[#FFFAF0] dark:text-[#3E1C00] rounded-full text-sm font-medium hover:bg-[#C68E17] dark:hover:bg-[#C68E17] dark:hover:text-white transition-colors">Sign In</a>
    </div>

    <div class="flex xl:hidden items-center gap-2 z-50">
        <button id="theme-toggle-mobile" class="p-2 rounded-full hover:bg-black/5 dark:hover:bg-white/10 transition-colors text-[#3E1C00] dark:text-[#F5F5DC]">
            <svg class="w-5 h-5 hidden dark:block" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
            <svg class="w-5 h-5 block dark:hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
        </button>
        <button class="p-2 text-[#3E1C00] dark:text-[#F5F5DC]" id="mobile-menu-btn">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        </button>
    </div>
  </div>
</header>

<!-- Mobile Menu Drawer -->
<div id="mobile-menu" class="fixed inset-y-0 right-0 w-64 bg-[#FFFAF0] dark:bg-[#1a0f08] shadow-2xl z-40 transform translate-x-full transition-transform duration-300 pt-24 px-6 flex flex-col gap-6 xl:hidden">
    <a href="index.html" class="text-lg font-medium text-[#3E1C00] dark:text-[#F5F5DC]">Home</a>
    <a href="studio.html" class="text-lg font-medium text-[#3E1C00] dark:text-[#F5F5DC]">Custom Cake Studio</a>
    <a href="menu.html" class="text-lg font-medium text-[#3E1C00] dark:text-[#F5F5DC]">Menu & Pastries</a>
    <a href="order.html" class="text-lg font-medium text-[#3E1C00] dark:text-[#F5F5DC]">Order & Delivery</a>
    <a href="about.html" class="text-lg font-medium text-[#3E1C00] dark:text-[#F5F5DC]">About Bakery</a>
    <a href="contact.html" class="text-lg font-medium text-[#3E1C00] dark:text-[#F5F5DC]">Contact</a>
    <a href="dashboard.html" class="text-lg font-medium text-[#3E1C00] dark:text-[#F5F5DC]">Dashboard</a>
    <hr class="border-[#3E1C00]/10 dark:border-[#F5F5DC]/10">
    <a href="login.html" class="mt-4 px-6 py-3 text-center bg-[#3E1C00] dark:bg-[#F5F5DC] text-[#FFFAF0] dark:text-[#3E1C00] rounded-full text-sm font-medium">Sign In</a>
</div>
"""

footer_html = """
<footer class="bg-[#2A1300] text-[#F5F5DC] pt-20 pb-4">
    <div class="container mx-auto px-6">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
            <div data-aos="fade-up">
                <a href="index.html" class="flex items-center gap-3 mb-6 group">
                    <div class="w-10 h-10 bg-[#D4AF37] rounded-full flex items-center justify-center transform group-hover:rotate-180 transition-transform duration-700">
                        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 21h18M5 21V8l4 3 3-6 3 6 4-3v13"></path></svg>
                    </div>
                    <span class="text-2xl font-serif font-bold text-[#F5F5DC]">Maison Dorée</span>
                </a>
                <p class="text-white/70 mb-6 leading-relaxed">Where artistry meets pastry. Creating unforgettable moments through bespoke baked goods.</p>
                <div class="flex gap-4">
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-[#C68E17] hover:-translate-y-1 transition-all duration-300">
                        <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-[#C68E17] hover:-translate-y-1 transition-all duration-300">
                        <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-[#C68E17] hover:-translate-y-1 transition-all duration-300">
                        <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                    </a>
                </div>
            </div>
            
            <div data-aos="fade-up" data-aos-delay="100">
                <h4 class="font-serif text-xl mb-6 font-semibold">Quick Links</h4>
                <ul class="space-y-3">
                    <li><a href="studio.html" class="text-white/70 hover:text-[#C68E17] transition-colors">Custom Cake Studio</a></li>
                    <li><a href="menu.html" class="text-white/70 hover:text-[#C68E17] transition-colors">Menu & Pastries</a></li>
                    <li><a href="order.html" class="text-white/70 hover:text-[#C68E17] transition-colors">Order & Delivery</a></li>
                    <li><a href="about.html" class="text-white/70 hover:text-[#C68E17] transition-colors">About</a></li>
                    <li><a href="contact.html" class="text-white/70 hover:text-[#C68E17] transition-colors">Contact</a></li>
                </ul>
            </div>
            
            <div data-aos="fade-up" data-aos-delay="200">
                <h4 class="font-serif text-xl mb-6 font-semibold">Visit Us</h4>
                <ul class="space-y-3 text-white/70">
                    <li>123 Patisserie Lane, Bakery District</li>
                    <li>City, Country 12345</li>
                    <li class="pt-2 text-[#C68E17]">hello@maisondoree.com</li>
                    <li>+1 (234) 567-8900</li>
                </ul>
            </div>
            
            <div data-aos="fade-up" data-aos-delay="300">
                <h4 class="font-serif text-xl mb-6 font-semibold">Newsletter</h4>
                <p class="text-white/70 mb-4 text-sm">Subscribe to receive sweet updates and seasonal offers.</p>
                <form class="flex gap-2">
                    <input type="email" placeholder="Your email address" class="bg-white/5 border border-white/10 rounded-lg px-4 py-2 w-full text-white placeholder-white/40 focus:outline-none focus:border-[#C68E17] transition-colors">
                    <button type="button" class="bg-[#C68E17] text-white px-4 py-2 rounded-lg hover:bg-[#D4AF37] transition-colors">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </button>
                </form>
            </div>
        </div>
        
        <div class="border-t border-white/10 pt-4 flex flex-col md:flex-row justify-between items-center text-xs text-white/50">
            <p>&copy; 2026 Maison Dorée. All rights reserved.</p>
            <div class="flex gap-4 mt-4 md:mt-0">
                <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
                <a href="#" class="hover:text-white transition-colors">Terms of Service</a>
            </div>
            <button type="button" id="back-to-top" aria-label="Back to top" onclick="window.scrollTo({top:0,behavior:'smooth'})" class="mt-3 md:mt-0 w-8 h-8 rounded-full border border-[#C68E17] text-[#C68E17] flex items-center justify-center hover:bg-[#C68E17] hover:text-white hover:-translate-y-1 transition-all duration-300">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"></path></svg>
            </button>
        </div>
    </div>
</footer>
"""

base_html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maison Dorée | {title}</title>
    <meta name="description" content="Premium Custom Bakery & Pastry Ordering Studio">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            ivory: '#FFFAF0',
                            cream: '#FFFDD0',
                            choco: '#3E1C00',
                            caramel: '#C68E17',
                            beige: '#F5F5DC',
                            gold: '#D4AF37',
                            darkChoco: '#2A1300'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="antialiased overflow-x-hidden">
    {header}
    
    <main>
    {content}
    </main>
    
    {footer}
    
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="script.js"></script>
    {extra_js}
</body>
</html>
"""

pages = {}

# 1. INDEX.HTML (4 sections)
pages['index.html'] = {
    'title': 'Home',
    'active': 'active_home',
    'extra_js': '',
    'content': """
    <!-- Section 1: Cinematic Hero -->
    <section class="relative min-h-screen flex items-center overflow-hidden bg-[#FFFAF0] dark:bg-[#1a0f08]">
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1464195244916-405fa0a82545?q=80&w=2070&auto=format&fit=crop" class="w-full h-full object-cover opacity-10 dark:opacity-5" alt="Bakery Background">
        </div>
        
        <!-- Floating 3D Elements -->
        <div class="absolute top-[10%] left-4 w-16 h-16 opacity-60 floating z-10 hidden lg:block">
            <img src="https://images.unsplash.com/photo-1550617931-e17a7b70dce2?w=500&auto=format&fit=crop" class="rounded-full object-cover w-full h-full shadow-2xl" alt="Floating Cupcake">
        </div>
        <div class="absolute bottom-1/4 right-20 w-32 h-32 floating-slow z-10 hidden lg:block opacity-70">
            <img src="https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?w=500&auto=format&fit=crop" class="rounded-full object-cover w-full h-full shadow-2xl opacity-80" alt="Floating Macaron">
        </div>

        <div class="container mx-auto px-6 relative z-20 pt-20">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <div class="w-full lg:w-1/2" data-aos="fade-right" data-aos-duration="1500">
                    <div class="inline-block px-4 py-2 rounded-full border border-[#C68E17] text-[#C68E17] text-sm font-medium mb-6">Maison Dorée Signature Studio</div>
                    <h1 class="text-5xl lg:text-7xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] leading-tight mb-6">
                        Your Imagination,<br>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#C68E17] to-[#D4AF37]">Baked Beautifully.</span>
                    </h1>
                    <p class="text-lg text-[#3E1C00]/80 dark:text-[#F5F5DC]/80 mb-10 max-w-lg">Experience the pinnacle of pastry art. We craft bespoke cakes and luxury desserts that transform your celebrations into unforgettable memories.</p>
                    <div class="flex flex-wrap gap-4">
                        <a href="studio.html" class="magnetic px-8 py-4 bg-[#3E1C00] dark:bg-[#F5F5DC] text-[#FFFAF0] dark:text-[#3E1C00] rounded-full font-medium hover:bg-[#C68E17] transition-all shadow-xl hover:shadow-2xl">Create Your Cake</a>
                        <a href="menu.html" class="magnetic px-8 py-4 bg-transparent border-2 border-[#3E1C00] dark:border-[#F5F5DC] text-[#3E1C00] dark:text-[#F5F5DC] rounded-full font-medium hover:bg-[#3E1C00] hover:text-[#FFFAF0] dark:hover:bg-[#F5F5DC] dark:hover:text-[#1a0f08] transition-all">Explore Menu</a>
                    </div>
                </div>
                
                <div class="w-full lg:w-1/2 relative perspective-1000">
                    <div class="parallax-container w-full h-[400px] lg:h-[450px] rounded-[2rem] overflow-hidden shadow-2xl clip-reveal" data-aos="fade-left" data-aos-duration="2000">
                        <img src="https://images.unsplash.com/photo-1621303837174-89787a7d4729?q=80&w=1936&auto=format&fit=crop" class="w-full h-full object-cover parallax-element scale-110 transition-transform duration-700" alt="Premium Custom Cake">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Interactive Cake Customizer Preview -->
    <section class="py-32 bg-white dark:bg-[#2A1300] relative overflow-hidden">
        <div class="container mx-auto px-6 relative z-10">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-4xl lg:text-5xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-4">Design Your Masterpiece</h2>
                <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 max-w-2xl mx-auto">Preview our custom cake studio and get a live estimate.</p>
            </div>
            
            <div class="flex flex-col lg:flex-row gap-8 items-center bg-[#FFFAF0] dark:bg-[#1a0f08] rounded-3xl p-6 lg:p-8 shadow-2xl max-w-5xl mx-auto">
                <div class="w-full lg:w-1/2 relative h-[350px] flex items-center justify-center hover-3d-tilt transition-transform duration-500" data-aos="zoom-in">
                    <!-- Layered Cake Visual -->
                    <img id="preview-cake" src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800&auto=format&fit=crop" class="w-4/5 h-full object-cover rounded-2xl shadow-lg z-20" alt="Cake Preview">
                    <div class="absolute -bottom-6 -right-6 w-32 h-32 bg-[#C68E17]/20 rounded-full blur-2xl z-0"></div>
                </div>
                
                <div class="w-full lg:w-1/2" data-aos="fade-left">
                    <div class="space-y-6">
                        <div>
                            <h3 class="text-lg font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-3">Cake Size</h3>
                            <div class="flex gap-3">
                                <button class="preview-opt active px-4 py-2 border border-[#C68E17] bg-[#C68E17] text-white rounded-lg" data-price="45">6"</button>
                                <button class="preview-opt px-4 py-2 border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-lg text-[#3E1C00] dark:text-[#F5F5DC] hover:border-[#C68E17]" data-price="65">8"</button>
                                <button class="preview-opt px-4 py-2 border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-lg text-[#3E1C00] dark:text-[#F5F5DC] hover:border-[#C68E17]" data-price="85">10"</button>
                            </div>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-3">Flavor Base</h3>
                            <div class="flex flex-wrap gap-3">
                                <button type="button" class="flavor-opt px-4 py-2 border border-[#C68E17] bg-[#C68E17] text-white rounded-lg transition-colors">Vanilla</button>
                                <button type="button" class="flavor-opt px-4 py-2 border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-lg text-[#3E1C00] dark:text-[#F5F5DC] hover:border-[#C68E17] transition-colors">Chocolate</button>
                                <button type="button" class="flavor-opt px-4 py-2 border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-lg text-[#3E1C00] dark:text-[#F5F5DC] hover:border-[#C68E17] transition-colors">Red Velvet</button>
                            </div>
                        </div>
                        
                        <div class="pt-6 border-t border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 flex flex-col sm:flex-row items-start sm:items-end justify-between gap-4 sm:gap-0">
                            <div>
                                <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 mb-1">Estimated Price</p>
                                <p class="text-4xl font-serif font-bold text-[#C68E17]">$<span id="live-price">45.00</span></p>
                            </div>
                            <a href="studio.html" class="magnetic w-full sm:w-auto text-center px-6 py-3 bg-[#3E1C00] dark:bg-[#F5F5DC] text-[#FFFAF0] dark:text-[#3E1C00] rounded-lg font-medium hover:bg-[#C68E17] transition-colors">Full Customizer →</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script>
            document.querySelectorAll('.flavor-opt').forEach(btn => {
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.flavor-opt').forEach(b => {
                        b.classList.remove('bg-[#C68E17]', 'text-white', 'border-[#C68E17]');
                        b.classList.add('border-[#3E1C00]/20', 'dark:border-[#F5F5DC]/20', 'text-[#3E1C00]', 'dark:text-[#F5F5DC]');
                    });
                    btn.classList.add('bg-[#C68E17]', 'text-white', 'border-[#C68E17]');
                    btn.classList.remove('border-[#3E1C00]/20', 'dark:border-[#F5F5DC]/20', 'text-[#3E1C00]', 'dark:text-[#F5F5DC]');
                });
            });
            document.querySelectorAll('.preview-opt').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    document.querySelectorAll('.preview-opt').forEach(b => {
                        b.classList.remove('bg-[#C68E17]', 'text-white', 'border-[#C68E17]', 'active');
                        b.classList.add('border-[#3E1C00]/20', 'dark:border-[#F5F5DC]/20');
                    });
                    e.target.classList.add('bg-[#C68E17]', 'text-white', 'border-[#C68E17]', 'active');
                    e.target.classList.remove('border-[#3E1C00]/20', 'dark:border-[#F5F5DC]/20');
                    
                    const price = e.target.getAttribute('data-price');
                    const priceEl = document.getElementById('live-price');
                    // animate count
                    let current = parseInt(priceEl.innerText);
                    let target = parseInt(price);
                    let step = target > current ? 1 : -1;
                    let timer = setInterval(() => {
                        current += step;
                        priceEl.innerText = current + ".00";
                        if(current === target) clearInterval(timer);
                    }, 20);
                });
            });
        </script>
    </section>

    <!-- Section 3: Signature Pastry Experience -->
    <section class="py-32 bg-[#FFFAF0] dark:bg-[#1a0f08]">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-4xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-4">Signature Pastries</h2>
                <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 mb-6 max-w-2xl mx-auto">Each creation is meticulously crafted using the finest seasonal ingredients, combining classic French techniques with modern flavor profiles.</p>
                <a href="menu.html" class="inline-flex items-center gap-2 text-[#3E1C00] dark:text-[#F5F5DC] font-bold hover:text-[#C68E17] transition-colors">
                    View Full Menu
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </a>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Item 1 -->
                <div class="relative group h-[400px] rounded-3xl overflow-hidden shadow-xl" data-aos="fade-up" data-aos-delay="0">
                    <img src="https://images.unsplash.com/photo-1588195538326-c5b1e9f80a1b?q=80&w=1950&auto=format&fit=crop" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-1000" alt="Signature Cake">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent transition-opacity"></div>
                    <div class="absolute bottom-8 left-8 right-8">
                        <h3 class="text-2xl font-serif font-bold text-white mb-2">The Royal Framboise</h3>
                        <p class="text-white/80 text-sm mb-4">Almond sponge, fresh raspberry confit, and whipped white chocolate ganache.</p>
                        <a href="menu.html" class="text-[#C68E17] font-medium hover:underline text-sm">View Details</a>
                    </div>
                </div>
                
                <!-- Item 2 -->
                <div class="relative group h-[400px] rounded-3xl overflow-hidden shadow-xl" data-aos="fade-up" data-aos-delay="200">
                    <img src="https://images.unsplash.com/photo-1558961363-fa8fdf82db35?q=80&w=1965&auto=format&fit=crop" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" alt="Macarons">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent transition-opacity"></div>
                    <div class="absolute bottom-8 left-8 right-8 text-white">
                        <h3 class="text-2xl font-serif font-bold mb-2">Parisian Macarons</h3>
                        <p class="text-white/80 text-sm mb-4">A delicate balance of crisp shells and rich ganache, crafted in signature flavors.</p>
                        <a href="menu.html" class="text-[#C68E17] font-medium hover:underline text-sm">View Details</a>
                    </div>
                </div>
                
                <!-- Item 3 -->
                <div class="relative group h-[400px] rounded-3xl overflow-hidden shadow-xl md:col-span-2 lg:col-span-1 md:w-[calc(50%-1rem)] lg:w-full mx-auto" data-aos="fade-up" data-aos-delay="400">
                    <img src="https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=800&auto=format&fit=crop" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" alt="Chocolate Truffles">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent transition-opacity"></div>
                    <div class="absolute bottom-8 left-8 right-8 text-white">
                        <h3 class="text-2xl font-serif font-bold mb-2">Artisan Chocolates</h3>
                        <p class="text-white/80 text-sm mb-4">Hand-rolled truffles infused with seasonal spirits and rich espresso.</p>
                        <a href="menu.html" class="text-[#C68E17] font-medium hover:underline text-sm">View Details</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 4: Custom Order CTA -->
    <section class="relative py-32 bg-[#2A1300] overflow-hidden text-center">
        <!-- Parallax Background -->
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=2072&auto=format&fit=crop" class="w-full h-full object-cover opacity-20 parallax-element" alt="Chocolate Texture">
        </div>
        
        <div class="container mx-auto px-6 relative z-10">
            <h2 class="text-4xl md:text-5xl lg:text-6xl font-serif font-bold text-[#F5F5DC] mb-8 clip-reveal" data-aos="fade-up">Made For Your Moment.</h2>
            <p class="text-xl text-[#F5F5DC]/80 max-w-2xl mx-auto mb-12" data-aos="fade-up" data-aos-delay="200">From intimate gatherings to grand celebrations, we ensure your centerpiece is as unforgettable as the occasion itself.</p>
            
            <div class="flex flex-col sm:flex-row gap-6 justify-center" data-aos="zoom-in" data-aos-delay="400">
                <a href="studio.html" class="magnetic px-10 py-5 bg-[#C68E17] text-white rounded-full text-lg font-bold hover:bg-[#D4AF37] transition-colors shadow-2xl">Start Custom Cake</a>
                <a href="order.html" class="magnetic px-10 py-5 bg-transparent border-2 border-[#F5F5DC] text-[#F5F5DC] rounded-full text-lg font-bold hover:bg-[#F5F5DC] hover:text-[#2A1300] transition-colors">Order Delivery</a>
            </div>
            
            <div class="mt-16 inline-flex items-center gap-3 text-[#F5F5DC]/60 text-sm" data-aos="fade-up" data-aos-delay="600">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                <span>48 hours minimum notice for custom orders. Local delivery available.</span>
            </div>
        </div>
    </section>
    """
}

# 2. STUDIO.HTML (3 sections)
pages['studio.html'] = {
    'title': 'Custom Cake Studio',
    'active': 'active_studio',
    'extra_js': '',
    'content': """
    <!-- Section 1: Intro -->
    <section class="pt-32 pb-20 bg-[#FFFAF0] dark:bg-[#1a0f08] relative overflow-hidden">
        <div class="container mx-auto px-6">
            <div class="flex flex-col lg:flex-row items-center gap-12">
                <div class="w-full lg:w-1/2" data-aos="fade-right">
                    <h1 class="text-5xl lg:text-6xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">Design Your Dream Cake</h1>
                    <p class="text-lg text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 mb-8 max-w-lg">Select your size, perfect your flavor profile, and choose the finishing touches. Our master bakers will bring your vision to life.</p>
                </div>
                <div class="w-full lg:w-1/2 relative h-[400px] rounded-3xl overflow-hidden clip-reveal" data-aos="fade-left">
                    <img src="https://images.unsplash.com/photo-1535141192574-5d4897c12636?q=80&w=1975&auto=format&fit=crop" class="w-full h-full object-cover" alt="Custom Cake Creation">
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Full Interactive Customizer -->
    <section class="py-20 bg-white dark:bg-[#2A1300]">
        <div class="container mx-auto px-6">
            <div class="flex flex-col lg:flex-row gap-16">
                <!-- Left: 3D Preview (Sticky) -->
                <div class="w-full lg:w-1/3">
                    <div class="sticky top-32 space-y-8">
                        <div class="relative h-[400px] bg-[#FFFAF0] dark:bg-[#1a0f08] rounded-3xl p-6 flex items-center justify-center shadow-2xl hover-3d-tilt transition-transform duration-500">
                            <img id="main-cake-preview" src="https://images.unsplash.com/photo-1535254973040-607b474cb50d?w=800&auto=format&fit=crop" class="w-4/5 max-h-[420px] object-cover rounded-xl shadow-xl transition-all duration-500" alt="Cake View">
                        </div>
                        <div class="bg-[#FFFAF0] dark:bg-[#1a0f08] p-6 rounded-3xl shadow-lg border border-[#3E1C00]/10 dark:border-[#F5F5DC]/10">
                            <h3 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-4 border-b border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 pb-4">Order Summary</h3>
                            <ul class="space-y-3 text-sm text-[#3E1C00]/80 dark:text-[#F5F5DC]/80 mb-6" id="summary-list">
                                <li class="flex justify-between"><span>Size:</span> <span id="sum-size">6 inch</span></li>
                                <li class="flex justify-between"><span>Flavor:</span> <span id="sum-flavor">Vanilla</span></li>
                                <li class="flex justify-between"><span>Filling:</span> <span id="sum-filling">Vanilla Cream</span></li>
                                <li class="flex justify-between"><span>Frosting:</span> <span id="sum-frosting">Buttercream</span></li>
                                <li class="flex justify-between"><span>Decorations:</span> <span id="sum-decor">Minimalist</span></li>
                            </ul>
                            <div class="flex justify-between items-end border-t border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 pt-4">
                                <span class="text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC]">Estimated Total</span>
                                <span class="text-3xl font-serif font-bold text-[#C68E17]">$<span id="total-price">45.00</span></span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Right: Options -->
                <div class="w-full lg:w-2/3 space-y-12" id="customizer-options">
                    
                    <!-- Size -->
                    <div class="step-card bg-[#FFFAF0] dark:bg-[#1a0f08] p-8 rounded-3xl shadow-sm border border-[#3E1C00]/5 dark:border-[#F5F5DC]/5" data-aos="fade-up">
                        <h2 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">1. Cake Size</h2>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                            <button class="opt-btn size-opt active p-4 rounded-xl border-2 border-[#C68E17] bg-[#C68E17]/10 flex flex-col items-center gap-2" data-type="size" data-val="6 inch" data-price="45">
                                <div class="w-8 h-8 rounded-full border-2 border-[#C68E17]"></div>
                                <span class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">6"</span>
                                <span class="text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Serves 8-10</span>
                            </button>
                            <button class="opt-btn size-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 hover:border-[#C68E17]/50 flex flex-col items-center gap-2" data-type="size" data-val="8 inch" data-price="65">
                                <div class="w-10 h-10 rounded-full border-2 border-[#3E1C00]/30 dark:border-[#F5F5DC]/30"></div>
                                <span class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">8"</span>
                                <span class="text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Serves 15-20</span>
                            </button>
                            <button class="opt-btn size-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 hover:border-[#C68E17]/50 flex flex-col items-center gap-2" data-type="size" data-val="10 inch" data-price="85">
                                <div class="w-12 h-12 rounded-full border-2 border-[#3E1C00]/30 dark:border-[#F5F5DC]/30"></div>
                                <span class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">10"</span>
                                <span class="text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Serves 25-30</span>
                            </button>
                            <button class="opt-btn size-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 hover:border-[#C68E17]/50 flex flex-col items-center gap-2" data-type="size" data-val="12 inch" data-price="120">
                                <div class="w-14 h-14 rounded-full border-2 border-[#3E1C00]/30 dark:border-[#F5F5DC]/30"></div>
                                <span class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">12"</span>
                                <span class="text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Serves 40-50</span>
                            </button>
                        </div>
                    </div>

                    <!-- Flavor -->
                    <div class="step-card bg-[#FFFAF0] dark:bg-[#1a0f08] p-8 rounded-3xl shadow-sm border border-[#3E1C00]/5 dark:border-[#F5F5DC]/5" data-aos="fade-up">
                        <h2 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">2. Flavor</h2>
                        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                            <button class="opt-btn flavor-opt active p-4 rounded-xl border-2 border-[#C68E17] bg-[#C68E17]/10 font-medium text-[#3E1C00] dark:text-[#F5F5DC]" data-type="flavor" data-val="Vanilla" data-price="0">Vanilla Bean</button>
                            <button class="opt-btn flavor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 font-medium text-[#3E1C00] dark:text-[#F5F5DC]" data-type="flavor" data-val="Chocolate" data-price="0">Rich Chocolate</button>
                            <button class="opt-btn flavor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 font-medium text-[#3E1C00] dark:text-[#F5F5DC]" data-type="flavor" data-val="Red Velvet" data-price="5">Red Velvet (+ $5)</button>
                            <button class="opt-btn flavor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 font-medium text-[#3E1C00] dark:text-[#F5F5DC]" data-type="flavor" data-val="Pistachio" data-price="10">Pistachio (+ $10)</button>
                            <button class="opt-btn flavor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 font-medium text-[#3E1C00] dark:text-[#F5F5DC]" data-type="flavor" data-val="Strawberry" data-price="5">Strawberry (+ $5)</button>
                            <button class="opt-btn flavor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 font-medium text-[#3E1C00] dark:text-[#F5F5DC]" data-type="flavor" data-val="Lemon" data-price="0">Zesty Lemon</button>
                        </div>
                    </div>

                    <!-- Filling & Frosting -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div class="step-card bg-[#FFFAF0] dark:bg-[#1a0f08] p-8 rounded-3xl shadow-sm border border-[#3E1C00]/5 dark:border-[#F5F5DC]/5" data-aos="fade-up">
                            <h2 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">3. Filling</h2>
                            <div class="flex flex-col gap-3">
                                <button class="opt-btn filling-opt active p-3 text-left rounded-xl border-2 border-[#C68E17] bg-[#C68E17]/10" data-type="filling" data-val="Vanilla Cream" data-price="0">Vanilla Cream</button>
                                <button class="opt-btn filling-opt p-3 text-left rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="filling" data-val="Chocolate Ganache" data-price="5">Chocolate Ganache (+ $5)</button>
                                <button class="opt-btn filling-opt p-3 text-left rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="filling" data-val="Strawberry Cream" data-price="0">Strawberry Cream</button>
                                <button class="opt-btn filling-opt p-3 text-left rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="filling" data-val="Salted Caramel" data-price="5">Salted Caramel (+ $5)</button>
                            </div>
                        </div>
                        <div class="step-card bg-[#FFFAF0] dark:bg-[#1a0f08] p-8 rounded-3xl shadow-sm border border-[#3E1C00]/5 dark:border-[#F5F5DC]/5" data-aos="fade-up">
                            <h2 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">4. Frosting</h2>
                            <div class="flex flex-col gap-3">
                                <button class="opt-btn frosting-opt active p-3 text-left rounded-xl border-2 border-[#C68E17] bg-[#C68E17]/10" data-type="frosting" data-val="Buttercream" data-price="0">Buttercream</button>
                                <button class="opt-btn frosting-opt p-3 text-left rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="frosting" data-val="Ganache" data-price="10">Ganache (+ $10)</button>
                                <button class="opt-btn frosting-opt p-3 text-left rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="frosting" data-val="Cream Cheese" data-price="5">Cream Cheese (+ $5)</button>
                                <button class="opt-btn frosting-opt p-3 text-left rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="frosting" data-val="Whipped Cream" data-price="0">Whipped Cream</button>
                            </div>
                        </div>
                    </div>

                    <!-- Decorations -->
                    <div class="step-card bg-[#FFFAF0] dark:bg-[#1a0f08] p-8 rounded-3xl shadow-sm border border-[#3E1C00]/5 dark:border-[#F5F5DC]/5" data-aos="fade-up">
                        <h2 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">5. Decorations</h2>
                        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                            <button class="opt-btn decor-opt active p-4 rounded-xl border-2 border-[#C68E17] bg-[#C68E17]/10" data-type="decor" data-val="Minimalist" data-price="0">Minimalist</button>
                            <button class="opt-btn decor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="decor" data-val="Fresh Flowers" data-price="15">Fresh Flowers (+ $15)</button>
                            <button class="opt-btn decor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="decor" data-val="Gold Details" data-price="20">Gold Details (+ $20)</button>
                            <button class="opt-btn decor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="decor" data-val="Chocolate Drip" data-price="10">Chocolate Drip (+ $10)</button>
                            <button class="opt-btn decor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="decor" data-val="Macarons" data-price="15">Macarons (+ $15)</button>
                            <button class="opt-btn decor-opt p-4 rounded-xl border-2 border-[#3E1C00]/10 dark:border-[#F5F5DC]/10" data-type="decor" data-val="Fresh Fruit" data-price="10">Fresh Fruit (+ $10)</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const state = {
                    size: { val: '6 inch', price: 45 },
                    flavor: { val: 'Vanilla', price: 0 },
                    filling: { val: 'Vanilla Cream', price: 0 },
                    frosting: { val: 'Buttercream', price: 0 },
                    decor: { val: 'Minimalist', price: 0 }
                };

                const updateSummary = () => {
                    document.getElementById('sum-size').innerText = state.size.val;
                    document.getElementById('sum-flavor').innerText = state.flavor.val;
                    document.getElementById('sum-filling').innerText = state.filling.val;
                    document.getElementById('sum-frosting').innerText = state.frosting.val;
                    document.getElementById('sum-decor').innerText = state.decor.val;
                    
                    const total = state.size.price + state.flavor.price + state.filling.price + state.frosting.price + state.decor.price;
                    document.getElementById('total-price').innerText = total + ".00";

                    // subtle animation on main image to simulate change
                    const img = document.getElementById('main-cake-preview');
                    img.style.opacity = 0.5;
                    setTimeout(() => img.style.opacity = 1, 300);
                };

                const setupButtons = (className, typeStr) => {
                    document.querySelectorAll(className).forEach(btn => {
                        btn.addEventListener('click', (e) => {
                            const target = e.currentTarget;
                            document.querySelectorAll(className).forEach(b => {
                                b.classList.remove('active', 'border-[#C68E17]', 'bg-[#C68E17]/10');
                                b.classList.add('border-[#3E1C00]/10', 'dark:border-[#F5F5DC]/10');
                            });
                            target.classList.add('active', 'border-[#C68E17]', 'bg-[#C68E17]/10');
                            target.classList.remove('border-[#3E1C00]/10', 'dark:border-[#F5F5DC]/10');
                            
                            state[typeStr].val = target.getAttribute('data-val');
                            state[typeStr].price = parseInt(target.getAttribute('data-price'));
                            updateSummary();
                        });
                    });
                };

                setupButtons('.size-opt', 'size');
                setupButtons('.flavor-opt', 'flavor');
                setupButtons('.filling-opt', 'filling');
                setupButtons('.frosting-opt', 'frosting');
                setupButtons('.decor-opt', 'decor');
            });
        </script>
    </section>

    <!-- Section 3: Saved Design CTA -->
    <section class="py-24 bg-[#FFFAF0] dark:bg-[#1a0f08] border-t border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 text-center">
        <div class="container mx-auto px-6">
            <h2 class="text-3xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6" data-aos="fade-up">Ready to order your custom creation?</h2>
            <div class="flex justify-center gap-6" data-aos="fade-up" data-aos-delay="100">
                <a href="order.html" class="magnetic px-10 py-4 bg-[#3E1C00] dark:bg-[#F5F5DC] text-[#FFFAF0] dark:text-[#3E1C00] rounded-full text-lg font-bold hover:bg-[#C68E17] dark:hover:bg-[#C68E17] dark:hover:text-white transition-colors shadow-xl">Continue to Order</a>
            </div>
            <p class="mt-6 text-sm text-[#3E1C00]/60 dark:text-[#F5F5DC]/60" data-aos="fade-up" data-aos-delay="200">Estimated preparation time: 48-72 hours based on complexity.</p>
        </div>
    </section>
    """
}

# 3. MENU.HTML (3 sections)
pages['menu.html'] = {
    'title': 'Menu & Pastries',
    'active': 'active_menu',
    'extra_js': '',
    'content': """
    <!-- Section 1: Menu Intro -->
    <section class="pt-32 pb-16 bg-[#FFFAF0] dark:bg-[#1a0f08]">
        <div class="container mx-auto px-6">
            <div class="text-center max-w-3xl mx-auto" data-aos="fade-up">
                <h1 class="text-5xl lg:text-6xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">Our Collection</h1>
                <p class="text-lg text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 mb-12">Discover our daily selection of artisanal pastries, signature cakes, and delicate confections baked fresh every morning.</p>
                
                <!-- Category Nav -->
                <div class="flex overflow-x-auto hide-scrollbar gap-4 pb-4 justify-start lg:justify-center">
                    <button class="filter-btn active whitespace-nowrap px-6 py-2 bg-[#C68E17] text-white border border-[#C68E17] rounded-full font-medium" data-filter="all">All</button>
                    <button class="filter-btn whitespace-nowrap px-6 py-2 bg-white dark:bg-[#2A1300] text-[#3E1C00] dark:text-[#F5F5DC] border border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 rounded-full font-medium hover:border-[#C68E17]" data-filter="cakes">Signature Cakes</button>
                    <button class="filter-btn whitespace-nowrap px-6 py-2 bg-white dark:bg-[#2A1300] text-[#3E1C00] dark:text-[#F5F5DC] border border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 rounded-full font-medium hover:border-[#C68E17]" data-filter="pastries">Pastries</button>
                    <button class="filter-btn whitespace-nowrap px-6 py-2 bg-white dark:bg-[#2A1300] text-[#3E1C00] dark:text-[#F5F5DC] border border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 rounded-full font-medium hover:border-[#C68E17]" data-filter="macarons">Macarons</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Premium Product Showcase (Masonry style) -->
    <section class="py-16 bg-[#FFFAF0] dark:bg-[#1a0f08]">
        <div class="container mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-start">
                
                <!-- Item 1: Signature Cake -->
                <div class="filter-item group rounded-3xl overflow-hidden relative shadow-lg bg-white dark:bg-[#2A1300] h-[400px] flex flex-col" data-aos="fade-up" data-category="cakes">
                    <div class="h-[55%] overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/9938873/pexels-photo-9938873.jpeg" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Black Forest Cake">
                        <span class="absolute top-4 left-4 px-3 py-1 bg-[#C68E17] text-white text-xs font-bold rounded-full">Signature</span>
                    </div>
                    <div class="p-6 flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Modern Black Forest</h3>
                            <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 line-clamp-2">Valrhona chocolate sponge, kirsch-infused cherries, and light vanilla bean chantilly cream.</p>
                        </div>
                        <div class="flex justify-between items-center mt-2">
                            <span class="text-lg font-bold text-[#C68E17]">$55.00</span>
                            <button class="text-sm font-medium hover:text-[#C68E17] transition-colors dark:text-[#F5F5DC]">Add to Order</button>
                        </div>
                    </div>
                </div>

                <!-- Item 2: Fruit Tart -->
                <div class="filter-item group rounded-3xl overflow-hidden relative shadow-lg bg-white dark:bg-[#2A1300] h-[400px] flex flex-col" data-aos="fade-up" data-aos-delay="100" data-category="pastries">
                    <div class="h-[55%] overflow-hidden">
                        <img src="https://images.pexels.com/photos/34208221/pexels-photo-34208221.jpeg" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Fruit Tart">
                    </div>
                    <div class="p-6 flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Seasonal Fruit Tart</h3>
                            <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 line-clamp-2">Buttery sable crust filled with vanilla pastry cream and topped with fresh seasonal berries.</p>
                        </div>
                        <div class="flex justify-between items-center mt-2">
                            <span class="text-lg font-bold text-[#C68E17]">$38.00</span>
                            <button class="text-sm font-medium hover:text-[#C68E17] transition-colors dark:text-[#F5F5DC]">Add to Order</button>
                        </div>
                    </div>
                </div>

                <!-- Item 3: Lemon Meringue -->
                <div class="filter-item group rounded-3xl overflow-hidden relative shadow-lg bg-white dark:bg-[#2A1300] h-[400px] flex flex-col" data-aos="fade-up" data-aos-delay="200" data-category="pastries">
                    <div class="h-[55%] overflow-hidden">
                        <img src="https://images.pexels.com/photos/31614314/pexels-photo-31614314.jpeg" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Lemon Meringue">
                    </div>
                    <div class="p-6 flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Lemon Meringue</h3>
                            <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 line-clamp-2">Tangy lemon curd in a crisp shell with toasted Italian meringue.</p>
                        </div>
                        <div class="flex justify-between items-center mt-2">
                            <span class="text-lg font-bold text-[#C68E17]">$35.00</span>
                            <button class="text-sm font-medium hover:text-[#C68E17] transition-colors dark:text-[#F5F5DC]">Add to Order</button>
                        </div>
                    </div>
                </div>

                <!-- Item 4: Assorted Macarons -->
                <div class="filter-item group rounded-3xl overflow-hidden relative shadow-lg bg-white dark:bg-[#2A1300] h-[400px] flex flex-col" data-aos="fade-up" data-aos-delay="300" data-category="macarons">
                    <div class="h-[55%] overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/38304842/pexels-photo-38304842.jpeg" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Macaron Box">
                        <span class="absolute top-4 left-4 px-3 py-1 bg-white/90 text-[#3E1C00] text-xs font-bold rounded-full">Gift Box</span>
                    </div>
                    <div class="p-6 flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Assorted Macarons</h3>
                            <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 line-clamp-2">A box of 12 signature Parisian macarons in assorted flavors.</p>
                        </div>
                        <div class="flex justify-between items-center mt-2">
                            <span class="text-lg font-bold text-[#C68E17]">$42.00</span>
                            <button class="text-sm font-medium hover:text-[#C68E17] transition-colors dark:text-[#F5F5DC]">Add to Order</button>
                        </div>
                    </div>
                </div>

                <!-- Item 5: Chocolate Eclair -->
                <div class="filter-item group rounded-3xl overflow-hidden relative shadow-lg bg-white dark:bg-[#2A1300] h-[400px] flex flex-col" data-aos="fade-up" data-aos-delay="400" data-category="pastries">
                    <div class="h-[55%] overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/13177922/pexels-photo-13177922.jpeg" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Chocolate Eclair">
                    </div>
                    <div class="p-6 flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Classic Chocolate Éclair</h3>
                            <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 line-clamp-2">Choux pastry filled with dark chocolate crème pâtissière and glazed with smooth fondant.</p>
                        </div>
                        <div class="flex justify-between items-center mt-2">
                            <span class="text-lg font-bold text-[#C68E17]">$8.50</span>
                            <button class="text-sm font-medium hover:text-[#C68E17] transition-colors dark:text-[#F5F5DC]">Add to Order</button>
                        </div>
                    </div>
                </div>

                <!-- Item 6: Opera Cake -->
                <div class="filter-item group rounded-3xl overflow-hidden relative shadow-lg bg-white dark:bg-[#2A1300] h-[400px] flex flex-col" data-aos="fade-up" data-aos-delay="500" data-category="cakes">
                    <div class="h-[55%] overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/11675722/pexels-photo-11675722.jpeg" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Opera Cake">
                        <span class="absolute top-4 left-4 px-3 py-1 bg-[#C68E17] text-white text-xs font-bold rounded-full">Signature</span>
                    </div>
                    <div class="p-6 flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-2">L'Opéra</h3>
                            <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 line-clamp-2">Layers of almond sponge soaked in coffee syrup, layered with ganache and coffee buttercream.</p>
                        </div>
                        <div class="flex justify-between items-center mt-2">
                            <span class="text-lg font-bold text-[#C68E17]">$12.00</span>
                            <button class="text-sm font-medium hover:text-[#C68E17] transition-colors dark:text-[#F5F5DC]">Add to Order</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 3: Seasonal Collection -->
    <section class="py-24 bg-white dark:bg-[#2A1300] relative overflow-hidden">
        <div class="container mx-auto px-6 relative z-10">
            <div class="flex flex-col lg:flex-row items-center gap-12">
                <div class="w-full lg:w-1/2" data-aos="fade-right">
                    <span class="text-[#C68E17] font-bold tracking-widest uppercase text-sm mb-2 block">Limited Time</span>
                    <h2 class="text-4xl md:text-5xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">Autumn Spice Collection</h2>
                    <p class="text-[#3E1C00]/80 dark:text-[#F5F5DC]/80 mb-8">Embrace the season with our new collection featuring warm spices, roasted nuts, and deep caramel flavors. Available only until November.</p>
                    <a href="order.html" class="inline-block px-8 py-4 bg-[#C68E17] text-white rounded-full font-medium hover:bg-[#D4AF37] transition-colors shadow-lg">Order Seasonal Box</a>
                </div>
                <div class="w-full lg:w-1/2 flex justify-center" data-aos="fade-left">
                    <img src="https://images.unsplash.com/photo-1612201142855-7873bc1661b4?w=800&auto=format&fit=crop" class="rounded-3xl shadow-2xl w-[80%] max-w-[400px] aspect-square object-cover" alt="Autumn Pastries">
                </div>
            </div>
        </div>
        <!-- Floating decor -->
        <div class="absolute top-10 right-10 w-16 h-16 opacity-10 dark:opacity-20 floating">
            <svg viewBox="0 0 100 100" fill="#C68E17"><path d="M50 0L60 40L100 50L60 60L50 100L40 60L0 50L40 40Z"/></svg>
        </div>
    </section>

    <!-- Section 4: CTA -->
    <section class="py-16 bg-[#FFFAF0] dark:bg-[#1a0f08]">
        <div class="container mx-auto px-6">
            <div class="bg-gradient-to-r from-[#3E1C00] to-[#2A1300] dark:from-[#C68E17]/20 dark:to-transparent rounded-3xl p-12 text-center shadow-2xl relative overflow-hidden" data-aos="fade-up">
                <div class="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] mix-blend-overlay"></div>
                <div class="relative z-10 max-w-3xl mx-auto">
                    <h3 class="text-3xl md:text-4xl font-serif font-bold text-[#F5F5DC] mb-4">Planning a Special Event?</h3>
                    <p class="text-[#F5F5DC]/80 mb-8 text-lg">We offer bespoke catering packages with miniature versions of our signature pastries and custom tiered cakes for weddings and corporate gatherings.</p>
                    <a href="contact.html" class="inline-block px-10 py-4 bg-[#C68E17] text-white rounded-full font-medium text-lg hover:bg-[#D4AF37] transition-all hover:scale-105 shadow-xl">Contact Our Events Team</a>
                </div>
            </div>
        </div>
    </section>
    """
}

def generate_file(filename):
    if filename in pages:
        p = pages[filename]
        
        # Determine active nav
        h_html = header_html.format(
            active_home='after:w-full' if p.get('active') == 'active_home' else '',
            active_studio='after:w-full' if p.get('active') == 'active_studio' else '',
            active_menu='after:w-full' if p.get('active') == 'active_menu' else '',
            active_order='after:w-full' if p.get('active') == 'active_order' else '',
            active_about='after:w-full' if p.get('active') == 'active_about' else '',
            active_contact='after:w-full' if p.get('active') == 'active_contact' else '',
            active_dashboard='after:w-full' if p.get('active') == 'active_dashboard' else ''
        )
        
        full_html = base_html_template.format(
            title=p['title'],
            header=h_html,
            content=p['content'],
            footer=footer_html,
            extra_js=p['extra_js']
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_html)

for fn in pages.keys():
    generate_file(fn)

print("Files generated successfully.")
