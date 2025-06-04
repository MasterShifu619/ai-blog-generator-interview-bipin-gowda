import openai
import os
from dotenv import load_dotenv
import requests

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_image_urls(keyword, count=3):
    try:
        response = requests.get(
            "https://pixabay.com/api/",
            params={
                "key": os.getenv("PIXABAY_API_KEY"),
                "q": keyword,
                "image_type": "photo",
                "safesearch": "true",
                "per_page": count
            }
        )
        data = response.json()
        return [hit['webformatURL'] for hit in data.get('hits', [])][:count]
    except Exception:
        return ["https://via.placeholder.com/800x400"] * count

def generate_blog_post(keyword, seo_data):
    image_urls = get_image_urls(keyword, 4)

    image_html_blocks = "\n".join(
        f'<div style="text-align:center;margin:20px 0;">'
        f'<img src="{url}" alt="{keyword} image" style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 0 10px rgba(0,0,0,0.1);">'
        f'<div style="font-size:0.9em; color:gray;">Illustration for {keyword}</div>'
        f'</div>' for url in image_urls
    )

    prompt = f"""
    Use the following SEO metrics as internal reference for tone, structure, and depth:
    - Search Volume: {seo_data['search_volume']}
    - Keyword Difficulty: {seo_data['keyword_difficulty']}
    - Average CPC: ${seo_data['avg_cpc']}

    Do not include or reference these metrics directly in the blog post.

    Now, write a highly polished, professional SEO-optimized blog post for the keyword: '{keyword}'.

    Include:
    - A bold, professional H1 title with a subtitle
    - Intro paragraph with a hook
    - At least 3 content sections (H2 and H3 structure)
    - Bullet lists and callout boxes styled with CSS
    - Add affiliate call-to-action using <a href=\"{{AFF_LINK_1}}\"> format

    Design:
    - HTML5 with professional inline CSS (modern font, spacing, colors)
    - Responsive layout with padding, shadows, and readable typography
    - Emulate visual and content quality similar to https://www.outrank.so/#examples

    Output full HTML with <html>, <head>, and <body> tags included.
    Also include the following HTML content (as visual elements in appropriate places):
    {image_html_blocks}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5000
    )

    raw_content = response.choices[0].message.content
    return raw_content.replace("{{AFF_LINK_1}}", "https://example.com/affiliate")