from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import sys


def get_letters(soup):
    letters_elements = soup.find_all("ul", {"class": "list list-icons list-primary list-icons-style-2"})
    letters = []
    for letter in letters_elements:
        try:
            letters.append(letter.find('a').contents[0])
        except (AttributeError, IndexError):
            continue
    return "Cartas: " + ', '.join(letters)


def get_sunrise_and_sunset_time(soup):
    try:
        result = f"Nascer do sol: {soup.sunrise.contents[0]}\nPôr do sol: {soup.sunset.contents[0]}"
    except (AttributeError, IndexError):
        result = f"Nascer do sol: Não encontrado\nPôr do sol: Não encontrado"
    return result


def get_metar_and_taf(soup):
    elements = soup.find_all("h5", string=["TAF", "METAR"])
    result = {}
    for element in elements:
        try:
            p = element.find_next()
            result[element.contents[0]] = p.contents[0]
        except IndexError:
            result[element.contents[0]] = 'Não encontrado'

    return f"TAF: {result.get('TAF', 'Não encontrado')}\nMETAR: {result.get('METAR', 'Não encontrado')}"


def code_was_found(soup):
    """Returns True for a valid code"""
    obj = soup.find("div", {"class": "alert alert-danger"})
    if obj:
        return not any(['não foi encontrado' in content for content in obj.contents])
    return True


def main(code):
    url = f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={code}"
    request = Request(url)
    try:
        html_page = urlopen(request, timeout=20).read()
        soup = BeautifulSoup(html_page, 'html.parser')
        if code_was_found(soup):
            letters = get_letters(soup)
            sunrise_and_sunset_time = get_sunrise_and_sunset_time(soup)
            metar_and_taf = get_metar_and_taf(soup)
            return f'{sunrise_and_sunset_time}\n{letters}\n{metar_and_taf}'
        return "Aeródromo não encontrado."
    except Exception as e:
        return f"Ocorreu um erro ao ler a página: {str(e)}."


if __name__ == '__main__':
    try:
        icao_code = sys.argv[1]
    except IndexError:
        icao_code = None
    if icao_code:
        print(main(icao_code))
    else:
        print("Código ICAO não foi informado.")









