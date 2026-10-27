# Welcome Restaurant - Pure Vegetarian Heritage (Est. 1984)

> Authentic South Indian Hospitality, slow-stone ground batters, pure A2 desi cow ghee, and frothy Kumbakonam degree filter coffee near Kapaleeshwarar Temple, Mylapore, Chennai.

Converted into a complete, interactive, multi-page website from Google Stitch project ID `17662367842895345093`.

---

## 🌟 Pages & Architecture

1. **[Home (`index.html`)](file:///c:/Users/infor/OneDrive/Desktop/restaraunt%20project%20self/index.html)**
   - Top announcement banner with quick call, operating hours, and pure veg certification.
   - Immersive hero section with trust badges and signature specialty showcase.
   - Three signature pillars: Morning Hot Tiffins, Evening Snacks, and Degree Filter Coffee.
   - Today's Signature Tiffins preview grid with interactive "Add to Order" buttons.
   - Chennai Tea-Time ritual spotlight (Mysore Bonda, Vazhaikkai Bajji, Frothy Filter Coffee).
   - The Welcome Restaurant Promise (Ayurvedic kitchen standards).
   - Customer testimonials and instant table reservation form.

2. **[Menus (`menus.html`)](file:///c:/Users/infor/OneDrive/Desktop/restaraunt%20project%20self/menus.html)**
   - Live interactive search bar filtering 22+ authentic dishes in real-time.
   - Category filtering pills: All Dishes, Morning Tiffins, Crispy Snacks, Hot Drinks, Weekend Combos.
   - 100% Pure Jain Friendly toggle highlighting sattvic preparations.
   - Weekend Tiffin Box & Grand Festival Banana Leaf Thali combo packages.
   - Sticky order bar with live count, subtotal, and direct checkout drawer trigger.
   - Print-ready Menu PDF export trigger.

3. **[Our Story (`about.html`)](file:///c:/Users/infor/OneDrive/Desktop/restaraunt%20project%20self/about.html)**
   - Four decades of pure vegetarian lineage since 1984.
   - Four kitchen pillars: Stone grinding, pure cow ghee, single-origin spices, zero cross-contamination.
   - The Pure Vegetarian & Sattvic Manifesto.
   - Master Craftsmen spotlights (Master Chef Ramanathan and Coffee Master Senthil).
   - Interactive historical timeline spanning 1984 to 2026.

4. **[Contact & Reservations (`contact.html`)](file:///c:/Users/infor/OneDrive/Desktop/restaraunt%20project%20self/contact.html)**
   - Multi-tab booking and inquiry form: Table Reservation, Outdoor Catering, Feedback & Queries.
   - Interactive Google Maps embed with GPS coordinates and one-click navigation to Kapaleeshwarar Temple West Gate, Mylapore.
   - Peak hours traffic guide and operating schedule.
   - Interactive FAQ accordion.

---

## ⚡ Global Interactive Features

- **Universal Slide-Out Cart Drawer (`localStorage` synchronized)**:
  - Add items from any page with real-time badge updates.
  - Quantity controls (`-` / `+`), item subtotal, item removal.
  - Order type selector: Dine-in Pre-order, Self Pickup (20 min), Express Delivery.
  - Bill breakdown with 5% GST and eco-friendly packing charges.
  - **Send Order via WhatsApp**: Formats items, quantities, and totals into an instant WhatsApp message to `+91 44 2434 5678`.
  - **Simulate Instant Order**: Generates an animated confirmation receipt with unique Order ID and estimated prep countdown.
- **Universal Table Reservation Modal**:
  - Callable from any "Book a Table" or "Reserve" button on every page.
  - Pre-fills today's date, dining time slots, guest count (1-10+), and seating preferences.
  - Live confirmation modal with booking reference number and SMS notification alert.
- **Mobile First Navigation**:
  - Slide-out mobile drawer with logo, quick links, and restaurant timings.
  - Bottom touch dock for one-handed mobile ordering and reservation checks.

---

## 🚀 Running Locally

The local HTTP server is running at:
```bash
http://localhost:3000
```

To run manually at any time:
```bash
python -m http.server 3000
```
or
```bash
npx serve .
```
