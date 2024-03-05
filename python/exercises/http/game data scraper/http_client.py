# I will use requesets library because I don't see a need for async library like aiohttp
# and it's more user-friendly than urllib and http.client libraries
import requests

# Get the html page as text from the website:
def get_page_as_text(url) -> str:
    res = requests.get(url)
    return res.text