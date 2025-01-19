# GoMarble Review Scraper API

![GoMarble Logo](https://via.placeholder.com/300x100.png?text=GoMarble) <!-- Replace with actual logo URL -->

## 📖 About the Project

**GoMarble Review Scraper API** is a dynamic solution designed to extract product reviews from e-commerce platforms like Shopify, Amazon, and others. It leverages **browser automation** and **AI-driven CSS selector generation** to adaptively scrape reviews, even from pages with dynamic content or complex structures.

This project is ideal for developers looking to:

- Automate the extraction of user reviews for data analysis.
- Build sentiment analysis tools based on customer feedback.
- Integrate scraping capabilities into larger data pipelines.

The project includes both a **backend API** for programmatic access and an **interactive front-end** for a user-friendly experience.

---

## 🌟 Features

1. **Dynamic Review Scraping**

   - Automatically adapts to different e-commerce platforms using **Gemini AI** to generate CSS selectors.
   - Handles pagination to ensure complete data extraction.

2. **Error Handling**

   - Detects and reports issues such as missing review sections, invalid URLs, or inaccessible pages.

3. **Interactive Front-End**

   - Allows users to input a product URL and see reviews in a clean, readable format.

4. **API Integration**

   - Exposes a `/api/reviews` endpoint for seamless integration with other systems.

5. **Scalable Architecture**

   - Modular structure for easy addition of new features or integration with other services.

6. **Testing**
   - Tested in Live Environment using POSTMAN

---

## 🛠️ Technical Details

1. **Backend:**

   - Built with **Flask**, a lightweight Python web framework.
   - API endpoints for review scraping.
   - Handles asynchronous data fetching and error management.

2. **Scraping Logic:**

   - Uses **Playwright** for browser automation, ensuring compatibility with JavaScript-heavy websites.
   - Integrates **Gemini AI** to dynamically identify CSS selectors for reviews.

3. **Front-End:**

   - Built with HTML, CSS, and JavaScript.
   - Styled with **Bootstrap** for a responsive design.
   - Includes form validation and dynamic result rendering.

4. **Error Management:**

   - Comprehensive logging for debugging.
   - User-friendly error messages for both the API and front-end.

5. **Environment:**
   - Environment variables managed with `.env` for API keys and configurations.
   - Easy-to-setup virtual environment and dependency management.

---

## 📂 Folder Structure
