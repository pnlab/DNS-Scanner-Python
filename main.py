# Import libraries
import dns.resolver
import tldextract
from urllib.parse import urlparse


def parse_url(s):
    extracted = tldextract.extract(s)
    return "{}.{}".format(extracted.domain, extracted.suffix)

def get_txt(domain):
    try:
        res = []
        answers = dns.resolver.query(domain, 'TXT')
        for rdata in answers:
            res.append(rdata.to_text())
        return res
    except:
        return None

url = "https://2k1.org"
domain = parse_url(url)
print(domain)

print(get_txt(domain))


res = {}

with open('domain.txt','r') as f:
    a = f.readlines()
    for u in a:
        url = u.strip()
        domain = parse_url(url)
        res[domain] = get_txt(domain)
        print(domain, res[domain])

with open('result.txt','w') as f:
    for k,v in res.items():
        f.write(k+'\n')
        if v:
            for i in v:
                f.write(i+'\n')
        else:
            f.write('No TXT record\n')
        strs = '='*10 + '\n'
        f.write(strs)