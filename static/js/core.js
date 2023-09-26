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
        // messageElement.textContent = "You selected Australia.";
        country = "Australia";
    } else if (selectedValue === "US") {
        // messageElement.textContent = "You selected US.";
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
    Populates in the stock table all data for a given stock
    */
    const tableBody = document.querySelector("#selectedStocksTable tbody");

    // Clear the table
    tableBody.innerHTML = "";

    // Define column information
    const columns = [
        { header: "Code", property: "code" },
        { header: "Country", property: "country" },

        { header: "Price", property: "stockInfo.price" },
        { header: "Market Cap", property: "stockInfo.marketCap" },
        { header: "Shares Available", property: "stockInfo.numSharesAvail" },
        { header: "Year Low Price", property: "stockInfo.yearlyLowPrice" },
        { header: "Year High Price", property: "stockInfo.yearlyHighPrice" },
        { header: "50 Day MA", property: "stockInfo.fiftyDayMA" },
        { header: "200 Day MA", property: "stockInfo.twoHundredDayMA" },

        { header: "Acquirers Multiple", property: "stockInfo.acquirersMultiple" },
        { header: "Current Ratio", property: "stockInfo.currentRatio" },
        { header: "Enterprise Value", property: "stockInfo.enterpriseValue" },
        { header: "EPS", property: "stockInfo.eps" },
        { header: "EV To EBITDA", property: "stockInfo.evToEBITDA" },
        { header: "EV To Revenue", property: "stockInfo.evToRev" },
        { header: "PE Ratio Trailing", property: "stockInfo.peRatioTrail" },
        { header: "PE Ratio Forward", property: "stockInfo.peRatioForward" },
        { header: "Price to Sales", property: "stockInfo.priceToSales" },
        { header: "Price to Book", property: "stockInfo.priceToBook" },

        { header: "Dividend Yield", property: "stockInfo.dividendYield" },
        { header: "Dividend Rate", property: "stockInfo.dividendRate" },
        { header: "Ex Div Date", property: "stockInfo.exDivDate" },
        { header: "Payout Ratio", property: "stockInfo.payoutRatio" },
        
        { header: "Book Value per Share", property: "stockInfo.bookValPerShare" },
        { header: "Cash", property: "stockInfo.cash" },
        { header: "Cash per Share", property: "stockInfo.cashPerShare" },
        { header: "Cash to Market Cap", property: "stockInfo.cashToMarketCap" },
        { header: "Cash to Debt", property: "stockInfo.cashToDebt" },
        { header: "Debt", property: "stockInfo.debt" },
        { header: "Debt to Market Cap", property: "stockInfo.debtToMarketCap" },
        { header: "Debt to Equity", property: "stockInfo.debtToEquityRatio" },
        { header: "Return on Assets", property: "stockInfo.returnOnAssets" },
        { header: "Return on Equity", property: "stockInfo.returnOnEquity" },

        { header: "EBITDA", property: "stockInfo.ebitda" },
        { header: "EBITDA Per Share", property: "stockInfo.ebitdaPerShare" },
        { header: "Earnings Growth", property: "stockInfo.earningsGrowth" },
        { header: "Gross Profit", property: "stockInfo.grossProfit" },
        { header: "Gross Profit per Share", property: "stockInfo.grossProfitPerShare" },
        { header: "Net Income", property: "stockInfo.netIncome" },
        { header: "Net Income per Share", property: "stockInfo.netIncomePerShare" },
        { header: "Operating Margin", property: "stockInfo.operatingMargin" },
        { header: "Profit Margin", property: "stockInfo.profitMargin" },
        { header: "Revenue", property: "stockInfo.revenue" },
        { header: "Revenue Growth", property: "stockInfo.revenueGrowth" },
        { header: "Revenue Per Share", property: "stockInfo.revenuePerShare" },

        { header: "FCF", property: "stockInfo.fcf" },
        { header: "FCF to Market Cap", property: "stockInfo.fcfToMarketCap" },
        { header: "FCF per Share", property: "stockInfo.fcfPerShare" },
        { header: "FCF to EV", property: "stockInfo.fcfToEV" },
        { header: "OCF", property: "stockInfo.ocf" },
        { header: "OCF to Revenue", property: "stockInfo.ocfToRevenueRatio" },
        { header: "OCF to Market Cap", property: "stockInfo.ocfToMarketCap" },
        { header: "OCF per Share", property: "stockInfo.ocfPerShare" },
        { header: "OCF to EV", property: "stockInfo.ocfToEV" }
    ];

    for (const stock of selectedStocks) {
        const row = tableBody.insertRow();

        for (const column of columns) {
            const cell = row.insertCell();
            const cellValue = getValueByProperty(stock, column.property);
            cell.textContent = cellValue;
        }
    }
}


function getValueByProperty(obj, property) {
    /*
    Retries property value of a given property
    */
    const properties = property.split(".");
    let value = obj;
    
    for (const prop of properties) {
        value = value[prop];
        if (value === undefined) break;
    }
    
    return value !== undefined ? value : "";
}


function sortTable(n) {
    /*
    Allows ascending and descending toggling functionality
    */
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("selectedStocksTable");
    switching = true;
    // Set the sorting direction to ascending:
    dir = "asc";
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
      // Start by saying: no switching is done:
      switching = false;
      rows = table.rows;
      /* Loop through all table rows (except the
      first, which contains table headers): */
      for (i = 1; i < (rows.length - 1); i++) {
        // Start by saying there should be no switching:
        shouldSwitch = false;
        /* Get the two elements you want to compare,
        one from current row and one from the next: */
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        /* Check if the two rows should switch place,
        based on the direction, asc or desc: */
        if (dir == "asc") {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            // If so, mark as a switch and break the loop:
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            // If so, mark as a switch and break the loop:
            shouldSwitch = true;
            break;
          }
        }
      }
      if (shouldSwitch) {
        /* If a switch has been marked, make the switch
        and mark that a switch has been done: */
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        // Each time a switch is done, increase this count by 1:
        switchcount ++;
      } else {
        /* If no switching has been done AND the direction is "asc",
        set the direction to "desc" and run the while loop again. */
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }