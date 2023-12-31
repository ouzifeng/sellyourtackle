from django.test import TestCase
from django.urls import reverse
from .models import Product, Category, Brand
from .forms import CheckoutForm, ContactSellerForm
from .views import ProductPage, ProductDeleteView, SearchView, ShopView
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryModelTest(TestCase):
    """
    Test class for the Category model.
    Tests the creation of Category instances.
    """
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")


class CheckoutFormTest(TestCase):
    """
    Test class for the CheckoutForm.
    Validates the form for correct data inputs.
    """
    def test_checkout_form_valid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'phone_number': '1234567890',
            'billing_address_line1': '123 Main St',
            'billing_city': 'City',
            'billing_state': 'State',
            'billing_postal_code': '12345',
            'payment_method': 'pm_12345'
        }
        form = CheckoutForm(data=form_data)
        self.assertTrue(form.is_valid())


class ContactSellerFormTest(TestCase):
    """
    Test class for the ContactSellerForm.
    Ensures the form is valid with correct inputs.
    """
    def test_contact_seller_form_valid(self):
        form_data = {'subject': 'Test Subject', 'message': 'Test message'}
        form = ContactSellerForm(data=form_data)
        self.assertTrue(form.is_valid())


class SearchViewTest(TestCase):
    """
    Test class for the SearchView.
    Verifies the functionality of the search feature.
    """
    def test_search_view(self):
        response = self.client.get(reverse('search'), {'search_text': 'query'})
        self.assertEqual(response.status_code, 200)


class ShopViewTest(TestCase):
    """
    Test class for the ShopView. Tests the view response and functionality.
    """
    def test_shop_view(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
