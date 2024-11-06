# main.py
from src.oii_fsds_textanalysis.reddit_scraper import RedditScraper
from oii_fsds_textanalysis.text_processor import preprocess_text
from oii_fsds_textanalysis.analysis import tfidf_analyze_subreddit, create_posts_dataframe
from src.oii_fsds_textanalysis.settings import USER_AGENT

def main():
    
    scraper = RedditScraper(USER_AGENT)
    posts = scraper.get_subreddit_posts("python", limit=100)
    
    df = create_posts_dataframe(posts)
    
    results = tfidf_analyze_subreddit(posts)
    

if __name__ == "__main__":
    main()