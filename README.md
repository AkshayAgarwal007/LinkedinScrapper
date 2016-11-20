# LinkedinScrapper

LinkedinScrapper searches linkedin pages using executive’s name, title, firm and get his / her best matching linked profile and extracts basic information of each individuals from their linkedin profile. 

The linkedinAPI sub-module provides a Python interface to the LinkedIn People REST API used to fetch Linkedin member information.

*Note: The information can be fetched only for those users who would provide this app an authorization to do so through a dialog portion and not for all Linkedin member profiles. (The same can be done by getting vetted access by applying for Linkedin partner program)*

## Techniques Used

Since the Linkedin people search API is closed now (more details [here](https://developer.linkedin.com/support/developer-program-transition)) searching for best matching profile is a liitle tricky.

The same is achieved here in the simplest and best possible way but still holds huge chances of improvement. It is based upon the following assumptions based upon empirical evaluation:

* Google is the best for Linkedin X-Ray Search.
* After using relevant search operators and putting in the right queries the first link is the most relevant link to the required user's profile.
* In the worst case it may be the 5th ranked link and if not the required person is possibly not on Linkedin or we may be searching with the wrong details.
* We should atleast have the person's (name, position and the company) he works in or some other information to form a well formed query which can isolate the required profile with tons of other profile with the same name.

After this we get the best matching profile url by simply comparing the extracting the name from the title of each result in Google search and then comparing it with the name (profile we're searching for) using [difflib](https://docs.python.org/2/library/difflib.html) (python module used for sequence matching)

Lastly we scrap the relevant information from the best matched Linkedin profile URL. 

Querying google and scrapping search results has been automated using Selenium and the Firefox webdriver. Scrapping of Linkedin profile has been automated via Selenium and Phantom JS. I used Selenium instead of traditional tools like requests/urllib in order to avoid the captcha blocking. Also because of lot of JavaScript and dynamic content on LinkedIn Selenium is a better scrapper than traditional tools and also it would be easier to extend this to automate authentication (there might be a requirement for this).

## How to Use?

### Profile Searching and Scrapping

1. Run extractProfileUrl.py by providing the path to the input excel file as a command line argument. A sample input file is there inside the **sampleIOfiles** folder.

        python extractProfileUrl.py fileName.xlsx 
   
   The output would be a json file (urls.json) containing Linkedin profile urls.
   
2. Run profScraper.py.

        python profScraper.py 
   
   The output would be a json fie (all_profiles.json) containing the profile information corresponding to each url.
   
### Using LinkedinAPI

#### Authentication

LinkedIn REST API uses Oauth 2.0 protocol for authentication. In order to use the LinkedIn API, you have an application key and application secret. You can get more detail from [here](https://developer.linkedin.com/docs/oauth2).

    API_KEY = '**replace this with your api key**'
    
    API_SECRET = '**replace this with your api secret**'

    RETURN_URL = '**replace this with your callback url**

After the filling the api keys and the call back url run **authcode.py**. An authorization link will be copied to your clipboard. Open a browser and paste it in the URL bar and you'll go through a dialog portion to authorize the application. 

Aftr you grant access you will be redirected to the return url with the following query strings appended to your RETURN_URL:

    http://localhost:8000/?code=authorization_code

Copy the authorization code and place it inside **accessToken.py**

    authentication.authorization_code = '**replace this with your authorization code**

After than execute accessToken.py. The access token will be saved in token.txt and will be read from there to make API calls. The access token expires is 60 days and the authorization process have to be repeated again to regenerate the access token.

During the refresh workflow, provided the following conditions are met, the authorization dialog portion of the flow is automatically skipped and the user is redirected back to your callback URL, making acquiring a refreshed access token a seamless behind-the-scenes user experience:

* The user is still logged into www.linkedin.com
* The user's current access token has not expired

If the user is no longer logged in to www.linkedin.com, or their access token has expired, they will be sent through the normal authorization process

Finally execute **profile.py** with the required selectors by modifying the code to get the basic profile details. 


### External Dependencies

* Selenium
* Clipboard (for using the Linkedin API code)

You also need to have Firefox web driver and PhantomJs set in your environment path.

### Sample output

``` urls.json ``` (list of urls)

["https://www.linkedin.com/in/masoncdm", "https://www.linkedin.com/in/masoncdm", "https://www.linkedin.com/in/masoncdm", null]


``` sample_profile.json ``` (profile information)

Try to view the contents of the above file using this tool http://jsonviewer.stack.hu/. This will give you an idea of the fields that are scrapped from the profile.

Based on this you can write a small piece to either dump the information to an excel sheet or make a small Flask web app to view the scrapped JSON information in prettified way  

### Possible Improvements:

* Linkedin profile URL scoring.
* optimizing the Scrapping.
* bypassing possible blocks on the bot.
* using thread or async ios to make parallelize scrapping URL and extracting profile information.
   



