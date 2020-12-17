# Google-Sheets-API-Python
 
Using Google Sheets With Python
If you are looking for a lightweight, easy to use and cheap database for small hobby projects google sheets might be the thing for you. This tutorial will show you how to use google sheets with python as a simple database.

Setup
There are a few steps that need to be followed to start using the google sheets API.

– Create a project on google cloud console
– Activate the google drive API
– Create credentials for the google drive API
– Activate the google sheets API
– Install a few modules with pip
– Open the downloaded json file and get the client email
– Share the desired sheet with that email
– Connect to the google sheet via python code

Creating a New Project on Google Cloud
Go to the following link and create a new project https://console.cloud.google.com/.

Watch the video for detailed instructions…

Adding the API’s
Now we need to add the following API’s :

– google drive
– google sheets

Once you add the google drive API it will ask you to create credentials. Follow the steps and you should see a JSON file gets downloaded. SAVE THIS FILE.

Sharing the Sheet
Open up the json file that was downloaded earlier and find the client email. Copy the email and share your google sheet with that email address.

Install Modules via pip
Then next step is to install the following modules using pip.

– gspread
– oauth2client

This can be done by running the following command in cmd: pip install gspread oauth2client
