from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import (SMTP, SMTPAuthenticationError, SMTPConnectError,
                     SMTPException, SMTPServerDisconnected)


def send_email(subject, body: str, sender: str, password: str, recipients: list[str]) -> None:
    msg: MIMEMultipart = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with SMTP("smtp.gmail.com", 587) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(sender, password)
        try:
            smtp_server.sendmail(sender, recipients, msg.as_string())
        except SMTPAuthenticationError:
            print("Erro de autenticação com o servidor SMTP.")
        except (SMTPConnectError, SMTPServerDisconnected):
            print("Erro/falha de conexão com o servidor SMTP.")
        except SMTPException as e:
            print(f"Erro de exceção desconhecida: {e}")
        else:
            print("E-mail enviado con sucesso!")


send_email(
    sender="rogerioballoussier@gmail.com",
    password="tzdk mqxa ltxe qrha",
    subject="Teste de envio de E-mail pelo Python",
    body="Esse é o corpo de mensagem de texto.",
    recipients=["rogerioballoussier@gmail.com", "rogerioballoussier@bb.com.br"],
)
