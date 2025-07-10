console.log("yes it's linked");

const sidebar = document.getElementById("sidebar");
const logo = document.getElementById("youtube-logo");

logo.addEventListener("click", () => {
  console.log("logo-clicked");

  console.log(sidebar.classList);
  sidebar.classList.toggle("hidden");
});
// logo.addEventListener("click", () => {
//   sidebar.classList.toggle("left-[-200px]");
// });
