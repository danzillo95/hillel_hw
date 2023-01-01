from urllib import parse
from http.cookies import SimpleCookie


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
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {k: v.value for k, v in cookie.items()}
    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('Hello world!') == {}
    assert parse_cookie('age=28;') == {'age': '28'}
    assert parse_cookie('__age=28;') == {'__age': '28'}
    assert parse_cookie('age=28; nthng= ;') == {'age': '28', 'nthng': ''}
    assert parse_cookie('_=_;') == {'_': '_'}
    assert parse_cookie('ckpf_ppid_safari=a271b829cc244d5c94faae14f73f34df; ckpf_ppid_safari=21ebcecf7ab7400483c654469c6b24fb; ecos.dt=1600401456420; ecos.dt=1600401456208; _em_vt=99882dac-6513-43f6-877f-4f53766e67e5-1749f19f996-5ca2782f; __gads=ID=a42c30d38b4350e3-227e540a95c3001b:T=1600399634:RT=1600399634:S=ALNI_MZ1UNYRqcXwTpGQPoMqq9sATyF6wg; _cb=Z6cFZqJKjWDvIPNE; _chartbeat2=.1600397040609.1600399633336.1.Bym-CVCpzqLyBCabklBCyznkC-mw7l.1; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22b8d29b9f-6075-4bb9-983a-36e64c3904d2%22%2C%22options%22%3A%7B%22end%22%3A%222021-10-20T03%3A27%3A12.114Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atuserid={%22val%22:%22b8d29b9f-6075-4bb9-983a-36e64c3904d2%22}; _cc_dc=2; _cc_id=b58f5f5f6411e8ab29f7d1086bd0409a; ckns_sa_labels_persist={}; ckpf_ppid=7b5b127c65d24d939298eb61b7b9a08f; ckns_orb_fig_cache={%22ad%22:1%2C%22ap%22:0%2C%22ck%22:0%2C%22eu%22:0%2C%22uk%22:0}; ckns_explicit=1; ckns_policy=111; ckns_policy_exp=1631933129982; ckns_sscid=4430f388-f05f-48ff-9aba-b4837297d7a1; _cb_ls=1; ckns_privacy=july2019') == {'ckpf_ppid_safari': '21ebcecf7ab7400483c654469c6b24fb', 'ecos.dt': '1600401456208', '_em_vt': '99882dac-6513-43f6-877f-4f53766e67e5-1749f19f996-5ca2782f', '__gads': 'ID=a42c30d38b4350e3-227e540a95c3001b:T=1600399634:RT=1600399634:S=ALNI_MZ1UNYRqcXwTpGQPoMqq9sATyF6wg', '_cb': 'Z6cFZqJKjWDvIPNE', '_chartbeat2': '.1600397040609.1600399633336.1.Bym-CVCpzqLyBCabklBCyznkC-mw7l.1', 'atuserid': '{%22val%22:%22b8d29b9f-6075-4bb9-983a-36e64c3904d2%22}', '_cc_dc': '2', '_cc_id': 'b58f5f5f6411e8ab29f7d1086bd0409a', 'ckns_sa_labels_persist': '{}', 'ckpf_ppid': '7b5b127c65d24d939298eb61b7b9a08f', 'ckns_orb_fig_cache': '{%22ad%22:1%2C%22ap%22:0%2C%22ck%22:0%2C%22eu%22:0%2C%22uk%22:0}', 'ckns_explicit': '1', 'ckns_policy': '111', 'ckns_policy_exp': '1631933129982', 'ckns_sscid': '4430f388-f05f-48ff-9aba-b4837297d7a1', '_cb_ls': '1', 'ckns_privacy': 'july2019'}
    assert parse_cookie('    name   =  Dima   ;') == {'name': 'Dima'}
    assert parse_cookie('=;') == {}
    assert parse_cookie('tasty_cookie=strawberry') == {'tasty_cookie': 'strawberry'}
    assert parse_cookie('tasty_cookie=strawberry=;test=;;') == {'tasty_cookie': 'strawberry=', 'test': ''}










