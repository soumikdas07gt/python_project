""" 
find most use urls : 
http://world.news.yahoo.com/news/olympics/
https://store.apple.com/iphone/
http://en.wikipedia.org/wiki/?lang=en
http://blog.example.com/articles/
https://developer.github.com/docs/api/v3/
https://stackoverflow.com/questions/?sort=votes
https://gist.github.com/code/
http://en.wikipedia.org/wiki/?lang=fr
https://store.apple.com/ipad/
http://example.com/products/
https://www.nps.gov/parks/
https://www.nps.gov/trails/

we can use counter 
items = ["a", "b", "a", "c", "b", "a"]
counts = Counter(items)
print(counts) 
c.most_common() --> descendig orer 

Counter({'a': 3, 'b': 2, 'c': 1})


"""

import requests
import logging
from urllib.parse import urlparse
from collections import Counter



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

class testProgram(): 
    
    def __init__(self) -> None :  
        logger.info("Inside init section")
        self.api_url = "https://public.karat.io/content/referrals_4.txt"
        self.api_service()     
        # api_data_list, hits = self.api_service()
        # self.api_data_process(api_data_list)

    def api_service(self):
        try:
            logger.info("inside the api_service method")
            logger.info(f"Paring URL :{self.api_url}")
            self.response = requests.get(
                    self.api_url ,
                    verify=False,  ## never recommended for prod code 
                    timeout=10
                        )
            
            logger.info(f"Paring URL done :{self.api_url}")
            lines = self.response.text.splitlines()  # convert to list
            v_domain = []
            for each_line in lines:
                d_domain = urlparse(each_line).netloc
                v_domain.append(d_domain)     # appended to a list variable
            v_domain.sort(reverse=True)
            domain_counts = Counter(v_domain)
            
            for domain, count in domain_counts.most_common():  ## printing in reverse order most_common()
                print(f"{domain}: {count}")

            return None
   
        except Exception as e:
            logger.error(f"API data process failed: {e}")       


# to instantiate we need this 
if __name__ == "__main__":
    testProgram()
