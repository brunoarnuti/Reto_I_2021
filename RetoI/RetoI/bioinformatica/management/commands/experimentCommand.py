from django.core.management.base import BaseCommand
import subprocess
import os

class Command(BaseCommand):
    def recursivePath(self,path,dirs,command):
        for nombre_directorio, dirs, ficheros in os.walk(dirs):
            print(nombre_directorio)
            for nombre_fichero in ficheros:
                print(nombre_fichero)

    def dirs(x, n):  # funcion principal
        di = glob(x + "/" + "*")  # vemos todo lo que esta adentro del directorio que nos manden
        tabs = "  " * n  # Algo de vista
        do = x.split('/')  # Esto es para mostrar el archivo(por culpa de glob)
        print (tabs + do[-1] + " /")  # Mostramos la vista
        for i in di:  # Recorremos el directorio
            if path.isdir(i):  # Si es direcotorio
                dirs(i, n + 1)  # Empezamos la función recursiva
            elif path.isfile(i):  # Si es archivo
                do = i.split('/')  # gracias a glob :/
                print("|" + tabs + do[-1] ) # Lo mostramos

    if __name__ == "__main__":  # Asi se ejecutan los scripts
        dirs(".", 0)  # Iniciamos el script buscando en el directorio actual
    def add_arguments(self, parser):
        parser.add_argument('command')
        parser.add_argument('name')
        parser.add_argument('project_id')
        parser.add_argument('--experiment_id')
        parser.add_argument('--location', default='Montevideo')

    def handle(self, *args, **options):
        # if options['command'] == 'agrupar':
        exp_id = options['experiment_id']
        #exp_obj = options['experiment']
        #proj_id = exp_obj.project_id.project_id
        #samp_id = exp_obj.sample_set.object.all()
        #samp_obj = self.env['bioinformatica_sample'].search([('sample_id','=',samp_id)])
        p = subprocess.Popen('echo %cd%',shell=True, stdout=subprocess.PIPE)
        out = p.communicate()[0].decode("utf-8").rstrip('\r\n') + '\\media\\UploadedFiles\\PROJ_' + str(options['project_id']) + '\\EXP_' + str(options['experiment_id']) + '\\'
        out = out.replace('\\','/')
        print(out)
        d = []
        for file in os.listdir(out.rstrip('\r\n')):
            r = os.path.join(out,file)
            print('R en este caso es: ' + r)
            d.append(r)
            print('D en este caso va siendo: ')
            #print(d)
            #print(type(d))
        #print(d + 'Este es el d')
        #self.dirs()
        #self.recursivePath('',d,options['command'])
        for direccion in d:
            #print('La direccion: ' + direccion)
            for base, dirs, files in os.walk(direccion):
                comando = 'cat *.txt > archivo0.txt'
                base = base.replace('\\','/')
                #print('La base : ' + base)
                listBase = base.split('/')
                #print(listBase)
                #print(listBase[len(listBase)-1])
                #print(len(base))
                if listBase[len(listBase)-1].startswith('FQ') and len(base)!=0:
                    print(base + ' El popen se ejecuta acá')
                    subprocess.Popen(comando, shell=True,cwd=base)




        ##subprocess.Popen(options['command'], shell=True,
        #                cwd='/Users/juanizquierdo/Documents/RETO/Reto_I_2021/RetoI/RetoI/media/UploadedFiles/PROJ_1/EXP_1/SAMP_1/FASTQs/FQ_1/')

#cat *.txt > archivo00.txt
#cd bioinformatica/media/UploadedFiles/PROJ_1/EXP_1/SAMP_1/FASTQs/FQ_1/