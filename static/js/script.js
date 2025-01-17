// Feather Icons Initialization
feather.replace();

// Toggle Menu Function
function toggleMenu() {
  const navbar = document.querySelector(".navbar");
  navbar.classList.toggle("active");
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#pesan form");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = document.querySelector("#name").value;
    const pesanan = document.querySelector("#pesanan").value;

    alert(`Hi ${name}, pesanan Anda (${pesanan}) sedang diproses.`);
  });
});
