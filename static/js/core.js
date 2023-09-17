function updateStocksDropdown() {
    /*
    * fetches all stocks, country dependent
    */
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
    /*
    * populates all stocks, country dependent into a dropdown
    */
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
    /**
    * determining which country stocks are to be displayed
    */
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
    /*
    * filters stocks depending on the country 
    */
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
    /*
    * filters stocks in the dropdown dependent on the country
    */
    
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
    /*
    * adds selected stock to the table
    */
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
    /*
    * Renders table dynamically
    */
    var tableBody = document.querySelector("#selectedStocksTable tbody");

    // Clear the table
    tableBody.innerHTML = "";

    // Add selected stocks to the table
    const num_cols = 53;

    for (var i = 0; i < selectedStocks.length; i++) {
        var row = tableBody.insertRow(i);

        // Create an array to store cell references
        var cellReferences = [];

        for (var j = 0; j < num_cols; j++) {
            var cell = row.insertCell(j);
            cellReferences.push(cell);
        }

        // Fill in cell values based on selectedStocks data
        cellReferences[0].textContent = selectedStocks[i].code;
        cellReferences[1].textContent = selectedStocks[i].country;

        if (selectedStocks[i].stockInfo) {
            const stockInfo = selectedStocks[i].stockInfo;
            cellReferences[2].textContent = stockInfo.price;
            cellReferences[3].textContent = stockInfo.marketCap;
            cellReferences[4].textContent = stockInfo.numSharesAvail;
            cellReferences[5].textContent = stockInfo.yearlyLowPrice;
            cellReferences[6].textContent = stockInfo.yearlyHighPrice;
            cellReferences[7].textContent = stockInfo.fiftyDayMA;
            cellReferences[8].textContent = stockInfo.twoHundredDayMA;

            // cellReferences[9].textContent  = stockInfo.acquirersMultiple;
            // cellReferences[10].textContent = stockInfo.currentRatio;
            // cellReferences[11].textContent = stockInfo.enterpriseValue;
            // cellReferences[12].textContent = stockInfo.eps;
            // cellReferences[13].textContent = stockInfo.evToEBITDA;
            // cellReferences[15].textContent = stockInfo.evToRev;
            // cellReferences[16].textContent = stockInfo.peRatioTrail;
            // cellReferences[17].textContent = stockInfo.peRatioForward;
            // cellReferences[18].textContent = stockInfo.priceToSales;
            // cellReferences[19].textContent = stockInfo.priceToBook;

            // cellReferences[20].textContent = stockInfo.dividendYield;
            // cellReferences[21].textContent = stockInfo.dividendRate;
            // cellReferences[22].textContent = stockInfo.exDivDate;
            // cellReferences[23].textContent = stockInfo.payoutRatio;

            // cellReferences[24].textContent = stockInfo.bookValPerShare;
            // cellReferences[25].textContent = stockInfo.cash;
            // cellReferences[26].textContent = stockInfo.cashPerShare;
            // cellReferences[27].textContent = stockInfo.cashToMarketCap;
            // cellReferences[28].textContent = stockInfo.cashToDebt;
            // cellReferences[29].textContent = stockInfo.debt;
            // cellReferences[30].textContent = stockInfo.debtToMarketCap;
            // cellReferences[31].textContent = stockInfo.debtToEquityRatio;
            // cellReferences[32].textContent = stockInfo.returnOnAssets;
            // cellReferences[33].textContent = stockInfo.returnOnEquity;

            // cellReferences[34].textContent = stockInfo.ebitda;
            // cellReferences[35].textContent = stockInfo.ebitdaPerShare;
            // cellReferences[36].textContent = stockInfo.earningsGrowth;
            // cellReferences[37].textContent = stockInfo.grossProfit;
            // cellReferences[38].textContent = stockInfo.grossProfitPerShare;
            // cellReferences[39].textContent = stockInfo.netIncome;
            // cellReferences[40].textContent = stockInfo.netIncomePerShare;
            // cellReferences[41].textContent = stockInfo.operatingMargin;
            // cellReferences[42].textContent = stockInfo.profitMargin;
            // cellReferences[43].textContent = stockInfo.revenue;
            // cellReferences[44].textContent = stockInfo.revenueGrowth;
            // cellReferences[45].textContent = stockInfo.revenuePerShare;

            // cellReferences[46].textContent = stockInfo.fcf;
            // cellReferences[47].textContent = stockInfo.fcfToMarketCap;
            // cellReferences[48].textContent = stockInfo.fcfPerShare;
            // cellReferences[49].textContent = stockInfo.fcfToEV;
            // cellReferences[50].textContent = stockInfo.ocf;
            // cellReferences[51].textContent = stockInfo.ocfToRevenueRatio;
            // cellReferences[52].textContent = stockInfo.ocfToMarketCap;
            // cellReferences[53].textContent = stockInfo.ocfPerShare;
            // cellReferences[54].textContent = stockInfo.ocfToEV
        }
    }
}