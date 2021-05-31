from websites.models import Profile, Project, Review
from django.test import TestCase
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    '''Test methods of profile model'''

    def setUp(self):
        self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        self.profile=Profile(profile_photo='imageurl.png',bio='Lorem ipsum',contact='2222356',user=self.user_1)

    
    def tearDown(self):
        self.user_1.delete()
        self.profile.delete()

    def test_save_profile(self):
        self.user_1.save()
        self.profile.save()

        profiles = Profile.objects.all()

        self.assertTrue(len(profiles)>0)


    def test_update_profile(self):
        self.user_1.save()
        self.profile.save()

        update_details = {'profile_photo':'newlink.png',
                               'bio':'new bio',
                               'contact':'2564895',
                                'user':self.user_1
                             }


        Profile.update_profile(update_details, self.profile.id)

        self.updated_profile= Profile.objects.get(pk = self.profile.id) #get new updated profile

        cloudinary_url_prefix = 'http://res.cloudinary.com/dtw9t2dom/image/upload/'

        self.assertEqual(self.updated_profile.profile_photo.url, cloudinary_url_prefix+'newlink.png')

    
    def test_delete_profile(self):
        self.user_1.save()
        self.profile.save()

        self.newprof = Profile.objects.get(pk=self.profile.id)

        self.newprof.delete_profile()

        self.assertTrue(len(Profile.objects.all()) == 0)



class ProjectTestClass(TestCase):
    '''Test methods of Project model'''

    def setUp(self):
        self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        self.project=Project(image='newimageurl.png',title='Test Project',description='Lorem ipsum',link='https://google.com',user=self.user_1)

    
    def tearDown(self):
        self.project.delete()
        self.user_1.delete()


    def test_save_project(self):
        self.user_1.save()
        self.project.save()

        projects = Project.objects.all()

        self.assertTrue(len(projects)>0)

    
    def test_update_caption(self):
        self.user_1.save()
        self.project.save()

        update_details = {'image':'newlink.png',
                               'title':'image_name',
                                'description':'some image description', 'link':'https://moringaschool.com',
               
                                'user':self.user_1,
                             }


        Project.update_project(update_details, self.project.id)

        self.updated_project = Project.objects.get(pk = self.project.id) #get new updated project

        cloudinary_url_prefix = 'http://res.cloudinary.com/dtw9t2dom/image/upload/'

        self.assertEqual(self.updated_project.image.url, cloudinary_url_prefix+'newlink.png')



    def test_delete_project(self):
        self.user_1.save()
        self.project.save()

        self.project2 = Project.objects.get(pk=self.project.id)



        self.project2.delete_project()

        projects = Project.objects.all()

        self.assertTrue(projects.count() == 0)




class TestReviewClass(TestCase):
    '''Test methods of Comment model'''

    def setUp(self):
        self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        self.project=Project(image='newimageurl.png',title='Test Project',description='Lorem ipsum',link='https://google.com',user=self.user_1)
        self.review = Review(design=2,usability=5,content=8,count=1,project=self.project)

    
    def tearDown(self):
        self.project.delete()
        self.user_1.delete()
        self.review.delete()


    def test_save_review(self):
        self.user_1.save()
        self.project.save()
        self.review.save()

        self.assertTrue( len(Review.objects.all()) > 0)





    
       



