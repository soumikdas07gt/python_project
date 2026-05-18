import requests
import pandas as pd
import io

"""
convert tot PD 
use str. funcations for repalce http use str.replace 
and use str.split """

class url_Test:
    def __init__(self):
        print("URL parsing class initialized.")
        self.url = "https://public.karat.io/content/referrals_4.txt"
        response = requests.get(url = self.url,
                                verify = False,
                                timeout = 10
                                )
        # print(response.text)
        header = ["url_list"]
        url_df = pd.read_csv(io.StringIO(response.text),
                            #  sep="\n", 
                             names = header,
                             )
        url_df["domain_0"] = url_df["url_list"].str.replace("http://","").str.replace("https://","")
        url_df["domain_1"] = url_df["domain_0"].str.split("/").str[0]
        url_df["domain_2"] = url_df["domain_1"].str.split(".").str[-2:].str.join(".")  ## str[-2:] last two eleent and str.join concate them
        print(url_df.head(10))


if __name__ == "__main__":
    url_Test()