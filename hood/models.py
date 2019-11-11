from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class NeighbourHood(models.Model):
    neighbourhood_name = models.CharField(max_length = 100)
    neighbourhood_location = models.CharField(max_length = 100)
    occupants_count = models.IntegerField()
    image = models.ImageField(upload_to = 'media/', null=True)

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()   


    def __str__(self):
        return self.neighbourhood_name

class Profile(models.Model):
    full_name = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to = 'images/', blank = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE,null = True)
    userId =models.IntegerField(default = 0)
    user_email = models.EmailField()


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()   


    @classmethod
    def find_user(cls, profile_id):
        profile = cls.objects.get(id=profile_id)
        return profile

    @classmethod
    def update_profile(cls,profile,update):
         updated = cls.objects.filter(Image_name=profile).update(name=update)
         return updated

    def __str__(self):
        return self.full_name

class Businesses(models.Model):
    business_name = models.CharField(max_length = 150)
    business_description = models.TextField(blank= True)
    contact_person = models.CharField(max_length = 150)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    business_neighbourhood = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE,null = True)
    business_email = models.EmailField()
    business_image = models.ImageField(upload_to = 'media/')

    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save()

    def delete_business(self):
        Businesses.objects.filter().delete()
    
    @classmethod
    def get_businesses(cls):
        businesses = Businesses.objects.all()
        return businesses

    @classmethod
    def get_business(cls, post_id):
        single_business = cls.objects.get(id=post_id)
        return single_business

    @classmethod
    def search_by_business_name(cls,search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business

    class Meta:
        ordering = ['-id']

class Posts(models.Model):
    Status_Choices=(
        ('1','Urgent'),
        ('2','Necessary'),
        ('3','Unessential'),
    )
    user = models.ForeignKey(Profile,on_delete = models.CASCADE,related_name='profile')
    title = models.CharField(max_length = 60)
    post = models.TextField(blank= True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE,null = True)
    status= models.CharField(max_length=50, choices=Status_Choices,default='None')
    pub_date = models.DateField(auto_now_add=True)
    poster_id = models.IntegerField(default=0)

    def save_post(self):
        self.save()

    def delete_post(self):
        Posts.objects.filter().delete()
    
    @classmethod
    def get_posts(cls):
        posts = Posts.objects.all()
        return posts

    @classmethod
    def get_post(cls, post_id):
        single_post = cls.objects.get(id=post_id)
        return single_post

    @classmethod
    def search_by_title(cls,search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post

    class Meta:
        ordering = ['-id']

    
    def __str__(self):
        return self.title