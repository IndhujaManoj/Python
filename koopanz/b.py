from bs4 import BeautifulSoup

# Read the HTML content from the file
with open('page.html', 'r') as html_file:
    html_content = html_file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Insert the image path into the 'src' attribute of the 'img' tag
img_tag = soup.find('img')
img_tag['src'] = 'imagess.png'

# Render the modified HTML content
rendered_html = str(soup)

# You can now display/render the HTML as needed
# For example, you can save it to an HTML file or display it in a web browser
with open('rendered_html.html', 'w') as output_file:
    output_file.write(rendered_html)
