function updateStocksDropdown() {
    var country = getSelectedCountry(); // Get the selected country from getSelectedCountry()
    var stockSelector = document.getElementById("Stock_selector");
    stockSelector.innerHTML = ""; // Clear the stock options

    if (country === "Australia") {
        // Populate stock options for Australia
        var ausStocks = ["Stock 1", "Stock 2", "Stock 3"];
        populateStockOptions(ausStocks);
    } else if (country === "US") {
        // Populate stock options for US
        var usStocks = ["Stock A", "Stock B", "Stock C"];
        populateStockOptions(usStocks);
    }
}

function populateStockOptions(stockArray) {
    var stockSelector = document.getElementById("Stock_selector");

    for (var i = 0; i < stockArray.length; i++) {
        var option = document.createElement("option");
        option.value = stockArray[i];
        option.text = stockArray[i];
        stockSelector.appendChild(option);
    }
}

function getSelectedCountry() {
    var selectElement = document.getElementById("Country_selector");
    var selectedValue = selectElement.value;
    var messageElement = document.getElementById("message");
    var country = "";

    if (selectedValue === "Aus") {
        messageElement.textContent = "You selected Australia.";
        country = "Australia";
    } else if (selectedValue === "US") {
        messageElement.textContent = "You selected US.";
        country = "US";
    } else {
        messageElement.textContent = ""; // Clear the message if no option is selected
    }

    return country;
}