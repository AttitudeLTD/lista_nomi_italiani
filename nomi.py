from bs4 import BeautifulSoup
import urllib.request
import codecs

def get_nomi(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        names = []
        for td in soup.find_all('td'):
            a = td.find('a')
            if a and a.has_attr('title'):
                names.append(a['title'][20:].strip())
            else:
                names.append(td.text.strip())
        return names

def process_names():
    letters_to_urls = {
        'A': 'https://www.nomix.it/nomi-italiani-maschili-e-femminili.php',
        'B': 'https://www.nomix.it/nomi-italiani-lettera-B.php',
        'C': 'https://www.nomix.it/nomi-italiani-lettera-C.php',
        'D': 'https://www.nomix.it/nomi-italiani-lettera-D.php',
        'E': 'https://www.nomix.it/nomi-italiani-lettera-E.php',
        'F': 'https://www.nomix.it/nomi-italiani-lettera-F.php',
        'G': 'https://www.nomix.it/nomi-italiani-lettera-G.php',
        'I': 'https://www.nomix.it/nomi-italiani-lettera-I.php',
        'L': 'https://www.nomix.it/nomi-italiani-lettera-L.php',
        'M': 'https://www.nomix.it/nomi-italiani-lettera-M.php',
        'NO': 'https://www.nomix.it/nomi-italiani-lettera-NO.php',
        'PQ': 'https://www.nomix.it/nomi-italiani-lettera-PQ.php',
        'R': 'https://www.nomix.it/nomi-italiani-lettera-R.php',
        'S': 'https://www.nomix.it/nomi-italiani-lettera-S.php',
        'TUV': 'https://www.nomix.it/nomi-italiani-lettera-TUV.php',
        'WZ': 'https://www.nomix.it/nomi-italiani-lettera-WZ.php',
    }

    all_names = []
    for letter_group, url in letters_to_urls.items():
        print(f"Processing {letter_group}...")
        names = get_nomi(url)
        all_names.extend(names)
    
    with codecs.open('italian_names.txt', 'w', encoding='utf-8') as file:
        for name in all_names:
            file.write(name + '\n')

if __name__ == '__main__':
    process_names()
    print("Completed. All names are saved in italian_names.txt.")
