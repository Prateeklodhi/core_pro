from django.apps import AppConfig


class RecipesBookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes_book'

    
    def ready(self):
        import recipes_book.signals