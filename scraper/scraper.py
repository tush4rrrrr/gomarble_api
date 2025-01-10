from playwright.sync_api import sync_playwright

def scrape_reviews(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try :
            page.goto(url, timeout = 1000)
        except Exception as e:
            return {"error" : f"Failed to load page : {str(e)}"}

        # Corrected CSS selector and JavaScript syntax issues
        reviews = page.evaluate('''
        Array.from(document.querySelectorAll('.review')).map(review => ({
            title: review.querySelector('.review-title')?.innerText || "No title",
            body: review.querySelector('.review-body')?.innerText || "No body",
            rating: review.querySelector('.review-rating')?.innerText || "No rating",
            reviewer: review.querySelector('.reviewer-name')?.innerText || "Anonymous"
        }))
        ''')

        # Pagination handling
        while True:
            next_button = page.query_selector('button.next-page')  
            if next_button and next_button.is_visible():
                next_button.click()
                page.wait_for_load_state('networkidle')
                new_reviews = page.evaluate('''
                Array.from(document.querySelectorAll('.review')).map(review => ({
                    title: review.querySelector('.review-title')?.innerText || "No title",
                    body: review.querySelector('.review-body')?.innerText || "No body",
                    rating: review.querySelector('.review-rating')?.innerText || "No rating",
                    reviewer: review.querySelector('.reviewer-name')?.innerText || "Anonymous"
                }))
                ''')
                reviews.extend(new_reviews)
            else:
                break

        browser.close()
        return reviews
    
