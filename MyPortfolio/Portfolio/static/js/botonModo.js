const btnSwitch = document.querySelector('#switch');
const nameInput = document.querySelector('#nameInput');

function toggleDarkMode() {
    document.body.classList.toggle('dark');
    nameInput.classList.toggle('bg-dark');
    btnSwitch.classList.toggle('active');
}

btnSwitch.addEventListener('click', toggleDarkMode);