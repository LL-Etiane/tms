showSideBar = true;
sidebar = document.getElementById("sidebar");
mainsection = document.getElementById("mainsection");
mainsectionDown = document.getElementById("main-section-down");
sidbarToggler = document.getElementById("togglesidebar");

mainsectionDown.addEventListener("click", () => {
  if (window.screen.width <= 780) {
    hideSidebar();
  }
});

function hideSidebar() {
  if (showSideBar) {
    showSideBar = false;
    sidebar.classList.add("hidesidebar");
  } else {
    sidebar.classList.remove("hidesidebar");
    showSideBar = true;
  }
}

function reduceSidebar() {
  sidebar.classList.remove("hidesidebar");
  if (showSideBar) {
    showSideBar = false;
    sidebar.classList.add("reducesidebarwidth");
  } else {
    sidebar.classList.remove("reducesidebarwidth");
    showSideBar = true;
  }
}

togglesidebar.addEventListener("click", () => {
  hideSidebar();
});

sidebar.addEventListener("resize", () => {
  console.log(window.screen.width);
});
