import requests
import pandas as pd
import io

class url_count:
    def __init__(self):
        print("Import URL count class")
        self.url = "https://public.karat.io/content/referrals_4.txt"
        response = requests.get(url = self.url,
                                verify = False,
                                timeout =10)
        url_df = pd.read_csv(io.StringIO(response.text), names=["url_list"])
        url_df["domain_0"]=url_df["url_list"].str.replace("http://","").str.replace("https://","")
        url_df["domain_1"] = url_df["domain_0"].str.split("/").str[0]
        domain_count = url_df.groupby("domain_1").size().reset_index(name="cnt").sort_values(by="cnt", ascending=False) 
        print(url_df.head())
        print(domain_count.head())

if __name__ == "__main__":
    url_count()