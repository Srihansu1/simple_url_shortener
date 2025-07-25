import string
import random

# Dictionary to store original and short URLs
url_mapping = {}

def generate_short_code(length=6):
    """Generate a random short code of given length"""
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if short_code not in url_mapping:
            return short_code

def shorten_url(original_url):
    """Shortens the given URL"""
    # Check if the URL is already shortened
    for code, url in url_mapping.items():
        if url == original_url:
            return code

    # Generate a new short code and store mapping
    short_code = generate_short_code()
    url_mapping[short_code] = original_url
    print(f"URL '{original_url}' has been shortened to code '{short_code}'")
    return short_code

def redirect_url(short_code):
    """Returns the original URL from a given short code"""
    return url_mapping.get(short_code, "Short code not found.")

# Example usage:
if __name__ == "__main__":
    original = "https://example.com/my-long-url"
    code = shorten_url(original)
    print("Shortened Code:", code)

    resolved = redirect_url(code)
    print("Original URL:", resolved)
