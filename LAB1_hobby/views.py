from django.shortcuts import render

# Przywrócona funkcja strony głównej lab1
def lab1_home(request):
    return render(request, 'LAB1_hobby/home.html') # upewnij się, że nazwa szablonu jest zgodna z Twoją

# Funkcja galerii, którą dodaliśmy wcześniej
def lab1_gallery(request):
    context = {
        "title": "Moja Galeria",
        "photos": [
            {"title": "Zdjęcie z gór", "filename": "gory.jpg"},
            {"title": "Kadr z miasta", "filename": "miasto.jpg"},
            {"title": "Portret w plenerze", "filename": "portret.jpg"}
        ]
    }
    return render(request, 'LAB1_hobby/gallery.html', context)

def lab1_about(request):
    return render(request, 'LAB1_hobby/about.html')
