let cart = JSON.parse(localStorage.getItem("cart")) || [];

function addToCart(product) {
  const existingItem = cart.find((item) => item.id === product.id);
  if (existingItem) {
    existingItem.quantity++;
  } else {
    cart.push(product);
  }
  updateCart();
}

function updateQuantity(productId, quantity) {
  const item = cart.find((item) => item.id == productId);
  if (item) {
    item.quantity = Math.max(1, quantity);
  }
  updateCart();
}

function removeFromCart(productId) {
  cart = cart.filter((item) => item.id != productId);
  updateCart();
}

function clearCart() {
  cart = [];
  updateCart();
}

function updateCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
  renderCart();
}
