/**
 * Vishnu Restaurant - Unified Application Logic
 * Pure Vegetarian Heritage • Est. 1984
 */

(function () {
  'use strict';

  // --- CART STATE MANAGEMENT ---
  const CART_KEY = 'vishnu_restaurant_cart';


  function getCart() {
    try {
      const data = localStorage.getItem(CART_KEY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  function saveCart(cart) {
    try {
      localStorage.setItem(CART_KEY, JSON.stringify(cart));
      updateCartUI();
    } catch (e) {
      console.error('Error saving cart:', e);
    }
  }

  window.addToCart = function (itemName, price, image = null, spice = 'Authentic') {
    const cart = getCart();
    const existingIndex = cart.findIndex((item) => item.name === itemName);

    if (existingIndex > -1) {
      cart[existingIndex].quantity += 1;
    } else {
      cart.push({
        id: 'item_' + Date.now(),
        name: itemName,
        price: Number(price),
        quantity: 1,
        image: image || 'https://lh3.googleusercontent.com/aida-public/AB6AXuCl34FFsNW2Hje1jnz2E7zMXxeGn2i_p8Pob-KbQYFeRl1FoA15VA7q8qpWcQQ5-F9U91G7z_CxNy6aNI6cMS3xwUl-Na9srsoaX72BKBKUcpwfv6IIkzvuqYQFAZaylg45CR3gD2ZG58K8zCx93AVJsgtUhMUpBIBkuBZQfce9vKxk7yKjYUft-p2-6kfWfHbqwDdSLOGqk1E6-sJUKouJXG1cKYJQ2Jh2d9DHEDUO89mfqqx9v6aOYg',
        spice: spice
      });
    }

    saveCart(cart);
    showToast(`Added ${itemName} to your order!`, 'success', 'shopping_bag');
    animateCartBounce();
  };

  window.updateItemQuantity = function (index, delta) {
    const cart = getCart();
    if (cart[index]) {
      cart[index].quantity += delta;
      if (cart[index].quantity <= 0) {
        cart.splice(index, 1);
      }
      saveCart(cart);
    }
  };

  window.removeItemFromCart = function (index) {
    const cart = getCart();
    if (cart[index]) {
      const name = cart[index].name;
      cart.splice(index, 1);
      saveCart(cart);
      showToast(`Removed ${name}`, 'warning', 'delete');
    }
  };

  window.clearAllCart = function () {
    saveCart([]);
    showToast('Your order basket has been cleared', 'warning', 'remove_shopping_cart');
  };

  function animateCartBounce() {
    const badges = document.querySelectorAll('.cart-badge-counter');
    badges.forEach((b) => {
      b.classList.add('cart-bounce');
      setTimeout(() => b.classList.remove('cart-bounce'), 400);
    });
  }

  function updateCartUI() {
    const cart = getCart();
    const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

    // Update Badges & Counters across all pages
    const badgeElements = document.querySelectorAll('.cart-badge-counter');
    badgeElements.forEach((el) => {
      el.textContent = totalCount;
      if (totalCount > 0) {
        el.classList.remove('hidden');
      } else {
        el.classList.add('hidden');
      }
    });

    const totalElements = document.querySelectorAll('.cart-total-text');
    totalElements.forEach((el) => {
      el.textContent = `₹${subtotal}`;
    });

    // Update Sticky Order Bar if present on Menus page
    const stickyBar = document.getElementById('stickyOrderBar');
    const itemCountLabel = document.getElementById('itemCountLabel');
    const itemSubtotalLabel = document.getElementById('itemSubtotalLabel');

    if (stickyBar && itemCountLabel && itemSubtotalLabel) {
      if (totalCount > 0) {
        stickyBar.classList.remove('translate-y-24', 'opacity-0', 'pointer-events-none');
        stickyBar.classList.add('translate-y-0', 'opacity-100', 'pointer-events-auto');
        itemCountLabel.innerText = `${totalCount} ${totalCount === 1 ? 'Item' : 'Items'} Added`;
        itemSubtotalLabel.innerText = `Subtotal: ₹${subtotal}`;
      } else {
        stickyBar.classList.add('translate-y-24', 'opacity-0', 'pointer-events-none');
        stickyBar.classList.remove('translate-y-0', 'opacity-100', 'pointer-events-auto');
      }
    }

    renderCartDrawer(cart, subtotal);
  }

  function renderCartDrawer(cart, subtotal) {
    const drawerList = document.getElementById('cart-items-list');
    const emptyState = document.getElementById('cart-empty-state');
    const cartFooter = document.getElementById('cart-footer-summary');

    if (!drawerList) return;

    if (cart.length === 0) {
      drawerList.innerHTML = '';
      if (emptyState) emptyState.classList.remove('hidden');
      if (cartFooter) cartFooter.classList.add('hidden');
      return;
    }

    if (emptyState) emptyState.classList.add('hidden');
    if (cartFooter) cartFooter.classList.remove('hidden');

    const gst = Math.round(subtotal * 0.05);
    const packing = subtotal > 0 ? 15 : 0;
    const finalTotal = subtotal + gst + packing;

    // Render items
    drawerList.innerHTML = cart.map((item, index) => `
      <div class="flex items-center justify-between p-3.5 bg-surface rounded-xl border border-outline-variant/30 shadow-sm gap-3">
        <img src="${item.image}" alt="${item.name}" class="w-14 h-14 rounded-lg object-cover shrink-0" />
        <div class="flex-1 min-w-0">
          <h4 class="font-title-md text-sm text-on-surface truncate font-semibold">${item.name}</h4>
          <p class="font-body-sm text-xs text-on-surface-variant">₹${item.price} each</p>
          <div class="flex items-center gap-2 mt-1">
            <span class="text-xs px-2 py-0.5 rounded-full bg-surface-container text-primary font-medium">₹${item.price * item.quantity}</span>
          </div>
        </div>
        <div class="flex items-center gap-1.5 shrink-0 bg-surface-container rounded-lg p-1">
          <button onclick="window.updateItemQuantity(${index}, -1)" class="w-7 h-7 flex items-center justify-center rounded bg-surface hover:bg-surface-container-high text-on-surface transition-colors font-bold text-sm" aria-label="Decrease quantity">
            <span class="material-symbols-outlined text-[16px]">remove</span>
          </button>
          <span class="w-6 text-center font-label-lg text-sm font-semibold">${item.quantity}</span>
          <button onclick="window.updateItemQuantity(${index}, 1)" class="w-7 h-7 flex items-center justify-center rounded bg-primary hover:bg-tertiary text-on-primary transition-colors font-bold text-sm" aria-label="Increase quantity">
            <span class="material-symbols-outlined text-[16px]">add</span>
          </button>
        </div>
        <button onclick="window.removeItemFromCart(${index})" class="text-outline hover:text-error transition-colors p-1" title="Remove item">
          <span class="material-symbols-outlined text-[18px]">close</span>
        </button>
      </div>
    `).join('');

    // Update numbers in summary
    const subtotalEl = document.getElementById('drawer-subtotal');
    const gstEl = document.getElementById('drawer-gst');
    const packingEl = document.getElementById('drawer-packing');
    const finalTotalEl = document.getElementById('drawer-final-total');

    if (subtotalEl) subtotalEl.textContent = `₹${subtotal}`;
    if (gstEl) gstEl.textContent = `₹${gst}`;
    if (packingEl) packingEl.textContent = `₹${packing}`;
    if (finalTotalEl) finalTotalEl.textContent = `₹${finalTotal}`;
  }

  // --- DRAWER & MODAL CONTROLLERS ---
  window.openCartDrawer = function () {
    const backdrop = document.getElementById('cart-drawer-backdrop');
    const panel = document.getElementById('cart-drawer-panel');
    if (backdrop && panel) {
      backdrop.classList.add('active');
      panel.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeCartDrawer = function () {
    const backdrop = document.getElementById('cart-drawer-backdrop');
    const panel = document.getElementById('cart-drawer-panel');
    if (backdrop && panel) {
      backdrop.classList.remove('active');
      panel.classList.remove('active');
      document.body.style.overflow = '';
    }
  };

  window.openMobileNav = function () {
    const backdrop = document.getElementById('mobile-nav-backdrop');
    const panel = document.getElementById('mobile-nav-panel');
    if (backdrop && panel) {
      backdrop.classList.add('active');
      panel.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeMobileNav = function () {
    const backdrop = document.getElementById('mobile-nav-backdrop');
    const panel = document.getElementById('mobile-nav-panel');
    if (backdrop && panel) {
      backdrop.classList.remove('active');
      panel.classList.remove('active');
      document.body.style.overflow = '';
    }
  };

  // --- UNIVERSAL TABLE RESERVATION MODAL ---
  window.openReservationModal = function (prefType = 'general') {
    const modalBackdrop = document.getElementById('reservation-modal-backdrop');
    if (modalBackdrop) {
      modalBackdrop.classList.add('active');
      document.body.style.overflow = 'hidden';

      // Set min date to today
      const dateInput = document.getElementById('res-modal-date');
      if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.value = today;
        dateInput.min = today;
      }
    }
  };

  window.closeReservationModal = function () {
    const modalBackdrop = document.getElementById('reservation-modal-backdrop');
    if (modalBackdrop) {
      modalBackdrop.classList.remove('active');
      document.body.style.overflow = '';
    }
  };

  window.handleModalReservationSubmit = function (e) {
    e.preventDefault();
    const form = e.target;
    const name = form.resName?.value || 'Guest';
    const phone = form.resPhone?.value || '';
    const date = form.resDate?.value || '';
    const time = form.resTime?.value || '';
    const guests = form.resGuests?.value || '2';
    const notes = form.resNotes?.value || 'None';

    const bookingId = 'VR-' + Math.floor(100000 + Math.random() * 900000);

    const confirmationDetails = document.getElementById('res-success-details');
    if (confirmationDetails) {
      confirmationDetails.innerHTML = `
        <div class="bg-surface p-4 rounded-xl border border-secondary/30 space-y-2 text-left">
          <div class="flex items-center justify-between border-b border-outline-variant/30 pb-2">
            <span class="font-label-heritage uppercase tracking-wider text-xs text-secondary font-bold">Booking Confirmed</span>
            <span class="font-title-md text-primary font-bold">#${bookingId}</span>
          </div>
          <p class="text-sm"><strong>Guest Name:</strong> ${name}</p>
          <p class="text-sm"><strong>Party Size:</strong> ${guests} Guests</p>
          <p class="text-sm"><strong>Date & Slot:</strong> ${date} at ${time}</p>
          <p class="text-xs text-on-surface-variant pt-1 border-t border-outline-variant/20">An SMS confirmation voucher has been dispatched to <strong>${phone}</strong>.</p>
        </div>
      `;
    }

    const formView = document.getElementById('res-modal-form-view');
    const successView = document.getElementById('res-modal-success-view');
    if (formView && successView) {
      formView.classList.add('hidden');
      successView.classList.remove('hidden');
    }

    showToast(`Table booked for ${name}! Ref: #${bookingId}`, 'success', 'celebration');
  };

  window.resetReservationModal = function () {
    const formView = document.getElementById('res-modal-form-view');
    const successView = document.getElementById('res-modal-success-view');
    const form = document.getElementById('reservation-modal-form');
    if (formView && successView) {
      formView.classList.remove('hidden');
      successView.classList.add('hidden');
    }
    if (form) form.reset();
    closeReservationModal();
  };

  // --- ORDER VIA WHATSAPP ---
  window.orderViaWhatsApp = function () {
    const cart = getCart();
    if (cart.length === 0) {
      showToast('Your order basket is empty!', 'warning', 'info');
      return;
    }

    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const gst = Math.round(subtotal * 0.05);
    const packing = 15;
    const finalTotal = subtotal + gst + packing;

    const orderType = document.querySelector('input[name="orderType"]:checked')?.value || 'Self Pickup';
    const notes = document.getElementById('cart-special-notes')?.value || 'None';

    let message = `*Namaskaram Vishnu Restaurant!*\n`;
    message += `I would like to place an order from your website.\n\n`;
    message += `*Order Type:* ${orderType}\n`;
    message += `*Items:*\n`;

    cart.forEach((item, i) => {
      message += `${i + 1}. ${item.name} x ${item.quantity} = ₹${item.price * item.quantity}\n`;
    });

    message += `\n*Subtotal:* ₹${subtotal}`;
    message += `\n*GST (5%):* ₹${gst}`;
    message += `\n*Packing:* ₹${packing}`;
    message += `\n*Total Payable:* ₹${finalTotal}\n`;
    if (notes && notes !== 'None') {
      message += `\n*Special Instructions:* ${notes}\n`;
    }
    message += `\nPlease confirm preparation time. Thank you!`;

    const encoded = encodeURIComponent(message);
    const waUrl = `https://wa.me/918870810456?text=${encoded}`;
    window.open(waUrl, '_blank');
  };


  // --- SIMULATED INSTANT CHECKOUT ---
  window.simulateInstantCheckout = function () {
    const cart = getCart();
    if (cart.length === 0) {
      showToast('Please add items to your cart first!', 'warning', 'info');
      return;
    }

    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const orderId = 'VR-ORD-' + Math.floor(10000 + Math.random() * 90000);

    closeCartDrawer();

    const checkoutModal = document.getElementById('checkout-success-modal');
    const orderIdEl = document.getElementById('checkout-order-id');
    const orderItemsSummary = document.getElementById('checkout-items-summary');

    if (orderIdEl) orderIdEl.textContent = orderId;
    if (orderItemsSummary) {
      orderItemsSummary.innerHTML = `
        <div class="space-y-1 text-sm text-on-surface-variant">
          <p><strong>Total Items:</strong> ${cart.reduce((s, it) => s + it.quantity, 0)} items</p>
          <p><strong>Total Paid:</strong> ₹${subtotal + Math.round(subtotal * 0.05) + 15}</p>
          <p><strong>Estimated Prep Time:</strong> 15-20 Minutes</p>
          <p class="text-xs text-secondary font-medium pt-1">Kitchen has received your order slip!</p>
        </div>
      `;
    }

    if (checkoutModal) {
      checkoutModal.classList.add('active');
    }

    // Clear cart after checkout
    saveCart([]);
    showToast(`Order #${orderId} Placed Successfully!`, 'success', 'check_circle');
  };

  window.closeCheckoutModal = function () {
    const checkoutModal = document.getElementById('checkout-success-modal');
    if (checkoutModal) checkoutModal.classList.remove('active');
  };

  // --- TOAST NOTIFICATIONS ---
  window.showToast = function (message, type = 'info', icon = 'info') {
    let container = document.getElementById('toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;

    let iconColor = 'text-primary';
    if (type === 'success') iconColor = 'text-secondary';
    if (type === 'warning') iconColor = 'text-tertiary';

    toast.innerHTML = `
      <span class="material-symbols-outlined ${iconColor} text-[22px] shrink-0">${icon}</span>
      <div class="flex-1 font-body-sm text-sm font-medium leading-snug">${message}</div>
      <button class="text-outline hover:text-on-surface" onclick="this.parentElement.remove()">
        <span class="material-symbols-outlined text-[16px]">close</span>
      </button>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.animation = 'toast-out 0.3s forwards';
      setTimeout(() => toast.remove(), 300);
    }, 3800);
  };

  // --- DOM READY INITIALIZATION ---
  document.addEventListener('DOMContentLoaded', function () {
    updateCartUI();

    // Sticky header shadow on scroll
    const header = document.querySelector('header');
    if (header) {
      window.addEventListener('scroll', () => {
        if (window.scrollY > 30) {
          header.classList.add('header-scrolled');
        } else {
          header.classList.remove('header-scrolled');
        }
      });
    }

    // Attach click listeners to all "Book a Table" buttons across page
    document.querySelectorAll('button, a').forEach((el) => {
      const text = el.textContent.trim().toLowerCase();
      if (text === 'book a table' || text === 'find our table / order' || text === 'reserve table' || text === 'reserve a table') {
        el.addEventListener('click', (e) => {
          if (!el.getAttribute('href')?.startsWith('#')) {
            e.preventDefault();
            openReservationModal();
          }
        });
      }
      if (text === 'order online') {
        el.addEventListener('click', (e) => {
          e.preventDefault();
          openCartDrawer();
        });
      }
    });

    // Menus Search & Filter logic (if on menus page)
    const menuSearchInput = document.getElementById('menuSearchInput');
    if (menuSearchInput) {
      menuSearchInput.addEventListener('input', function (e) {
        const query = e.target.value.toLowerCase().trim();
        const cards = document.querySelectorAll('.menu-dish-card, .menu-card');
        let matchCount = 0;

        cards.forEach((card) => {
          const text = card.textContent.toLowerCase();
          if (!query || text.includes(query)) {
            card.style.display = '';
            matchCount++;
          } else {
            card.style.display = 'none';
          }
        });

        const countFeedback = document.getElementById('search-result-count');
        if (countFeedback) {
          if (query) {
            countFeedback.textContent = `Found ${matchCount} dishes matching "${query}"`;
            countFeedback.classList.remove('hidden');
          } else {
            countFeedback.classList.add('hidden');
          }
        }
      });
    }

  });

})();
