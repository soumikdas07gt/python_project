"""
2021-05-07 00:01:30.034 Block 74.152.237.66
2021-05-07 00:05:05.984 Block 79.118.67.43
2021-05-07 00:05:52.435 Block 183.35.232.214
2021-05-07 00:13:08.376 Release 74.152.237.66
2021-05-07 00:15:23.802 Block 157.152.167.232
2021-05-07 00:16:46.374 Block 190.96.92.169

fnd the block list of URLs 
block: 5
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
        self.api_url = "https://public.karat.io/content/test/test_log.txt"
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
            print(lines[:5]) ## check the top 5  
            v_action = []
            for each_line in lines:
                parts = each_line.split() ## split line with space
                action = parts[2]
                ip = parts[3]
                v_action.append(action)
            cnt = Counter(v_action)
            print(cnt)
            for action, cnt in cnt:
                print(f"{action}: {cnt}")

            return None
   
        except Exception as e:
            logger.error(f"API data process failed: {e}")       


# to instantiate we need this 
if __name__ == "__main__":
    testProgram()