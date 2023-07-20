const btnSwitch = document.querySelector('#switch');
const nameInput = document.querySelector('#nameInput');
const emailInput = document.querySelector('#emailInput');
const telInput = document.querySelector('#telInput');
const MensajeTextarea = document.querySelector('#MensajeTextarea');


function toggleDarkMode() {
    document.body.classList.toggle('dark');
    nameInput.classList.toggle('bg-dark');
    emailInput.classList.toggle('bg-dark');
    telInput.classList.toggle('bg-dark');
    MensajeTextarea.classList.toggle('bg-dark');
    btnSwitch.classList.toggle('active');
}

btnSwitch.addEventListener('click', toggleDarkMode);