from random import Random


@provides(
    type='function',
    name='get_user_applications',
    description='Retrieve all applications registered for the current user.',
    arguments={},
    is_public=True,
    is_async=False,
)
def get_user_applications():
    """
    Retrieve all applications registered for the current user.
    """
    return ["home"]

@provides(
    type='class_singleton',
    name='get_home_config',
    description='Retrieve the configuration settings for the home application.',
    arguments={},
    is_public=True,
    is_async=False,
)
class HomeConfig:
    random_int: int = Random().randint(0, 100)

    def get_wathever(self):
        return self.random_int