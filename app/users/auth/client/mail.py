from worker.celery import send_email_task


class MailClient:

    @staticmethod
    def send_welcome_mail(to: str)->None:
        return send_email_task.delay(
            f"Welcome email",
            f"Welcome email to {to}",
            to
        )
