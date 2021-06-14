# Pokémon OCR & Price Comparator

## Overview

This repository hosts source code & background information for a Pokémon TCG card scanner & price checker. 

## Topic Rationale

This topic was selected due to the light-heartedness of its nature and to demonstrate the mastery of data visualization, data base administration & management, and machine learning. For all intents and purposes, the project shall hence forth be referred to as an 'app'. A flow chart representing the processes of the app is shown below.

![concept](/Resources/concept.png)

The purpose of this app is to price check a Pokémon TCG card based on the user input via a still frame image (captured via video, scan or static image of the card) they wish to know about. Then through machine learning & computer vision, a packet of information consisting at minimum of the collector number, if recognizable, will be sent to a function that will perform the query in a regularly updatable database.

Below is an example card with collector number located in bottom left corner. Pokémon cards belong to Sets, indicated by the symbol also located in the bottom left corner. Each Set is a part of a larger Series. A Pokémon may exist as more than one version. In the example below, this version of the Cramorant card is from the Sword & Shield base Set of the Sword & Shield Series.

![cramorant](/Resources/cramorant.png)

The database has its entries pulled from the [Pokémon TCG API](https://pokemontcg.io/). This API contains information on prices from [TCGPlayer.com](https://www.tcgplayer.com/) as well as a great deal of other data. The data was transformed & optimized to consist of information needed for our visualization. As an initial proof of concept, the initial data was be pulled from the 'Sword and Shield' series only and from the Pokémon however room for expansion on this would be to obtain prices from other vendors.

The final visualization is anticipated as an HTML page that would consist of details, prices and image of the card.

## Team Members & Project Map

Due to the nature & scope of the project, roles will be similar but not identical week to week with some roles being responsibilities of multiple team members.

| Team Member    | Segment 1 Role  | Segment 2 Role | Segment 3 Role | Segment 4 Role |
|----------------|--------------|-------------|-------------|-------------|
| Aryana Akhavan | ○            | X / ○            |     △ / ○        |  X / △       |
| Asmae Benazizi | ▢            | X / ○            |    △ / ○         |  X / △        |
| Ian Fan        | X / △        | X / △ / ▢        |   ▢ / ○ / X     |  X / △ / ○ / ▢      |
| Kun Zhao       | ○            | X / △            |     △ / ○        |  X / △       |
| Lydia Zhang    | X / ○        | X / △            |     △ / ○        |  X / △      |

## Team Communication Protocol

Team members communicated through Slack and voice communications supported by Microsoft Teams & Google Hangouts. Screen-sharing capabilities on such platforms were crucial to facilitate information sharing and troubleshooting.

Current tasks, scratchpad and brainstormed ideas were on [Google Sheets](https://docs.google.com/spreadsheets/d/133HnyivTdR334dvsgrOn8IoTsdS8Uze6dNppac0ljDY/edit#gid=0) and [Trello](https://trello.com/b/3LoHN9J1/final-project-squirtlesquad). 

## Resources

Languages, Libraries, Software Used for this project are listed by tasks.

### Database & Storage

* [Pokémon TCG API](https://pokemontcg.io/)
* Python
* Pandas
* SQLAlchemy
* Boto3
* AWS - Amazon Web Services

The initialized proof of concept database pulled from only the Sword and Shield series of sets, to ensure that the project had a reasonable size and scope. Using Python, the data extracted from the Pokémon TCG API was first examined to identify the desired variables necessary for the app, then cleaned to keep only those that were meaningful. From there, an engine link was created to the Postgresql database hosted at Amazon Web Services (AWS). Our minimalized data was then imported into the database through Pandas `to_sql` method into a table named `SwShSeries`. After, the dataset was saved into a .csv file for local use and examination.

For the visualization, we required the following information:

* Pokémon Name
* Legality
* Photo (parsed from link)
* Prices for the type of card (normal, holofoil, reverse holofoil)

For query purposes, we required the following additional information:

* Collector Number

For future expansion, we opted to keep the following additional fields: 

* Set ID
* Set Name
* Card ID
* Date (Newly created: indicates the datetime time stamp of when the database was updated)

Ultimately, we went from 24 columns of data to 9 columns of data. The database would then be usable to query a specific entry or entries in order to further narrow down what information can be used to present to the user.

We further used AWS Buckets for the purpose of hosting Uniform Resource Identifiers (URI) as a temporary location to pass to later described parts of the process. AWS was accessed using the Boto3, the AWS SDK for Python. 

#### Database Future Development

For prototyping, the database is also only setup to contain one entry of each Sword and Shield Series card however using the date field, it would be possible to have one of the columns of data is a generated Datetime field. In further development, the database could hold more than one entry of each Sword and Shield Series card and be scripted to pull regularly from the Pokemon TCG API to create a log of prices by date. Further expansion would include adding additional vendor sourcing and other API pulls. The Pokemon TCG API specifically uses pricing information from TCGPlayer.com. The database could also be scripted to delete entries beyond a certain date threshold in attempts to keep the database slim.

### Machine Learning Model

* Tesseract OCR (Optical Character Recognition)
* TensorFlow
* OpenCV
* Google Cloud Vision
* RegEx

The proof of concept prototype used Google Cloud Vision to detect and read text from the uploaded card still frame. For this process, the user's uploaded still frame image would be uploaded to AWS's Bucket, then the image URI would be sent as a request to Google Cloud Vision's API. On return of a response, the JSON was deciphered and the ideal was the whole card's text would be able to be read. If unable to be read, the script would return an error which would be displayed to the user. Assuming the text was all read, RegEx was used to filter out the collector number from the text of the card since the collector number holds a unique set of patterns.

#### Further Development & Experimented Tie-ins

We had initially and additionally attempted to create a custom learning model however ran into resource capability difficulties. The intention for machine learning use in this project was to train a deep neural network for object detection for a Pokemon TCG card within a still image. The technology opted for proof of concept for this was Tensorflow, an open source platform for machine learning. Upon being able to detect the card, the image would then be subjected to processing through cropping the image around the detected object. The intention from there is to further zooming in to a certain pixel height/width size while maintaining aspect ratio. A correctional rotation can then be applied should the card in the still frame not be dead on. The image may be further cropped at this point and zoomed in again. These three steps are within the capabilities of OpenCV, the technology opted to try for this project and a library of programming functions aimed towards computer vision. This step may or may not be necessary depending on the competency of optical character recognition (OCR), which is another form of machine learning. However, before OCR is done, a region of interest could be trained on the newly cropped and zoomed image using Tensorflow as a platform and OpenCV backing it up since OpenCV supports model execution for machine learning. The region of interest we were interested in would be the lower 10-15% of the card in modern Pokemon TCG cards. Specifically, the lower 10-15% of a card contains the collector number and set symbol used to identify it. The set symbol could be compared using OpenCV’s image differences and scored using a reference of trained set symbol images. Alternatively, the set symbol could be detected using object detection models through Tensorflow. Similarly, using Tensorflow and OpenCV, it would be possible to object and pattern detect for the collector number, as in modern Pokemon TCG cards, the set symbol is located next to the collector number. While vintage cards may not follow this same pattern, the possibility to expand the machine learning aspects to include the identification of collector numbers and set symbols would not be beyond the realm of possibility. Finally, once the collector number location has been identified, OCR is required to obtain a queryable string for the database. Tesseract, an open source OCR engine and application of machine learning, was experimented with for the OCR portion. The scope of the layered machine learning described above is complex but within reason due to being able to break the process down into smaller steps. However, the difficulty encountered during the execution of the project was partially resource based. Even with the included use of the GPU, the personal machine used to attemptran out of memory while attempting to train 50 sample images resulting in an incomplete model that could not be used for evaluation. There were also errors involving windows access denial. Unfortunately due to these circumstances, the machine learning aspect of the project had to settle for something more readily available as opposed to attempting to custom train an object detection model. 

### Visualization

* Python Flask
* HTML
* CSS
* Javascript
* Jinja2

We opted for Flask implementation which required HTML, Javascript, CSS, and Jinja2. Further to that, we used SQLAlchemy, Boto3, to connect our Flask application to the database and storage to provide a URI to the Google Cloud Vision API. The low level proof of concept visualization is to present the high resolution image of the card being scanned/taken-the-still-image-of as well as have drop down selection dynamically built using Javascript to display what the prices of the cards are. The visualization via HTML would be built with mobile in mind. This is because the app’s common use case scenario would be to be combined with an on-machine camera like a mobile device. In order to only display what is desired, the database would need to be queried and entries narrowed down via SQLAlchemy queries.

#### Future development

By expanding the database, the app could include a graph plotting the prices as a graph over time assuming the database were further developed in the mentioned methods in aforementioned description. Additional plots could be made per vendor if the database were to be expanded to include other vendors.

### Presentation

- [Google Slides](https://docs.google.com/presentation/d/1qF4vChUlj-rcls2imSxiKIAQhV3nn66cnlHZGZnHb6g/edit?usp=sharing)

Google Slides was used to create the group presentation as it allows for collaboration from multiple participants. Images were sourced from Google Image searches in order to increase the visual appeal of the presentation. Most visuals are of Pokémon from the Sword & Shield Series to align with the app's current capabilities.

![PokeScanner](/Resources/slides/PokeScanner.png)

### Demo

Attached is a gif of the app in demo. Due to the capture process, there was some delay in speed and responsiveness of the machine the app was being demo'd off of. 

![demo](/Resources/demo.gif)

### Flow Chart of App

![appflow](/Resources/AppFlowChart.png)

To delve deeper into the flow of the app, the above flow chart represents the steps and communications the app takes between databases and API's where the steps are labelled above and described below.

1. User opens app; app sends request from host server (GET request)
2. App responds with home page
3. User uploads image via a POST request. The app recognizes the POST request has occured and has an `if` block
4. The uploaded image is passed and uploaded into S3 Buckets
5. URI for the image in the Bucket is created and passed back to the app.
6. The app passes this URI to Google Cloud Vision API.
7. Google Cloud Vision API responds. The app's internal script takes the response and filters out what is needed for the database querying (ie: The collector number)
8. The home page redirects to the Visualization page passing along the collector number as the query string.
9. Visualization flask runs query from database using the query string
10. The Database returns an entry where the Visualization takes the response assigns the returned data as a dictionary for the HTML and Javascript to use.
11. The HTML and Javascript take the information from the Flask and presents it to the user.
