function toggleMode() {
    var body = document.querySelector("body");
    body.classList.toggle("dark-mode");
    body.classList.toggle("light-mode");
}

document.addEventListener("DOMContentLoaded", function() {
    // Obtiene el elemento del interruptor de modo
    var switchButton = document.querySelector("#flexSwitchCheckChecked");

    // Verifica si el elemento existe antes de asignar el evento
    if (switchButton) {
        // Ejecuta la función toggleMode cuando el interruptor cambie su estado
        switchButton.addEventListener("change", toggleMode);
    }
});
