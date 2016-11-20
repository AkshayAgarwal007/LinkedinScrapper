from linkedin import linkedin

API_KEY = '**replace this with your api key**'
API_SECRET = '**replace this with your api secret**'
RETURN_URL = '**replace this with your callback url**'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
authentication.authorization_code = '**replace this with your authorization code**'
token = authentication.get_access_token()
print ("The authentication token is\n" + token[0])
print ("\nWriting authentication token into token.txt...")
f=open("token.txt","w")
f.write(str(token[0]))
application = linkedin.LinkedInApplication(token)
