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
  
  if (dropdownToggle && dropdownItem) {
    dropdownToggle.addEventListener("click", (e) => {
      e.preventDefault();
      dropdownItem.classList.toggle("active");
    });
    
    // Close dropdown when clicking outside
    document.addEventListener("click", (e) => {
      if (!dropdownItem.contains(e.target)) {
        dropdownItem.classList.remove("active");
      }
    });
    
    // Close dropdown when clicking on a link inside it
    const dropdownLinks = document.querySelectorAll(".Dropdown-content a");
    dropdownLinks.forEach(link => {
      link.addEventListener("click", () => {
        dropdownItem.classList.remove("active");
      });
    });
  }
});
