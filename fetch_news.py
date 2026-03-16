import urllib.request
import urllib.parse
import re
import sys

def search_ddg_html(query):
    encoded_query = urllib.parse.quote(query)
    # df=d means past day
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({
        'q': query,
        'df': 'd',
        'ia': 'news'
    }).encode('utf-8')
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        req = urllib.request.Request(url, data=data, headers=headers) # POST because data is present
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
        print(html)
        sys.exit(0)



    except Exception as e:
        return [f"Error: {str(e)}"]

if __name__ == "__main__":
    query = "US Iran conflict news"
    if len(sys.argv) > 1:
        query = sys.argv[1]
    
    hits = search_ddg_html(query)
    for i, hit in enumerate(hits, 1):
        if isinstance(hit, dict):
            print(f"{i}. {hit['title']}")
            print(f"   {hit['link']}")
            print(f"   {hit['snippet']}\n")
        else:
            print(hit)
