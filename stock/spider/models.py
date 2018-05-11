from django.db import models


# Create your models here.

class ShopId(models.Model):
    shop_id = models.CharField(max_length=20, primary_key=True)
    from_url = models.CharField(max_length=200, null=True)


class ShopInfo(models.Model):
    shop_id = models.CharField(max_length=20, primary_key=True)
    shop_name = models.CharField(max_length=200, default='')
    review_count = models.CharField(max_length=20, default='')
    avg_price = models.CharField(max_length=20, default='')
    taste = models.CharField(max_length=10, default='')
    env = models.CharField(max_length=10, default='')
    service = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=200, default='')
    open_time = models.CharField(max_length=200, default='')
    rank_star = models.CharField(max_length=20, default='')
    place = models.CharField(max_length=20, default='')
    classify = models.CharField(max_length=20, default='')
    star_all = models.CharField(max_length=20, default='')
    star_5 = models.CharField(max_length=20, default='')
    star_4 = models.CharField(max_length=20, default='')
    star_3 = models.CharField(max_length=20, default='')
    star_2 = models.CharField(max_length=20, default='')
    star_1 = models.CharField(max_length=20, default='')
    feature = models.BooleanField(default=False)
    feature2 = models.CharField(max_length=200, default='')


class ReviewDedail(models.Model):
    shop_id = models.CharField(max_length=20, primary_key=True)
    star_all = models.CharField(max_length=20, null=True)
    star_5 = models.CharField(max_length=20, null=True)
    star_4 = models.CharField(max_length=20, null=True)
    star_3 = models.CharField(max_length=20, null=True)
    star_2 = models.CharField(max_length=20, null=True)
    star_1 = models.CharField(max_length=20, null=True)
    first_review_time = models.CharField(max_length=100, null=True)
    first_review_content = models.TextField(null=True)


class Quote(models.Model):
    id = models.AutoField(max_length=20, primary_key=True)
    author = models.CharField(max_length=20, null=False)
    text = models.CharField(max_length=1000, null=True)
