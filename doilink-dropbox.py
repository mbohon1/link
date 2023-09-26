import requests
import re
import pyshorteners
import pyperclip  # Import pyperclip library for copying to the clipboard

# Replace 'YOUR_BITLY_API_KEY' with your actual bit.ly API key
BITLY_API_KEY = 'a2ea1f8108234fa7f336ae0c77f38d4690b04888'

def get_dl_link(dropbox_link):
    try:
        # Replace "www.dropbox.com" with "dl.dropboxusercontent.com" in the URL
        dl_link = re.sub(r'www.dropbox.com', 'dl.dropboxusercontent.com', dropbox_link)

        return dl_link
    except Exception as e:
        print(f"Error converting Dropbox link: {e}")
        return None

def shorten_url(url):
    try:
        # Initialize a bit.ly URL shortener with your API key
        s = pyshorteners.Shortener(api_key=BITLY_API_KEY)
        # Shorten the URL
        short_url = s.bitly.short(url)

        return short_url
    except Exception as e:
        print(f"Error shortening URL: {e}")
        return None

if __name__ == "__main__":
    dropbox_link = input("Enter the input Dropbox link: ")
    
    # Get dl.dropboxusercontent.com link
    dl_link = get_dl_link(dropbox_link)
    if dl_link:
        print("dl.dropboxusercontent.com link:")
        print(dl_link)
        
        # Shorten the dl.dropboxusercontent.com link using bit.ly
        short_url = shorten_url(dl_link)
        if short_url:
            print("Shortened URL:")
            print(short_url)
            
            # Copy the shortened URL to the clipboard
            pyperclip.copy(short_url)
            print("Shortened URL copied to clipboard.")
    else:
        print("Conversion to dl.dropboxusercontent.com link failed.")