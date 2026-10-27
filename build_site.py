import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

with open('tailwind_config.json', 'r', encoding='utf-8') as f:
    tailwind_config_content = f.read().strip()

def get_head_html(title, description):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="Vishnu Restaurant, South Indian Vegetarian, Mayiladuthurai, Filter Coffee, Malli Idly, Ghee Roast Dosa, Pure Veg, Jain Food" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:type" content="restaurant" />
  <meta property="og:image" content="https://lh3.googleusercontent.com/aida-public/AB6AXuAyH4rnenavu3M09LifFBhx_Sakj8yOGTNwTJ8KKruQViBDlVVuQloGMR9ygVHWi1_h3rM6CnqpXw8PMHjjFM0ux1fsTCQ-eepY4SDR97HZm8D2jLOm7wInUp-CwxNMGwNpprkujV65EhTu5p5cdg71aOByC-oGNjzXi8IdhNtxLi9lT1JrH5KN94TE_LiwsKO4c2hNgzHhuXQX2UuVubZLS7GTgj3l8QAlHBaDHdLVstzTOqvG9v8iQw" />
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>☕</text></svg>" />
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet" />
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {tailwind_config_content};
  </script>
  
  <!-- Custom Application Stylesheet -->
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body class="bg-surface font-body-md text-on-surface antialiased">
"""

def get_header_html(current_page):
    def nav_class(page):
        if page == current_page:
            return 'aria-current="page" class="px-space-md py-2 transition-colors bg-surface-container text-primary font-title-md rounded-lg shadow-sm"'
        return 'class="px-space-md py-2 font-label-lg text-label-lg text-on-surface-variant hover:text-on-surface rounded-lg transition-colors"'

    return f"""<header class="fixed top-0 left-0 w-full z-50 header-glass shadow-[0_1px_8px_rgba(41,21,11,0.06)]">
  <!-- Top Announcement Bar -->
  <div class="w-full bg-surface-container-high border-b border-outline-variant/30">
    <div class="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-12 h-10 flex items-center justify-between text-on-surface-variant font-label-md text-xs sm:text-label-md">
      <div class="flex items-center gap-2 overflow-hidden">
        <span class="w-2.5 h-2.5 rounded-full bg-secondary shrink-0 animate-pulse"></span>
        <span class="truncate">100% Pure Vegetarian | Traditional South Indian Delights | Daily: 6:30 AM - 10:30 PM</span>
      </div>
      <div class="hidden md:flex items-center gap-space-lg shrink-0">
        <a class="flex items-center gap-1.5 text-tertiary hover:text-primary transition-colors font-semibold" href="tel:+918870810456">
          <span class="material-symbols-outlined text-[16px]">call</span>
          <span>+91 8870810456</span>
        </a>
        <span class="text-outline-variant">|</span>
        <span class="flex items-center gap-1 text-on-surface-variant">
          <span class="material-symbols-outlined text-[16px] text-secondary">verified</span>
          <span>Authentic Ghee &amp; Filter Coffee</span>
        </span>
      </div>
    </div>
  </div>

  <!-- Main Navigation Bar -->
  <div class="h-20 bg-surface/95 backdrop-blur-md">
    <div class="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-12 h-full flex items-center justify-between gap-space-md">
      <!-- Logo & Brand -->
      <a href="index.html" class="flex items-center gap-3 group">
        <div class="w-10 h-10 rounded-xl gold-brass-gradient flex items-center justify-center text-white shadow-md group-hover:scale-105 transition-transform shrink-0">
          <span class="material-symbols-outlined text-[24px]">coffee</span>
        </div>
        <div class="flex flex-col">
          <span class="font-headline-sm text-lg sm:text-headline-sm text-primary tracking-tight font-semibold leading-tight">Vishnu Restaurant</span>
          <span class="font-label-heritage text-[10px] text-tertiary uppercase tracking-widest font-semibold">Pure Veg Heritage • Est. 1984</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav class="hidden lg:flex items-center gap-space-sm p-1">
        <a href="index.html" {nav_class('home')}>Home</a>
        <a href="menus.html" {nav_class('menus')}>Menus</a>
        <a href="about.html" {nav_class('about')}>Our Story</a>
        <a href="contact.html" {nav_class('contact')}>Contact &amp; Reserve</a>
      </nav>

      <!-- Right CTAs -->
      <div class="flex items-center gap-2 sm:gap-space-md">
        <!-- 100% Pure Veg Tag -->
        <div class="hidden sm:flex items-center gap-2 px-3 py-1 rounded bg-secondary/10 border border-secondary/20">
          <span class="w-3.5 h-3.5 rounded-sm border border-secondary flex items-center justify-center p-0.5">
            <span class="w-2 h-2 rounded-full bg-secondary block"></span>
          </span>
          <span class="font-label-heritage text-label-heritage text-secondary tracking-wider uppercase font-semibold">100% Pure Veg</span>
        </div>

        <!-- Book a Table Button -->
        <button onclick="openReservationModal()" class="hidden md:flex h-10 px-4 rounded-lg bg-surface-container hover:bg-surface-container-high text-primary font-label-lg text-label-lg transition-colors items-center gap-1.5" type="button">
          <span class="material-symbols-outlined text-[18px]">table_restaurant</span>
          <span>Book a Table</span>
        </button>

        <!-- Order Online / Cart Button with Live Counter -->
        <button onclick="openCartDrawer()" class="h-10 px-3.5 sm:px-4 rounded-lg bg-primary hover:bg-tertiary text-on-primary font-label-lg text-label-lg transition-all shadow-[0_2px_8px_rgba(144,63,0,0.2)] flex items-center gap-2 relative" type="button" aria-label="Open Shopping Basket">
          <span class="material-symbols-outlined text-[20px]">shopping_bag</span>
          <span class="hidden sm:inline">Order Online</span>
          <span class="cart-badge-counter hidden min-w-[20px] h-5 px-1 rounded-full bg-secondary text-white text-xs font-bold flex items-center justify-center">0</span>
        </button>

        <!-- Mobile Hamburger Button -->
        <button onclick="openMobileNav()" class="lg:hidden p-2 rounded-lg text-primary hover:bg-surface-container flex items-center justify-center" aria-label="Open Navigation Drawer">
          <span class="material-symbols-outlined text-[28px]">menu</span>
        </button>
      </div>
    </div>
  </div>
</header>
"""

def get_footer_html():
    return """<footer class="w-full bg-surface-container-low border-t border-outline-variant/30 mt-12 pb-16 lg:pb-0">
  <div class="max-w-[1280px] mx-auto px-6 lg:px-12 pt-space-xl pb-space-lg">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-space-xl mb-space-xl">
      <!-- Col 1: Brand Info -->
      <div class="space-y-space-md">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-lg bg-primary-container flex items-center justify-center text-on-primary-container">
            <span class="material-symbols-outlined text-[20px]">restaurant</span>
          </div>
          <div class="flex flex-col">
            <span class="font-headline-sm text-headline-sm text-primary font-semibold">Vishnu Restaurant</span>
            <span class="font-label-heritage text-label-heritage text-tertiary uppercase tracking-wider">Pure Veg Tradition</span>
          </div>
        </div>
        <p class="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
          Honoring timeless South Indian kitchen craftsmanship since 1984. Prepared with slow-stone ground batter, 100% pure farm cow ghee, and freshly hand-pounded spices.
        </p>
        <div class="flex items-center gap-2 pt-1">
          <div class="w-4 h-4 rounded-sm border-2 border-secondary flex items-center justify-center">
            <span class="w-2 h-2 rounded-full bg-secondary block"></span>
          </div>
          <span class="font-label-heritage text-label-heritage text-secondary tracking-widest uppercase font-semibold">Certified Pure Vegetarian Sanctuary</span>
        </div>
      </div>

      <!-- Col 2: Tiffin Specialties -->
      <div class="space-y-space-sm">
        <span class="font-title-md text-title-md text-on-surface block font-bold">Tiffin Specialties</span>
        <ul class="space-y-2 font-body-sm text-body-sm text-on-surface-variant">
          <li><a class="hover:text-primary transition-colors flex items-center gap-1.5" href="menus.html#section-tiffins"><span class="text-tertiary">›</span> Malli Steamed Idly &amp; Medu Vada</a></li>
          <li><a class="hover:text-primary transition-colors flex items-center gap-1.5" href="menus.html#section-tiffins"><span class="text-tertiary">›</span> Crispy Ghee Roast Masala Dosa</a></li>
          <li><a class="hover:text-primary transition-colors flex items-center gap-1.5" href="menus.html#section-tiffins"><span class="text-tertiary">›</span> Melts-in-Mouth Ven Pongal</a></li>
          <li><a class="hover:text-primary transition-colors flex items-center gap-1.5" href="menus.html#section-tiffins"><span class="text-tertiary">›</span> Lace Appam with Coconut Milk</a></li>
          <li><a class="hover:text-primary transition-colors flex items-center gap-1.5" href="menus.html#section-drinks"><span class="text-tertiary">›</span> Kumbakonam Degree Filter Coffee</a></li>
        </ul>
      </div>

      <!-- Col 3: Dining Hours -->
      <div class="space-y-space-sm">
        <span class="font-title-md text-title-md text-on-surface block font-bold">Dining Hours &amp; Timings</span>
        <div class="space-y-2 font-body-sm text-body-sm text-on-surface-variant">
          <div class="flex justify-between py-1 border-b border-outline-variant/20">
            <span class="text-on-surface font-medium">Morning Tiffins</span>
            <span>6:30 AM - 11:30 AM</span>
          </div>
          <div class="flex justify-between py-1 border-b border-outline-variant/20">
            <span class="text-on-surface font-medium">Full Meals &amp; Thali</span>
            <span>11:45 AM - 3:30 PM</span>
          </div>
          <div class="flex justify-between py-1 border-b border-outline-variant/20">
            <span class="text-on-surface font-medium">Snacks &amp; Coffee</span>
            <span>3:30 PM - 6:30 PM</span>
          </div>
          <div class="flex justify-between py-1">
            <span class="text-on-surface font-medium">Dinner Tiffins</span>
            <span>6:30 PM - 10:30 PM</span>
          </div>
        </div>
      </div>

      <!-- Col 4: Location & Contact -->
      <div class="space-y-space-sm">
        <span class="font-title-md text-title-md text-on-surface block font-bold">Visit Us</span>
        <p class="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
          No 27-A Hajiyar nagar,4th cross street,koranadu, Mayiladuthurai, Tamilnadu,609001.
        </p>
        <div class="space-y-1.5 font-body-sm text-body-sm text-on-surface-variant pt-2">
          <p class="flex items-center gap-2">
            <span class="material-symbols-outlined text-[18px] text-tertiary">call</span>
            <a href="tel:+918870810456" class="hover:text-primary transition-colors">+91 8870810456</a>
          </p>
          <p class="flex items-center gap-2">
            <span class="material-symbols-outlined text-[18px] text-tertiary">mail</span>
            <a href="mailto:inform2ranjith247456@gmail.com" class="hover:text-primary transition-colors">inform2ranjith247456@gmail.com</a>
          </p>
          <p class="flex items-center gap-2">
            <span class="material-symbols-outlined text-[18px] text-tertiary">room_service</span>
            <a href="tel:+918870810456" class="hover:text-primary transition-colors">Catering: 8870810456</a>
          </p>
        </div>
      </div>
    </div>

    <!-- Bottom copyright row -->
    <div class="pt-space-md border-t border-outline-variant/30 flex flex-col sm:flex-row items-center justify-between gap-4 font-body-sm text-body-sm text-on-surface-variant text-xs">
      <p>© 2026 Vishnu Restaurant. All Rights Reserved. Pure Vegetarian Culinary Trust Since 1984.</p>
      <div class="flex flex-wrap items-center gap-space-lg">
        <a class="hover:text-primary transition-colors" href="index.html">Home</a>
        <a class="hover:text-primary transition-colors" href="menus.html">Menu</a>
        <a class="hover:text-primary transition-colors" href="about.html">Story</a>
        <a class="hover:text-primary transition-colors" href="contact.html">Contact</a>
        <span class="text-outline-variant">|</span>
        <span class="text-on-surface-variant">FSSAI Lic. #12418002001928</span>
      </div>
  </div>
</footer>
"""

def get_shared_modals_html():
    return """<!-- CART DRAWER BACKDROP & PANEL -->
<div id="cart-drawer-backdrop" class="drawer-backdrop fixed inset-0 bg-black/60 z-50 transition-opacity backdrop-blur-xs" onclick="closeCartDrawer()"></div>
<div id="cart-drawer-panel" class="drawer-panel fixed top-0 right-0 h-full w-full max-w-md bg-surface shadow-2xl z-50 flex flex-col transition-transform duration-300">
  <div class="p-5 border-b border-outline-variant/30 flex items-center justify-between bg-surface-container-low">
    <div class="flex items-center gap-2.5">
      <div class="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center text-primary">
        <span class="material-symbols-outlined text-[22px]">shopping_cart</span>
      </div>
      <div>
        <h3 class="font-headline-sm text-lg text-on-surface font-semibold">Your Tiffin Basket</h3>
        <p class="font-label-heritage text-xs text-secondary font-semibold uppercase tracking-wider">100% Pure Vegetarian</p>
      </div>
    </div>
    <button onclick="closeCartDrawer()" class="p-1.5 rounded-lg text-on-surface-variant hover:bg-surface-container transition-colors" aria-label="Close Cart">
      <span class="material-symbols-outlined text-[22px]">close</span>
    </button>
  </div>

  <div class="flex-1 overflow-y-auto p-5 space-y-3">
    <div id="cart-empty-state" class="py-16 text-center space-y-4">
      <div class="w-20 h-20 mx-auto rounded-full bg-surface-container-high flex items-center justify-center text-tertiary">
        <span class="material-symbols-outlined text-[40px]">lunch_dining</span>
      </div>
      <div class="space-y-1">
        <h4 class="font-headline-sm text-lg text-on-surface">Your basket is feeling empty</h4>
        <p class="font-body-sm text-on-surface-variant max-w-xs mx-auto text-xs">Explore our hot morning tiffins, golden dosas, and degree filter coffee!</p>
      </div>
      <a href="menus.html" onclick="closeCartDrawer()" class="inline-flex items-center gap-2 px-6 py-2.5 rounded-lg bg-primary hover:bg-tertiary text-on-primary font-label-lg text-sm transition-colors shadow">
        <span>Browse Our Menu</span>
        <span class="material-symbols-outlined text-sm">arrow_forward</span>
      </a>
    </div>
    <div id="cart-items-list" class="space-y-3"></div>
  </div>

  <div id="cart-footer-summary" class="hidden p-5 border-t border-outline-variant/30 bg-surface-container-low space-y-4">
    <div class="space-y-1.5">
      <label class="block font-label-md text-xs font-semibold text-on-surface uppercase tracking-wider">Order Preference</label>
      <div class="grid grid-cols-3 gap-2">
        <label class="flex items-center justify-center gap-1.5 py-2 px-2 rounded-lg border border-outline-variant/50 cursor-pointer text-xs font-medium text-on-surface hover:bg-surface-container has-[:checked]:bg-primary has-[:checked]:text-on-primary has-[:checked]:border-primary transition-all">
          <input type="radio" name="orderType" value="Dine-in Pre-order" class="hidden" checked />
          <span>Dine-In</span>
        </label>
        <label class="flex items-center justify-center gap-1.5 py-2 px-2 rounded-lg border border-outline-variant/50 cursor-pointer text-xs font-medium text-on-surface hover:bg-surface-container has-[:checked]:bg-primary has-[:checked]:text-on-primary has-[:checked]:border-primary transition-all">
          <input type="radio" name="orderType" value="Self Pickup (20 Min)" class="hidden" />
          <span>Pickup</span>
        </label>
        <label class="flex items-center justify-center gap-1.5 py-2 px-2 rounded-lg border border-outline-variant/50 cursor-pointer text-xs font-medium text-on-surface hover:bg-surface-container has-[:checked]:bg-primary has-[:checked]:text-on-primary has-[:checked]:border-primary transition-all">
          <input type="radio" name="orderType" value="Express Delivery" class="hidden" />
          <span>Delivery</span>
        </label>
      </div>
    </div>

    <div class="space-y-1">
      <input id="cart-special-notes" type="text" placeholder="Kitchen instructions (e.g., Less spicy, extra sambar)" class="w-full text-xs px-3 py-2 rounded-lg bg-surface border border-outline-variant/50 focus:border-primary focus:outline-none text-on-surface" />
    </div>

    <div class="space-y-1.5 text-xs text-on-surface-variant pt-2 border-t border-outline-variant/20">
      <div class="flex justify-between">
        <span>Item Subtotal</span>
        <span id="drawer-subtotal" class="font-semibold text-on-surface">₹0</span>
      </div>
      <div class="flex justify-between">
        <span>GST (5%)</span>
        <span id="drawer-gst">₹0</span>
      </div>
      <div class="flex justify-between">
        <span>Eco-friendly Packing</span>
        <span id="drawer-packing">₹15</span>
      </div>
      <div class="flex justify-between text-base font-bold text-on-surface pt-2 border-t border-outline-variant/30">
        <span>Total Payable</span>
        <span id="drawer-final-total" class="text-primary font-headline-sm">₹0</span>
      </div>
    </div>

    <div class="space-y-2 pt-1">
      <button onclick="orderViaWhatsApp()" class="w-full h-11 rounded-lg bg-[#25D366] hover:bg-[#20BD5A] text-white font-label-lg text-sm font-semibold transition-all flex items-center justify-center gap-2 shadow">
        <span class="material-symbols-outlined text-[18px]">chat</span>
        <span>Send Order via WhatsApp</span>
      </button>
      <button onclick="simulateInstantCheckout()" class="w-full h-11 rounded-lg bg-primary hover:bg-tertiary text-on-primary font-label-lg text-sm font-semibold transition-all flex items-center justify-center gap-2 shadow">
        <span class="material-symbols-outlined text-[18px]">bolt</span>
        <span>Simulate Instant Online Order</span>
      </button>
      <div class="flex items-center justify-between text-[11px] text-on-surface-variant px-1">
        <span>Instant preparation in 15-20 mins</span>
        <button onclick="clearAllCart()" class="text-error hover:underline">Clear Basket</button>
      </div>
    </div>
  </div>
</div>

<!-- MOBILE NAVIGATION DRAWER -->
<div id="mobile-nav-backdrop" class="drawer-backdrop fixed inset-0 bg-black/60 z-50 transition-opacity backdrop-blur-xs" onclick="closeMobileNav()"></div>
<div id="mobile-nav-panel" class="drawer-panel-left fixed top-0 left-0 h-full w-[85%] max-w-sm bg-surface shadow-2xl z-50 flex flex-col transition-transform duration-300">
  <div class="p-6 border-b border-outline-variant/30 bg-surface-container-low flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="w-8 h-8 rounded-lg gold-brass-gradient flex items-center justify-center text-white shrink-0">
        <span class="material-symbols-outlined text-[18px]">coffee</span>
      </div>
      <div>
        <span class="font-headline-sm text-base text-primary block leading-tight font-semibold">Vishnu Restaurant</span>
        <span class="font-label-heritage text-[10px] text-tertiary uppercase tracking-widest font-semibold">Pure Veg Heritage • Est. 1984</span>
      </div>
    </div>
    <button onclick="closeMobileNav()" class="p-1 rounded-lg text-on-surface hover:bg-surface-container" aria-label="Close Menu">
      <span class="material-symbols-outlined text-[24px]">close</span>
    </button>
  </div>

  <nav class="flex-1 overflow-y-auto p-5 space-y-1">
    <a href="index.html" class="flex items-center gap-3 px-4 py-3 rounded-xl font-label-lg text-base text-on-surface hover:bg-surface-container transition-colors">
      <span class="material-symbols-outlined text-primary text-[20px]">home</span>
      <span>Home</span>
    </a>
    <a href="menus.html" class="flex items-center gap-3 px-4 py-3 rounded-xl font-label-lg text-base text-on-surface hover:bg-surface-container transition-colors">
      <span class="material-symbols-outlined text-primary text-[20px]">restaurant_menu</span>
      <span>Menus &amp; Specialties</span>
    </a>
    <a href="about.html" class="flex items-center gap-3 px-4 py-3 rounded-xl font-label-lg text-base text-on-surface hover:bg-surface-container transition-colors">
      <span class="material-symbols-outlined text-primary text-[20px]">history_edu</span>
      <span>Our Story &amp; Masters</span>
    </a>
    <a href="contact.html" class="flex items-center gap-3 px-4 py-3 rounded-xl font-label-lg text-base text-on-surface hover:bg-surface-container transition-colors">
      <span class="material-symbols-outlined text-primary text-[20px]">pin_drop</span>
      <span>Contact &amp; Reservations</span>
    </a>

    <div class="pt-6 mt-6 border-t border-outline-variant/30 space-y-3">
      <button onclick="closeMobileNav(); openReservationModal();" class="w-full py-3 rounded-xl bg-surface-container hover:bg-surface-container-high text-primary font-label-lg font-semibold flex items-center justify-center gap-2">
        <span class="material-symbols-outlined text-[20px]">table_restaurant</span>
        <span>Book a Family Table</span>
      </button>
      <button onclick="closeMobileNav(); openCartDrawer();" class="w-full py-3 rounded-xl bg-primary hover:bg-tertiary text-on-primary font-label-lg font-semibold flex items-center justify-center gap-2 shadow">
        <span class="material-symbols-outlined text-[20px]">shopping_bag</span>
        <span>Order Online Basket</span>
      </button>
    </div>

    <div class="pt-6 space-y-2 text-xs text-on-surface-variant">
      <p class="flex items-center gap-2"><span class="material-symbols-outlined text-secondary text-sm">schedule</span> Open Daily: 6:30 AM - 10:30 PM</p>
      <p class="flex items-center gap-2"><a href="tel:+918870810456" class="hover:text-primary flex items-center gap-2"><span class="material-symbols-outlined text-tertiary text-sm">call</span> +91 8870810456</a></p>
      <p class="flex items-center gap-2"><span class="material-symbols-outlined text-primary text-sm">location_on</span> No 27-A Hajiyar nagar, Mayiladuthurai</p>
    </div>
  </nav>
</div>

<!-- UNIVERSAL TABLE RESERVATION MODAL -->
<div id="reservation-modal-backdrop" class="modal-backdrop drawer-backdrop fixed inset-0 bg-black/60 z-50 flex items-center justify-center p-4 backdrop-blur-xs">
  <div class="modal-content bg-surface max-w-lg w-full rounded-2xl shadow-2xl border border-outline-variant/30 overflow-hidden relative max-h-[90vh] flex flex-col">
    <div class="p-6 bg-surface-container-low border-b border-outline-variant/30 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center text-primary">
          <span class="material-symbols-outlined text-[22px]">table_restaurant</span>
        </div>
        <div>
          <h3 class="font-headline-sm text-xl text-on-surface font-semibold">Reserve Your Table</h3>
          <p class="font-label-heritage text-xs text-secondary font-semibold uppercase tracking-wider">Instant Confirmation • No Waiting</p>
        </div>
      </div>
      <button onclick="closeReservationModal()" class="p-1.5 rounded-lg text-on-surface-variant hover:bg-surface-container" aria-label="Close Reservation Modal">
        <span class="material-symbols-outlined text-[22px]">close</span>
      </button>
    </div>

    <div id="res-modal-form-view" class="p-6 overflow-y-auto space-y-4">
      <form id="reservation-modal-form" onsubmit="handleModalReservationSubmit(event)" class="space-y-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block font-label-md text-xs font-semibold text-on-surface mb-1" for="resName">Your Full Name *</label>
            <input required id="resName" name="resName" type="text" placeholder="e.g. Radhakrishnan" class="w-full h-10 px-3 rounded-lg bg-surface-container text-on-surface font-body-sm text-sm border border-outline-variant/40 focus:border-primary focus:outline-none" />
          </div>
          <div>
            <label class="block font-label-md text-xs font-semibold text-on-surface mb-1" for="resPhone">Phone Number (SMS Alert) *</label>
            <input required id="resPhone" name="resPhone" type="tel" placeholder="+91 98400 12345" class="w-full h-10 px-3 rounded-lg bg-surface-container text-on-surface font-body-sm text-sm border border-outline-variant/40 focus:border-primary focus:outline-none" />
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div>
            <label class="block font-label-md text-xs font-semibold text-on-surface mb-1" for="res-modal-date">Dining Date *</label>
            <input required id="res-modal-date" name="resDate" type="date" class="w-full h-10 px-2 rounded-lg bg-surface-container text-on-surface font-body-sm text-sm border border-outline-variant/40 focus:border-primary focus:outline-none" />
          </div>
          <div>
            <label class="block font-label-md text-xs font-semibold text-on-surface mb-1" for="resTime">Preferred Slot *</label>
            <select required id="resTime" name="resTime" class="w-full h-10 px-2 rounded-lg bg-surface-container text-on-surface font-body-sm text-sm border border-outline-variant/40 focus:border-primary focus:outline-none">
              <option value="7:30 AM">Breakfast (7:30 AM)</option>
              <option value="9:00 AM">Breakfast (9:00 AM)</option>
              <option value="12:30 PM" selected>Lunch Thali (12:30 PM)</option>
              <option value="1:45 PM">Lunch Thali (1:45 PM)</option>
              <option value="4:30 PM">Evening Tiffin (4:30 PM)</option>
              <option value="6:00 PM">Evening Snacks (6:00 PM)</option>
              <option value="8:00 PM">Dinner (8:00 PM)</option>
              <option value="9:15 PM">Dinner (9:15 PM)</option>
            </select>
          </div>
          <div>
            <label class="block font-label-md text-xs font-semibold text-on-surface mb-1" for="resGuests">Guests *</label>
            <select required id="resGuests" name="resGuests" class="w-full h-10 px-2 rounded-lg bg-surface-container text-on-surface font-body-sm text-sm border border-outline-variant/40 focus:border-primary focus:outline-none">
              <option value="1">1 Person</option>
              <option value="2" selected>2 Persons</option>
              <option value="4">4 Persons (Family)</option>
              <option value="6">6 Persons</option>
              <option value="8">8 Persons</option>
              <option value="10+">10+ Persons</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block font-label-md text-xs font-semibold text-on-surface mb-1" for="resSeating">Seating &amp; Dining Preference</label>
          <select id="resSeating" name="resSeating" class="w-full h-10 px-3 rounded-lg bg-surface-container text-on-surface font-body-sm text-sm border border-outline-variant/40 focus:border-primary focus:outline-none">
            <option value="Main AC Hall">Main Air-Conditioned Family Dining Hall</option>
            <option value="Traditional Banana Leaf">Traditional Banana Leaf Service Wing</option>
            <option value="Heritage Window Section">Heritage Temple-Facing Window View</option>
          </select>
        </div>

        <div>
          <label class="block font-label-md text-xs font-semibold text-on-surface mb-1" for="resNotes">Special Requests (Optional)</label>
          <input id="resNotes" name="resNotes" type="text" placeholder="e.g., Jain / Sattvic preparation, High chair for toddler" class="w-full h-10 px-3 rounded-lg bg-surface-container text-on-surface font-body-sm text-sm border border-outline-variant/40 focus:border-primary focus:outline-none" />
        </div>

        <button type="submit" class="w-full h-12 rounded-lg bg-primary hover:bg-tertiary text-on-primary font-label-lg font-semibold transition-all flex items-center justify-center gap-2 shadow-md">
          <span class="material-symbols-outlined text-[20px]">event_seat</span>
          <span>Confirm Table Reservation</span>
        </button>
      </form>
    </div>

    <div id="res-modal-success-view" class="hidden p-8 text-center space-y-5">
      <div class="w-16 h-16 mx-auto rounded-full bg-secondary/15 flex items-center justify-center text-secondary">
        <span class="material-symbols-outlined text-[36px]" style="font-variation-settings: 'FILL' 1;">check_circle</span>
      </div>
      <div>
        <h4 class="font-headline-sm text-2xl text-on-surface font-semibold">Vanakkam! Your Table is Reserved</h4>
        <p class="font-body-sm text-on-surface-variant max-w-sm mx-auto mt-1">We look forward to honoring you with our authentic Dakshin vegetarian hospitality.</p>
      </div>

      <div id="res-success-details"></div>

      <button onclick="resetReservationModal()" class="w-full h-11 rounded-lg bg-primary hover:bg-tertiary text-on-primary font-label-lg font-semibold transition-colors">
        Done
      </button>
    </div>
  </div>
</div>

<!-- SIMULATED ORDER CHECKOUT SUCCESS MODAL -->
<div id="checkout-success-modal" class="modal-backdrop drawer-backdrop fixed inset-0 bg-black/60 z-50 flex items-center justify-center p-4 backdrop-blur-xs">
  <div class="modal-content bg-surface max-w-md w-full rounded-2xl shadow-2xl border border-outline-variant/30 p-6 text-center space-y-4">
    <div class="w-16 h-16 mx-auto rounded-full bg-secondary/15 flex items-center justify-center text-secondary">
      <span class="material-symbols-outlined text-[36px]">receipt_long</span>
    </div>
    <div>
      <span class="font-label-heritage uppercase tracking-wider text-xs text-secondary font-bold block">Order Sent to Kitchen</span>
      <h3 class="font-headline-sm text-xl text-on-surface mt-1 font-semibold">Order #<span id="checkout-order-id">WR-ORD-1001</span></h3>
      <p class="font-body-sm text-on-surface-variant mt-1 text-sm">Our master chefs are slow-roasting your dosas and simmering fresh filter coffee right now.</p>
    </div>
    <div id="checkout-items-summary" class="bg-surface-container-low p-4 rounded-xl border border-outline-variant/20 text-left"></div>
    <button onclick="closeCheckoutModal()" class="w-full h-11 rounded-lg bg-primary hover:bg-tertiary text-on-primary font-label-lg font-semibold transition-colors">
      Back to Website
    </button>
  </div>
</div>

<!-- MOBILE BOTTOM DOCK -->
<div class="mobile-bottom-dock lg:hidden fixed bottom-0 left-0 w-full z-40 px-4 py-2 flex items-center justify-around text-on-surface-variant">
  <a href="index.html" class="flex flex-col items-center gap-0.5 text-xs font-medium hover:text-primary transition-colors">
    <span class="material-symbols-outlined text-[22px]">home</span>
    <span>Home</span>
  </a>
  <a href="menus.html" class="flex flex-col items-center gap-0.5 text-xs font-medium hover:text-primary transition-colors">
    <span class="material-symbols-outlined text-[22px]">restaurant_menu</span>
    <span>Menu</span>
  </a>
  <button onclick="openCartDrawer()" class="flex flex-col items-center gap-0.5 text-xs font-medium text-primary hover:text-tertiary transition-colors relative" aria-label="View Order Basket">
    <div class="relative">
      <span class="material-symbols-outlined text-[24px]">shopping_bag</span>
      <span class="cart-badge-counter hidden absolute -top-1 -right-2 min-w-[18px] h-[18px] px-1 rounded-full bg-secondary text-white text-[10px] font-bold flex items-center justify-center">0</span>
    </div>
    <span>Basket</span>
  </button>
  <button onclick="openReservationModal()" class="flex flex-col items-center gap-0.5 text-xs font-medium hover:text-primary transition-colors" aria-label="Book a Table">
    <span class="material-symbols-outlined text-[22px]">table_restaurant</span>
    <span>Reserve</span>
  </button>
  <a href="tel:+918870810456" class="flex flex-col items-center gap-0.5 text-xs font-medium hover:text-primary transition-colors">
    <span class="material-symbols-outlined text-[22px]">call</span>
    <span>Call</span>
  </a>
</div>

<!-- TOAST CONTAINER -->
<div id="toast-container"></div>

<!-- Application Scripts -->
<script src="assets/js/menu-data.js"></script>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

print("Helper functions ready.")

def apply_custom_replacements(html):
    """Sweep any remaining old values from raw HTML and replace with Vishnu Restaurant details."""
    replacements = [
        # Restaurant name
        ("Welcome Restaurant", "Vishnu Restaurant"),
        ("welcome restaurant", "vishnu restaurant"),
        # Phones - various old formats
        ("+91 44 2434 5678 / +91 44 2434 5679", "+91 8870810456"),
        ("+91 44 2434 5678", "+91 8870810456"),
        ("+91 44 2434 5679", "+91 8870810456"),
        ("+91 44 2847 1984", "+91 8870810456"),
        ("+91 98400 12345", "8870810456"),
        ("+91 98401 23456", "8870810456"),
        ("98400 12345", "8870810456"),
        ("98401 23456", "8870810456"),
        # Tel hrefs
        ('href="tel:+914424345678"', 'href="tel:+918870810456"'),
        ('href="tel:+914424345679"', 'href="tel:+918870810456"'),
        ('href="tel:+914428471984"', 'href="tel:+918870810456"'),
        ('href="tel:+919840123456"', 'href="tel:+918870810456"'),
        ('href="tel:+919840012345"', 'href="tel:+918870810456"'),
        ('placeholder="+91 98400 12345"', 'placeholder="+91 8870810456"'),
        ('placeholder="+91 98400 00000"', 'placeholder="+91 8870810456"'),
        # Email
        ("dine@welcomerestaurant.in", "inform2ranjith247456@gmail.com"),
        ("info@welcomerestaurant.in", "inform2ranjith247456@gmail.com"),
        ("contact@welcomerestaurant.in", "inform2ranjith247456@gmail.com"),
        ('href="mailto:contact@welcomerestaurant.in"', 'href="mailto:inform2ranjith247456@gmail.com"'),
        ('href="mailto:dine@welcomerestaurant.in"', 'href="mailto:inform2ranjith247456@gmail.com"'),
        # Catering hotline text variations
        ("Catering &amp; Bulk Orders: +91 98400 12345", "Catering &amp; Bulk Orders: 8870810456"),
        ("Catering Hotline (+91 98400 12345)", "Catering Hotline (8870810456)"),
        # Old address variants
        ("No. 42, Temple Tower Road, Near Kapaleeshwarar Temple, Mylapore, Chennai, Tamil Nadu 600004",
         "No 27-A Hajiyar nagar,4th cross street,koranadu, Mayiladuthurai, Tamilnadu,609001."),
        ("No. 42, Temple Tower Road, Near Kapaleeshwarar Temple West Gate, Mylapore, Chennai, Tamil Nadu 600004",
         "No 27-A Hajiyar nagar,4th cross street,koranadu, Mayiladuthurai, Tamilnadu,609001."),
        ("No. 42, Temple Tower Road, Near Kapaleeshwarar Temple, Mylapore, Chennai",
         "No 27-A Hajiyar nagar,4th cross street,koranadu, Mayiladuthurai, Tamilnadu,609001."),
        ("#42 Heritage Temple Road, Gandhi Nagar, Mylapore Quarter, Tamil Nadu 600004",
         "No 27-A Hajiyar nagar,4th cross street,koranadu, Mayiladuthurai, Tamilnadu,609001."),
        # Visit Us heading in footer
        ("Visit Us in Mylapore", "Visit Us"),
        # Near temple text in footer nav
        ("Near Kapaleeshwarar Temple, Mylapore", "No 27-A Hajiyar nagar, Mayiladuthurai"),
        # Copyright
        ("© 2024 Welcome Restaurant. All Rights Reserved. Pure Vegetarian Culinary Trust.",
         "© 2026 Vishnu Restaurant. All Rights Reserved. Pure Vegetarian Culinary Trust Since 1984."),
        # Keywords meta
        ('content="Welcome Restaurant, South Indian Vegetarian, Mylapore, Chennai, Filter Coffee, Malli Idly, Ghee Roast Dosa, Pure Veg, Jain Food"',
         'content="Vishnu Restaurant, South Indian Vegetarian, Mayiladuthurai, Filter Coffee, Malli Idly, Ghee Roast Dosa, Pure Veg, Jain Food"'),
    ]
    for old, new in replacements:
        html = html.replace(old, new)
    return html

def extract_main_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract content between <main...> and </main>
    match = re.search(r'(<main.*?</main>)', html, re.DOTALL)
    if not match:
        raise ValueError(f"No <main> tag found in {filepath}")
    
    main_html = match.group(1)
    return main_html

def build_index():
    main = extract_main_content('home.raw.html')
    
    # Wire hero buttons
    main = main.replace('href="#signature-tiffins"', 'href="menus.html"')
    main = main.replace('href="#visit-reserve"', 'href="javascript:void(0)" onclick="openReservationModal()"')
    
    # Wire evening menu link
    main = main.replace('href="#visit-reserve"', 'href="menus.html#section-snacks"')
    
    # Ensure home reservation form has ID and listener
    main = main.replace('action="#"', 'action="javascript:void(0)" onsubmit="handleHomeReservation(event)"')
    
    # Add page specific script for home reservation form
    page_script = """
<script>
  function handleHomeReservation(e) {
    e.preventDefault();
    const form = e.target;
    const name = form.querySelector('input[type="text"]')?.value || 'Guest';
    const phone = form.querySelector('input[type="tel"]')?.value || '';
    const bookingId = 'VR-' + Math.floor(100000 + Math.random() * 900000);
    
    showToast(`Vanakkam ${name}! Your table is confirmed! Ref #${bookingId}`, 'success', 'celebration');
    form.reset();
  }
</script>
"""
    
    main = apply_custom_replacements(main)
    
    full_html = get_head_html(
        "Vishnu Restaurant | Authentic South Indian Pure Veg Heritage • Est. 1984",
        "Experience Mayiladuthurai's beloved pure vegetarian heritage. Slow-fermented malli idlis, golden crispy ghee roast dosas, and authentic Kumbakonam degree filter coffee since 1984."
    ) + get_header_html('home') + main + page_script + get_footer_html() + get_shared_modals_html()
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Generated index.html successfully.")

def build_menus():
    main = extract_main_content('menus.raw.html')
    
    # Ensure all cards have menu-dish-card class for searching
    main = main.replace('class="menu-card ', 'class="menu-card menu-dish-card ')
    
    # Insert search input bar before category tabs
    search_bar_html = """
<div class="mb-4 max-w-xl">
  <div class="relative">
    <span class="material-symbols-outlined absolute left-3.5 top-3 text-[20px] text-tertiary">search</span>
    <input id="menuSearchInput" type="text" placeholder="Search dishes (e.g., Ghee Roast, Podi Idly, Pongal, Bonda, Filter Coffee)..." class="w-full h-11 pl-11 pr-4 rounded-xl bg-surface text-on-surface font-body-sm text-sm border border-outline-variant/50 focus:border-primary focus:ring-2 focus:ring-primary/20 focus:outline-none shadow-sm transition-all" />
  </div>
  <p id="search-result-count" class="hidden text-xs text-primary font-medium mt-2 pl-1"></p>
</div>
"""
    main = main.replace('<div class="mt-10 pt-6">', '<div class="mt-10 pt-6">' + search_bar_html)
    
    # Hook print menu button
    main = main.replace('id="downloadPdfBtn"', 'id="downloadPdfBtn" onclick="window.print()"')
    
    # Hook sticky bar checkout button
    main = main.replace('<button class="h-10 px-4 rounded-lg bg-primary hover:bg-tertiary text-on-primary font-label-lg text-label-lg transition-colors shadow-sm">\n        Checkout\n      </button>', '<button onclick="openCartDrawer()" class="h-10 px-4 rounded-lg bg-primary hover:bg-tertiary text-on-primary font-label-lg text-label-lg transition-colors shadow-sm">\n        Checkout\n      </button>')

    
    # Add page specific script for menus page
    page_script = """
<script>
  // Menus Page Specific Interactive Filter Scripts
  document.addEventListener('DOMContentLoaded', function() {
    const categoryTabs = document.querySelectorAll('.category-pill');
    const sections = {
      'tiffins': document.getElementById('section-tiffins'),
      'snacks': document.getElementById('section-snacks'),
      'drinks': document.getElementById('section-drinks')
    };

    categoryTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        categoryTabs.forEach(t => {
          t.classList.remove('bg-primary', 'text-on-primary');
          t.classList.add('bg-surface', 'text-on-surface-variant');
        });
        tab.classList.remove('bg-surface', 'text-on-surface-variant');
        tab.classList.add('bg-primary', 'text-on-primary');

        const target = tab.getAttribute('data-category');
        if (target === 'all') {
          Object.values(sections).forEach(s => s && (s.style.display = 'block'));
        } else {
          Object.entries(sections).forEach(([key, sec]) => {
            if (sec) {
              sec.style.display = (key === target) ? 'block' : 'none';
            }
          });
          if (sections[target]) {
            sections[target].scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }
      });
    });

    // Jain Filter Toggle
    const jainToggle = document.getElementById('jainToggle');
    let jainActive = false;
    if (jainToggle) {
      jainToggle.addEventListener('click', () => {
        jainActive = !jainActive;
        if (jainActive) {
          jainToggle.classList.add('bg-secondary', 'text-on-secondary');
          jainToggle.classList.remove('bg-surface', 'text-secondary');
          document.querySelectorAll('.menu-dish-card, .menu-card').forEach(card => {
            const text = card.textContent.toLowerCase();
            if (text.includes('jain') || text.includes('mallipoo') || text.includes('idly') || text.includes('coffee') || text.includes('appam')) {
              card.style.opacity = '1';
              card.style.display = '';
            } else {
              card.style.opacity = '0.25';
            }
          });
          showToast('Showing Pure Jain Friendly selections', 'success', 'eco');
        } else {
          jainToggle.classList.remove('bg-secondary', 'text-on-secondary');
          jainToggle.classList.add('bg-surface', 'text-secondary');
          document.querySelectorAll('.menu-dish-card, .menu-card').forEach(card => {
            card.style.opacity = '1';
            card.style.display = '';
          });
        }
      });
    }

    // Attach Add to Cart to all add buttons
    document.querySelectorAll('.menu-dish-card, .menu-card, div[class*="rounded-2xl"]').forEach(card => {
      const addBtn = card.querySelector('button');
      if (addBtn && (addBtn.textContent.includes('Add') || addBtn.textContent.includes('+'))) {
        const titleEl = card.querySelector('h3, h4, span[class*="font-bold"]');
        const priceEl = card.querySelector('span[class*="font-title"], span[class*="text-primary"], span[class*="font-bold"]');
        
        let title = titleEl ? titleEl.textContent.trim() : 'Tiffin Item';
        let price = 85;
        if (priceEl) {
          const match = priceEl.textContent.match(/₹\\s*(\\d+)/);
          if (match) price = parseInt(match[1], 10);
        }
        
        const imgEl = card.querySelector('img');
        const img = imgEl ? imgEl.src : null;

        addBtn.addEventListener('click', (e) => {
          e.preventDefault();
          addToCart(title, price, img);
        });
      }
    });
  });
</script>
"""

    main = apply_custom_replacements(main)

    full_html = get_head_html(
        "Traditional South Indian Pure Veg Menus | Vishnu Restaurant Mayiladuthurai",
        "Explore our authentic tiffin and snacks menu: Malli Steamed Idly, Crispy Ghee Roast Dosa, Ven Pongal, Kumbakonam Degree Filter Coffee, and Weekend Family Tiffin Boxes in Mayiladuthurai."
    ) + get_header_html('menus') + main + page_script + get_footer_html() + get_shared_modals_html()

    with open('menus.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Generated menus.html successfully.")

def build_about():
    main = extract_main_content('about.raw.html')
    
    # Remove duplicate modal in about.raw.html if present, since get_shared_modals_html handles it
    main = re.sub(r'<div[^>]*id="bookingModal".*?</div>\s*</div>\s*</div>', '', main, flags=re.DOTALL)
    
    # Hook reserve button to universal reservation modal
    main = main.replace('id="reserveTableBtn"', 'onclick="openReservationModal()"')
    
    # Clean up empty or broken links
    main = main.replace('href="#"', 'href="javascript:void(0)"')
    
    main = apply_custom_replacements(main)

    full_html = get_head_html(
        "Our Story & Heritage Since 1984 | Vishnu Restaurant Mayiladuthurai",
        "Four decades of authentic South Indian vegetarian heritage. Learn how our masters keep ancient culinary traditions alive in Mayiladuthurai, Tamilnadu."
    ) + get_header_html('about') + main + get_footer_html() + get_shared_modals_html()

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Generated about.html successfully.")

def build_contact():
    main = extract_main_content('contact.raw.html')
    
    # Replace placeholder map image with real interactive Google Maps iframe (Mayiladuthurai)
    map_iframe = """<div class="w-full h-80 relative overflow-hidden rounded-t-xl">
  <iframe 
    src="https://www.google.com/maps?q=No+27-A+Hajiyar+nagar,+4th+cross+street,+koranadu,+Mayiladuthurai,+Tamilnadu+609001&output=embed" 
    width="100%" 
    height="100%" 
    style="border:0;" 
    allowfullscreen="" 
    loading="lazy" 
    referrerpolicy="no-referrer-when-downgrade"
    title="Vishnu Restaurant Location Map - No 27-A Hajiyar nagar, Mayiladuthurai">
  </iframe>
</div>"""

    main = re.sub(r'<div class="w-full h-80 bg-cover bg-center relative"[^>]*data-location="[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>', map_iframe, main, flags=re.DOTALL)
    main = main.replace('href="https://maps.google.com"', 'href="https://www.google.com/maps/search/?api=1&query=No+27-A+Hajiyar+nagar,+4th+cross+street,+koranadu,+Mayiladuthurai,+Tamilnadu+609001"')
    main = apply_custom_replacements(main)

    
    # Page specific script for contact
    page_script = """
<script>
  function switchFormTab(tabType) {
    const btnRes = document.getElementById('tab-btn-reservation');
    const btnCat = document.getElementById('tab-btn-catering');
    const btnFeed = document.getElementById('tab-btn-feedback');
    const helper = document.getElementById('tab-helper-text');
    const submitBtn = document.getElementById('submit-btn-text');
    const guestWrapper = document.getElementById('guest-count-wrapper');
    const datetimeWrapper = document.getElementById('datetime-wrapper');

    [btnRes, btnCat, btnFeed].forEach(btn => {
      if (btn) btn.className = "flex-1 min-w-[140px] py-2.5 px-3 rounded-md font-label-lg text-label-lg text-center transition-all text-on-surface-variant hover:text-on-surface flex items-center justify-center gap-1.5";
    });

    const activeClasses = "flex-1 min-w-[140px] py-2.5 px-3 rounded-md font-label-lg text-label-lg text-center transition-all bg-primary text-on-primary shadow-sm flex items-center justify-center gap-1.5";

    if (tabType === 'reservation') {
      if (btnRes) btnRes.className = activeClasses;
      if (helper) helper.innerHTML = '<span class="material-symbols-outlined text-secondary text-[20px]">verified</span><span>Direct instant table confirmation via SMS and WhatsApp within 2 minutes.</span>';
      if (submitBtn) submitBtn.innerText = 'Reserve My Table (Instant Confirmation SMS)';
      if (guestWrapper) guestWrapper.style.display = 'block';
      if (datetimeWrapper) datetimeWrapper.style.display = 'grid';
    } else if (tabType === 'catering') {
      if (btnCat) btnCat.className = activeClasses;
      if (helper) helper.innerHTML = '<span class="material-symbols-outlined text-tertiary text-[20px]">soup_kitchen</span><span>Inquiry goes directly to our head caterer. Free menu quote sent in 15 minutes.</span>';
      if (submitBtn) submitBtn.innerText = 'Request Free Catering Quote';
      if (guestWrapper) guestWrapper.style.display = 'block';
      if (datetimeWrapper) datetimeWrapper.style.display = 'grid';
    } else if (tabType === 'feedback') {
      if (btnFeed) btnFeed.className = activeClasses;
      if (helper) helper.innerHTML = '<span class="material-symbols-outlined text-primary text-[20px]">favorite</span><span>Your feedback directly reaches our restaurant founders. We reply within 24 hours.</span>';
      if (submitBtn) submitBtn.innerText = 'Submit My Message / Feedback';
      if (guestWrapper) guestWrapper.style.display = 'none';
      if (datetimeWrapper) datetimeWrapper.style.display = 'none';
    }
  }

  function handleFormSubmit(e) {
    e.preventDefault();
    const btn = document.getElementById('form-submit-btn');
    const banner = document.getElementById('confirmation-banner');
    const form = e.target;
    const name = form.fullName?.value || 'Guest';
    
    if (btn) {
      btn.disabled = true;
      btn.classList.add('opacity-75');
      btn.innerHTML = '<span class="material-symbols-outlined animate-spin text-[20px]">progress_activity</span><span>Transmitting Details...</span>';
    }

    setTimeout(() => {
      if (btn) btn.classList.add('hidden');
      if (banner) banner.classList.remove('hidden');
      showToast(`Thank you ${name}! Request received successfully.`, 'success', 'check_circle');
    }, 800);
  }

  function toggleFaq(id) {
    const ans = document.getElementById('faq-ans-' + id);
    const icon = document.getElementById('faq-icon-' + id);
    if (!ans || !icon) return;

    if (ans.classList.contains('hidden')) {
      ans.classList.remove('hidden');
      icon.style.transform = 'rotate(180deg)';
    } else {
      ans.classList.add('hidden');
      icon.style.transform = 'rotate(0deg)';
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    const dateInput = document.getElementById('bookingDate');
    if (dateInput) {
      const today = new Date().toISOString().split('T')[0];
      dateInput.value = today;
      dateInput.min = today;
    }
  });
</script>
"""

    full_html = get_head_html(
        "Contact, Table Reservations & Catering | Vishnu Restaurant Mayiladuthurai",
        "Reserve a table, order outdoor wedding catering, or find directions to Vishnu Restaurant at No 27-A Hajiyar nagar, Mayiladuthurai, Tamilnadu 609001. Call +91 8870810456."
    ) + get_header_html('contact') + main + page_script + get_footer_html() + get_shared_modals_html()

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Generated contact.html successfully.")

if __name__ == '__main__':
    build_index()
    build_menus()
    build_about()
    build_contact()
    print("ALL PAGES COMPILED SUCCESSFULLY!")

