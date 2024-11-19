from atlassian import Confluence
import sys

confluence = Confluence(
    url='https://exampleco.atlassian.net',
    username="jim.weller@exampleco.com",
    password='YOURAPIKEY',
    cloud=True)


space = get_space_export(space_key="NUCLEUS", export_type="html")
