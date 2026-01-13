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

  // Topup form submission
  const topupForm = document.getElementById("topup-form");
  if (topupForm) {
    topupForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      
      // Get game name from page - extract from image alt or use generic name
      const gameImg = document.querySelector(".ML-PAGE .First img");
      const gameName = gameImg ? gameImg.alt.replace('-Logo', '').trim() : "Unknown Game";
      
      // Get form data using FormData API
      const formData = new FormData(topupForm);
      const username = formData.get('username');
      const email = formData.get('email');
      
      // Get the currency value (could be golds, diamond, Shells, or Nexus depending on game)
      const golds = formData.get('golds') || formData.get('diamond') || formData.get('Shells') || formData.get('Nexus');
      const payment = formData.get('payment');
      
      // Validate inputs
      if (!username || !email || !golds || !payment) {
        alert("Please fill in all required fields");
        return;
      }
      
      // Get the price from the selected radio button's data attribute
      const selectedInput = document.querySelector('input[name="golds"]:checked, input[name="diamond"]:checked, input[name="Shells"]:checked, input[name="Nexus"]:checked');
      const amount = parseFloat(selectedInput.dataset.price) || parseFloat(golds);
      
      // Prepare data for API
      const transactionData = {
        username: username,
        email: email,
        game: gameName,
        amount: amount,
        payment_method: payment,
        game_user_id: formData.get('userid'),
        zone_id: formData.get('userserver')
      };
      
      try {
        // Send to backend
        const response = await fetch('/api/record-topup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(transactionData)
        });
        
        const result = await response.json();
        
        if (result.success) {
          alert(`✓ Top Up Successfully Processed!\n\nTransaction ID: ${result.transaction_id}\nUsername: ${username}\nGame: ${gameName}\nAmount: ₱${amount}\nPayment: ${payment}`);
          // Reset form
          topupForm.reset();
        } else {
          alert(`✗ Error: ${result.error}`);
        }
      } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while processing your top-up. Please try again.');
      }
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
