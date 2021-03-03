from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('command')
        parser.add_argument('name')
        parser.add_argument('--experiment_id')
        parser.add_argument('--location', default='Montevideo')

    def handle(self, *args, **options):
        # experiment = Experiment(name=options['name'],location=options['location'])
        # experiment.save()
        # comentario
        subprocess.Popen(options['command'], shell=True)
