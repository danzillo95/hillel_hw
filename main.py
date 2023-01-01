from urllib import parse


def parser(url: str) -> dict:
    return dict(parse.parse_qsl(parse.urlsplit(url).query))


if __name__ == '__main__':
    assert parser('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parser('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parser('http://example.com/') == {}
    assert parser('http://example.com/?') == {}
    assert parser('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parser('https://example.com/?name=Dima&#hi') == {'name': 'Dima'}
    assert parser('https://example.com/path/to/page?name=ferret&color=purple&test=passed') == {'name': 'ferret', 'color': 'purple', 'test': 'passed'}
    assert parser('http://example.com/?name=&color=purple') == {'color': 'purple'}
    assert parser('http://example.com/?name=Dima=amiD') == {'name': 'Dima=amiD'}
    assert parser('Hello world!') == {}
    assert parser('http://example.com/?name=Dima=amiD') == {'name': 'Dima=amiD'}
    assert parser('example.com/?name=&color=purple') == {'color': 'purple'}
    assert parser('http://example.com/?name=Dima&gender=male') == {'name': 'Dima', 'gender': 'male'}
    assert parser('smth/?name=Dima&gender=male') == {'name': 'Dima', 'gender': 'male'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
