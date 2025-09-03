from django.shortcuts import render

def show_main(request):
    context = {
        'npm': '2406398381',
        'name': 'Prasetya Surya Syahputra',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
