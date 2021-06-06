// From flask to HTML passed
const card_info = card_data;

// Get select reference
var selectDropDown = d3.select("#cardtype");

// Attach event to listen for change
selectDropDown.on("change",buildPriceTable)

// Build the dropdown menu
function buildSelectD3(card_info) {
    Object.keys(card_info.prices).forEach(card_type => 
        {
            selectDropDown
            .append("option")
            .property("value",card_type)
            .text(card_type)
        }
        )
    }

// Get image reference & apply new
d3.select("#card_image").attr("src", card_info.images.large)


// Build the table
function buildPriceTable() {
    
    // Populate the Header
    let thead = d3.select("#tableHead")
    thead.html("");
    
    let header = d3.select("#tableHead").append("tr");
    Object.keys(card_info['prices'][d3.select("#cardtype").node().value]).forEach(priceLevel =>
        {
            let columnName = header.append("th")
            columnName.text(priceLevel.charAt(0).toUpperCase()+priceLevel.slice(1))
        }
        )

    // Populate the body
    let tbody = d3.select("#tableBody")
    tbody.html("");
    
    let row = d3.select("#tableBody").append("tr");
    Object.values(card_info['prices'][d3.select("#cardtype").node().value]).forEach(priceLevel =>
        {
            let cell = row.append("td")
            cell.text(priceLevel)
        }
        )
}

function buildlegalityTable() {
    
    // Clear the Header
    let thead = d3.select("#legalityHead")
    thead.html("");
    
    // Select the header
    let header = d3.select("#legalityHead").append("tr");
    // Add some spacing
    header.append("th")
    // Populate the header
    Object.keys(card_info['legalities']).forEach(gameFormat =>
        {
            let columnName = header.append("th")
            columnName.text(gameFormat.charAt(0).toUpperCase()+gameFormat.slice(1))
            header.append("th")
        }
        )

    // Clear the body
    let tbody = d3.select("#legalityBody")
    tbody.html("");
    
    // Select the body
    let row = d3.select("#legalityBody").append("tr");

    // Add some spacing
    row.append("td")
    // Populate the body
    Object.values(card_info['legalities']).forEach(gameFormat =>
        {
            if (gameFormat=="Legal") {
                row.append("td").style("background-color", 'green').text(gameFormat)
            } else {
                row.append("td").style("background-color", 'light-red').text(gameFormat)
            }
            row.append("td")
        }
        )
}

// Build when page loads
buildSelectD3(card_info)
buildPriceTable()
buildlegalityTable()