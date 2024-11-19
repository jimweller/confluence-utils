from atlassian import Confluence
import sys

confluence = Confluence(
    url='https://exampleco.atlassian.net',
    username="jim.weller@exampleco.com",
    password='YOURAPIKEY',
    cloud=True)


pages = confluence.cql("ancestor=2037940785", start=0, limit=None, expand=None, include_archived_spaces=None, excerpt=None)

for page in pages["results"]:
    print("FCC,\"" + page["title"] + "\",\"https://exampleco.atlassian.net/wiki/spaces/HFCH/pages/" + page["content"]["id"] + "\"")

pages = confluence.cql("ancestor=2089812035", start=0, limit=None, expand=None, include_archived_spaces=None, excerpt=None)
for page in pages["results"]:
    print("CF,\"" + page["title"] + "\",\"https://exampleco.atlassian.net/wiki/spaces/HFCH/pages/" + page["content"]["id"] + "\"")

pages = confluence.cql("ancestor=2019688522", start=0, limit=None, expand=None, include_archived_spaces=None, excerpt=None)
for page in pages["results"]:
    print("SEU,\"" + page["title"] + "\",\"https://exampleco.atlassian.net/wiki/spaces/HFCH/pages/" + page["content"]["id"] + "\"")
