document.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    window.location.href = "/games";
  }
});

// Contact form submission
document.addEventListener("DOMContentLoaded", function() {
  const ctcsubmit = document.getElementById("ctcsubmit");
  if (ctcsubmit) {
    ctcsubmit.addEventListener("click", (e) => {
      e.preventDefault(); // para hindi mag-submit agad yung form
      alert("Message sent! Thanks for reaching out.");
    });
  }

  // Purchase button for all topup pages
  const buyNowBtn = document.getElementById("buy-now");
  if (buyNowBtn) {
    buyNowBtn.addEventListener("click", (e) => {
      e.preventDefault(); // para hindi mag-submit agad yung form
      alert("Top Up successfully. Thanks for purchasing!");
    });
  }

  // Dropdown toggle for More menu
  const dropdownToggle = document.querySelector(".Dropdown-toggle");
  const dropdownItem = document.querySelector(".Dropdown-item");
  const dropdownContent = document.querySelector(".Dropdown-content");
  
  if (dropdownToggle && dropdownItem) {
    // Function to check if on mobile
    function isMobile() {
      return window.innerWidth <= 576;
    }
    
    // Function to position dropdown on mobile (fixed positioning)
    function positionDropdown() {
      if (window.innerWidth < 768 && dropdownContent) {
        // Mobile: use fixed positioning
        const toggleRect = dropdownToggle.getBoundingClientRect();
        dropdownContent.style.top = (toggleRect.bottom) + "px";
        dropdownContent.style.left = (toggleRect.left) + "px";
      }
    }
    
    dropdownToggle.addEventListener("click", (e) => {
      e.preventDefault();
      
      // On mobile, scroll to footer instead of showing dropdown
      if (isMobile()) {
        const footer = document.getElementById("footer");
        if (footer) {
          footer.scrollIntoView({ behavior: "smooth" });
        }
      } else {
        // On desktop, toggle the dropdown menu
        dropdownItem.classList.toggle("active");
        if (dropdownItem.classList.contains("active")) {
          positionDropdown();
        }
      }
    });
    
    // Reposition on window resize
    window.addEventListener("resize", positionDropdown);
    
    // Close dropdown when clicking outside (desktop only)
    document.addEventListener("click", (e) => {
      if (!dropdownItem.contains(e.target)) {
        dropdownItem.classList.remove("active");
      }
    });
    
    // Close dropdown when clicking on a link inside it (desktop only)
    const dropdownLinks = document.querySelectorAll(".Dropdown-content a");
    dropdownLinks.forEach(link => {
      link.addEventListener("click", () => {
        dropdownItem.classList.remove("active");
      });
    });
  }
});
