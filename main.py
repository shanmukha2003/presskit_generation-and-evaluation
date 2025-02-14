from user_input import get_user_input
from news_fetcher import fetch_latest_news
from llama_model import generate_press_kit

if __name__ == "__main__":
    company, topic, media, tone = get_user_input()
    supplementary_data = fetch_latest_news(company)
    press_kit = generate_press_kit(company, topic, tone, supplementary_data)
    print("\nFinal Press Kit Generated!")