# webscraping_winterschool
This final project for the VU winter school makes use of BeautifulSoup and Pandas in order to do the following:
1) pubmed_webscraping_v.0.2.py fetches a pubmed search page and creates a csv file with Authors, Title, Journal, Abstract and Keywords
2) pandas_author.py counts the frequencies of author names and plots a graph of the 10 most published authors within that search
3) pandas_interest.py checks certain words present in the keywords and sorts the spreadsheet by interest (e.g. I defined papers with "photometry" to have +10 interest and "miniscope" to have +20 interest)

How to adapt the code?
1) On pubmed_webscraping_v.0.2.py: 
- Adapt the xml search By right-clicking on Google chrome, it is possible to select “Inspect” and hover over elements of a website. When you click it, you will be able to see the xml structure.
- Adapt the looping index If your website has an index page at the end (e.g. www.site.com/page/1), you can just copy the entire link up to the page number (e.g. www.site.com/page/) and replace it on the source = requests.get() line; if your website has an index page in the middle (e.g. www.site.com/something/1.html), you should concatenate the string using the following syntax:

2) On pandas_interest.py:
- Change the keywords and the interest values to whatever seems appropriate to your search.
