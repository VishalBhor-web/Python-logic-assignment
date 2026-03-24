1.Query parameters are key-value pairs added to aURL to send extra  information to the server.They come after a ? and are 
seperated by &.
In our code when we pass params=params  
Python converts it  into
https://api.github.com/search/repositories?q=python&sort=stars&order=desc&per_page=5

Without query parameter ,API wouldnt knnow what to search,how to sort,how many result we want.


2.response.json converts response into a python dictionary
response.text returns response in a string.We get plain text and is  not uable like a dictionary.

