### app.py
from flask import Flask, request, jsonify
from ai_generator import generate_blog_post
from seo_fetcher import fetch_seo_data
import os
from datetime import datetime
import re
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

POSTS_DIR = 'posts'
os.makedirs(POSTS_DIR, exist_ok=True)

scheduler = BackgroundScheduler()

ROTATING_KEYWORDS = [
    "smart home devices",
    "wireless earbuds",
    "electric bikes",
    "gaming laptops",
    "best travel backpacks",
    "eco-friendly gadgets"
]

keyword_index = {"index": 0}  # use a dict to allow modification in closure

def sanitize_filename_component(name):
    return re.sub(r'[^\w\-_]', '_', name)

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Missing 'keyword' query param"}), 400

    seo_data = fetch_seo_data(keyword)
    blog_content = generate_blog_post(keyword, seo_data)
    filename = save_blog(keyword, blog_content)

    return jsonify({
        "keyword": keyword,
        "seo_data": seo_data,
        "file": filename,
        "content": blog_content
    })

def save_blog(keyword, content):
    date_str = datetime.now().strftime('%Y-%m-%d')
    safe_keyword = sanitize_filename_component(keyword)
    filename = f"{POSTS_DIR}/{date_str}_{safe_keyword}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename

def scheduled_job():
    index = keyword_index["index"] % len(ROTATING_KEYWORDS)
    keyword = ROTATING_KEYWORDS[index]
    keyword_index["index"] += 1

    seo_data = fetch_seo_data(keyword)
    blog_content = generate_blog_post(keyword, seo_data)
    filename = save_blog(keyword, blog_content)
    print(f"[Scheduler] Generated blog post: {filename}")

scheduler.add_job(scheduled_job, 'interval', days=1, next_run_time=datetime.now())
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
