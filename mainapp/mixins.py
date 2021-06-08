from django.views import View

from mainapp.models import Customer, Cart


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                castomer = Customer.objects.create(user=request.user)
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        else:
            cart = Cart.objects.filter(for_anonymously_user=True).first()
            if not cart:
                 cart = Cart.objects.create(for_anonymously_user=True)
        self.cart = cart
        self.cart.final_price = 0
        print(self.cart.final_price)
        self.cart.save()
        return super().dispatch(request, *args, **kwargs)