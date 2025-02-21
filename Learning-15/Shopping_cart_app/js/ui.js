document.addEventListener("DOMContentLoaded", () => {
  renderCart();
  document.getElementById("clear-cart").addEventListener("click", clearCart);
});

function renderCart() {
  const cartItemsList = document.getElementById("cart-items");
  const cartCount = document.getElementById("cart-count");
  const cartTotal = document.getElementById("cart-total");

  cartItemsList.innerHTML = "";
  let total = 0;

  cart.forEach((item) => {
    total += item.price * item.quantity;

    const listItem = document.createElement("li");
    listItem.classList.add("list-group-item");
    listItem.innerHTML = `
            ${item.name} - $${item.price} x 
            <input type="number" value="${item.quantity}" min="1" data-id="${item.id}" class="cart-qty">
            <button class="btn btn-danger btn-sm remove-item" data-id="${item.id}">Remove</button>
        `;

    cartItemsList.appendChild(listItem);
  });

  cartCount.textContent = cart.length;
  cartTotal.textContent = total.toFixed(2);

  document.querySelectorAll(".cart-qty").forEach((input) => {
    input.addEventListener("change", (event) => {
      updateQuantity(event.target.dataset.id, parseInt(event.target.value));
    });
  });

  document.querySelectorAll(".remove-item").forEach((button) => {
    button.addEventListener("click", (event) => {
      removeFromCart(event.target.dataset.id);
    });
  });
}
