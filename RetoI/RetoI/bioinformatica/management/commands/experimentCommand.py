from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('command')
        parser.add_argument('name')
        parser.add_argument('--experiment_id')
        parser.add_argument('--location', default='Montevideo')

    def handle(self, *args, **options):
        # if options['command'] == 'agrupar':
        #     exp_id = options['experiment_id']
        #     exp_obj = self.env['bioinformatica_experiment'].search([('experiment_id', '=', exp_id)])
        #     proj_id = exp_obj.project_id.project_id
        #     samp_id = exp_obj.sample_set.object.all()
        subprocess.Popen(options['command'], shell=True,
                         cwd='/Users/juanizquierdo/Documents/RETO/Reto_I_2021/RetoI/RetoI/media/UploadedFiles/PROJ_1/EXP_1/SAMP_1/FASTQs/FQ_1/')

#cat *.txt > archivo00.txt
#cd bioinformatica/media/UploadedFiles/PROJ_1/EXP_1/SAMP_1/FASTQs/FQ_1/