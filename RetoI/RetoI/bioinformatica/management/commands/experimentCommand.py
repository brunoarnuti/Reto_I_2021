from django.core.management.base import BaseCommand
import subprocess
import os


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('command')
        parser.add_argument('name')
        parser.add_argument('project_id')
        parser.add_argument('--experiment_id')
        parser.add_argument('--location', default='Montevideo')

    def handle(self, *args, **options):
        # if options['command'] == 'agrupar':
        exp_id = options['experiment_id']
        print(options['command'].split('\r\n'))
        list_commands = options['command'].split('\r\n')
        for command in list_commands:
            if command.__contains__('cat'):
                p = subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE)
                out = p.communicate()[0].decode("utf-8").rstrip('\r\n') + '\\media\\UploadedFiles\\PROJ_' + str(
                    options['project_id']) + '\\EXP_' + str(options['experiment_id']) + '\\'
                out = out.replace('\\', '/')
                d = []
                for file in os.listdir(out.rstrip('\r\n')):
                    r = os.path.join(out, file)
                    d.append(r)
                for direccion in d:
                    for base, dirs, files in os.walk(direccion):
                        base = base.replace('\\', '/')
                        listBase = base.split('/')
                        if listBase[len(listBase) - 1].startswith('FQ') and len(base) != 0:
                            print(base + ' El popen se ejecuta acá')
                            command = 'cat *.txt > archivo_0.txt'
                            subprocess.Popen(command, shell=True, cwd=base)
            elif command.__contains__('nextflow'):
                print()
            else:
                subprocess.Popen(command, shell=True)
