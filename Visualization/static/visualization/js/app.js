// from flask to html passed
const card_info = card_data;

// get select reference
var selectDropDown = d3.select("#cardtype");

// Attach event to listen for change
selectDropDown.on("change",buildPriceTable)
//selectDropDown.on("change",buildPage)

// two in 1 functions
function buildPage(){
    buildChart()
    buildPriceTable()
}

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


function buildChart() {
    let price_history = d3.select("#price_history")
    price_history.html("");

    var data = []
    let style_category = graph_data[d3.select("#cardtype").node().value]

    for (let price_category in style_category) {
        data.push(
            {
                type: "scatter",
                mode: "lines",
                x: graph_data['date'],
                y: graph_data[d3.select("#cardtype").node().value][price_category],
                name: price_category
            }
        )
    }

    /*
    var traceLow = {
        type: "scatter",
        mode: "lines",
        x: graph_data['date'],
        y: graph_data[d3.select("#cardtype").node().value]["low"]
    }

    var traceMid = {
        type: "scatter",
        mode: "lines",
        x: graph_data['date'],
        y: graph_data[d3.select("#cardtype").node().value]["mid"]
    }
    
    var traceHigh = {
        type: "scatter",
        mode: "lines",
        x: graph_data['date'],
        y: graph_data[d3.select("#cardtype").node().value]["high"]
    }

    var traceMarket= {
        type: "scatter",
        mode: "lines",
        x: graph_data['date'],
        y: graph_data[d3.select("#cardtype").node().value]["market"]
    }
    
    var data = [traceLow,traceMid,traceHigh,traceMarket]
    */

    var layout = {
        title: "Price History",
        xaxis:{
            type: 'date'
        },
        yaxis:{
            type: 'linear'
        }
    }
    
    Plotly.newPlot('price_history', data, layout, {responsive:true});
}



// Build when page loads
buildSelectD3()
buildPriceTable()
buildLegalityTable()
buildChart()

