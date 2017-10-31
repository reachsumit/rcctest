# rcctest
I made this Django project as part of a test assignment given by RCC, Uchicago. Project demonstrates a basic web app that updates a database in the back-end and displays results to the user on front-end. Web app is being hosted at: https://rcctest.herokuapp.com/.
___
## Project details
* For this project I scraped data of 570+ bikes from [this link](http://thebicyclechain.com/product-list/bikes-1000/) of [The Bicycle Chain](http://thebicyclechain.com/). 
* Scraping script (Python) and scraped data (csv) are both available in this source.
* Scraped data was then passed to a Python script that created a database on cleardb mysql server with this data. Script for this database submission is also attached.
* A Django [webapp](https://rcctest.herokuapp.com/) hosted on Heroku provides front-end for accessing this database.
* [Home page of the webapp](https://rcctest.herokuapp.com/) displays all the available bikes in the database in pagination format. 10 bikes per page are displayed.
* At the bottom of the page, there is a link to add new entries to the database. (NOTE: in current implementation, for saving image, user will have to provide direct image url).
* Each bike has it's own unique product description page.
* Each product description page has a delete option to delete the corresponding bike entry.
___
## Further Enahancements required
* Use javascript/css to enahnce user-experience and beautify the interface.
* Use Django's in-built authentication system to control access to database write/delete operations from front-end.
* Provide dynamic filtering of the catalogue view.
___
## Screenshots
### Home page
![Imgur](https://i.imgur.com/O8wiUHm.png)
### Product page
![Imgur](https://i.imgur.com/1Ak7RZM.png)
### Add new bike 
![Imgur](https://i.imgur.com/g4FmFCC.png)
