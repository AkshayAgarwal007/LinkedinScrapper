from linkedin import linkedin
import clipboard

API_KEY = '**replace this with your api key**'
API_SECRET = '**replace this with your api secret**'
RETURN_URL = '**replace this with your callback url**'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url  
f=open("auth.txt","w")
f.write(authentication.authorization_url)
clipboard.copy(authentication.authorization_url)
print ("\nCopied authorization code to clipboard...")
application = linkedin.LinkedInApplication(authentication)
