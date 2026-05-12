""" https://public.karat.io/content/referrals_4.txt -->    
    http://world.news.yahoo.com/news/olympics/  --> {'host': 'world.news.yahoo.com', 'domain': 'yahoo.com'}
    https://store.apple.com/iphone/  -->  {'host': 'store.apple.com', 'domain': 'apple.com'}
"""

import requests
import logging
from urllib.parse import urlparse
from publicsuffix2 import get_sld, get_tld


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

class testProgram(): 
    
    def __init__(self) -> None :  
        logger.info("Inside init section")
        self.api_url = "https://public.karat.io/content/referrals_4.txt"        
        api_data_list = self.api_service()
        self.api_data_process(api_data_list)

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
            
            return lines
        except Exception as e:
            logger.error(f"API call failed: {e}")

    def api_data_process(self, data):
        try:
            d_domain = []
            logger.info("processing data initiated")
            print(type(data))
            for lines in data:
                d_parsed = urlparse(lines)   ## this will come as  ParseResult(scheme='https', netloc='www.britishmuseum.org', path='/collections/', params='', query='', fragment='')
                if d_parsed.netloc:
                    # d_domain.append(d_parsed.netloc)                    
                    sld = get_sld(d_parsed.netloc)  # second level domain 
                    tld = get_tld(d_parsed.netloc)  # top level domain
                    base_domain = sld if sld else tld           # If SLD exists, use it; otherwise fallback to TLD
                    d_domain.append(                            # we are creating list of dictionaries like [{},{},{}]
                        { 
                            "host": d_parsed.netloc,
                            "domain":  base_domain
                        }
                    )
                    print(type(d_domain))
                    print(d_domain)
        
        except Exception as e:
            logger.error(f"API data process failed: {e}")       


# to instantiate we need this 
if __name__ == "__main__":
    testProgram()
