import unittest as test
from main import vowel_change


class TestString(test.TestCase):
    def test_vowel_change(self):
        self.assertEqual(vowel_change("hannah hannah bo-bannah banana fanna fo-fannah fee, fy, mo-mannah. hannah!", 'i'),
            'hinnih hinnih bi-binnih binini finni fi-finnih fii, fy, mi-minnih. hinnih!')
        self.assertEqual(vowel_change('adira wants to go to the park', 'o'), 'odoro wonts to go to tho pork')