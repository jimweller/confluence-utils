from atlassian import Confluence
import sys

confluence = Confluence(
    url='https://exampleco.atlassian.net',
    username="jim.weller@exampleco.com",
    password='YOURAPIKEY',
    cloud=True)


page = confluence.get_page_by_id(page_id=2227667711, expand="body.storage", status=None, version=None)
#labels = confluence.get_page_labels(page_id=2227667711, prefix=None, start=None, limit=None)


#confluence.create_page(space="HFCH", title="JIM WAS HERE 2", body=status["body"]["view"]["value"], parent_id=2089451583, type='page', representation='storage', editor='v2', full_width=False)

title = sys.argv[1]

# personal
#page = confluence.create_page(space="~71202072dac46aa2cf405f81eb310fd06cf726", title=title, body=page["body"]["storage"]["value"], parent_id="2230255651", type='page', representation='storage', editor='v2', full_width=True)

# FCC
page = confluence.create_page(space="HFCH", title=title, body=page["body"]["storage"]["value"], parent_id="2230387004", type='page', representation='storage', editor='v2', full_width=True)
confluence.set_page_label(page_id=page["id"], label="cf-adr")

#print(page);

# shell command line
#cat seu.txt | while read i; do  python sprayer.py "$i";done
