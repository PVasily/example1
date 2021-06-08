from rest_framework import serializers

from ..models import (
    BlogCategory,
    BlogPost,
    Customer,
    ProdCategories,
    Notebook,
    Smartphone, Cart
)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class BlogCategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogCategoryDetailSerialiser(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = BlogCategory
        fields = '__all__'

    @staticmethod
    def get_posts(obj):
        return BlogPostSerialiser(BlogPost.objects.filter(blog_category=obj), many=True).data


class BlogPostSerialiser(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostListRetrieveSerializer(serializers.ModelSerializer):
    blog_category = BlogCategorySerialiser()

    class Meta:
        model = BlogPost
        fields = '__all__'


#  #########  Cart ##########

class ProdCategorySerializer(serializers.ModelSerializer):
    # context = ProdCategories.objects.get_categories_for_left_sidebar()

    class Meta:
        model = ProdCategories
        fields = '__all__'


class NotebookListRetrieveSerializer(serializers.ModelSerializer):
    category = ProdCategorySerializer()

    class Meta:
        model = Notebook
        fields = '__all__'


class SmartphoneListRetrieveSerializer(serializers.ModelSerializer):
    category = ProdCategorySerializer()

    class Meta:
        model = Smartphone
        fields = '__all__'


# class ProdCategoryListRetrieveSerializer(serializers.ModelSerializer):

#     notebooks = serializers.SerializerMethodField()
#     smartphones = serializers.SerializerMethodField()

#     class Meta:
#         model = ProdCategories
#         fields = '__all__'

#     @staticmethod
#     def get_notebooks(obj):

#         return NotebookSerializer(Notebook.objects.filter(category=obj))

#     @staticmethod
#     def get_smartphones(obj):

#         return SmartphoneSerializer(Smartphone.objects.filter(category=obj))


class ProdCategoryListRetrieveSerializer(serializers.ModelSerializer):
    # context = serializers.SerializerMethodField()

    # print(context)

    class Meta:
        model = ProdCategories
        fields = '__all__'

    @staticmethod
    def get_context():
        context = ProdCategories.objects.get_categories_for_left_sidebar()
        return context

    @staticmethod
    def get_smartphones(obj):
        sm = SmartphoneSerializer(Smartphone.objects.filter(category=obj))
        # return SmartphoneSerializer(Smartphone.objects.filter(category=obj))
        print(sm)
        return sm


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = '__all__'


class SmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphone
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Cart
        fields = '__all__'
