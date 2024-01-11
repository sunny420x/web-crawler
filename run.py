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
no_prefix = False
blank_link = 0

WelcomeUI()
print("-h to display lists of commands.\n")

if(len(sys.argv) == 1):
    print("[!] Please enter URL. \n")
elif(len(sys.argv) == 2):
    if(sys.argv[1] == "-h"):
        print("----- Web Crawler Help -----\n")
        print("-h to display lists of commands.")
        print("-o [filename] to use costom output.")
        print("[url] -np to not include origin URL (Show just path instead)")
        print("\n----------------------------\n")
    else:
        links = crawlpage(sys.argv[1])

elif(len(sys.argv) == 3):
    if(sys.argv[2] == "-np"):
        no_prefix = True
    links = crawlpage(sys.argv[1])

elif(len(sys.argv) == 4):
    if(sys.argv[2] == "-o"):
        print("[+] Custom output file is: "+"output/"+sys.argv[3])
        savefilename = "output/"+sys.argv[3]
    links = crawlpage(sys.argv[1])

if(len(sys.argv) >= 2):
    #Get domain name from input URL.
    site = sys.argv[1].split("/")
    site = site[2]
    
    file = open(savefilename, 'a')
    file.write("==== Crawing on "+sys.argv[1]+" ====\n")

    for link in links:
        #Detect Internal/Local Path Link (No domain included in the link).
        if link[0] == "/":
            if(no_prefix == False):
                file.write("https://"+site+link+"\n")
            else:
                file.write(link+"\n")
        #Detect External Link like https://abc.
        elif link[0] == "h":
            file.write(link+"\n")
        #Detect and remove In-Page Link like abc.com/#menu .
        elif link[0] == "#":
            blank_link+=1
        else:
            file.write(site+"/"+link+"\n")


    file.write("==== End crawing on "+sys.argv[1]+" ====\n")
    file.write("\n")
    file.close()
    print("[+] Done crawing and data has been saved to: output/"+savefilename+"\n")
    print("Founds: "+str(blank_link)+" blank link with #.")