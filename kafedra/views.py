from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import article_main, gallery_main, gallery_foto, esp_kafedra_articles, eng_kafedra_articles, novosti_articles



def index(request):
    # главная статья про школу
    article_main_position1 = article_main.objects.filter(title='position1')
    gallery_main_title = gallery_main.objects.filter(position='position_main')
    # галерея картинок и названий традиций
    gallery_main_articles = gallery_main.objects.filter(show_item=True)
    # галерея актуальных фото
    gallery_foto_sch = gallery_foto.objects.filter(show_item=True)

    # блок отправки письма
    return render(request, 'index.html', {'article_main_position1': article_main_position1,
                                          'gallery_main_title': gallery_main_title,
                                          'gallery_foto_sch': gallery_foto_sch,
                                          'gallery_main_articles': gallery_main_articles})



def esp_kaf(request):
    # главная статья про школу
    esp_main_frase_1 = esp_kafedra_articles.objects.filter(position='position_1')
    esp_main_frase_2 = esp_kafedra_articles.objects.filter(position='position_profe')

    # блок отправки письма
    return render(request, 'main_pages/esp_kaf.html', {'esp_main_frase_1': esp_main_frase_1,
                                                       'esp_main_frase_2': esp_main_frase_2,

                                          })


def eng_kaf(request):
    # главная статья про школу
    eng_main_frase_1 = eng_kafedra_articles.objects.filter(position='position_1')
    eng_main_frase_2 = eng_kafedra_articles.objects.filter(position='position_profe')

    # блок отправки письма
    return render(request, 'main_pages/eng_kaf.html', {'eng_main_frase_1': eng_main_frase_1,
                                                       'eng_main_frase_2': eng_main_frase_2,

                                          })


def novosti(request):
    # главная статья про школу
    novosti_1 = novosti_articles.objects.filter(position='position_1')
    novosti_2 = novosti_articles.objects.filter(show_item=True)

    # блок отправки письма
    return render(request, 'main_pages/novosti.html', {'novosti_1': novosti_1,
                                                       'novosti_2': novosti_2,

                                          })