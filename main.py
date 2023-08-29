import os
import praw
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Define a function to handle NoneType values


def handle_none(value):
    return "Not Available" if value is None else value


# Reddit post URL
post_url = "https://www.reddit.com/r/VideojuegosMX/comments/1636rbb/recomienden_juegos_de_pc/"

# Extract post information
post = reddit.submission(url=post_url)
post_id = post.id
post_author_id = post.author.id
post_creation = datetime.fromtimestamp(post.created_utc)

# Database setup
try:
    db_connection = sqlite3.connect("reddit_data.db")
    db_cursor = db_connection.cursor()

    # Create a table if it doesn't exist
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS reddit_data (
            id INTEGER PRIMARY KEY,
            reddit_post_id TEXT,
            reddit_post_url TEXT,
            author_id TEXT,
            text_comment TEXT,
            text_comment_id TEXT,
            votes INTEGER,
            author_name TEXT,
            post_creation TEXT,
            comment_creation TEXT,
            api_read_timestamp TEXT
        )
    """)

    for comment in post.comments.list():
        comment_id = comment.id
        comment_text = comment.body
        if comment.author is None:
            comment_author_id = -1
            comment_author_name = "Not Available"
        else:
            comment_author_id = comment.author.id
            comment_author_name = comment.author.name
        comment_creation = datetime.fromtimestamp(comment.created_utc)
        comment_votes = comment.score

        db_cursor.execute("""
                        INSERT INTO reddit_data (reddit_post_id, reddit_post_url, author_id, text_comment, text_comment_id, votes, author_name, post_creation, comment_creation, api_read_timestamp)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """,
                          (handle_none(post_id), handle_none(post_url), handle_none(post_author_id), handle_none(comment_text), handle_none(comment_id), handle_none(comment_votes), handle_none(comment_author_name), handle_none(post_creation), handle_none(comment_creation), handle_none(datetime.now())))
        print(f"Imported comment {comment_id} from post {post_id}")
        db_connection.commit()

except sqlite3.Error as e:
    print("SQLite error:", e)
finally:
    db_connection.close()
