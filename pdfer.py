from atlassian import Confluence
import sys

confluence = Confluence(
    url='https://exampleco.atlassian.net',
    username="jim.weller@exampleco.com",
    password='YOURAPIKEY',
    cloud=True)


pages = confluence.cql("ancestor=1298804812", start=0, limit=None,
                       expand=None, include_archived_spaces=None, excerpt=None)

# print("NUCLEUS,\"" + page["title"] + "\",\"https://exampleco.atlassian.net/wiki/spaces/HFCH/pages/" + page["content"]["id"] + "\"")



pdf = confluence.get_page_as_pdf("1298842750")

print(pdf.decode('utf-8'))  # Decode and print the first 1000 characters to inspect the response content



with open("it.pdf", 'wb') as file_pdf:
    file_pdf.write(pdf)


# file_pdf = open("it.pdf", 'wb')
# file_pdf.write(pdf)
# file_pdf.close()


# for page in pages["results"]:
#     print("NUCLEUS,\"" + page["title"] + "\",\"https://exampleco.atlassian.net/wiki/spaces/HFCH/pages/" + page["content"]["id"] + "\"")
#     pdf = confluence.get_page_as_pdf(page["content"]["id"])
#     file_pdf = open("it.pdf", 'wb')
#     file_pdf.write(pdf)
#     file_pdf.close()
