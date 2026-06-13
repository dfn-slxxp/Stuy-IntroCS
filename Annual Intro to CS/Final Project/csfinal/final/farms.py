from django.shortcuts import render
import csv, os

def renderFarms(request):
    page = render(request, "farms.html")

    for i in range(3):
        page.content += f"""
        
            <table>

        """.encode('utf-8')

    page.content += endhtml()
    return page

def endhtml():
    return b"<p>this is a test</p></body></html>"

FARM_FILE = os.path.join(os.path.dirname(__file__), "farms_data.csv")
ALLOWED_CATEGORIES = {"Overworld_Mobs", "Nether_Mobs", "End_Mobs", "Blocks", "Other_Items"}


def newFarm(request):

    if request.method == "POST":


    return render(request, "submit_farm.html")