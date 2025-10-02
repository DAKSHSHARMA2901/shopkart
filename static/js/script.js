document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.subcategory-link').forEach(function(link) {
      link.onclick = function() {
          const subcategoryId = this.dataset.subcategory;
          fetch(`/filter/${subcategoryId}/`)
          .then(response => response.text())
          .then(data => {
              document.querySelector('#filtered-products').innerHTML = data;
          });
          return false;
      };
  });
});
function sortPrice(order) {
    let productList = document.getElementById('productList');
    let items = Array.from(productList.children);
    
    items.sort(function(a, b) {
      let priceA = parseFloat(a.getAttribute('data-price'));
      let priceB = parseFloat(b.getAttribute('data-price'));
      
      if (order === 'asc') {
        return priceA - priceB;
      } else {
        return priceB - priceA;
      }
    });
    
    // Clear the existing list
    while (productList.firstChild) {
      productList.removeChild(productList.firstChild);
    }
    
    // Append sorted items to the list
    items.forEach(function(item) {
      productList.appendChild(item);
    });
  }
  