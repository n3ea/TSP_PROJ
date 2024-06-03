
#tbase/tbase/book/apps.py
from django.apps import AppConfig

class BookConfig(AppConfig):
    name = 'book'

    def ready(self):
        import book.signals


# class NewsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'book'
