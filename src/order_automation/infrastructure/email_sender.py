import smtplib
from email.message import EmailMessage


class EmailSender:

    def __init__(
        self,
        smtp_host: str,
        smtp_port: int,
        username: str,
        password: str,
    ):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send(
        self,
        recipient: str,
        subject: str,
        body: str,
        attachment: str,
    ):

        message = EmailMessage()

        message["From"] = self.username
        message["To"] = recipient
        message["Subject"] = subject

        message.set_content(body)

        with open(attachment, "rb") as file:

            message.add_attachment(
                file.read(),
                maintype="application",
                #subtype="xlsx",
                subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                filename=attachment,
            )
            
       #with something as variable:
        with smtplib.SMTP(
            self.smtp_host,
            self.smtp_port,
        ) as smtp:

            smtp.starttls()

            smtp.login(
                self.username,
                self.password,
            )

            smtp.send_message(message)

