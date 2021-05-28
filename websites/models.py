from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()
    contact = models.CharField(max_length=60)
    user = models.OneToOneField(
                User,
                on_delete=models.CASCADE,
            )

    def save_profile(self):
        return self.save()


    @classmethod
    def update_profile(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(profile_photo=update_details['profile_photo'],
                                               bio=update_details['bio'],
                                               user=update_details['user'])

    def delete_profile(self):
        return self.delete()


    class Meta:
        ordering = ["-pk"]


    def __str__(self):
        return f'{self.user.username}'


class Project(models.Model):
    title = models.CharField(max_length=60)
    image = CloudinaryField('image')
    link = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='projects')
    
    


    def save_project(self):
        return self.save()
       

    @classmethod
    def update_caption(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(image=update_details['image'],
                                               name=update_details['name'],
                                               caption=update_details['caption'],
                                               profile=update_details['profile'])
    


    def delete_image(self):
        return self.delete()

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f'Image: {self.title} '



class Review(models.Model):
    design = models.IntegerField( validators=[
                                    MaxValueValidator(10),
                                    MinValueValidator(0)
                                ])

    usability = models.IntegerField( validators=[
                                    MaxValueValidator(10),
                                    MinValueValidator(0)
                                ])

    content = models.IntegerField( validators=[
                                    MaxValueValidator(10),
                                    MinValueValidator(0)
                                ])

    project = models.OneToOneField(
                Project,
                on_delete=models.CASCADE,
                related_name='review'
            )