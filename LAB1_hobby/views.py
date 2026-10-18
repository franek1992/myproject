from django.shortcuts import render

def lab1_home(request):
    context = {
        "hobby_name": "Moja pasja: Fotografowanie",
        "description": "Tutaj dzielę się moimi ulubionymi kadrami, technikami oraz sprzętem, którego używam do uwieczniania chwil."
    }
    return render(request, 'LAB1_hobby/home.html', context)

def lab1_about(request):
    context = {
        "hobby_name": "O moim hobby",
        "description": "Fotografia to dla mnie coś więcej niż tylko robienie zdjęć – to sposób patrzenia na świat i zatrzymywania czasu."
    }
    return render(request, 'LAB1_hobby/about.html', context)

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
