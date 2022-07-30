import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
from tqdm import tqdm
def main():
    ids = pd.read_csv("C:/Users/29616/Downloads/打杂/biomap/protabank/prop_Gibbs_ids.tsv",sep='\t')
    for i in tqdm(range(len(ids))):
        id = ids.loc[i,'ids']
        url = f'https://www.protabank.org/study_analysis/{id}'
        print(url)
        web_data = requests.get(url)
        # 设为utf-8编码，预防乱码
        web_data.encoding = 'utf-8'
        # print(web_data.text)
        soup = BeautifulSoup(web_data.text, 'html.parser')
        submission_date = soup.select('#gi-container > div.row.gi-body > div:nth-child(1) > p:nth-child(6)')
        print(submission_date)
        submission_date = str(submission_date).split('Date:')[1]
        submission_date = str(submission_date).split('</p>')[0]
        print(submission_date)
        ids.loc[i,'submission_date'] = submission_date
    ids.to_csv("C:/Users/29616/Downloads/打杂/biomap/protabank/prop_Gibbs_ids_subdate.tsv",sep='\t')

if __name__ == '__main__':
    main()