
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("hero-image");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 10000); // Change image every 5 seconds
}

function openNav() {
 document.getElementById("side-nav").style.width = "250px";
}

function closeNav() {
 document.getElementById("side-nav").style.width = "0";
}

document.querySelector('#search-icon').onclick = () =>{
  document.querySelector('#search-form').classList.toggle('active');
  }

  document.querySelector('#close').onclick = () =>{
  document.querySelector('#search-form').classList.remove('active');
  }

  document.addEventListener('DOMContentLoaded', function () {
      // Set the initial cart count
      let cartCount = 0;
      const cartCountElement = document.getElementById('cart-count');
      updateCartCount(cartCount); // Call the function to update the cart count

      // Function to update the cart count in the DOM
      function updateCartCount(count) {
          cartCount = count;
          cartCountElement.innerText = cartCount;
          cartCountElement.style.display = cartCount > 0 ? 'inline' : 'none';

      }
      // Add click event listener to all "Add to Cart" links
      const addToCartLinks = document.querySelectorAll('.add-to-cart-link');
      addToCartLinks.forEach(function (link) {
          link.addEventListener('click', function (event) {
              // event.preventDefault(); // Prevent the default link behavior
              const productId = this.getAttribute('data-product-id');                
              cartCount += 1;
              updateCartCount(cartCount); 
          });
      });
  });






