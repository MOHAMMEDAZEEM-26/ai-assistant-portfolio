import google.generativeai as genai
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

genai.configure(api_key="AIzaSyCnAbkyxfFr7Au79Ng72F70U4vuavt3mLM")
model = genai.GenerativeModel("models/gemini-1.5-pro-001")

@app.route("/")
def home():
    html_structure = """
    <!DOCTYPE html>
    <html lang="en">
    <head><meta charset="UTF-8" /><title>Portfolio</title></head>
    <body>
        <header>
            <div class="profile">
                <img src="profile.jpg" alt="Azeemuddin" />
                <h1>Shaik Mohammed Azeemuddin</h1>
                <p>B.Tech Student | UI/UX Designer | Cloud Enthusiast</p>
            </div>
        </header>
        <section class="about"><h2>About Me</h2><p>...</p></section>
        <section class="skills"><h2>My Skills</h2><div class="skill-icons"><span>HTML</span>...</div></section>
        <section class="experience"><h2>Projects</h2><ul><li>Phishing URL Detection</li>...</ul></section>
        <section class="contact"><h2>Contact Me</h2><p>Email...</p></section>
        <footer><p>© 2025 Shaik Mohammed Azeemuddin</p></footer>
    </body>
    </html>
    """

    prompt = f"""
You are a creative CSS designer. Based on the following HTML structure, generate a complete modern, visually appealing, responsive CSS stylesheet.(add animations, colors, effects, styles etc)

Every time this is called, give a **unique design**: different colors, fonts, button styles, layout tweaks, and animations (if desired).

### HTML structure:
{html_structure}

### Requirements:
- Don't change the HTML.
- Ensure full layout coverage (header, profile image, sections, etc.)
- Make it mobile-responsive.
- Use modern UI/UX design principles.
- Output only valid CSS, no explanations.
"""

    response = model.generate_content(prompt)
    css_code = response.text

    # Save the generated CSS
    with open("static/css/style.css", "w", encoding="utf-8") as f:
        f.write(css_code)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
