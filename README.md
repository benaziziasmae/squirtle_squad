
# Pokémon OCR & Price Comparator

## Overview

This repository hosts source code & background information for a Pokémon TCG card scanner & price checker. This README will be updated periodically through out the project's progress.

## Topic Rationale

This topic was selected due to the light-heartedness of its nature which at the same time demonstrates the mastery of data visualization, data base administration & management, and machine learning. For all intents and purposes, the project shall hence forth be referred to as an 'app'. A flow chart representing the processes of the app is shown below.

![process](/Resources/process.png)

The purpose of this app is to price check a Pokémon TCG card based on the user input via a video, scan or static image of the card they wish to know about. The first form of implementation that will be attempted will be for a user to submit a static image of the card. Then through machine learning & computer vision, a packet of information consisting at minimum of the collector number will be sent to a module that will perform the query in a regularly updatable database.

Below is an example card with collector number located in bottom left corner. Pokémon cards belong to Sets, indicated by the symbol also located in the bottom left corner. Each Set is a part of a larger Series. This version of the cramorant card is from the Sword & Shield base Set of the Sword & Shield Series (currently on-going).

![cramorant](/Machine_Learning/train/cramorant.png)

The database shall have its entries pulled from the Pokemon TCG API. This API contains information on prices from [TCGPlayer.com](https://www.tcgplayer.com/). The data will be transformed & optimized to consist of information needed for our visualization. As an initial proof of concept, the initial data will be pulled from the Pokemon TCG API however room for expansion on this would be to obtain prices from other vendors.

The final visualization is anticipated as an HTML page that would consist of details, prices and image of the card.

## Team Members & Project Map

Due to the nature & scope of the project, roles will be similar but not identical week to week with some roles being responsibilities of multiple team members.

| Team Member    | Week 1 Role  | Week 2 Role | Week 3 Role | Week 4 Role |
|----------------|--------------|-------------|-------------|-------------|
| Aryana Akhavan | ○       |             |             |             |
| Asmae Benazizi | ▢       |             |             |             |
| Ian Fan        | x / △ |             |             |             |
| Kun Zhao       | ○       |             |             |             |
| Lydia Zhang    | x / ○    |             |             |             |

## Team Communication Protocol

Team members communicated through Slack and voice communications supported by Microsoft Teams & Google Hangouts. Screen-sharing capabilities on such platforms were crucial to facilitate information sharing and troubleshooting.

Current tasks, scratchpad and brainstormed ideas are on [Google Sheets](https://docs.google.com/spreadsheets/d/133HnyivTdR334dvsgrOn8IoTsdS8Uze6dNppac0ljDY/edit#gid=0) and [Trello](https://trello.com/b/3LoHN9J1/final-project-squirtlesquad). A Gantt Chart is within the realm of possibility to be added.

## Resources

Languages, Libraries, Software Used for this project are listed by tasks.

### Database

* [Pokemon TCG API](https://pokemontcg.io/)
* Python ETL
* SQL PostGRES (established database named *SwShSeries*)

### Machine Learning Model

* Optical Character Recognition
* Tesseract
* OpenCV

### Visualization

* HTML/ Flask

### Presentation

* [Google Slides](https://docs.google.com/presentation/d/1qF4vChUlj-rcls2imSxiKIAQhV3nn66cnlHZGZnHb6g/edit?usp=sharing)

Google Slides was used to create the group presentation as it allows for collaboration from multiple participants. Various images were sourced from Google Images in order to increase the visual appeal of the presentation. Most visuals are of Pokémon from the Sword & Shield Series to align with the app's current capabilities.

![slide_sample](/Resources/PokeScanner.png)
