from shortener import shorten_url, redirect_url

# Test if the shortener and redirect are working
original = "https://example.com"
code = shorten_url(original)

print("Short Code:", code)

# Try to get the original URL back
result = redirect_url(code)

print("Original URL from short code:", result)
