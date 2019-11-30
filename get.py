from urllib.request import urlopen
from urllib.request import Request
import datetime
import json


def get_statistics(owner, name, headers):
    url = 'https://api.github.com/repos/{owner}/{name}/stats/contributors?page=2&per_page=100'.format(owner=owner,
                                                                                                      name=name)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    if len(response) == 0:
        return response
    else:
        result = json.loads(response.decode())
        return result


def get_results(search, headers):
    url = 'https://api.github.com/repos/jumpserver/jumpserver?q={search}&page=1&per_page=100&sort=stars&order=desc'.format(
        search=search)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = json.loads(response.decode())
    return result


if __name__ == '__main__':

    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'token 6e410d73e64c4dc9afde648281e90032f35dee8f',
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }

    search = 'languages'

    results = get_results(search, headers)

    x = open('language.json', 'w', encoding='utf-8')
    x.write(json.dumps(results, ensure_ascii=False) + '\n')


    search = ''

    results = get_results(search, headers)
