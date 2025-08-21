🏠 Zillow Scraper & Google Form Auto-Filler
This Python project automates real estate data collection from Zillow (or a Zillow clone) and inputs the scraped listings into a Google Form automatically. It’s a great demonstration of web scraping and form automation with Python.

🚀 Features
Scrapes property addresses, prices, and links from Zillow clone site

Cleans and structures scraped data

Automatically fills a Google Form with the collected listings

Uses BeautifulSoup for HTML parsing and Selenium for browser automation

Easily adaptable for real Zillow or other property sites

🛠️ Technologies Used
    Python 3.x

    requests – for making HTTP requests

    beautifulsoup4 – for parsing HTML

    selenium – for browser automation

    ChromeDriver – for controlling Chrome

📁 Project Structure

📦 zillow-form-bot/

├── main.py              # Main script to scrape Zillow and fill Google Form

▶️ How to Use
1. Clone the repository

    git clone https://github.com/bunyaminenis/zillow-form-bot.git
    cd zillow-form-bot
2. Install dependencies

    pip install requests beautifulsoup4 selenium
3. Download ChromeDriver

    Get ChromeDriver for your Chrome version.

    Add it to your system PATH.

4. Update URLs

    Change ZILLOW_URL in main.py to your Zillow (or Zillow clone) target.

    Change FORM_URL to your Google Form link.

5. Run the bot

    python main.py
The bot will:

Scrape addresses, prices, and listing links from Zillow

Open the Google Form

Fill and submit each property one by one

Form Submission:
The bot will open Chrome, fill the form fields with each address, price, and link, then submit.
