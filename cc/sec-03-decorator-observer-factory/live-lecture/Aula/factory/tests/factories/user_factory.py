from model.user import User
import factory

factory.Faker._DEFAULT_LOCALE = "pt_BR"


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name = factory.Faker("name")
    email = factory.Faker("email")
    password = factory.Faker("word")


# python3 -m pip install -r dev-requirements.txt