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


var selectedStocks = [];

function addSelectedStock() {
    var stockSelector = document.getElementById("Stock_selector");
    var filterInput = document.getElementById("Filter_input");
    var selectedValue = stockSelector.value || filterInput.value;
    var country = getSelectedCountry();

    if (selectedValue !== "") {
        // Create an object to represent the selected stock
        var selectedStock = {
            code: selectedValue,
            country: country
        };

        // Create an instance of AusStockClass with the selected stock code
        fetch(`/get_stock_info/${country}/${selectedValue}`)
            .then(response => response.json())
            .then(data => {
                // Add the selected stock with its attributes to the array
                selectedStock.stockInfo = data;
                selectedStocks.push(selectedStock);
                // Update the table with the selected stocks
                updateSelectedStocksTable();
            });

        // Clear the filter input
        filterInput.value = "";
        stockSelector.value = "";
    }
}

function updateSelectedStocksTable() {
    var tableBody = document.querySelector("#selectedStocksTable tbody");

    // Clear the table
    tableBody.innerHTML = "";

    // Add selected stocks to the table
    for (var i = 0; i < selectedStocks.length; i++) {
        var row = tableBody.insertRow(i);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        // Add more cells for other attributes as needed

        cell1.textContent = selectedStocks[i].code;
        cell2.textContent = selectedStocks[i].country;

        // Access and add the attributes from the stockInfo property
        if (selectedStocks[i].stockInfo) {
            cell3.textContent = selectedStocks[i].stockInfo.price;
            cell4.textContent = selectedStocks[i].stockInfo.marketCap;
            // Add more cells for other attributes as needed
        }
    }
}



