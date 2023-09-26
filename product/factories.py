import factory

from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
  title = factory.Faker('pystr')
  slug = factory.Faker('pystr')
  description = factory.Faker('pystr')
  active = factory.Iterator([True, False])

  class Meta:
    model = Category

class ProductFactory(factory.django.DjangoModelFactory):
  price = factory.Faker('pystr')
  Category = factory.LazyAttribute(CategoryFactory)
  title = factory.Faker('pystr')

  @factory.post_generation
  def Category(self, create, extracted, **kwargs):
    if not create:
      return
    
    if extracted:

      for Category in extracted:
        self.category.add(category)

  class Meta:
    model = Product
