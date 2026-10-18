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
