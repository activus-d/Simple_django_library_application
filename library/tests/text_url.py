from django.urls import reverse, resolve


class TestUrls:
    def test_book_list(self):
        path = reverse('book_list')
        assert resolve(path).view_name == 'book_list'
