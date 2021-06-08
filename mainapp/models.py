from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.urls import reverse

User = get_user_model()


class Good(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Goods"
        verbose_name_plural = "Good"
        ordering = ['title']


class Things(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Goods"
        verbose_name_plural = "Good"


class BlogCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя категории")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPostQuerySet(models.QuerySet):

    def find_by_title_in_qs(self, post_title):
        return self.filter(title__icontains=post_title)


class BlogPostManager(models.Manager):

    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().filter(in_arhive=False)

    def find_by_title_in_qs(self, post_title):
        return self.get_queryset().find_by_title_in_qs(post_title)


def upload_path(instance, filename):
    return '/'.join(['images', str(instance.title), filename])


class BlogPost(models.Model):
    blog_category = models.ForeignKey(BlogCategory, verbose_name="Имя категории", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название поста")
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    pub_date = models.DateTimeField(auto_now=True)
    in_arhive = models.BooleanField(default=False)
    objects = BlogPostManager()

    def __str__(self):
        return f"{self.title} из категории \"{self.blog_category.name}\""


# ProdCategories
# Product
# CartProduct
# Cart
# Customer
# Specification
# Order

def get_model_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_products_url(obj, viewname):
    ct_model = obj.__class__.__meta__.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class CategoryManager(models.Manager):
    CATEG_NAME_CAT_COUNT = {
        'Ноутбуки': 'notebook__count',
        'Смартфоны': 'smartphone__count'
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_model_for_count('notebook', 'smartphone')
        qs = list(self.get_queryset().annotate(*models).values())

        return [dict(name=c['name'], slug=c['slug'], count=c[self.CATEG_NAME_CAT_COUNT[c['name']]]) for c in qs]


# class LatestProdManager:

#     @staticmethod
#     def get_products_for_main_page():
#         user_type = ContentType.objects.get(app_label='mainapp', model='notebook')
#         return user_type
#         # with_respect_to = kwargs.get('with_respect_to')
#         # products = []
#         # ct_models = ContentType.objects.filter(model__in=args)
#         # for ct_model in ct_models:
#         #     model_product = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
#         #     products.extend(model_product)
#         # # if with_respect_to:
#         # #     ct_model = ContentType.objects.filter(model=with_respect_to)
#         # #     if ct_model.exists():
#         # #         if with_respect_to in args:
#         # #             return sorted(
#         # #                 products, key=lambda x: x.__class__._meta.model_name(with_respect_to), reverse=True
#         # #             )
#         # return products

# class LPs:

#     objects = LatestProdManager()


class ProdCategories(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя категории")
    slug = models.SlugField(unique=True)

    objects = CategoryManager()

    def __str__(self):
        return self.name


# ------------ manager Product --------------------------------
class ProductQuerySet(models.QuerySet):

    def find_by_title_in_qs(self, product_title):
        return self.filter(title__icontains=product_title)


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    # def all(self):
    #     return self.get_queryset().filter(in_arhive=False)

    def find_by_title_in_qs(self, product_title):
        return self.get_queryset().find_by_title_in_qs(product_title)


# --------------------------------------------------------------

class Product(models.Model):
    category = models.ForeignKey(ProdCategories, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Продукт")
    # specifications = models.ForeignKey('Specification', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    discription = models.TextField(verbose_name="Описание продукта", null=True)
    image = models.ImageField(verbose_name="Изображение", upload_to='img_prod')
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Notebook(Product):
    diagonal = models.CharField(max_length=20, verbose_name='Диагональ')
    display_type = models.CharField(max_length=20, verbose_name='Тип дисплея')
    processor = models.CharField(max_length=20, verbose_name='Процессор')
    video = models.CharField(max_length=20, verbose_name='Видео')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)


class Smartphone(Product):
    diagonal = models.CharField(max_length=20, verbose_name='Диагональ')
    display_type = models.CharField(max_length=20, verbose_name='Тип дисплея')
    processor = models.CharField(max_length=20, verbose_name='Процессор')
    sd_volume = models.CharField(max_length=20, verbose_name='Встр. память')
    accume_value = models.CharField(max_length=20, verbose_name='Длит. зарядки')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name="Покупатель", on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name="Корзина", on_delete=models.CASCADE, related_name='related_product')
    # product = models.ForeignKey(Product, verbose_name="Товар в корзине",on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Общая цена")

    def __str__(self):
        return 'Продукт: {} (для корзины)'.format(self.content_object.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Корзина', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymously_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name="Адрес")
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    customer = models.ForeignKey(Customer, verbose_name="Покупатель", on_delete=models.CASCADE,
                                 related_name='related_customer')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField(max_length=100, verbose_name='Тип заказа', choices=BUYING_TYPE_CHOICES,
                                   default=BUYING_TYPE_SELF)
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='Дата создания заказа', auto_now=True)
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)

# class Specification(models.Model):
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     name = models.CharField(max_length=255, verbose_name="Имя товара для характеристик")

#     def __str__(self):
#         return "Характеристики для товара: {}".format(self.name)
