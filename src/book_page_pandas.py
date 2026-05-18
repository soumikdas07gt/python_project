import requests
import pandas as pd 
import io

class check_book_page:
    def __init__(self):
        print("check book_ session")
        self.url = "https://public.karat.io/content/test/test_file.txt"
        response = requests.get(self.url,
                                verify =False,
                                timeout=10)
        # print(type(response.text))
        header = ["student_id","student_name","book_name","Pages"]
        book_df = pd.read_csv(io.StringIO(response.text),
                                          sep = ",",
                                          names = header
                                )
                                
        print(book_df.head())
        """
        select count(book_name),sum(pages)
        from book_df
        """
        book_count = book_df[['book_name', 'Pages']].agg(
                    {
                            'book_name': 'count',
                            'Pages': 'sum'
                        }                    
                    )
        print(book_count)
        
if __name__ =="__main__":
    check_book_page()