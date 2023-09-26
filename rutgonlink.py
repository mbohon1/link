import pyshorteners
import time
import pyperclip

# Replace 'YOUR_BITLY_API_KEY' with your actual bit.ly API key
BITLY_API_KEY = 'a2ea1f8108234fa7f336ae0c77f38d4690b04888'

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
    input_link = input("Enter the input link: ")
    
    # Shorten the input link using bit.ly
    short_url = shorten_url(input_link)
    if short_url:
        print(f"Shortened URL:")
        print(short_url)
        
        # Copy the shortened URL to the clipboard
        pyperclip.copy(short_url)
        print("Shortened URL copied to clipboard.")
        
        # Wait for 1 minute (60 seconds) before closing the program
        print("Waiting for 1 minute before closing the program...")
        time.sleep(60)
    else:
        print("Shortening the URL failed.")
