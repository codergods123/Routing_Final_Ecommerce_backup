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
});
