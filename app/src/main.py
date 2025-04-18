from src.ai_utils.market_trends import analyze_market_trend
from src.constants.prompts import DAILY_NEWS_PROMPT


if __name__ == "__main__":
    trend_analysis = analyze_market_trend(DAILY_NEWS_PROMPT)
    print(trend_analysis)