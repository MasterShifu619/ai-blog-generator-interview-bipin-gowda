# AI Blog Generator

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/MasterShifu619/ai-blog-generator-interview-bipin-gowda/actions)
[![license badge](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![issues badge](https://img.shields.io/github/issues/MasterShifu619/ai-blog-generator-interview-bipin-gowda)](https://github.com/MasterShifu619/ai-blog-generator-interview-bipin-gowda/issues)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Flask](https://img.shields.io/badge/flask-2.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![GitHub Release](https://img.shields.io/badge/release-v1.0.0-blue)](https://github.com/MasterShifu619/ai-blog-generator-interview-bipin-gowda/releases)

## AI-Powered Blog Post Generator

**AI Blog Generator** is a smart Flask-based web app that automatically creates SEO-optimized blog posts using OpenAI's GPT models and Pixabay image integration. With daily scheduled post generation and rotating keyword support, it's a hands-free tool for building content-rich blog sites.

### Demo

Watch a quick demo on how the system works:  
[YouTube Demo](https://www.youtube.com/watch?v=your_demo_link)

---

## Features

- 🔍 SEO-aware blog post generation
- 🧠 Powered by GPT (`gpt-4.1-nano`) with real image injection
- 🖼️ Fetches relevant images from Pixabay
- 🗓️ Automatically generates one post daily at 8:00 AM
- 📂 Stores posts as professional HTML files in `/posts`
- 🔁 Rotates through multiple keywords

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/ai-blog-generator.git
cd ai-blog-generator


2. Set Up Environment

python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt

3. Create a .env File
OPENAI_API_KEY=sk-xxxxx
PIXABAY_API_KEY=your_pixabay_key

4. Run the App
python app.py

Folder Structure

.
├── app.py               # Main Flask app with daily job scheduler
├── ai_generator.py      # OpenAI integration and image injection
├── seo_fetcher.py       # Mock SEO data generator
├── posts/               # Generated blog posts saved here
├── requirements.txt
└── .env


License
This project is licensed under the MIT License - see the LICENSE file for details.


Contributors
<table> <tr> <td align="center"><a href="https://github.com/YourUsername"><img src="https://avatars.githubusercontent.com/u/112150278?v=4" width="100px;" alt=""/><br /><sub><b>Bipin Gowda</b></sub></a></td> </tr> </table>
:email: Support
Need help? Reach out at: bipin.919@gmail.com
