from . import BaseTestCase

from {{cookiecutter.repo_name}} import {{cookiecutter.repo_name}}


class Test{{cookiecutter.repo_name|capitalize}}Integration(BaseTestCase):

    def test_some_long_running_non_mocked_thing(self):
        self.assertEquals(
            'Hello World!',
            {{cookiecutter.repo_name}}(),
        )

