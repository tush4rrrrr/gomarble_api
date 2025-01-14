from playwright.sync_api import sync_playwright
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

def get_css_selectors(url):
    """Use Gemini API to generate accurate CSS selectors."""
    prompt = (
        f"Generate exactly 5 CSS selectors for scraping reviews from this page: {url}. "
        "Return only CSS selectors separated by newlines. No backticks, no numbering, no labels."
    )
    
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        selectors = [line.strip() for line in response.text.splitlines() if line.strip()]

        if len(selectors) != 5:
            raise ValueError("Incorrect number of CSS Selectors generated.")
        
        return selectors
    except Exception as e:
        return {"error": f"Failed to fetch CSS selectors: {str(e)}"}

def scrape_reviews(url):
    """Scrape reviews using Playwright and Gemini-generated selectors."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to False for debugging
        page = browser.new_page()

        try:
            # Set User-Agent early to avoid bot detection
            page.set_extra_http_headers({"User-Agent": "Mozilla/5.0"})
            page.goto(url, timeout=60000, wait_until="domcontentloaded")

            # Scrolling to trigger lazy loading
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            page.wait_for_load_state("networkidle")  # Wait for dynamic content to load fully
            page.wait_for_timeout(5000)

        except Exception as e:
            browser.close()
            return {"error": f"Failed to load page: {str(e)}"}

        # Generate CSS Selectors using Gemini
        css_selectors = get_css_selectors(url)
        print("Generated Selectors : ", css_selectors)
        if isinstance(css_selectors, dict):
            browser.close()
            return css_selectors

        # Confirm if the first selector exists
        try:
            page.wait_for_selector(css_selectors[0], timeout=10000)
        except Exception as e:
            browser.close()
            return {"error": f"Review section not found: {str(e)}"}

        # Extract reviews using the generated CSS selectors
        try:
            reviews = page.evaluate(f'''
            Array.from(document.querySelectorAll('{css_selectors[0]}')).map(review => ({{
                title: review.querySelector('{css_selectors[1]}')?.innerText.trim() || "No title",
                body: review.querySelector('{css_selectors[2]}')?.innerText.trim() || "No body",
                rating: review.querySelector('{css_selectors[3]}')?.innerText.trim() || "No rating",
                reviewer: review.querySelector('{css_selectors[4]}')?.innerText.trim() || "Anonymous"
            }}))
            ''')
        except Exception as e:
            browser.close()
            return {"error": f"Error extracting reviews: {str(e)}"}

        browser.close()
        return reviews
