import sendgrid

class Message:
    def __init__(self, _from, _to, _subject, _content ):
        self.client = sendgrid.SendGridClient('maliksjsu', 'Anaconda@2')
        self.message = sendgrid.Mail()
        self.set_from = _from
        self.to = _to 
        self.subject = _subject
        self.content = _content
        
    def send_message(self):

        self.message.add_to(self.to)
        self.message.set_from(self.set_from)
        self.message.set_subject(self.subject)
        self.message.set_html(self.content)

        status, msg = self.client.send(self.message)
        
        print ("SENDGRID- STATUS: " + str(status) + "  MSG: " + str(msg))