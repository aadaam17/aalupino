// Grab elements
const selectElement = (selector) => {
  const element = document.querySelector(selector);
  if (element) return element;
  throw new Error(
    `Something went wrong! Make sure that ${selector} exists/is typed correctly.`
  );
};

//Nav styles on scroll
const scrollHeader = () => {
  const navbarElement = selectElement("#header");
  if (this.scrollY >= 15) {
    navbarElement.classList.add("activated");
  } else {
    navbarElement.classList.remove("activated");
  }
};

window.addEventListener("scroll", scrollHeader);

// Open menu & search pop-up
const menuToggleIcon = selectElement("#menu-toggle-icon");
const formOpenBtn = selectElement("#search-icon");
const formCloseBtn = selectElement("#form-close-btn");
const searchContainer = selectElement("#search-form-container");
const mobileMenu = selectElement("#menu");

const toggleMenu = () => {
  mobileMenu.classList.toggle("activated");
  menuToggleIcon.classList.toggle("activated");
};

menuToggleIcon.addEventListener("click", toggleMenu);

/*
const iicon = selectElement(".iicon");
const subMenu = selectElement(".sub-menu");

window.addEventListener("click", function (e) {
  if (e.target != iicon && e.target != menuToggleIcon && e.target != mobileMenu) {
    menuToggleIcon.classList.remove("activated");
    mobileMenu.classList.remove("activated");
    subMenu.classList.remove("activated");
    console.log("Outside Menu")
  }
})
*/

// Open/Close search form popup
formOpenBtn.addEventListener("click", () =>
  searchContainer.classList.add("activated")
);
formCloseBtn.addEventListener("click", () =>
  searchContainer.classList.remove("activated")
);
// -- Close the search form popup on ESC keypress
window.addEventListener("keyup", (event) => {
  if (event.key === "Escape") searchContainer.classList.remove("activated");
});

// Opening and Closing Sub Menu

const subMenu = document.getElementsByClassName("sub-menu");
const menuLinker = document.getElementsByClassName("menu-linker");
const closeMenuBtn = document.getElementsByClassName("close-menu-btn");

const openSubMenu = () => {


  for (let i = 0; i < menuLinker.length; i++) {

    menuLinker[i].addEventListener("click", () => {
      subMenu[i].classList.add("activated")
      menuToggleIcon.classList.add("deactivated")
    })

    closeMenuBtn[i].addEventListener("click", () => {
      subMenu[i].classList.remove("activated")
      menuToggleIcon.classList.remove("deactivated")
    })

  }

};

openSubMenu();

// Switch theme/add to local storage
const body = document.body;
const themeToggleBtn = selectElement("#theme-toggle-btn");
const currentTheme = localStorage.getItem("currentTheme");

// Check to see if there is a theme preference in local Storage, if so add the ligt theme to the body
if (currentTheme) {
  body.classList.add("dark-theme");
}

themeToggleBtn.addEventListener("click", function () {
  // Add dark theme on click
  body.classList.toggle("dark-theme");

  // If the body has the class of light theme then add it to local Storage, if not remove it
  if (body.classList.contains("dark-theme")) {
    localStorage.setItem("currentTheme", "themeActive");
  } else {
    localStorage.removeItem("currentTheme");
  }
});

// Swiper 
const swiper = new Swiper(".swiper1", {
  // How many slides to show
  slidesPerView: "auto",
  // For free slides
  freeMode: true,
  // How much space between slides
  spaceBetween: 12,
  // Make the next and previous buttons work
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  // Make the pagination indicators work
  pagination: {
    el: '.swiper-pagination-1'
  },
  //Responsive breakpoints for how many slides to show at that view
  breakpoints: {
    // 700px and up shoes 2 slides
    700: {
      slidesPerView: 2
    },
    // 1200px and up shoes 3 slides
    1200: {
      slidesPerView: 3
    }
  }
});

/* Image Switcher */
const mainImg = selectElement("#main-img")
const smImg = document.getElementsByClassName("sm-img")
const smImgX = document.getElementsByClassName("sm-img-x")

const selectImg = () => {
  for (let i = 0; i < smImg.length; i++) {
    smImg[i].addEventListener("click", function () {
      mainImg.src = smImgX[i].src;
      let currentImg = selectElement(".active-img");
      currentImg.classList.remove("active-img");
      this.classList.add("active-img")
    })
  }
}

selectImg();

/* Swiper II */
const swiper2 = new Swiper(".swiper2", {
  // How many slides to show
  slidesPerView: "auto",
  // For free slides
  freeMode: true,
  // How much space between slides
  spaceBetween: 4,
  // Make the next and previous buttons work
  navigation: {
    nextEl: '.swiper-button-next-2',
    prevEl: '.swiper-button-prev-2',
  },
  // Make the pagination indicators work
  pagination: {
    el: '.swiper-pagination-2'
  },
  //Responsive breakpoints for how many slides to show at that view
  breakpoints: {
    // 700px and up shoes 2 slides
    700: {
      slidesPerView: 2
    },
    // 1200px and up shoes 3 slides
    1200: { slidesPerView: 3 }
  }
});