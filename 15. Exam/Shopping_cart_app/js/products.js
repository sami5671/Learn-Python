document.addEventListener("DOMContentLoaded", () => {
  fetch("https://fakestoreapi.com/products")
    .then((response) => response.json())
    .then((products) => {
      const productList = document.getElementById("product-list");

      products.forEach((product) => {
        const productCard = document.createElement("div");
        productCard.classList.add("col-md-4");

        productCard.innerHTML = `
            <div class="card p-3">
              <img src="${product.image}" class="card-img-top" alt="${product.title}">
              <div class="card-body">
                <h5 class="card-title">${product.title}</h5>
                <p class="card-text">${product.description}</p>
                <p class="card-text"><strong>$${product.price}</strong></p>
                <button class="btn btn-primary add-to-cart" 
                        data-id="${product.id}" 
                        data-name="${product.title}" 
                        data-price="${product.price}">
                  Add to Cart
                </button>
              </div>
            </div>
          `;

        productList.appendChild(productCard);
      });

      // Attach event listeners after rendering the product list
      document.querySelectorAll(".add-to-cart").forEach((button) => {
        button.addEventListener("click", (event) => {
          const product = {
            id: event.target.dataset.id,
            name: event.target.dataset.name,
            price: parseFloat(event.target.dataset.price),
            quantity: 1,
          };
          addToCart(product);
        });
      });
    })
    .catch((error) => console.error("Error fetching products:", error));
});
