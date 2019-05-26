import smtplib
from email.message import EmailMessage

def sendEmail(receiver, topic, content):

    subjects = {'recipe': 'Recipe from the recipe-application', 'shoppinglist': 'Shoppinglist from the recipe-application'}
    messages = {'recipe': 'This is your chosen recipe. Enjoy!!\n',
                'shoppinglist': 'This is your shopping list: '}

    msg = EmailMessage()
    msg['Subject'] = subjects[topic]
    msg['From'] = 'codingathsg@gmail.com'
    msg['To'] = receiver

    if topic == 'recipe':
        recipemail = []
    
        content[1] = '<br>'.join(content[1].split('\n'))
        # Construct the email in HTML
        recipemail.append('<DOCTYPE HTML!>\n<html>\n<body>')
        recipemail.append('<h1>' +messages[topic] +'</h1>')
        recipemail.append(f'The price is approximately: {content[0]} CHF in Coop! (For more info check the shopping list)<br><br>{content[1]}<br><br>{content[2]}')
        recipemail.append('</body>\n</html>')
        recipemail = '<br>'.join(recipemail)

        msg.set_content(messages[topic] +'\n' +str(recipemail))
        msg.add_alternative(recipemail, subtype='html')

    if topic == 'shoppinglist':

        try:
            for i in range(len(content[1])):
                content[0].remove('0,0,0.0')
                content[1].remove(0.0)
        except ValueError:
            pass

        shoppinglist = []

        # Construct the email in HTML
        shoppinglist.append('<DOCTYPE HTML!>\n<html>\n<body>')
        shoppinglist.append('<h1>' + messages[topic] + '</h1>')
        shoppinglist.append(f'<p> The price is approximately: {content[2]} CHF in Coop!</p><br>')
        for i in range(len(content[0])):
            shoppinglist.append((f'{content[0][i].split(",")[0:2]} - { "%.2f" % (content[1][i])} CHF'))
        shoppinglist.append('</body>\n</html>')
        shoppinglist = '<br>'.join(shoppinglist)

        msg.set_content(messages[topic] + '\n' + str(shoppinglist))
        msg.add_alternative(shoppinglist, subtype='html')

    # Send the constructed messages
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('codingathsg@gmail.com', ']GcU[2za<p3ms<w8')
            smtp.send_message(msg)


if __name__ == '__main__':
    pass
