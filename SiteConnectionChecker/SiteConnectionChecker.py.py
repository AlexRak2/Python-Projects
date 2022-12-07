import urllib.request as urlib

def check_url(url):
    print("Checking connectivity")

    response = urlib.urlopen(url)
    print("Connected to", url , "succesfully")
    print("Response Code:", response.getcode())

input_url = input("Input url for the site to check: ")
check_url(input_url)