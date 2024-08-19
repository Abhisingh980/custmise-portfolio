document.addEventListener("DOMContentLoaded", function () {
  const navLinks = document.querySelectorAll(".nav-link");

  // Check if there's an active link stored in localStorage
  const activeLinkId = localStorage.getItem("activeLink");

  if (activeLinkId) {
    document.getElementById(activeLinkId).classList.add("active");
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", function () {
      // Remove the 'active' class from all links
      navLinks.forEach((link) => link.classList.remove("active"));

      // Add the 'active' class to the clicked link
      this.classList.add("active");

      // Store the clicked link's ID in localStorage
      localStorage.setItem("activeLink", this.id);
    });
  });
});
