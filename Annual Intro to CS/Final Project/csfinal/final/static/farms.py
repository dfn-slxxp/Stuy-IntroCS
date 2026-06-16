#!/usr/bin/env python3
import cgi, cgitb, csv, os
cgitb.enable()

BASE = "/~swaldman80"
STATIC = f"{BASE}/static"
FARM_FILE = os.path.expanduser("farms_db.csv")
ALLOWED_CATEGORIES = {"Overworld_Mobs", "Nether_Mobs", "End_Mobs", "Blocks", "Other_Items"}

form = cgi.FieldStorage()
category = form.getvalue("category", "")

def page_head():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>MC Farms</title>
    <link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet">
    <style>
        * {{
            font-family: 'VT323', sans-serif;
            font-stretch: 150%;
            color: #ffffff;
        }}

        body {{
            text-align: center;
        }}

        .navbar {{
            position: sticky;
            top: 0;
            z-index: 40;
            border: 5px solid #51515187;
            font-size: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 2rem;
            height: 72px;
            background-color: #0000002c;
            margin-bottom: 20px;
        }}

        .content_wrappers {{
            border: 5px solid #51515187;
            background-color: #0000002c;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
            padding: 2rem;
            width: 35%;
        }}

        .content_wrappers table {{
            margin: 0 auto;
        }}

        .home-button {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .home-button h1 {{
            color: #ffffffcc;
            font-size: 2rem;
            font-weight: 600;
            margin: 0;
            padding: 0.5rem;
        }}

        .home-button img {{
            object-fit: contain;
        }}

        .links a {{
            color: #ffffffcc;
            text-decoration: none;
            font-size: 1.5rem;
            padding: .5rem .75rem;
            border-radius: 4px;
        }}

        .links a:hover {{
            color: #ffffff;
        }}

        .content {{
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}

        .category_badge {{
            display: inline-block;
            background-color: #51515187;
            border: 2px solid #ffffff44;
            border-radius: 4px;
            padding: 0.1rem 0.5rem;
            font-size: 1rem;
            margin: 0.2rem;
        }}

        .show-all {{
            background: #0000002a;
            border: 1px solid #51515187;
            border-radius: 5px;
            padding: 0.75rem 1rem;
            font-family: 'VT323', monospace;
            font-size: 1.2rem;
            color: #fff;
            text-decoration: none;
            margin-bottom: 1rem;
            display: inline-block;
        }}

        .categories {{
            background: #0000004a;
            border: 2px solid #51515187;
            border-radius: 5px;
            padding: 1rem 0.5rem;
            text-align: center;
            font-size: 1.2rem;
            text-decoration: none;
        }}

        .selected_category {{
            background: #b4b4b44a;
            border: 2px solid #51515187;
            border-radius: 5px;
            padding: 1rem 0.5rem;
            text-align: center;
            font-size: 1.2rem;
            text-decoration: none;
        }}

        .home-categories {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 0.75rem;
            padding: 2rem;
        }}

        .link_button {{
            display: inline-block;
            background-color: #3a3a3a11;
            border: 2px solid #ffffff2c;
            border-radius: 4px;
            padding: 0.3rem 0.7rem;
            font-size: 1rem;
            margin: 0.2rem;
            color: #fff;
            text-decoration: none;
        }}
    </style>
</head>
<body background="{STATIC}/Dirt.png">
    <div class="navbar">
        <a href="{BASE}/" class="home-button">
            <img src="{STATIC}/image.png" width="48px" height="48px" alt="website logo">
            <h1>Farm Discovery</h1>
        </a>
        <div class="links">
            <a href="{BASE}/">About</a>
            <a href="{BASE}/quiz.py">Play the Quiz</a>
            <a href="{BASE}/farms.py">Farms</a>
            <a href="{BASE}/add.py">Add a Farm</a>
        </div>
    </div>
    <div class="content">
"""

def get_categories(category):
    def cls(cat): return "selected_category" if category == cat else "categories"
    return f"""
        <div class="home-categories">
            <a href="{BASE}/farms.py?category=Overworld_Mobs" class="{cls('Overworld_Mobs')}">Overworld Mobs</a>
            <a href="{BASE}/farms.py?category=Nether_Mobs" class="{cls('Nether_Mobs')}">Nether Mobs</a>
            <a href="{BASE}/farms.py?category=End_Mobs" class="{cls('End_Mobs')}">End Mobs</a>
            <a href="{BASE}/farms.py?category=Blocks" class="{cls('Blocks')}">Blocks</a>
            <a href="{BASE}/farms.py?category=Other_Items" class="{cls('Other_Items')}">Other Items</a>
        </div>
"""

def get_categories_str(cats):
    return "".join(f'<span class="category_badge">{c}</span>' for c in cats)

def get_image(img):
    if not img:
        return ""
    if img.startswith("https"):
        return f'<tr><td><img src="{img}" width="50%"></td></tr>'
    return f'<tr><td><img src="{STATIC}/{img}" width="50%"></td></tr>'

def get_video(vid):
    if vid:
        return f'<tr><td><a href="{vid}" class="link_button">Farm Video</a></td></tr>'
    return ""

def farm_html(name, author, versions, desc, cats, vid, img):
    return f"""
        <div class="content_wrappers">
            <table>
                <tr><td><h2>{name}</h2></td></tr>
                <tr><td><h3>By: {author}</h3></td></tr>
                <tr><td>Supports Version(s): {versions}</td></tr>
                <tr><td>{get_categories_str(cats)}</td></tr>
                <tr><td><p>{desc}</p></td></tr>
                {get_video(vid)}
                {get_image(img)}
            </table>
        </div>
"""

print("Content-Type: text/html\n")
print(page_head())
print(get_categories(category))

if category:
    print(f'        <a href="{BASE}/farms.py" class="show-all">Show All Farms</a>')

try:
    with open(FARM_FILE, "r", newline="", encoding="utf-8") as f:
        farms = sorted(csv.reader(f), key=lambda row: row[0].lower())
    for farm in farms:
        if len(farm) < 6:
            continue
        if category and category not in farm[4].split("|"):
            continue
        img = farm[6] if len(farm) > 6 else ""
        print(farm_html(farm[0], farm[1], farm[2], farm[3], farm[4].split("|"), farm[5], img))
except FileNotFoundError:
    print("        <p>No farms yet.</p>")

print("    </div>\n</body>\n</html>")
