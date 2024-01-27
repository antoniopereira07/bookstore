import factory
from django.contrib.auth.models import User
from order.models.order import Order


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_post_generation_save = True

    email = factory.Faker("pystr")
    username = factory.Faker("pystr")


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.products.add(product)

    class Meta:
        model = Order
