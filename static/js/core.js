function updateStocksDropdown() {
    var country = getSelectedCountry();
    var stockSelector = document.getElementById("Stock_selector");
    stockSelector.innerHTML = "";

    if (country !== "") {
        fetch('/get_stocks/' + country)
            .then(response => response.json())
            .then(data => populateStockOptions(data));
    }
}

function populateStockOptions(stockArray) {
    var stockSelector = document.getElementById("Stock_selector");
    
    // Sort the stockArray in alphabetical order
    stockArray.sort();
    
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


function filterStocks() {
    var inputElement = document.getElementById("Filter_input");
    var filterText = inputElement.value.toUpperCase();
    var country = getSelectedCountry();
    
    if (country !== "") {
        fetch('/get_stocks/' + country)
            .then(response => response.json())
            .then(data => filterStocksDropdown(data, filterText));
    }
}

function filterStocksDropdown(stockArray, filterText) {
    // Sort the stockArray in alphabetical order
    stockArray.sort();

    var filteredStocks = stockArray.filter(stock => stock.toUpperCase().startsWith(filterText));

    var filteredStocksDropdown = document.getElementById("filteredStocksDropdown");
    filteredStocksDropdown.innerHTML = "";  // Clear the existing dropdown options
    
    var dropdown = document.createElement("select");
    for (var i = 0; i < filteredStocks.length; i++) {
        var option = document.createElement("option");
        option.value = filteredStocks[i];
        option.text = filteredStocks[i];
        dropdown.appendChild(option);
    }

    filteredStocksDropdown.appendChild(dropdown);
}
