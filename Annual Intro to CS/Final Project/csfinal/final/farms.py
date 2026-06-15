from django.shortcuts import render, redirect
import csv, os

def renderFarms(request):
    page = render(request, "farms.html")
    category = request.GET.get("category", "")

    with open(FARM_FILE, "r", newline="", encoding="utf-8") as file:
        farms = sorted(csv.reader(file), key=lambda row: row[0].lower())

    page.content += getCategories(category)

    if category:
        page.content += b"""<a href="/farms/" class="show-all">Show All Farms</a>"""

    for farm in farms:
        if category and category not in farm[4].split("|"):
            continue
        page.content += getInformationAsHtmlTableItem(farm[0], farm[1], farm[2], farm[3], farm[4].split('|'), farm[5], farm[6] if len(farm) > 6 else "").encode('utf-8')

    page.content += endhtml()
    return page

def endhtml():
    return f"</div></body></html>".encode('utf-8')

def getInformationAsHtmlTableItem(name, author, versions, desc, categories, vid, image):
    t = f"""

            <div class="content_wrappers">
                <table>
                    <tr><td><h2>{name}</h2></td></tr>
                    <tr><td><h3>By: {author}</h3></td></tr>
                    <tr><td>Supports Version(s): {versions}</td></tr>
                    <tr>
                        <td>
                            {getCategoriesAsString(categories)}
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <p>{desc}</p>
                        </td>
                    </tr>
                    {getVideoIfExists(vid)}
                    {getImageIfExists(image)}
                </table>
            </div>

        """
    return t

def getCategoriesAsString(cats):
    s = ""
    for cat in cats:
        s += f"""<span class="category_badge">{cat}</span>"""

    return s

def getImageIfExists(img):
    if img.startswith("https"):
        return f"""<tr><td><img src="{img}" width="50%"></td></tr>"""
    return f"""<tr><td><img src="/static/{img}" width="50%"></td></tr>""" if img != "" else ""

def getVideoIfExists(vid):
    if vid:
        return f"""<tr><td><a href="{vid}" width="50%" class="link_button">Farm Video</a></td></tr>"""
    else:
        return ""
    
def getCategories(category):
    s = f"""

    <div class="home-categories">   
        <a href="/farms/?category=Overworld_Mobs" class="{"categories" if category != "Overworld_Mobs" else "selected_category"}">Overworld Mobs</a>
        <a href="/farms/?category=Nether_Mobs" class="{"categories" if category != "Nether_Mobs" else "selected_category"}">Nether Mobs</a>
        <a href="/farms/?category=End_Mobs" class="{"categories" if category != "End_Mobs" else "selected_category"}">End Mobs</a>
        <a href="/farms/?category=Blocks" class="{"categories" if category != "Blocks" else "selected_category"}">Blocks</a>
        <a href="/farms/?category=Other_Items" class="{"categories" if category != "Other_Items" else "selected_category"}">Other Items</a>
    </div>

    """
    return s.encode()


FARM_FILE = os.path.join(os.path.dirname(__file__), "farms_db.csv")
ALLOWED_CATEGORIES = {"Overworld_Mobs", "Nether_Mobs", "End_Mobs", "Blocks", "Other_Items"}

def newFarm(request):

    if request.method == "POST":
        name    = request.POST.get("name", "").strip()[:200]
        author  = request.POST.get("author", "").strip()[:200]
        mc_ver  = request.POST.get("minecraft_version", "").strip()[:50]
        desc    = request.POST.get("farm_description", "").strip()[:1000]
        vid     = request.POST.get("video_url", "").strip()[:200]
        img     = request.POST.get("img_url", "").strip()[:200]
        cats    = [c for c in request.POST.getlist("categories") if c in ALLOWED_CATEGORIES]

        with open(FARM_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, lineterminator='\n').writerow([name, author, mc_ver, desc, "|".join(cats) if cats else "", vid, img])
        return redirect("/farms/")
    
    return render(request, "submit_farm.html")