import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin

BASE_URL = "https://www.fons.org"
START_URL = "https://www.fons.org/library/journal-ipdj-home"
OUTPUT_DIR = "fons_knowledge_base"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def harvest():
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    print(f"🚀 Downloading FULL Library...")
    try:
        soup = BeautifulSoup(requests.get(START_URL, headers=HEADERS).text, "html.parser")
        links = [urljoin(BASE_URL, a['href']) for a in soup.find_all('a', href=True) if '/library/journal/volume' in a['href']]
        unique_links = list(set(links))
        
        count = 0
        for link in unique_links:
            try:
                issue_soup = BeautifulSoup(requests.get(link, headers=HEADERS).text, "html.parser")
                pdfs = [urljoin(BASE_URL, a['href']) for a in issue_soup.find_all('a', href=True) if '.pdf' in a['href']]
                for pdf in pdfs:
                    name = pdf.split('/')[-1]
                    name = "".join([c for c in name if c.isalpha() or c.isdigit() or c in '._-'])
                    path = os.path.join(OUTPUT_DIR, name)
                    if not os.path.exists(path):
                        content = requests.get(pdf, headers=HEADERS).content
                        if len(content) > 1000:
                            with open(path, 'wb') as f: f.write(content)
                            count += 1
                            if count % 5 == 0: print(f"   ⬇️  Downloaded {count} articles...", end="\r")
                        time.sleep(0.1)
            except: pass
        print(f"\n✅ Harvest Complete. Files: {len(os.listdir(OUTPUT_DIR))}")
    except Exception as e: print(e)
if __name__ == "__main__": harvest()
