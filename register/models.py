from django.db import models
#from django.forms import ModelForm

# Create your models here.
class register (models.Model):
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    
    def __str__(self):
        return f"{self.name},{self.password}"







"""
    # Create a Django form.
class registerForm(ModelForm):
    class Meta:
        model = register
        fields = ['name', 'password']
# Save the form data to the database.
form = registerForm()
if form.is_valid():
    form.save()    """