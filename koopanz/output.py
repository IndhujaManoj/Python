from selenium import webdriver

input_file = 'input.html'
output_file = 'output.png'

# Create a headless Chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# Load the HTML file
driver.get(f'file://{input_file}')

# Take a screenshot
driver.save_screenshot(output_file)

# Close the browser
driver.quit()

print(f'Image saved as {output_file}')
