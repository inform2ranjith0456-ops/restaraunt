// Structured Menu Catalog for Vishnu Restaurant (Est. 1984)
const MENU_DATA = [
  // MORNING & ALL-DAY TIFFINS
  {
    id: "tiffin-1",
    name: "Malli Steamed Idly (4 Pcs)",
    category: "tiffins",
    price: 85,
    spice: "Mild",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Cotton-soft, feather-light steamed cakes fermented overnight. Served with coconut, coriander, and tomato relish with drumstick sambar.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuCl34FFsNW2Hje1jnz2E7zMXxeGn2i_p8Pob-KbQYFeRl1FoA15VA7q8qpWcQQ5-F9U91G7z_CxNy6aNI6cMS3xwUl-Na9srsoaX72BKBKUcpwfv6IIkzvuqYQFAZaylg45CR3gD2ZG58K8zCx93AVJsgtUhMUpBIBkuBZQfce9vKxk7yKjYUft-p2-6kfWfHbqwDdSLOGqk1E6-sJUKouJXG1cKYJQ2Jh2d9DHEDUO89mfqqx9v6aOYg"
  },
  {
    id: "tiffin-2",
    name: "Crispy Ghee Roast Dosa",
    category: "tiffins",
    price: 140,
    spice: "Med",
    isVeg: true,
    isJain: false,
    bestseller: true,
    desc: "Crisped to perfection over seasoned cast iron with pure A2 farm cow ghee. Accompanied by spiced potato masala and three fresh chutneys.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuBayzyNyu2tXh3gO85RpT4zhGGtoTB-tHjPDtY0TeVrVHfVCMimed1tmOvf5cnVve5t_ZCiEsnV50WUSVdOclENIjO8SDvegJOBe0Ng1n2NzC-AB-eLNfT_gD0wP_V5Y6JubAhe-tHWTWOT98NJem7FBfVwM8uuwXVOqDvL4AUE9Pdxbs-U6kdKlyqYaiNPGSASJFrw8t9Nh9Qc3uMRB8VJAFbXN7KjznFLgPOV_BWkpp84ZaXoUiloAw"
  },
  {
    id: "tiffin-3",
    name: "Melts-in-Mouth Ven Pongal",
    category: "tiffins",
    price: 110,
    spice: "Mild",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Slow-cooked raw rice and moong dal infused with whole Tellicherry peppercorns, cumin, fresh ginger, and generous roasted cashews in pure ghee. Includes 1 Medu Vada.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuDjeuJf47Uu04W_mpVWjSth_55W765oHVPiFG3HaxK3SCIMKaxt1oFMOnznp66wULoPz8PRFd16QFlFY3-kuRZjrWq5onIWhC_eh4JT_179-JyCH6dW2lmJTHabj9Jeaw9-Xlk1QuSNSM3V-s4yjPzt6shgTrw0yJY8XkyO0sv3oYGl2LnphpPDs59iKH9DDUPY7Dkc_4lGgVq5A3myDmeXtBRMqwWzeolYwjvpAvX5_lJdq_MQaoA1Wg"
  },
  {
    id: "tiffin-4",
    name: "Puffed Golden Poori (2 Pcs)",
    category: "tiffins",
    price: 95,
    spice: "Mild",
    isVeg: true,
    isJain: false,
    bestseller: false,
    desc: "Delicate, ballooned golden pooris paired with our classic spiced turmeric potato mash, tempered with mustard seeds and curry leaves.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAl2bb8iT236aVmgk68gkVMo2-71cOxa5vF4xYceddz249MA4eGYHpqC5HnrPpgVVQltjfZ-5JP2Xqx9o3gMvT4F8GpcubjkuKyUBuMMj1XT5AwEk3DIjOcBFFfe0w93b6oIQ0t6t7W4OJcuR164y8E-eKBbIHc173-sCf_347Us5x1rhKn7Ma7B6A9f3la4MtHQWpqomwVnFqxOjTcKUcI8InWS0UHPt1IES6PYdcT7WBnKBdz1Bxw2w"
  },
  {
    id: "tiffin-5",
    name: "Lace Appam & Sweet Coconut Milk",
    category: "tiffins",
    price: 120,
    spice: "Sweet",
    isVeg: true,
    isJain: true,
    bestseller: false,
    desc: "Delicate, soft-spongy center with golden crispy filigree lacy rims. Served with freshly squeezed cardamom-infused coconut milk. Gluten-free.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAYrXR152HCAdDqrJWTxkt7cqw42ATtzszbOf5ucDcPTtVQ2G4ZWPB8fAPSsHVlIyXtHXpfnPe3zZosXr3grGsopLwMW5dBO8yevxDfKDdQaJzHxeLFefx-ZAHEcq2axPnpocaF4a5Ez72Q-ae4Wzw846fRHgmVb7_p8KGoNTGDArJRC-bmSxAAo_tTm_NqYWhurrJpf_5skIqs_GZ_Xb5vLpcupfAJkOwEHo-IdpUNc67pzA433Ak3IA"
  },
  {
    id: "tiffin-6",
    name: "Ghee Podi Thattu Idly",
    category: "tiffins",
    price: 105,
    spice: "Spicy",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Large circular steamed tiffin drenched in steaming hot cow ghee and dusted with our hand-pounded 14-spice gun powder podi.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAu1iG03B6YljbbHhIQQzfTyvWX-FNcJ7YzWrIGvmyH-RAtrF3LNBXofRC8XTPBHm20BRMyq0g_EW9x0VviVvIUAQeiMcYRGc2db-ABO25JAncWbHxyWXSDr420zbkMPP4KdhUQQnKbjXCyKWPtH2dZesPFOlXLt76uXFg9aCvABLPcuKJYfeyvsR8EUIGTta8x0UW_7CQplOwL0Bk3bsJcSfzBuZgIFQExnMFdCN70S_HK8dkcYnyhrQ"
  },
  {
    id: "tiffin-7",
    name: "Mini Sambar Idly (14 Pcs)",
    category: "tiffins",
    price: 110,
    spice: "Med",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Fourteen bite-sized button idlis submerged in piping hot shallot drumstick sambar, topped with golden ghee and fresh cilantro.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuCHOTWlptBHCGiUapfgEo2eXiZO6x_7439QWk7E5m0Z8V_uV466922sNfU29c54gX8N3sC3214"
  },
  {
    id: "tiffin-8",
    name: "Onion Rava Dosa",
    category: "tiffins",
    price: 115,
    spice: "Med",
    isVeg: true,
    isJain: false,
    bestseller: false,
    desc: "Ultra-crispy semolina crepe studded with crushed black pepper, green chilies, cumin, and caramelized shallots.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuBayzyNyu2tXh3gO85RpT4zhGGtoTB-tHjPDtY0TeVrVHfVCMimed1tmOvf5cnVve5t_ZCiEsnV50WUSVdOclENIjO8SDvegJOBe0Ng1n2NzC-AB-eLNfT_gD0wP_V5Y6JubAhe-tHWTWOT98NJem7FBfVwM8uuwXVOqDvL4AUE9Pdxbs-U6kdKlyqYaiNPGSASJFrw8t9Nh9Qc3uMRB8VJAFbXN7KjznFLgPOV_BWkpp84ZaXoUiloAw"
  },

  // CRISPY EVENING SNACKS (3:30 PM - 7:30 PM)
  {
    id: "snack-1",
    name: "Golden Mysore Bonda (4 Pcs)",
    category: "snacks",
    price: 75,
    spice: "Mild",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Crisp golden outer shell with airy, melt-in-mouth centers tempered with whole black peppercorns, crushed ginger, and curry leaves. Served with shallot coconut chutney.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuBo6xIWLgzcTJmI4UL3CGczgRJloTK-u9H8V2M4Z1Q"
  },
  {
    id: "snack-2",
    name: "Vazhaikkai (Raw Banana) Bajji",
    category: "snacks",
    price: 70,
    spice: "Med",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Thinly sliced raw country plantain batter-fried to golden crispness in wood-pressed groundnut oil. Accompanied by spicy mint coriander relish.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuD_JGb8i4iC_L8ROllPdzmpfM3qqQVr_1SXPt0dOrlg8kraw0cAmOySlp5COEaw7mqpE3EDdeE7aX7quD2Qh54ocLRSIyhS6aXc1PbnTuy_-I1qT6S_nW0c_rxPI2iPuS8IFk0BI3XLY6soBsygOXbMNXkFDX83bDR4lmPEgVUo9Y1rUdD1Xv2r-N9egC68HmYVpg6BcEZsWG3pBiQqDuWYXnrEGumsR8lk9tifChk7-aCiiG3rfrR0Vw"
  },
  {
    id: "snack-3",
    name: "Milagai (Chilli) Bajji Special",
    category: "snacks",
    price: 75,
    spice: "Spicy",
    isVeg: true,
    isJain: false,
    bestseller: false,
    desc: "Fresh, mild Bhavnagri long green chillies filled with tangy roasted cumin-tamarind masala, dipped in gram flour batter and fried until crunchy.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuD_JGb8i4iC_L8ROllPdzmpfM3qqQVr_1SXPt0dOrlg8kraw0cAmOySlp5COEaw7mqpE3EDdeE7aX7quD2Qh54ocLRSIyhS6aXc1PbnTuy_-I1qT6S_nW0c_rxPI2iPuS8IFk0BI3XLY6soBsygOXbMNXkFDX83bDR4lmPEgVUo9Y1rUdD1Xv2r-N9egC68HmYVpg6BcEZsWG3pBiQqDuWYXnrEGumsR8lk9tifChk7-aCiiG3rfrR0Vw"
  },
  {
    id: "snack-4",
    name: "Crunchy Medu Vada (2 Pcs)",
    category: "snacks",
    price: 65,
    spice: "Mild",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Fluffy urad dal fritters with crackling golden crusts, aromatic curry leaves, and black pepper. Perfect with our heirloom hot sambar.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuCl34FFsNW2Hje1jnz2E7zMXxeGn2i_p8Pob-KbQYFeRl1FoA15VA7q8qpWcQQ5-F9U91G7z_CxNy6aNI6cMS3xwUl-Na9srsoaX72BKBKUcpwfv6IIkzvuqYQFAZaylg45CR3gD2ZG58K8zCx93AVJsgtUhMUpBIBkuBZQfce9vKxk7yKjYUft-p2-6kfWfHbqwDdSLOGqk1E6-sJUKouJXG1cKYJQ2Jh2d9DHEDUO89mfqqx9v6aOYg"
  },

  // HOT DRINKS & DEGREE FILTER COFFEE
  {
    id: "drink-1",
    name: "Kumbakonam Degree Filter Coffee",
    category: "drinks",
    price: 45,
    spice: "Classic",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Brewed through authentic South Indian brass drip filters using freshly ground Chikmagalur plantation beans with 15% chicory. Poured piping hot in brass tumbler & davarah.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuD_JGb8i4iC_L8ROllPdzmpfM3qqQVr_1SXPt0dOrlg8kraw0cAmOySlp5COEaw7mqpE3EDdeE7aX7quD2Qh54ocLRSIyhS6aXc1PbnTuy_-I1qT6S_nW0c_rxPI2iPuS8IFk0BI3XLY6soBsygOXbMNXkFDX83bDR4lmPEgVUo9Y1rUdD1Xv2r-N9egC68HmYVpg6BcEZsWG3pBiQqDuWYXnrEGumsR8lk9tifChk7-aCiiG3rfrR0Vw"
  },
  {
    id: "drink-2",
    name: "Karupatti (Palm Jaggery) Coffee",
    category: "drinks",
    price: 55,
    spice: "Organic",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Decoction naturally sweetened with unrefined single-estate Tirunelveli palm jaggery. Rich in minerals with a distinctive earthy aroma.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuD_JGb8i4iC_L8ROllPdzmpfM3qqQVr_1SXPt0dOrlg8kraw0cAmOySlp5COEaw7mqpE3EDdeE7aX7quD2Qh54ocLRSIyhS6aXc1PbnTuy_-I1qT6S_nW0c_rxPI2iPuS8IFk0BI3XLY6soBsygOXbMNXkFDX83bDR4lmPEgVUo9Y1rUdD1Xv2r-N9egC68HmYVpg6BcEZsWG3pBiQqDuWYXnrEGumsR8lk9tifChk7-aCiiG3rfrR0Vw"
  },
  {
    id: "drink-3",
    name: "Sukku Malli Herbal Coffee",
    category: "drinks",
    price: 50,
    spice: "Herbal",
    isVeg: true,
    isJain: true,
    bestseller: false,
    desc: "Caffeine-free Ayurvedic decoction of dry ginger (sukku), coriander seeds (malli), cardamom, and black pepper simmered with country jaggery.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuD_JGb8i4iC_L8ROllPdzmpfM3qqQVr_1SXPt0dOrlg8kraw0cAmOySlp5COEaw7mqpE3EDdeE7aX7quD2Qh54ocLRSIyhS6aXc1PbnTuy_-I1qT6S_nW0c_rxPI2iPuS8IFk0BI3XLY6soBsygOXbMNXkFDX83bDR4lmPEgVUo9Y1rUdD1Xv2r-N9egC68HmYVpg6BcEZsWG3pBiQqDuWYXnrEGumsR8lk9tifChk7-aCiiG3rfrR0Vw"
  },
  {
    id: "drink-4",
    name: "Saffron Badam Milk (Cold / Hot)",
    category: "drinks",
    price: 70,
    spice: "Sweet",
    isVeg: true,
    isJain: true,
    bestseller: false,
    desc: "Stone-ground almond paste simmered with full-cream farm milk, infused with Kashmiri saffron strands and crushed green cardamom.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuD_JGb8i4iC_L8ROllPdzmpfM3qqQVr_1SXPt0dOrlg8kraw0cAmOySlp5COEaw7mqpE3EDdeE7aX7quD2Qh54ocLRSIyhS6aXc1PbnTuy_-I1qT6S_nW0c_rxPI2iPuS8IFk0BI3XLY6soBsygOXbMNXkFDX83bDR4lmPEgVUo9Y1rUdD1Xv2r-N9egC68HmYVpg6BcEZsWG3pBiQqDuWYXnrEGumsR8lk9tifChk7-aCiiG3rfrR0Vw"
  },

  // WEEKEND COMBOS & TIFFIN PACKS
  {
    id: "combo-1",
    name: "Weekend Tiffin Box (Feeds 2)",
    category: "combos",
    price: 299,
    spice: "Varied",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "Complete South Indian breakfast: 4 Steamed Idlis, 2 Medu Vadas, 1 Masala Dosa, 1 portion of Ven Pongal, Kesari sweet, 3 Chutneys, Sambar & 2 Brass Flask Filter Coffees.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAyH4rnenavu3M09LifFBhx_Sakj8yOGTNwTJ8KKruQViBDlVVuQloGMR9ygVHWi1_h3rM6CnqpXw8PMHjjFM0ux1fsTCQ-eepY4SDR97HZm8D2jLOm7wInUp-CwxNMGwNpprkujV65EhTu5p5cdg71aOByC-oGNjzXi8IdhNtxLi9lT1JrH5KN94TE_LiwsKO4c2hNgzHhuXQX2UuVubZLS7GTgj3l8QAlHBaDHdLVstzTOqvG9v8iQw"
  },
  {
    id: "combo-2",
    name: "Grand Festival Banana Leaf Thali",
    category: "combos",
    price: 349,
    spice: "Traditional",
    isVeg: true,
    isJain: true,
    bestseller: true,
    desc: "22-item royal vegetarian feast served on pure banana leaf: Ponni rice, Drumstick sambar, Milagu rasam, Mor kuzhambu, Avial, Poriyal, Kootu, Appalam, Vada, Payasam & Curd.",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAyH4rnenavu3M09LifFBhx_Sakj8yOGTNwTJ8KKruQViBDlVVuQloGMR9ygVHWi1_h3rM6CnqpXw8PMHjjFM0ux1fsTCQ-eepY4SDR97HZm8D2jLOm7wInUp-CwxNMGwNpprkujV65EhTu5p5cdg71aOByC-oGNjzXi8IdhNtxLi9lT1JrH5KN94TE_LiwsKO4c2hNgzHhuXQX2UuVubZLS7GTgj3l8QAlHBaDHdLVstzTOqvG9v8iQw"
  }
];
