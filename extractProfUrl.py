from difflib import get_close_matches
from fetchInput import fetch
from searchController import *
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', help="the excel file containing the input search data")
    return parser.parse_args()

def urlMatch(titles_urls, name):
    links = []
    titles= []
    for item in titles_urls:
        if "linkedin.com/in/" in item[1]:
            titles.append(item[0].split('|')[0].strip())
            links.append(item[1])
    if titles == []: return None
    elif len(titles)==1: return links[0]
    else:
        best_match = get_close_matches(name,titles,n=1)
        return links[titles.index(best_match[0])]

            
def main():
    args = parse_args()
    br = start_browser()
    searchList,names = fetch(args.inputfile)
    profile_urls = []
    
    for index, query in enumerate(searchList):
        go_to_page(br, query)
        titles_urls = scrape_results(br)
        if titles_urls == []:
            profile_urls.append(None)
        else:
            best_match = urlMatch (titles_urls, names[index])
            profile_urls.append(best_match)       
        
    for i in profile_urls:
        print '[+]  ' + str(i) 
        
    with open('urls.json','wb') as outputfile:
        json.dump(profile_urls,outputfile)

if __name__ == "__main__":
    main()
    
    
    
    
    
