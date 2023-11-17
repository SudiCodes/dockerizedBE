from django.apps import AppConfig


class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'

    # register signal when the app gets ready
    def ready(self):
        import blogapp.signals
