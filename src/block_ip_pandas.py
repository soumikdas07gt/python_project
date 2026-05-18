
import requests
import pandas as pd 
import io

class test_Practice:
    def __init__(self):
        print("check practice session")
        self.url = "https://public.karat.io/content/test/test_log.txt"
        response = requests.get(self.url,
                               verify = False,
                               timeout = 10
                               )
        header = ["Timestamp","Status","IP"]
        test_df = pd.read_csv(io.StringIO(response.text),sep=" ", 
                              names=header)
        print(test_df.head())
        group_df = test_df.groupby('Status').size().reset_index(name = "cnt")        
        print(group_df[group_df["Status"] == "Block"])       


if __name__ =="__main__":
    test_Practice()