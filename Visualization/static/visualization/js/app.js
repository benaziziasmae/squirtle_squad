// from flask to html passed
const card_info = card_data;

// get select reference
var selectDropDown = d3.select("#cardtype");

// Attach event to listen for change
selectDropDown.on("change",buildPriceTable)

// build the dropdown menu
function buildSelectD3() {
    Object.keys(card_info.prices).forEach(card_type =>
        {
            selectDropDown
            .append("option")
            .property("value",card_type)
            .text(card_type)
        }
        )
    }

// get image reference & apply new
d3.select("#card_image").attr("src", card_info.images.large)

// Build the table
function buildPriceTable() {

    //Populate the Header
    let thead = d3.select("#PriceHead")
    thead.html("");

    let header = d3.select("#PriceHead").append("tr");
    Object.keys(card_info['prices'][d3.select("#cardtype").node().value]).forEach(priceLevel =>
        {
            let columnName = header.append("th")
            columnName.text(priceLevel.charAt(0).toUpperCase()+priceLevel.slice(1))
        }
        )

    //Populate the body
    let tbody = d3.select("#PriceBody")
    tbody.html("");

    let row = d3.select("#PriceBody").append("tr");
    Object.values(card_info['prices'][d3.select("#cardtype").node().value]).forEach(priceLevel =>
        {
            let cell = row.append("td")
            cell.text(priceLevel)
        }
        )
}

function buildLegalityTable() {

    //clear the Header
    let thead = d3.select("#LegalityHead")
    thead.html("");

    //select the header
    let header = d3.select("#LegalityHead").append("tr");
    //add some spacing
    header.append("th")
    //populate the header
    Object.keys(card_info['legalities']).forEach(gameFormat =>
        {
            let columnName = header.append("th")
            columnName.text(gameFormat.charAt(0).toUpperCase()+gameFormat.slice(1))
            header.append("th")
        }
        )

    //clear the body
    let tbody = d3.select("#LegalityBody")
    tbody.html("");

    //select the body
    let row = d3.select("#LegalityBody").append("tr");
    //add some spacing
    row.append("td")
    //populate the body
    Object.values(card_info['legalities']).forEach(gameFormat =>
        {
            if (gameFormat=="Legal") {
                row.append("td").style("background-color", 'green').text(gameFormat)
            } else {
                row.append("td").style("background-color", 'red').text(gameFormat)
            }
            row.append("td")
        }
        )
}

/*
function graphOverTime() {

    graph_data[0]['prices'][d3.select("#cardtype").node().value]
    }
*/


// Build when page loads

buildSelectD3()
buildPriceTable()
buildLegalityTable()
