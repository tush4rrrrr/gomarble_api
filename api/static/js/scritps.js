document.getElementById("scraperForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const url = document.getElementById("productUrl").value;
    const resultsDiv = document.getElementById("results");

    resultsDiv.innerHTML = "<p>Loading reviews...</p>";

    try {
        const response = await fetch(`/api/reviews?page=${encodeURIComponent(url)}`);
        const data = await response.json();

        if (data.error) {
            resultsDiv.innerHTML = `<p class="text-danger">Error: ${data.error}</p>`;
        } else {
            resultsDiv.innerHTML = `<p class="text-success">Found ${data.reviews_count} reviews:</p>`;
            const reviewsList = document.createElement("ul");
            reviewsList.classList.add("list-group");
            data.reviews.forEach((review) => {
                const listItem = document.createElement("li");
                listItem.classList.add("list-group-item");
                listItem.innerHTML = `
                    <h5>${review.title}</h5>
                    <p>${review.body}</p>
                    <small>Rating: ${review.rating} | Reviewer: ${review.reviewer}</small>
                `;
                reviewsList.appendChild(listItem);
            });
            resultsDiv.appendChild(reviewsList);
        }
    } catch (error) {
        resultsDiv.innerHTML = `<p class="text-danger">Error fetching reviews: ${error.message}</p>`;
    }
});
