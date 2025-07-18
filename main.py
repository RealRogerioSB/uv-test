def send_email(subject: str, body: str, sender: str, password: str, recipients: list[str]) -> None:
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg: MIMEMultipart = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(sender, password)
        try:
            smtp_server.send_message(msg)
        except smtplib.SMTPAuthenticationError:
            print("Erro de autenticação com o servidor SMTP.")
        except (smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected):
            print("Erro/falha de conexão com o servidor SMTP.")
        except smtplib.SMTPException as e:
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
