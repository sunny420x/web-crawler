import sys
import requests
from lxml import html

def WelcomeUI():
    print("""\
          
    ==================================================
                Web Crawler by Sunny420x.com
    ==================================================
                    """)

def crawlpage(site):
    page = requests.get(site)
    webpage = html.fromstring(page.content)
    return webpage.xpath('//a/@href')

savefilename = 'output/links.txt' #Default Output File.

WelcomeUI()
print("-h to display lists of commands.\n")

if(len(sys.argv) == 1):
    print("[!] Please enter URL. \n")
elif(len(sys.argv) == 2):
    if(sys.argv[1] == "-h"):
        print("----- Web Crawler Help -----\n")
        print("-h to display lists of commands.")
        print("-o [filename] to use costom output.")
        print("\n----------------------------\n")

elif(len(sys.argv) == 4):
    if(sys.argv[2] == "-o"):
        print("[+] Custom output file is: "+"output/"+sys.argv[3])
        savefilename = "output/"+sys.argv[3]
    links = crawlpage(sys.argv[1])

if(len(sys.argv) > 2):
    file = open(savefilename, 'a')
    file.write("==== Crawing on "+sys.argv[1]+" ====\n")

    for link in links:
        if link[0] != "h":
            file.write(sys.argv[1]+link+"\n")
        else:
            file.write(link+"\n")


    file.write("==== End crawing on "+sys.argv[1]+" ====\n")
    file.write("\n")
    file.close()
    print("[+] Done crawing and data has been saved to: output/"+savefilename+"\n")