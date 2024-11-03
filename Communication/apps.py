from django.apps import AppConfig


class CommunicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Communication'

    def ready(self):
        import Communication.signals
        