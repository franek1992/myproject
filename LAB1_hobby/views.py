from django.shortcuts import render

def lab1_home(request):
    context = {
        "hobby_name": "Fotografia",
        "description": "Zatrzymywanie chwil w kadrze. Moja pasja, która pozwala patrzeć na świat inaczej."
    }
    return render(request, 'LAB1_hobby/home.html', context)

def lab1_about(request):
    context = {
        "title": "O mojej pasji",
        "details": "Fascynuję się głównie fotografią krajobrazową oraz uliczną (street photography)."
    }
    return render(request, 'LAB1_hobby/about.html', context)

def lab1_gallery(request):
    context = {
        "title": "Moja Galeria",
        "items": ["Zdjęcie z gór", "Kadr z miasta", "Portret w plenerze"]
    }
    return render(request, 'LAB1_hobby/gallery.html', context)
