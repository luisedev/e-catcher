import email
from urllib.parse import urlparse

# Open the EML file
with open('email.eml', 'r') as f:
    # Parse the email
    msg = email.message_from_file(f)
    
    # Extract the subject
    subject = msg['Subject']
    
    # Extract the sender
    sender = msg['From']
    
    # Extract the recipients
    recipients = msg['To']
    
    # Extract the sender IP
    sender_ip = msg['X-Originating-IP']
    
    # Extract the sender domain
    sender_domain = sender.split('@')[1]
    
    # Extract the message-id
    msg_id = msg['Message-ID']
    
    # Extract the body
    body = msg.get_payload()
    
    # Extract the URLs
    urls = []
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            html = part.get_payload()
            for url in html:
                o = urlparse(url)
                urls.append(o.geturl())
                
    # Extract the domains
    domains = [urlparse(url).netloc for url in urls]
    
    # Print the results
    print('Subject:', subject)
    print('Sender:', sender)
    print('Recipients:', recipients)
    print('Sender IP:', sender_ip)
    print('Message-ID:', msg_id)
    print('Sender domain:', sender_domain)
    print('Body:', body)
    print('URLs:', urls)
    print('Domains:', domains)