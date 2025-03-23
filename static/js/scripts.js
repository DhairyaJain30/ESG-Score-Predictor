/*!
* Start Bootstrap - Creative v7.0.7 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

    const form = document.getElementById('contactForm');
    const submitButton = document.getElementById('submitButton');

    if (form && submitButton) {
    const inputs = form.querySelectorAll('input[required]');

  // Function to check if all required fields are filled
  function validateForm() {
    let allFilled = true;
    inputs.forEach(input => {
      if (!input.value.trim()) {
        allFilled = false;
      }
    });
    submitButton.disabled = !allFilled;
  }

  // Add input event listener to all required fields
  inputs.forEach(input => {
    input.addEventListener('input', validateForm);
  });

  // Form submission handler
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!submitButton.disabled) {
      // Add your form submission logic here
      console.log('Form submitted successfully');
      // Make an AJAX request, for example:
      // fetch('/predict', {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json'
      //   },
      //   body: JSON.stringify(Object.fromEntries(new FormData(form)))
      // })
      // .then(response => response.json())
      // .then(data => {
      //   console.log('Prediction:', data.prediction);
      // })
      // .catch(error => {
      //   console.error('Error:', error);
      // });
    }
  });

  // Initial validation check
  validateForm();
}});