"""
157,Kelly,a wrinkle in time,50
231,Selina,to kill a mockingbird,300
74,Juan,to kill a mockingbird,300
558,Elysse,hush hush,200

book count: 4
page count : 850
"""


import logging as log
import requests

log.basicConfig(
    level=log.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = log.getLogger(__name__)

class pythonPractice():
    def __init__(self):
        try:
            log.info("Starting program ")
            self.url = "https://public.karat.io/content/test/test_file.txt"
            response = requests.get(self.url, verify = False, timeout=10)
            lines = response.text.splitlines()
            print(lines[:5]) ## sample check 
            no_of_books = len(lines)
            print(no_of_books)
            total_pages = 0
            for i in lines: 
                parts = i.split(",")
                pages = int(parts[3])
                total_pages = total_pages + pages  ##  adding line no with prev one 
                #print(f" ID: {parts[0]} -- Reader_name: {parts[1]} --  Book_name: {parts[2]} -- Pages: {parts[3]} ")
            
            print(f"total_books:  {no_of_books} ---  total pages read: {total_pages}")

        except Exception as e :
            log.error(f"code failed {e}")




if __name__ == "__main__":
    pythonPractice()