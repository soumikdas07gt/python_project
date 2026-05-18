
import requests
import pandas as pd 
import io

class test_Practice:
    def __init__(self):
        print("check practice session")
        self.url = "https://public.karat.io/content/students.txt"
        response = requests.get(self.url,
                               verify = False,
                               timeout = 10
                               )
        header = ["Date","ID","subject","score"]
        print(response.text)
        test_df = pd.read_csv(io.StringIO(response.text),sep=",", 
                              names=header)
        # test_df[test_df["score"]] = test_df["score"].astype(int)
        test_df["rank"] = test_df.groupby("ID")["score"].rank(method = "dense", ascending = False)
        test_df.sort_values(by=["ID","rank"], inplace = True)
        print(test_df.dtypes)
        top_records_df = test_df[test_df["rank"]==1]
        print(top_records_df)
        # print(test_df[test_df["ID"]==61])


if __name__ =="__main__":
    test_Practice()
