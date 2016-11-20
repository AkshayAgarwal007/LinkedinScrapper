from linkedin import linkedin


f = open("token.txt","r")
token_ = f.read().strip()
print (token_)
application = linkedin.LinkedInApplication(token =token_ )
print (application.get_profile(selectors=['id', 'summary', 'picture-url', 'positions', 'specialties','first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations']))
