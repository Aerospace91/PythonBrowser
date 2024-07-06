import url
import tkinter

def main ():
    # print(f"The URL scheme is: {url.scheme}, the URL host is {url.host} and the URL path is {url.path}")
    url.load(url.URL(input("Enter URL: ")))   
    
if __name__ == '__main__':
    main()