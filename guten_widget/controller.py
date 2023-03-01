"""controller.py will manage making API calls to the Gutendex and 
format the results for display."""

# import statements
import requests

#set some variables to help our API call
domain = "https://gutendex.com/"
endpoint = "books/?search="

# Make an API call
def make_call(query: str) -> str:
    """take the terms (of the search) and use it to make an API call
    then return formatted results or error if does not return a 200 code"""

    # create our url
    url = domain + endpoint + query

    # make the call
    response  = requests.get(url)
    print()

# get the top results (we don't want hundreds)

# format results