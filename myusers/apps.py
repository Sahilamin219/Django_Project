from django.apps import AppConfig


class MyusersConfig(AppConfig):
    name = 'myusers'

    def ready(self):
    	import myusers.signals
