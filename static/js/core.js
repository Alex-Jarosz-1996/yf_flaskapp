function displayMessage() {
    var selectElement = document.getElementById("Country_selector");
    var selectedValue = selectElement.value;
    var messageElement = document.getElementById("message");

    if (selectedValue === "Aus") {
        messageElement.textContent = "You selected Australia.";
    } else if (selectedValue === "US") {
        messageElement.textContent = "You selected US.";
    } else {
        messageElement.textContent = ""; // Clear the message if no option is selected
    }
}
