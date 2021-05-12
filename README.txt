The following packages need to be installed using pip through command line :
    - robin_stocks
    - beautifulsoup4
    - gspread
    - pyyaml
    - oauth2client



A credentials.yml file needs to be created and placed at the root with the following format :
---------------------------------------------------------------------------------------------
    user:
        email: "Your email"
        password: " Your Password"
        key: "Your Robinhood mfa key"
---------------------------------------------------------------------------------------------
The credentials.yml file contains your login credentials for Robinhood.



Need to go to the google dev console and install the google drive api and the google sheets api.

Go to manage google drive api and create a service account.

Then take the email that the service account created and add it to the share list of the google
sheet that you want to access.

Go to manage google drive api and create credentials and name it "robinhood-webscraper-key".

Add "robinhood-webscraper-key.json" to root of project.