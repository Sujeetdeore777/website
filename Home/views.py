from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
    form = ContactForm(request.POST)
    return render(request,'index.html',{'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Create an EmailMessage
            subject = 'New Contact Form Submission'
            body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            sender_name = name # Replace with your name
            sender_email = 'sujeetdeore777@gmail.com'  # Replace with your Gmail email address
            recipients = ['sam@gmail.com']  # Replace with your email address

            email_message = EmailMessage(subject, body, f'{sender_name} <{sender_email}>', to=recipients)


            try:
                # Send the email
                email_message.send()
                return HttpResponse("Message sent successfully")
            except Exception as e:
                print(f"Email sending failed: {e}")
                return HttpResponse("Failed to send message. Please try again later.")
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})