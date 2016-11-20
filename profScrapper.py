import json
from LinkedinController import LinkedinController
import json

def main():
    profile_data={}

    linkedinTool = LinkedinController()

    with open('urls.json') as data_file:    
        urls = json.load(data_file)
    for url in urls:
        if url is not None:
            profile = linkedinTool.extractProfile(url)
            profile_data[url]=profile
            print json.dumps(profile, indent=4, sort_keys=True)

    with open('all_profiles.json', 'w') as outfile:
        json.dump(profile_data, outfile)
        
if __name__ == "__main__":
    main()
    