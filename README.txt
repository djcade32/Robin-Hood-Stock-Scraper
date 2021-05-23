The following packages need to be installed using "pip install -r requirements.txt" through command line:
    - robin-stocks
    - beautifulsoup4
    - pyyaml
    - openpyxl
    - keyring
    - pyyaml



A credentials.yml file needs to be created and placed at the root with the following format :
---------------------------------------------------------------------------------------------
    user:
        email: "Your email"
        password: " Your password"
        key: "Your Robinhood mfa key"
        workbookPath: "URL path to the excel sheet that will be populated"
---------------------------------------------------------------------------------------------
The credentials.yml file contains your login credentials for Robinhood.
