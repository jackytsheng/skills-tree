from bs4 import BeautifulSoup

with open('algorithm.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Insert custom CSS or modify existing CSS
# This is a basic example that adds a CSS rule
# You'll need to adjust based on the actual changes you want
style_tag = soup.find('style')

if style_tag:
    # Append custom CSS to the existing style content
    custom_css = """
    /* Add your custom CSS rules here */

    #mynetwork {
       border: none
    }
    .card{
        border:none
    }
    """
    style_tag.append(custom_css)

with open('algorithm.html', 'w') as file:
    file.write(str(soup))
