from requests import get
from bs4 import BeautifulSoup as BS


### ADD YOUR WORD HERE SURROUNDED BY QUOTES LIKE search_word = "YOU WORD HERE"
search_word = 'bleak'
####



def synonyms(word):
    res = get(f'https://www.merriam-webster.com/thesaurus/{word}')
    soup = BS(res.text, 'html.parser')
    vg = soup.select('.vg')

    lines = []

    vg_list = vg[0].text.split('\n')
    for index, element in enumerate(vg_list):
        line = element.strip()
        if line and index not in [2,4]:
            lines.append(line)

    # for index, line in enumerate(lines):
    #     if word not in line:
    #         if len(line) > 2:
    #             print(line)

    words = [word]

    for index, line in enumerate(lines):
        if word not in line:
            if len(line) > 2:
                split_line = line.split(',')
                if len(split_line) > 1:
                    for synonym in split_line:
                        words.append(synonym.strip())
    
    return words, word


def rhyme_scraper(word):
    words = []

    res = get(f'https://www.rhymezone.com/r/rhyme.cgi?Word={word}&typeofrhyme=nry&org1=syl&org2=l&org3=y')
    soup = BS(res.text, 'html.parser')
    rhyme_words = soup.select('.r')
    for i in rhyme_words[:6]:
        words.append(i.text)

    return words



words, first_word = synonyms(search_word)
with open(f'{first_word.title()}.txt', 'a') as file:
    file.write(f'\t\t{first_word.upper()}\n\n')
    for i in words:
        print(i)
        file.write(f'{i}\n')
        for rhyme in rhyme_scraper(i):
            print(f'\t{rhyme}\n')
            file.write(f'\t{rhyme}\n')