#!/usr/bin/env python3
import cgi, cgitb, csv, os
cgitb.enable()

BASE = "/~swaldman80"
STATIC = f"{BASE}/static"
FARM_FILE = os.path.expanduser("farms_db.csv")
ALLOWED_CATEGORIES = {"Overworld_Mobs", "Nether_Mobs", "End_Mobs", "Blocks", "Other_Items"}

def page_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Add a Farm</title>
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

        .form_item {{
            padding-top: 1rem;
            padding-bottom: 1rem;
        }}

        .form_item label {{
            margin: .25rem;
            display: inline-block;
        }}

        input, button {{
            color: black;
        }}

        h1 {{
            font-size: 350%;
        }}

        label, input {{
            font-size: 150%;
        }}

        .category_option {{
            display: flex;
            align-items: center;
            gap: 0.4rem;
            margin: 0.25rem 0.5rem;
        }}

        #game_version {{
            display: inline-flex;
            flex-direction: column;
            align-items: flex-start;
        }}
    </style>
</head>
<body background="{STATIC}/Dirt.png">
    <div class="navbar">
        <a href="{BASE}/index.html" class="home-button">
            <img src="{STATIC}/image.png" width="48px" height="48px" alt="website logo">
            <h1>Farm Discovery</h1>
        </a>
        <div class="links">
            <a href="{BASE}/index.html">About</a>
            <a href="{BASE}/quiz.py">Play the Quiz</a>
            <a href="{BASE}/farms.py">Farms</a>
            <a href="{BASE}/add.py">Add a Farm</a>
        </div>
    </div>
    <div class="content">
        <form class="content_wrappers" method="post" action="{BASE}/add.py">
            <h1>Submit a Farm</h1>

            <div class="form_item">
                <label for="name">Farm Name</label>
                <input type="text" id="name" name="name" placeholder="Farm Name" required>
            </div>

            <div class="form_item">
                <label for="author">Farm Author</label>
                <input type="text" id="author" name="author" placeholder="Farm Author" required>
            </div>

            <div class="form_item">
                <label for="minecraft_version">Supported Minecraft Version(s)</label>
                <input type="text" id="minecraft_version" name="minecraft_version" placeholder="Supported Version(s)" required>
            </div>

            <div class="form_item">
                <label for="farm_description">Description</label>
                <input type="text" id="farm_description" name="farm_description" placeholder="Farm Description" required>
            </div>

            <div class="form_item">
                <label style="display: block; margin-bottom: 0.5rem;">Farm Categories</label>
                <div id="game_version">
                    <div class="category_option">
                        <input type="checkbox" id="Overworld_Mobs" value="Overworld_Mobs" name="categories">
                        <label for="Overworld_Mobs">Overworld Mobs</label>
                    </div>
                    <div class="category_option">
                        <input type="checkbox" id="Nether_Mobs" value="Nether_Mobs" name="categories">
                        <label for="Nether_Mobs">Nether Mobs</label>
                    </div>
                    <div class="category_option">
                        <input type="checkbox" id="End_Mobs" value="End_Mobs" name="categories">
                        <label for="End_Mobs">End Mobs</label>
                    </div>
                    <div class="category_option">
                        <input type="checkbox" id="Blocks" value="Blocks" name="categories">
                        <label for="Blocks">Blocks</label>
                    </div>
                    <div class="category_option">
                        <input type="checkbox" id="Other_Items" value="Other_Items" name="categories">
                        <label for="Other_Items">Other Items</label>
                    </div>
                </div>
            </div>

            <div class="form_item">
                <label for="video_url">Video URL</label>
                <input type="text" id="video_url" name="video_url" placeholder="Video URL">
            </div>

            <div class="form_item">
                <label for="img_url">Image URL</label>
                <input type="text" id="img_url" name="img_url" placeholder="Image URL">
            </div>

            <div class="form_item">
                <button type="submit">Submit Farm</button>
            </div>
        </form>
    </div>
</body>
</html>"""

def main():
    form = cgi.FieldStorage()

    if os.environ.get("REQUEST_METHOD") == "POST":
        name     = form.getvalue("name", "").strip()[:200]
        author   = form.getvalue("author", "").strip()[:200]
        mc_ver   = form.getvalue("minecraft_version", "").strip()[:50]
        desc     = form.getvalue("farm_description", "").strip()[:1000]
        vid      = form.getvalue("video_url", "").strip()[:200]
        img      = form.getvalue("img_url", "").strip()[:200]
        cats_raw = form.getlist("categories")
        cats     = [c for c in cats_raw if c in ALLOWED_CATEGORIES]

        if name and author and mc_ver and desc and cats:
            with open(FARM_FILE, "a", newline="", encoding="utf-8") as f:
                csv.writer(f, lineterminator='\n').writerow([name, author, mc_ver, desc, "|".join(cats), vid, img])
            print(f'<html><head><meta http-equiv="refresh" content="0;url={BASE}/farms.py"></head><body></body></html>')
            return

    print(page_html())

if __name__ == '__main__':
    print("Content-type:text/html\r\n\r\n")
    try:
        main()
    except:
        cgi.print_exception()
