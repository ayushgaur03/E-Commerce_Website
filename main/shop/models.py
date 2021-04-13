from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    '''
    Using the ImageField, we will add an option of uploading image in the Django admin. Each time we upload image 
    over there the pic will get in to 'shop/images' folder of the shop-app. So we can see that in our project code.
    However, this is not a recommended method and we will make use of media directory by makaing changes in the 
    setting.py and urls.py of the main folder. This way we will upload pics but it will not save in the folder like
    we have given but we can simply see the pic attached to a particular product from the Django admin panel. This 
    way we can be aware about which pic is linked to which product.
    '''
    def __str__(self):
        return self.product_name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000, default="")
    name=models.CharField(max_length=5000, default="")
    email=models.EmailField(max_length=50, default="")
    phone=models.CharField(max_length=10,default="")
    address=models.CharField(max_length=5000, default="")
    city=models.CharField(max_length=5000, default="")
    state=models.CharField(max_length=5000, default="")
    zip_code=models.CharField(max_length=7, default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=500, default="")
    timestamp=models.DateField(auto_now_add=True)  #If no date is specified it will take the current timestamp

    def __str__(self):
        return self.update_desc[0:7]+ "..."
    
    


# After changing or adding fields in the models file we need to run two commands in the Terminal:
# 1) python manage.py makemigrations
'''
    The above command will create new files everytime we will run this command in the migrations
    folder of the app. These files basically store the data variables that will be used by database.
    At this point, it has not made any changes to database, for updating, we need to run next command.
'''

# 2) python manage.py migrate
''' 
    When we run the above cmd, Django will look for updates in the models. If suppose 
    it does not detect any changes then we can just reload our page and changes made
    in the models.py file will render. This happen mostly in cases when we added some
    functions to the models.py page wihtout changing the fields
'''

## Admin Login Details
'''
    username: ayush
    password: sukisadmin
'''