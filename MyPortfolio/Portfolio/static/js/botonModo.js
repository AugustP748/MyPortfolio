const btnSwitch = document.querySelector('#switch');

function toggleDarkMode() {
    document.body.classList.toggle('dark');
    btnSwitch.classList.toggle('active');
}

btnSwitch.addEventListener('click', toggleDarkMode);