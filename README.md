
# Pokemon OCR & Price Comparator

## Project Overview

This repository hosts source code & background information for a Pokemon TCG card scanner & price checker. This Readme will exclusively dedicated to Deliverable 2/Visualization.

In this Deliverable Our team is working on analysing the Pokemon Data gathered from [Pokemon TCG API](https://pokemontcg.io/) and contained the record of plenty of pokemon exposing cards and set details in an easy to consume format.

The base information provided are:
- Pokemon Name
- Release date 
- Legality 
- Images
- prices

## Team Members & Project Map

Due to the nature & scope of the project, roles will be similar but not identical week to week with some roles being responsibilities of multiple team members.

| Team Member    | Week 1 Role  | Week 2 Role | Week 3 Role | Week 4 Role |
|----------------|--------------|-------------|-------------|-------------|
| Aryana Akhavan | ○       |      X / △       |             |             |
| Asmae Benazizi | ⬜       |    X / △      |             |             |
| Ian Fan        | X / △ |        △/X     |             |             |
| Kun Zhao       | ○       |     ○      |             |             |
| Lydia Zhang    | X / ○    |    ○       |             |             |


## Topic Rationale

We decided on this topic for something light-hearted that demonstrates the mastery of data visualization, data base administration & management, & machine learning. For all intents & purposes, the project shall hence forth be referred to as an 'app'. A flow chart representing the processes of the app is shown below (flow chart will be regularly updated & made aesthetically pleasing by week 4)


The purpose of this app is to price check a Pokemon TCG card where the user searches via a video, scan or static image of the card they wish to know about. The first form of implementation that will be attempted will be for a user to submit a static image of the card. Then through machine learning & computer vision, a packet of information consisting at minimum of the collector number will be sent to a module that will perform the query in a regularly updatable database.

Below is an example card with collector number located in bottom left corner for this particular set.

![cramorant](/Resources/cramorant.png)

The database shall have its entries pulled from the Pokemon TCG API. This API contains information on prices from [TCGPlayer.com](https://www.tcgplayer.com/). The data will be transformed & optimized to consist of information needed for our visualization. As an initial proof of concept, the initial data will be pulled from the Pokemon TCG API however room for expansion on this would be to obtain prices from other vendors.

The final visualization is anticipated as an HTML page that would consist of prices & image of the card.



## Team communication Protocol

Team members communicated through Slack & voice communications supported by Microsoft Teams & Google Hangouts.

Team members are meeting at least once a week.

Current tasks, scratchpad & brainstorm ideas are on Google sheets ([GOOGLE SHEET LINK](https://docs.google.com/spreadsheets/d/133HnyivTdR334dvsgrOn8IoTsdS8Uze6dNppac0ljDY/edit#gid=0)) & [Trello](https://trello.com/b/3LoHN9J1/final-project-squirtlesquad). A Gantt chart is within the realm of possibility to be added.

## Resources

Languages, Libraries, Software Used for this project are listed by tasks.

### Machine Learning Model

* Optical Character Recognition
* Tesseract
* OpenCV

### Database

* PostGRES
* SQL
* Python ETL
* [Pokemon TCG API](https://pokemontcg.io/)

### Visualization

Under consideration -

* HTML
