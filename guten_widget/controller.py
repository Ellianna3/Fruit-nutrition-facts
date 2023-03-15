"""controller.py will manage making API calls to the Gutendex and 
format the results for display."""

# import statements
import requests

# example url: https://fruityvice.com/api/fruit/banana

#set some variables to help our API call
domain = "https://fruityvice.com/"
endpoint = "api/fruit/"

# Make an API call
def make_call(query: str) -> str:
    """take the terms (of the search) and use it to make an API call
    then return formatted results or error if does not return a 200 code"""

    # create our url
    url = domain + endpoint + query

    # make the call
    response  = requests.get(url)
    results = ""
    if response.ok:
        results = format_results(response)
    else:
        results = "There was an error. Please try later."
    return results

def format_results(results) -> str:
    """take results (a list), extract the info we need and return a 
    formatted string"""
    results = results.json()["nutritions"]
    formatted_results = "<ul>"
    #loop
    for nutrition, value in results.items():
        formatted_results += "<li><b>" + nutrition + "</b>: " + str(value) + "</li>\n"
    formatted_results += "</ul>"

    return formatted_results

if __name__ == "__main__":
    call_results = make_call("banana")
    print(call_results)