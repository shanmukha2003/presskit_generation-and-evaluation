import requests
from config import NEWS_API_KEY

def fetch_latest_news(company_name):
    """Fetches latest English news articles about the company using NewsAPI."""
    print(f"\nFetching news related to: {company_name}...")

    url = f"https://newsapi.org/v2/everything?qInTitle={company_name} AND (announces OR launches OR unveils OR releases)&sortBy=publishedAt&pageSize=10&language=en&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: API request failed with status {response.status_code}")
            return []

        data = response.json()
        articles = data.get("articles", [])[:5]  # Get top 5 news articles

        if not articles:
            print("No relevant news articles found.")
            return []

        print("\n[Supplementary Data Summary]")
        for i, art in enumerate(articles, start=1):
            title = art['title']
            source = art['source']['name']
            print(f"{i}. \"{title}\" (Source: {source})")

        # Ask the user which articles to include
        selected_indexes = input("\nEnter the numbers of the articles to include (comma-separated, e.g., 1,3,5): ").strip()
        
        # Process user input
        selected_indexes = [int(x) - 1 for x in selected_indexes.split(",") if x.isdigit() and 1 <= int(x) <= len(articles)]
        news_summary = [f"\"{articles[i]['title']}\" (Source: {articles[i]['source']['name']})" for i in selected_indexes]

        return news_summary
    
    except Exception as e:
        print("Error fetching news:", e)
        return []

# Run the function with a test company name
if __name__ == "__main__":
    company = input("Enter Company Name: ")  # Take input from user
    selected_news = fetch_latest_news(company)

    print("\nFinal Selected News:")
    for news in selected_news:
        print(f"- {news}")
