from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

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