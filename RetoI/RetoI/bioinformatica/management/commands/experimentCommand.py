from django.core.management.base import BaseCommand
from bioinformatica.models.experiment import Experiment

class Command(BaseCommand):
    def add_arguments(selfself,parser):
        parser.add_argument('name')
        parser.add_argument('--experiment_id')
        parser.add_argument('--location',default = 'Montevideo')

    def handle(self,*args,**options):
        #experiment = Experiment(name=options['name'],location=options['location'])
        #experiment.save()
        self.stdout.write(self.style.SUCCESS('Added experiment'))