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

# 4. ORDER & DELIVERY (3 sections)
pages['order.html'] = {
    'title': 'Order & Delivery',
    'active': 'active_order',
    'extra_js': '',
    'content': """
    <!-- Section 1: Order Process -->
    <section class="pt-32 pb-20 bg-[#FFFAF0] dark:bg-[#1a0f08]">
        <div class="container mx-auto px-6">
            <div class="text-center max-w-3xl mx-auto mb-16" data-aos="fade-up">
                <h1 class="text-5xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">Complete Your Order</h1>
                <p class="text-lg text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">We deliver our creations with the utmost care, ensuring they arrive perfectly presented and ready for your celebration.</p>
            </div>
            
            <div class="relative">
                <div class="absolute top-1/2 left-0 w-full h-1 bg-[#3E1C00]/10 dark:bg-[#F5F5DC]/10 -translate-y-1/2 hidden md:block"></div>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                    <div class="relative z-10 flex flex-col items-center text-center" data-aos="fade-up" data-aos-delay="0">
                        <div class="w-16 h-16 rounded-full bg-[#C68E17] text-white flex items-center justify-center text-xl font-bold mb-4 shadow-lg">01</div>
                        <h3 class="font-serif font-bold text-xl text-[#3E1C00] dark:text-[#F5F5DC]">Select</h3>
                        <p class="text-sm text-[#3E1C00]/60 dark:text-[#F5F5DC]/60 mt-2">Choose your items</p>
                    </div>
                    <div class="relative z-10 flex flex-col items-center text-center" data-aos="fade-up" data-aos-delay="100">
                        <div class="w-16 h-16 rounded-full bg-[#3E1C00] dark:bg-[#F5F5DC] text-[#FFFAF0] dark:text-[#3E1C00] flex items-center justify-center text-xl font-bold mb-4 shadow-lg">02</div>
                        <h3 class="font-serif font-bold text-xl text-[#3E1C00] dark:text-[#F5F5DC]">Customize</h3>
                        <p class="text-sm text-[#3E1C00]/60 dark:text-[#F5F5DC]/60 mt-2">Add personal touches</p>
                    </div>
                    <div class="relative z-10 flex flex-col items-center text-center opacity-50" data-aos="fade-up" data-aos-delay="200">
                        <div class="w-16 h-16 rounded-full bg-white dark:bg-[#2A1300] border-2 border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 text-[#3E1C00] dark:text-[#F5F5DC] flex items-center justify-center text-xl font-bold mb-4 shadow-sm">03</div>
                        <h3 class="font-serif font-bold text-xl text-[#3E1C00] dark:text-[#F5F5DC]">Schedule</h3>
                        <p class="text-sm text-[#3E1C00]/60 dark:text-[#F5F5DC]/60 mt-2">Pick date & time</p>
                    </div>
                    <div class="relative z-10 flex flex-col items-center text-center opacity-50" data-aos="fade-up" data-aos-delay="300">
                        <div class="w-16 h-16 rounded-full bg-white dark:bg-[#2A1300] border-2 border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 text-[#3E1C00] dark:text-[#F5F5DC] flex items-center justify-center text-xl font-bold mb-4 shadow-sm">04</div>
                        <h3 class="font-serif font-bold text-xl text-[#3E1C00] dark:text-[#F5F5DC]">Confirm</h3>
                        <p class="text-sm text-[#3E1C00]/60 dark:text-[#F5F5DC]/60 mt-2">Secure payment</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Delivery Slot Picker -->
    <section class="py-16 bg-white dark:bg-[#2A1300]">
        <div class="container mx-auto px-6 max-w-4xl">
            <div class="bg-[#FFFAF0] dark:bg-[#1a0f08] p-8 md:p-12 rounded-3xl shadow-xl" data-aos="fade-up">
                <h2 class="text-3xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-8 border-b border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 pb-4">Delivery Details</h2>
                
                <div class="space-y-8">
                    <div>
                        <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Delivery Address</label>
                        <input type="text" class="w-full bg-white dark:bg-[#2A1300] border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-xl px-4 py-3 text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] transition-colors" placeholder="123 Example Street, Apt 4B">
                    </div>
                    
                    <div>
                        <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] mb-4">Select Date</label>
                        <div class="flex gap-4 overflow-x-auto pb-4 hide-scrollbar">
                            <div class="date-opt flex-none w-24 p-3 bg-white dark:bg-[#2A1300] border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-xl text-center cursor-pointer hover:border-[#C68E17] transition-all">
                                <span class="block text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Mon</span>
                                <span class="block text-2xl font-bold text-[#3E1C00] dark:text-[#F5F5DC]">12</span>
                                <span class="block text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Oct</span>
                            </div>
                            <div class="date-opt is-selected flex-none w-24 p-3 bg-white dark:bg-[#2A1300] border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-xl text-center cursor-pointer hover:border-[#C68E17] transition-all">
                                <span class="block text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Tue</span>
                                <span class="block text-2xl font-bold text-[#3E1C00] dark:text-[#F5F5DC]">13</span>
                                <span class="block text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Oct</span>
                            </div>
                            <div class="date-opt flex-none w-24 p-3 bg-white dark:bg-[#2A1300] border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-xl text-center cursor-pointer hover:border-[#C68E17] transition-all">
                                <span class="block text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Wed</span>
                                <span class="block text-2xl font-bold text-[#3E1C00] dark:text-[#F5F5DC]">14</span>
                                <span class="block text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Oct</span>
                            </div>
                            <div class="flex-none w-24 p-3 bg-[#3E1C00]/5 dark:bg-[#F5F5DC]/5 border border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 rounded-xl text-center opacity-50 cursor-not-allowed">
                                <span class="block text-xs text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Thu</span>
                                <span class="block text-2xl font-bold text-[#3E1C00] dark:text-[#F5F5DC]">15</span>
                                <span class="block text-xs text-red-500">Full</span>
                            </div>
                        </div>
                    </div>
                    
                    <div>
                        <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] mb-4">Select Time Slot</label>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                            <button type="button" class="slot-opt py-3 px-4 border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-xl text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] hover:border-[#C68E17] bg-white dark:bg-[#2A1300] transition-all">09:00 - 11:00</button>
                            <button type="button" class="slot-opt is-selected py-3 px-4 border border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 rounded-xl text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] hover:border-[#C68E17] bg-white dark:bg-[#2A1300] transition-all">11:00 - 13:00</button>
                            <button type="button" class="slot-opt py-3 px-4 border border-orange-300 dark:border-orange-700 bg-orange-50 dark:bg-orange-900/20 rounded-xl text-sm font-medium text-orange-700 dark:text-orange-300">13:00 - 15:00<br><span class="text-xs">Almost Full</span></button>
                            <button class="py-3 px-4 border border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 bg-[#3E1C00]/5 dark:bg-[#F5F5DC]/5 rounded-xl text-sm font-medium text-[#3E1C00]/50 dark:text-[#F5F5DC]/50 cursor-not-allowed">15:00 - 17:00<br><span class="text-xs">Fully Booked</span></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <style>
            .date-opt.is-selected { background:#C68E17 !important; border-color:#C68E17 !important; box-shadow:0 4px 12px rgba(198,142,23,.4); transform:scale(1.05); }
            .date-opt.is-selected span { color:#fff !important; }
            .slot-opt.is-selected { background:rgba(198,142,23,.12) !important; border-color:#C68E17 !important; color:#C68E17 !important; font-weight:700; }
        </style>
        <script>
            ['date-opt','slot-opt'].forEach(cls => {
                document.querySelectorAll('.' + cls).forEach(el => {
                    el.addEventListener('click', () => {
                        document.querySelectorAll('.' + cls).forEach(o => o.classList.remove('is-selected'));
                        el.classList.add('is-selected');
                    });
                });
            });
        </script>
    </section>

    <!-- Section 3: Order Summary -->
    <section class="py-16 bg-[#FFFAF0] dark:bg-[#1a0f08] border-t border-[#3E1C00]/10 dark:border-[#F5F5DC]/10">
        <div class="container mx-auto px-6 max-w-4xl">
            <div class="bg-white dark:bg-[#2A1300] p-8 md:p-12 rounded-3xl shadow-xl border border-[#C68E17]/20" data-aos="fade-up">
                <h2 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-8">Order Summary</h2>
                
                <div class="space-y-4 mb-8">
                    <div class="flex justify-between items-center pb-4 border-b border-[#3E1C00]/10 dark:border-[#F5F5DC]/10">
                        <div>
                            <h4 class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Custom 6" Cake</h4>
                            <p class="text-sm text-[#3E1C00]/60 dark:text-[#F5F5DC]/60">Vanilla, Vanilla Cream, Buttercream, Minimalist</p>
                        </div>
                        <span class="font-medium text-[#3E1C00] dark:text-[#F5F5DC]">$45.00</span>
                    </div>
                    <div class="flex justify-between items-center text-sm text-[#3E1C00]/80 dark:text-[#F5F5DC]/80">
                        <span>Subtotal</span>
                        <span>$45.00</span>
                    </div>
                    <div class="flex justify-between items-center text-sm text-[#3E1C00]/80 dark:text-[#F5F5DC]/80">
                        <span>Delivery Fee</span>
                        <span>$15.00</span>
                    </div>
                </div>
                
                <div class="flex justify-between items-end pt-6 border-t-2 border-[#3E1C00] dark:border-[#F5F5DC] mb-10">
                    <span class="text-lg font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Total</span>
                    <span class="text-4xl font-serif font-bold text-[#C68E17]">$60.00</span>
                </div>
                
                <button class="w-full py-5 bg-[#3E1C00] dark:bg-[#F5F5DC] text-[#FFFAF0] dark:text-[#3E1C00] rounded-xl text-lg font-bold hover:bg-[#C68E17] dark:hover:bg-[#C68E17] dark:hover:text-white transition-colors shadow-xl group overflow-hidden relative">
                    <span class="relative z-10 flex items-center justify-center gap-2">
                        Complete Order & Pay
                        <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </span>
                </button>
            </div>
        </div>
    </section>
    """
}

# 5. ABOUT BAKERY (3 sections)
pages['about.html'] = {
    'title': 'About Bakery',
    'active': 'active_about',
    'extra_js': '',
    'content': """
    <!-- Section 1: Our Story -->
    <section class="pt-32 pb-20 bg-[#FFFAF0] dark:bg-[#1a0f08] overflow-hidden">
        <div class="container mx-auto px-6">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <div class="w-full lg:w-1/2 relative h-[600px] clip-reveal" data-aos="fade-right">
                    <img src="images/storefront.jpg" class="w-full h-full object-cover rounded-[3rem]" alt="Bakery Storefront">
                    <div class="absolute -bottom-10 -right-10 w-48 h-48 bg-[#C68E17] rounded-full mix-blend-multiply filter blur-2xl opacity-50"></div>
                </div>
                <div class="w-full lg:w-1/2" data-aos="fade-left" data-aos-delay="200">
                    <h1 class="text-5xl lg:text-7xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-8">Our Heritage of Baking.</h1>
                    <p class="text-lg text-[#3E1C00]/80 dark:text-[#F5F5DC]/80 mb-6 leading-relaxed">Founded in 2012, Maison Dorée began with a simple philosophy: to elevate traditional baking into an art form. We believe that every pastry should tell a story of passion, precision, and the finest ingredients.</p>
                    <p class="text-lg text-[#3E1C00]/80 dark:text-[#F5F5DC]/80 mb-10 leading-relaxed">What started as a small neighborhood studio has blossomed into a premier destination for custom cakes and artisanal desserts, beloved by those who appreciate true culinary craftsmanship.</p>
                    <style>@import url('https://fonts.googleapis.com/css2?family=Mrs+Saint+Delafield&display=swap');</style>
                    <p class="text-6xl text-[#3E1C00] dark:text-[#F5F5DC] opacity-80 leading-none -rotate-3 origin-left" style="font-family:'Mrs Saint Delafield','Brush Script MT',cursive;" aria-label="Founder Signature">Julian Mercier</p>
                    <svg class="w-40 h-3 text-[#C68E17] mt-1" viewBox="0 0 160 12" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M2 8 C 30 2, 60 11, 90 6 S 140 3, 158 7"/></svg>
                    <p class="mt-2 font-serif font-bold text-[#C68E17]">Julian Mercier, Head Chef</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Our Craft (Horizontal Scroll feel) -->
    <section class="py-24 bg-white dark:bg-[#2A1300]">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-4xl lg:text-5xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC]">The Creative Process</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 relative">
                <!-- Line connecting steps (hidden since it's a grid now, but kept for aesthetic if desired, let's just make it cross the middle) -->
                <div class="hidden md:block absolute top-1/3 left-0 w-full h-0.5 bg-[#C68E17]/20 z-0"></div>
                
                <div class="relative z-10 group" data-aos="fade-up" data-aos-delay="0">
                    <div class="h-64 rounded-3xl overflow-hidden mb-6 shadow-xl">
                        <img src="images/process-source.jpg" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" alt="Mixing Ingredients">
                    </div>
                    <h3 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-3">01. Source</h3>
                    <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">We source only Madagascar vanilla, Valrhona chocolate, and local organic dairy.</p>
                </div>
                
                <div class="relative z-10 group" data-aos="fade-up" data-aos-delay="100">
                    <div class="h-64 rounded-3xl overflow-hidden mb-6 shadow-xl border-4 border-white dark:border-[#2A1300]">
                        <img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800&auto=format&fit=crop" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" alt="Baking">
                    </div>
                    <h3 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-3">02. Craft</h3>
                    <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">Precision temperature control and classic French folding techniques create our signature textures.</p>
                </div>
                
                <div class="relative z-10 group md:col-span-2 lg:col-span-1 md:w-[calc(50%-1rem)] lg:w-full mx-auto" data-aos="fade-up" data-aos-delay="200">
                    <div class="h-64 rounded-3xl overflow-hidden mb-6 shadow-xl">
                        <img src="images/process-design.jpg" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" alt="Decorating">
                    </div>
                    <h3 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-3">03. Design</h3>
                    <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">Every cake is hand-finished with edible gold, fresh blooms, and bespoke sugar work.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 3: Meet The Bakers -->
    <section class="py-24 bg-[#FFFAF0] dark:bg-[#1a0f08]">
        <div class="container mx-auto px-6">
            <h2 class="text-4xl lg:text-5xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-16 text-center" data-aos="fade-up">The Artisans</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">
                <!-- Baker 1 -->
                <div class="group" data-aos="fade-up">
                    <div class="relative h-[400px] rounded-3xl overflow-hidden mb-6 shadow-lg hover-3d-tilt">
                        <img src="https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=800&auto=format&fit=crop" class="w-full h-full object-cover" alt="Julian Mercier">
                        <div class="absolute inset-0 bg-[#3E1C00]/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center p-6 text-center">
                            <p class="text-white text-sm">"Pastry is the perfect balance of strict science and unbounded imagination."</p>
                        </div>
                    </div>
                    <h3 class="text-2xl font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Julian Mercier</h3>
                    <p class="text-[#C68E17] font-medium mb-2">Executive Pastry Chef</p>
                    <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 text-sm">Trained in Paris, Julian brings 15 years of Michelin-starred experience.</p>
                </div>
                
                <!-- Baker 2 -->
                <div class="group" data-aos="fade-up" data-aos-delay="100">
                    <div class="relative h-[400px] rounded-3xl overflow-hidden mb-6 shadow-lg hover-3d-tilt">
                        <img src="https://images.unsplash.com/photo-1581349485608-9469926a8e5e?w=800&auto=format&fit=crop" class="w-full h-full object-cover" alt="Elena Rostova">
                        <div class="absolute inset-0 bg-[#3E1C00]/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center p-6 text-center">
                            <p class="text-white text-sm">"A cake isn't just dessert; it's the centerpiece of someone's core memory."</p>
                        </div>
                    </div>
                    <h3 class="text-2xl font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Elena Rostova</h3>
                    <p class="text-[#C68E17] font-medium mb-2">Lead Cake Designer</p>
                    <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 text-sm">A background in fine arts translates to breathtaking sugar sculpting and floral design.</p>
                </div>
                
                <!-- Baker 3 -->
                <div class="group md:col-span-2 lg:col-span-1 md:w-[calc(50%-1.5rem)] lg:w-full mx-auto" data-aos="fade-up" data-aos-delay="200">
                    <div class="relative h-[400px] rounded-3xl overflow-hidden mb-6 shadow-lg hover-3d-tilt">
                        <img src="https://images.unsplash.com/photo-1578738288760-05ce9be719d3?w=800&auto=format&fit=crop" class="w-full h-full object-cover" alt="Marcus Chen">
                        <div class="absolute inset-0 bg-[#3E1C00]/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center p-6 text-center">
                            <p class="text-white text-sm">"Working with chocolate requires patience, timing, and profound respect."</p>
                        </div>
                    </div>
                    <h3 class="text-2xl font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Marcus Chen</h3>
                    <p class="text-[#C68E17] font-medium mb-2">Master Chocolatier</p>
                    <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 text-sm">Our resident chocolate expert, crafting truffles and ganache that melt flawlessly.</p>
                </div>
            </div>
        </div>
    </section>
    <!-- Section 4: Awards -->
    <section class="py-24 bg-white dark:bg-[#2A1300] border-t border-[#3E1C00]/10 dark:border-white/10">
        <div class="container mx-auto px-6">
            <h2 class="text-3xl lg:text-4xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-12 text-center" data-aos="fade-up">Recognized for Excellence</h2>
            <div class="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-80 grayscale hover:grayscale-0 transition-all duration-500" data-aos="fade-up" data-aos-delay="100">
                <div class="text-center">
                    <div class="w-16 h-16 mx-auto mb-4 rounded-full border-2 border-[#C68E17] flex items-center justify-center">
                        <svg class="w-8 h-8 text-[#C68E17]" viewBox="0 0 24 24" fill="currentColor" aria-label="Michelin Star"><path d="M12 2l2.9 6.6 7.1.7-5.4 4.8 1.6 7-6.2-3.7-6.2 3.7 1.6-7L2 9.3l7.1-.7z"/></svg>
                    </div>
                    <p class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">1 Michelin Star</p>
                    <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">2024, 2025</p>
                </div>
                <div class="text-center">
                    <div class="w-16 h-16 mx-auto mb-4 rounded-full border-2 border-[#C68E17] flex items-center justify-center">
                        <span class="font-serif font-bold text-[#C68E17] text-xl tracking-widest" aria-label="Vogue">V</span>
                    </div>
                    <p class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">"A Pastry Revelation"</p>
                    <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">Vogue Magazine, 2023</p>
                </div>
                <div class="text-center">
                    <div class="w-16 h-16 mx-auto mb-4 rounded-full border-2 border-[#C68E17] flex items-center justify-center">
                        <span class="font-serif font-bold text-[#C68E17] text-xl">Top 10</span>
                    </div>
                    <p class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Best Bakeries</p>
                    <p class="text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">Culinary Weekly, 2024</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 5: Promise -->
    <section class="relative py-16 bg-[#3E1C00] dark:bg-[#1a0f08]">
        <div class="container mx-auto px-6 relative z-10 text-center text-[#F5F5DC]">
            <h2 class="text-4xl lg:text-5xl font-serif font-bold mb-8" data-aos="fade-up">Our Promise to You</h2>
            <p class="max-w-2xl mx-auto text-lg text-white/90 mb-10 leading-relaxed" data-aos="fade-up" data-aos-delay="100">
                We believe that dessert is not an afterthought, but the grand finale. Every piece that leaves our kitchen is a testament to our dedication, crafted with the intention of making your ordinary days special and your special days unforgettable.
            </p>
            <a href="menu.html" class="inline-block px-10 py-4 bg-[#C68E17] text-white rounded-full font-medium text-lg hover:bg-[#D4AF37] transition-all hover:scale-105 shadow-xl" data-aos="fade-up" data-aos-delay="200">Taste the Difference</a>
        </div>
    </section>
    """
}

# 6. CONTACT (3 sections)
pages['contact.html'] = {
    'title': 'Contact',
    'active': 'active_contact',
    'extra_js': '',
    'content': """
    <!-- Section 1: Contact Intro -->
    <section class="pt-32 pb-16 bg-[#FFFAF0] dark:bg-[#1a0f08]">
        <div class="container mx-auto px-6">
            <div class="flex flex-col lg:flex-row gap-16 items-center">
                <div class="w-full lg:w-1/2" data-aos="fade-right">
                    <h1 class="text-5xl lg:text-7xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-6">Let's Talk Cake.</h1>
                    <p class="text-lg text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 mb-10">Whether you're planning a grand wedding or simply craving a box of macarons, our team is here to assist you.</p>
                    
                    <div class="space-y-6">
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-full bg-[#C68E17]/10 flex items-center justify-center text-[#C68E17]">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                            </div>
                            <div>
                                <h4 class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Call Studio</h4>
                                <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">+1 (234) 567-8900</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-full bg-[#C68E17]/10 flex items-center justify-center text-[#C68E17]">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            </div>
                            <div>
                                <h4 class="font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Email Us</h4>
                                <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">hello@maisondoree.com</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Social Icons added after Email Us -->
                    <div class="flex items-center gap-6 mt-10 pt-8 border-t border-[#3E1C00]/10 dark:border-[#F5F5DC]/10">
                        <a href="#" class="w-12 h-12 rounded-full bg-[#3E1C00]/5 dark:bg-white/5 flex items-center justify-center text-[#3E1C00] dark:text-[#F5F5DC] hover:bg-[#C68E17] hover:text-white transition-all duration-300 transform hover:-translate-y-1">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                        </a>
                        <a href="#" class="w-12 h-12 rounded-full bg-[#3E1C00]/5 dark:bg-white/5 flex items-center justify-center text-[#3E1C00] dark:text-[#F5F5DC] hover:bg-[#C68E17] hover:text-white transition-all duration-300 transform hover:-translate-y-1">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                        </a>
                        <a href="#" class="w-12 h-12 rounded-full bg-[#3E1C00]/5 dark:bg-white/5 flex items-center justify-center text-[#3E1C00] dark:text-[#F5F5DC] hover:bg-[#C68E17] hover:text-white transition-all duration-300 transform hover:-translate-y-1">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                        </a>
                    </div>
                </div>
                
                <div class="w-full lg:w-1/2 relative h-[500px] clip-reveal" data-aos="fade-left">
                    <img src="https://images.unsplash.com/photo-1550617931-e17a7b70dce2?q=80&w=2070&auto=format&fit=crop" class="w-full h-full object-cover rounded-[3rem]" alt="Bakery Details">
                    <!-- Floating Decor -->
                    <div class="absolute top-10 -left-10 w-24 h-24 floating">
                        <img src="https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?w=200&auto=format&fit=crop" class="rounded-full shadow-2xl" alt="Macaron">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Enquiry Form -->
    <section class="py-20 bg-white dark:bg-[#2A1300]">
        <div class="container mx-auto px-6 max-w-4xl">
            <div class="bg-[#FFFAF0] dark:bg-[#1a0f08] p-10 md:p-14 rounded-[3rem] shadow-2xl border border-[#3E1C00]/5 dark:border-[#F5F5DC]/5" data-aos="fade-up">
                <h2 class="text-3xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-8 text-center">Custom Order Enquiry</h2>
                
                <form class="space-y-6 relative" id="contact-form">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="relative">
                            <input type="text" id="name" class="peer w-full bg-transparent border-b-2 border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 px-0 py-3 text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] placeholder-transparent transition-colors" placeholder="Name" required>
                            <label for="name" class="absolute left-0 top-3 text-[#3E1C00]/50 dark:text-[#F5F5DC]/50 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-xs peer-focus:text-[#C68E17]">Full Name</label>
                        </div>
                        <div class="relative">
                            <input type="email" id="email" class="peer w-full bg-transparent border-b-2 border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 px-0 py-3 text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] placeholder-transparent transition-colors" placeholder="Email" required>
                            <label for="email" class="absolute left-0 top-3 text-[#3E1C00]/50 dark:text-[#F5F5DC]/50 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-xs peer-focus:text-[#C68E17]">Email Address</label>
                        </div>
                    </div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="relative">
                            <input type="text" id="phone" class="peer w-full bg-transparent border-b-2 border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 px-0 py-3 text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] placeholder-transparent transition-colors" placeholder="Phone">
                            <label for="phone" class="absolute left-0 top-3 text-[#3E1C00]/50 dark:text-[#F5F5DC]/50 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-xs peer-focus:text-[#C68E17]">Phone Number</label>
                        </div>
                        <div class="relative">
                            <select class="w-full bg-transparent border-b-2 border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 px-0 py-3 text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] transition-colors appearance-none cursor-pointer">
                                <option value="" disabled selected class="text-[#3E1C00]/50">Occasion</option>
                                <option value="wedding">Wedding</option>
                                <option value="birthday">Birthday</option>
                                <option value="anniversary">Anniversary</option>
                                <option value="corporate">Corporate Event</option>
                                <option value="other">Other</option>
                            </select>
                            <div class="absolute right-0 top-4 pointer-events-none text-[#3E1C00] dark:text-[#F5F5DC]">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </div>
                        </div>
                    </div>
                    
                    <div class="relative">
                        <textarea id="message" rows="4" class="peer w-full bg-transparent border-b-2 border-[#3E1C00]/20 dark:border-[#F5F5DC]/20 px-0 py-3 text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] placeholder-transparent transition-colors resize-none" placeholder="Message" required></textarea>
                        <label for="message" class="absolute left-0 top-3 text-[#3E1C00]/50 dark:text-[#F5F5DC]/50 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-xs peer-focus:text-[#C68E17]">Tell us about your dream cake...</label>
                    </div>
                    
                    <button type="submit" class="w-full py-4 bg-[#3E1C00] dark:bg-[#F5F5DC] text-[#FFFAF0] dark:text-[#3E1C00] rounded-xl text-lg font-bold hover:bg-[#C68E17] dark:hover:bg-[#C68E17] dark:hover:text-white transition-all shadow-lg hover:shadow-xl mt-4">Send Enquiry</button>
                    
                    <!-- Success message -->
                    <div id="success-msg" class="absolute inset-0 bg-[#FFFAF0] dark:bg-[#1a0f08] flex flex-col items-center justify-center rounded-[3rem] opacity-0 pointer-events-none transition-opacity duration-500 z-10">
                        <div class="w-20 h-20 bg-green-500 text-white rounded-full flex items-center justify-center mb-4">
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                        </div>
                        <h3 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC]">Message Sent!</h3>
                        <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 mt-2">We'll get back to you shortly.</p>
                    </div>
                </form>
            </div>
        </div>
        <script>
            document.getElementById('contact-form').addEventListener('submit', (e) => {
                e.preventDefault();
                document.getElementById('success-msg').classList.remove('opacity-0', 'pointer-events-none');
                setTimeout(() => {
                    document.getElementById('success-msg').classList.add('opacity-0', 'pointer-events-none');
                    e.target.reset();
                }, 3000);
            });
        </script>
    </section>

    <!-- Section 3: Location & Visit -->
    <section class="py-0 relative h-[600px] overflow-hidden group">
        <!-- Google Maps iframe -->
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.25280017042!2d-74.14448731307675!3d40.69763123331908!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2s!4v1700000000000!5m2!1sen!2s" width="100%" height="100%" style="border:0; filter: grayscale(50%) contrast(120%);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        
        <!-- Info Panel -->
        <div class="absolute bottom-10 left-10 md:left-20 bg-white/90 dark:bg-[#1a0f08]/90 backdrop-blur-md p-8 rounded-3xl shadow-2xl max-w-sm border border-white/20 dark:border-white/10" data-aos="fade-up">
            <h3 class="text-2xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Visit The Studio</h3>
            <p class="text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 mb-4 text-sm">123 Patisserie Lane<br>Bakery District, City 12345</p>
            <div class="space-y-1 text-sm text-[#3E1C00] dark:text-[#F5F5DC] font-medium border-t border-[#3E1C00]/10 dark:border-[#F5F5DC]/10 py-4">
                <div class="flex justify-between"><span>Mon - Fri:</span> <span>8:00 AM - 6:00 PM</span></div>
                <div class="flex justify-between"><span>Saturday:</span> <span>9:00 AM - 5:00 PM</span></div>
                <div class="flex justify-between text-[#C68E17]"><span>Sunday:</span> <span>Closed</span></div>
            </div>

        </div>
    </section>
    """
}

# 7. LOGIN PAGE
pages['login.html'] = {
    'title': 'Sign In',
    'active': 'none',
    'extra_js': '',
    'content': """
    <section class="relative min-h-[85vh] flex items-center justify-center bg-[#FDFBF7] dark:bg-[#2A1300] py-20 px-4 sm:px-6">
        <button id="theme-toggle" class="absolute top-6 right-6 p-2 rounded-full bg-white dark:bg-[#1a0f08] shadow-md text-[#3E1C00] dark:text-[#F5F5DC] hover:-translate-y-1 transition-transform z-50">
            <svg class="w-5 h-5 hidden dark:block" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
            <svg class="w-5 h-5 block dark:hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
        </button>
        <div class="max-w-xl w-full bg-white dark:bg-[#1a0f08] rounded-3xl shadow-2xl overflow-hidden flex flex-col" data-aos="zoom-in">
            <!-- Form Side -->
            <div class="p-6 sm:p-10 md:p-16 flex flex-col justify-center">
                <div class="text-center mb-10">
                    <a href="index.html" class="flex items-center justify-center gap-4 mb-6 hover:opacity-80 transition-opacity">
                        <div class="w-12 h-12 bg-[#D4AF37] rounded-full flex items-center justify-center">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 21h18M5 21V8l4 3 3-6 3 6 4-3v13"></path></svg>
                        </div>
                        <span class="text-2xl sm:text-3xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] whitespace-nowrap">Maison Dorée</span>
                    </a>
                    <h3 class="text-xl font-serif text-[#3E1C00]/80 dark:text-[#F5F5DC]/80">Sign In</h3>
                </div>
                
                <form class="space-y-6">
                    <div>
                        <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Email Address</label>
                        <input type="email" class="w-full px-5 py-3 rounded-xl border border-[#3E1C00]/20 dark:border-white/20 bg-transparent text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] transition-colors" placeholder="you@example.com" required>
                    </div>
                    <div>
                        <div class="flex justify-between items-center mb-2">
                            <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC]">Password</label>
                            <a href="#" class="text-xs text-[#C68E17] hover:underline">Forgot Password?</a>
                        </div>
                        <input type="password" class="w-full px-5 py-3 rounded-xl border border-[#3E1C00]/20 dark:border-white/20 bg-transparent text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] transition-colors" placeholder="••••••••" required>
                    </div>
                    
                    <div class="flex items-center">
                        <input type="checkbox" id="remember" class="w-4 h-4 rounded border-[#3E1C00]/20 text-[#C68E17] focus:ring-[#C68E17]">
                        <label for="remember" class="ml-2 text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">Remember me for 30 days</label>
                    </div>
                    
                    <a href="dashboard.html" class="block text-center w-full py-4 bg-[#C68E17] hover:bg-[#D4AF37] text-white rounded-xl font-medium transition-all hover:-translate-y-1 shadow-lg">Sign In</a>
                </form>
                
                <p class="mt-8 text-center text-[13px] sm:text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 whitespace-nowrap tracking-tight sm:tracking-normal">
                    Don't have an account? <a href="signup.html" class="text-[#C68E17] font-bold hover:underline">Create Account</a>
                </p>
            </div>
        </div>
    </section>
    """
}

# 8. SIGNUP PAGE
pages['signup.html'] = {
    'title': 'Create Account',
    'active': 'none',
    'extra_js': '',
    'content': """
    <section class="relative min-h-[85vh] flex items-center justify-center bg-[#FDFBF7] dark:bg-[#2A1300] py-20 px-4 sm:px-6">
        <button id="theme-toggle" class="absolute top-6 right-6 p-2 rounded-full bg-white dark:bg-[#1a0f08] shadow-md text-[#3E1C00] dark:text-[#F5F5DC] hover:-translate-y-1 transition-transform z-50">
            <svg class="w-5 h-5 hidden dark:block" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
            <svg class="w-5 h-5 block dark:hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
        </button>
        <div class="max-w-xl w-full bg-white dark:bg-[#1a0f08] rounded-3xl shadow-2xl overflow-hidden flex flex-col" data-aos="zoom-in">
            <!-- Form Side -->
            <div class="p-6 sm:p-10 md:p-16 flex flex-col justify-center">
                <div class="text-center mb-10">
                    <a href="index.html" class="flex items-center justify-center gap-4 mb-6 hover:opacity-80 transition-opacity">
                        <div class="w-12 h-12 bg-[#D4AF37] rounded-full flex items-center justify-center">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 21h18M5 21V8l4 3 3-6 3 6 4-3v13"></path></svg>
                        </div>
                        <span class="text-2xl sm:text-3xl font-serif font-bold text-[#3E1C00] dark:text-[#F5F5DC] whitespace-nowrap">Maison Dorée</span>
                    </a>
                    <h3 class="text-xl font-serif text-[#3E1C00]/80 dark:text-[#F5F5DC]/80">Create an Account</h3>
                </div>
                
                <form class="space-y-6">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] mb-2">First Name</label>
                            <input type="text" class="w-full px-5 py-3 rounded-xl border border-[#3E1C00]/20 dark:border-white/20 bg-transparent text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] transition-colors" placeholder="John" required>
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Last Name</label>
                            <input type="text" class="w-full px-5 py-3 rounded-xl border border-[#3E1C00]/20 dark:border-white/20 bg-transparent text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] transition-colors" placeholder="Doe" required>
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Email Address</label>
                        <input type="email" class="w-full px-5 py-3 rounded-xl border border-[#3E1C00]/20 dark:border-white/20 bg-transparent text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] transition-colors" placeholder="you@example.com" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-[#3E1C00] dark:text-[#F5F5DC] mb-2">Password</label>
                        <input type="password" class="w-full px-5 py-3 rounded-xl border border-[#3E1C00]/20 dark:border-white/20 bg-transparent text-[#3E1C00] dark:text-[#F5F5DC] focus:outline-none focus:border-[#C68E17] transition-colors" placeholder="••••••••" required>
                    </div>
                    
                    <div class="flex items-start mt-2">
                        <input type="checkbox" id="terms" class="mt-1 w-4 h-4 rounded border-[#3E1C00]/20 text-[#C68E17] focus:ring-[#C68E17]" required>
                        <label for="terms" class="ml-2 text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70">I agree to the <a href="#" class="text-[#C68E17] hover:underline">Terms of Service</a> and <a href="#" class="text-[#C68E17] hover:underline">Privacy Policy</a>.</label>
                    </div>
                    
                    <a href="dashboard.html" class="block text-center w-full py-4 bg-[#3E1C00] dark:bg-[#F5F5DC] hover:bg-[#2A1300] dark:hover:bg-white text-white dark:text-[#3E1C00] rounded-xl font-bold transition-all hover:-translate-y-1 shadow-lg">Create Account</a>
                </form>
                
                <p class="mt-8 text-center text-[13px] sm:text-sm text-[#3E1C00]/70 dark:text-[#F5F5DC]/70 whitespace-nowrap tracking-tight sm:tracking-normal">
                    Already have an account? <a href="login.html" class="text-[#C68E17] font-bold hover:underline">Sign In</a>
                </p>
            </div>
        </div>
    </section>
    """
}

def generate_file(filename):
    if filename in pages:
        p = pages[filename]
        
        # Determine active nav
        if filename in ['login.html', 'signup.html']:
            h_html = ''
            f_html = ''
        else:
            h_html = header_html.format(
                active_home='after:w-full' if p.get('active') == 'active_home' else '',
                active_studio='after:w-full' if p.get('active') == 'active_studio' else '',
                active_menu='after:w-full' if p.get('active') == 'active_menu' else '',
                active_order='after:w-full' if p.get('active') == 'active_order' else '',
                active_about='after:w-full' if p.get('active') == 'active_about' else '',
                active_contact='after:w-full' if p.get('active') == 'active_contact' else '',
                active_dashboard='after:w-full' if p.get('active') == 'active_dashboard' else ''
            )
            f_html = footer_html
        
        full_html = base_html_template.format(
            title=p['title'],
            header=h_html,
            content=p['content'],
            footer=f_html,
            extra_js=p['extra_js']
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_html)

for fn in pages.keys():
    generate_file(fn)

print("Files 2 generated successfully.")

