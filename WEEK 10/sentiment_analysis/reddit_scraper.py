import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

class RedditScraper:
    def __init__(self):
        self.base_url = 'https://www.reddit.com/r/technology/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.delay = 1  # 1 second delay between requests (60 requests per minute)

    def scrape_posts(self, max_posts=10):
        """Scrape Reddit posts with rate limiting"""
        time.sleep(self.delay)  # Respect rate limit
        
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()  # Raise exception for bad status codes
            
            soup = BeautifulSoup(response.content, 'html.parser')
            posts = []
            
            # Find all post containers (structure may vary)
            post_containers = soup.find_all('div', {'data-testid': 'post-container'})
            
            for container in post_containers[:max_posts]:
                post = {}
                
                # Extract title
                title_elem = container.find('a', {'data-testid': 'post-title'})
                post['title'] = title_elem.text.strip() if title_elem else 'N/A'
                
                # Extract author
                author_elem = container.find('a', {'data-testid': 'post_author-link'})
                post['author'] = author_elem.text.strip() if author_elem else 'N/A'
                
                # Extract creation date/time
                time_elem = container.find('span', {'data-testid': 'post_timestamp'})
                if time_elem and 'datetime' in time_elem.attrs:
                    dt = datetime.fromisoformat(time_elem['datetime'])
                    post['created'] = dt.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    post['created'] = 'N/A'
                
                # Extract score (upvotes)
                score_elem = container.find('div', {'data-testid': 'post-upvote-button'})
                post['score'] = score_elem.find_next('span').text.strip() if score_elem else 'N/A'
                
                # Extract number of comments
                comments_elem = container.find('a', {'data-testid': 'post-comments-link'})
                post['comments'] = comments_elem.text.strip().split()[0] if comments_elem else 'N/A'
                
                # Extract permalink
                permalink_elem = container.find('a', {'data-testid': 'post-title'})
                post['permalink'] = permalink_elem['href'] if permalink_elem else 'N/A'
                
                posts.append(post)
            
            return posts
            
        except Exception as e:
            print(f"Error scraping Reddit: {e}")
            return []

    def print_posts(self, posts):
        """Print scraped posts in a readable format"""
        for i, post in enumerate(posts, 1):
            print(f"\nPost #{i}:")
            print(f"Title: {post['title']}")
            print(f"Author: {post['author']}")
            print(f"Created: {post['created']}")
            print(f"Score: {post['score']}")
            print(f"Comments: {post['comments']}")
            print(f"Permalink: https://www.reddit.com{post['permalink']}")

def main():
    scraper = RedditScraper()
    posts = scraper.scrape_posts(max_posts=5)  # Scrape first 5 posts
    scraper.print_posts(posts)

if __name__ == "__main__":
    main()