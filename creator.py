
from pyscript import display, document # pyright: ignore[reportMissingImports]

creator = {
    "Name": "Rhys Lozano",
    "Nickname": "Kuch",
    "Grade & Section": "10 - Topaz",
    "Hobbies": "Reading, coding, and listening to music",
    "Interests": "Technology, literature, and creativity",
    "Fun Fact": "I enjoy creating projects using Python and HTML!"
}

def show_creator(e):
    document.getElementById("output").innerHTML = ""

    display(f"Name: {creator['Name']}", target="output")
    display(f"Nickname: {creator['Nickname']}", target="output")
    display(f"Grade & Section: {creator['Grade & Section']}", target="output")
    display(f"Hobbies: {creator['Hobbies']}", target="output")
    display(f"Interests: {creator['Interests']}", target="output")
    display(f"Fun Fact: {creator['Fun Fact']}", target="output")