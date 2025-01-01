let menuActive = false;

const hamMenu = document.querySelector('.hamburger-menu');
const menu = document.querySelector('.menu');

hamMenu.addEventListener('click', () => {
    menuActive = !menuActive;
    hamMenu.classList.toggle('active');
    menu.classList.toggle('active');
});


