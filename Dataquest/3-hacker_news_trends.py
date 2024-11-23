import requests


def fetch_top_posts():
    """Fetch the top 5 posts from Hacker News API and print their titles."""
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    response = requests.get(url)

    if response.status_code == 200:
        top_post_ids = response.json()[:5]  # Get top 5 post IDs

        for post_id in top_post_ids:
            post_url = f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json?print=pretty"
            post_response = requests.get(post_url)

            if post_response.status_code == 200:
                post = post_response.json()
                print(post.get("title"))
            else:
                print("Failed to fetch post details.")
    else:
        print("Failed to fetch top posts.")


if __name__ == "__main__":
    fetch_top_posts()
