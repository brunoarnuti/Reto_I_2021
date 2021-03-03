from celery import shared_task
from django.core.management import call_command


@shared_task(bind=True)
def printer(self, exp):
    print(f"Tomando experimento nro: {exp}")
    call_command("experimentCommand", exp.executionCommands, exp.name, experiment_id=exp.id)
    print("casdasd")


