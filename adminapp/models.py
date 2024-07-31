from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

professions = [
    ("Medical Doctor", "Medical Doctor"),
    ("Engineer", "Engineer"),
    ("Lawyer", "Lawyer"),
    ("Teacher", "Teacher"),
    ("Nurse", "Nurse"),
    ("Software Developer", "Software Developer"),
    ("Architect", "Architect"),
    ("Chef", "Chef"),
    ("Accountant", "Accountant"),
    ("Dentist", "Dentist"),
    ("Pharmacist", "Pharmacist"),
    ("Psychologist", "Psychologist"),
    ("Graphic Designer", "Graphic Designer"),
    ("Electrician", "Electrician"),
    ("Plumber", "Plumber"),
    ("Mechanic", "Mechanic"),
    ("Artist", "Artist"),
    ("Writer", "Writer"),
    ("Photographer", "Photographer"),
    ("Musician", "Musician"),
    ("Dancer", "Dancer"),
    ("Marketing Specialist", "Marketing Specialist"),
    ("Consultant", "Consultant"),
    ("Financial Advisor", "Financial Advisor"),
    ("Real Estate Agent", "Real Estate Agent"),
    ("IT Specialist", "IT Specialist"),
    ("Web Developer", "Web Developer"),
    ("Data Scientist", "Data Scientist"),
    ("Project Manager", "Project Manager"),
    ("Human Resources Manager", "Human Resources Manager"),
    ("Event Planner", "Event Planner"),
    ("Fitness Trainer", "Fitness Trainer"),
    ("Interior Designer", "Interior Designer"),
    ("Journalist", "Journalist"),
    ("Translator", "Translator"),
    ("Law Enforcement Officer", "Law Enforcement Officer"),
    ("Firefighter", "Firefighter"),
    ("Paramedic", "Paramedic"),
    ("Flight Attendant", "Flight Attendant"),
    ("Pilot", "Pilot"),
    ("Veterinarian", "Veterinarian"),
    ("Biologist", "Biologist"),
    ("Chemist", "Chemist"),
    ("Geologist", "Geologist"),
    ("Meteorologist", "Meteorologist"),
    ("Librarian", "Librarian"),
    ("Social Worker", "Social Worker"),
    ("others", "others"),
]

branches = [
        ('Evbotubu', 'Evbotubu'),
        ('GRA', 'GRA'),
        ('Sakpoba', 'Sakpoba'),
        ('Italy', 'Italy'),
        ('Uselu', 'Uselu'),
        ('United Kingdom', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('USA', 'USA'),
        # Add more branches as needed
    ]

class User(AbstractUser):  
    phonenumber = models.CharField(max_length=15)
    profession = models.CharField(max_length=50, choices=professions)
    location = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='user_images/', null=True, blank=True)
    church_branch = models.CharField(max_length=50, choices=branches)


class Meeting(models.Model):
    week = models.CharField(max_length=20)
    date = models.DateField()
    link = models.URLField()
    attendees = models.ManyToManyField(User, related_name='attended_meetings')
    is_meeting_done= models.BooleanField(default=False)

    def __str__(self):
        return f"Meeting on {self.date}"
    
class AdminSetting(models.Model):
    number_of_meetings =models.IntegerField(default=10)
    def __str__(self):
        return f"Meeting setting {self.pk}, Number of Meeting {self.number_of_meetings}"


