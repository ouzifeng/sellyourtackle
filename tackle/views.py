from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Brand, Category, Product, ProductImage, ProductVisibility
from slugify import slugify
from decimal import Decimal, InvalidOperation
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView, RedirectView, View
from PIL import Image
from django.conf import settings
from django.contrib import messages

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    product.delete()
    return redirect(reverse('selling'))


@method_decorator(login_required, name='dispatch')
class ListProduct(View):
    template_name = 'list-product.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        # Get data from the form
        brand_name = request.POST.get('brand')
        category_name = request.POST.get('category')
        price = request.POST.get('price', 0)
        shipping = request.POST.get('shipping', 0)
        
        # Validation for positive price
        try:
            price = float(price)
            if price < 0:
                raise ValueError
        except ValueError:
            context = {
                'error_message': 'Please enter a valid positive price.'
            }
            return render(request, self.template_name, context)

        # Validation for positive shipping
        try:
            shipping = float(shipping)
            if shipping < 0:
                raise ValueError
        except ValueError:
            context = {
                'error_message': 'Please enter a valid positive shipping cost.'
            }
            return render(request, self.template_name, context)

        try:
            # Fetch brand and category from the database
            brand_instance = Brand.objects.get(name=brand_name)
            category_instance = Category.objects.get(name=category_name)
        except ObjectDoesNotExist:
            # Handle error if brand or category is not found
            context = {
                'error_message': 'Invalid brand or category. Please select from the suggestions.'
            }
            return render(request, self.template_name, context)

        name = request.POST.get('name')
        variation1 = request.POST.get('more-info-1', "")
        variation2 = request.POST.get('more-info-2', "")
        condition = request.POST.get('condition')
        description = request.POST.get('description')

        # Create product instance
        product = Product(
            brand=brand_instance,
            category=category_instance,
            name=name,
            variation1=variation1,
            variation2=variation2,
            condition=condition,
            description=description,
            price=price,
            shipping=shipping,
            user=request.user,
            visibility=ProductVisibility.LIVE
        )
        product.save()

        # Handle images
        for uploaded_file in request.FILES.getlist('images'):
            processed_image = process_image(uploaded_file)
            # Convert the processed image back to a Django InMemoryUploadedFile to save to the model
            from io import BytesIO
            from django.core.files.uploadedfile import InMemoryUploadedFile
            temp_file = BytesIO()
            processed_image.save(temp_file, format='JPEG')
            uploaded_file = InMemoryUploadedFile(temp_file, None, uploaded_file.name, 'image/jpeg', temp_file.tell(), None)
            
            product_image = ProductImage(product=product, image=uploaded_file)
            product_image.save()

        # If successful:
        context = {
            'success_message': 'Product added successfully!'
        }
        return render(request, self.template_name, context)
    
class SearchBrands(View):
    def get(self, request, *args, **kwargs):
        if 'term' in request.GET:
            brands = Brand.objects.filter(name__icontains=request.GET.get('term'))
            brand_list = list(brands.values_list('name', flat=True))
            return JsonResponse(brand_list, safe=False)
        return JsonResponse([], safe=False)

class SearchCategories(View):
    def get(self, request, *args, **kwargs):
        if 'term' in request.GET:
            cats = Category.objects.filter(name__icontains=request.GET.get('term'))
            cat_list = list(cats.values_list('name', flat=True))
            return JsonResponse(cat_list, safe=False)
        return JsonResponse([], safe=False)


class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(visibility=ProductVisibility.LIVE)
        return context



@method_decorator(login_required, name='dispatch')
class EditProduct(View):
    template_name = 'product-seller-page.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id, user=request.user)
        context = {
            'product': product
        }
        return render(request, self.template_name, context)

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id, user=request.user)
        
    
        # Check if the "delete_product" button was clicked
        if 'delete_product' in request.POST:
            product.delete()
            return redirect('selling')
        
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.shipping = request.POST.get('shipping')
        brand_name = request.POST.get('brand')
        brand_instance = Brand.objects.get(name=brand_name)
        product.brand = brand_instance
        category_name = request.POST.get('category')
        category_instance = Category.objects.get(name=category_name)
        product.category = category_instance
        product.variation1 = request.POST.get('more-info-1')
        product.variation2 = request.POST.get('more-info-2')
        product.description = request.POST.get('description')
        product.visibility = request.POST.get('visibility')
        
        product.save()
    
        images_to_delete = request.POST.getlist('delete_images')
        for image_id in images_to_delete:
            image = ProductImage.objects.get(id=image_id)
            image.delete()

        for uploaded_file in request.FILES.getlist('images'):
            ProductImage.objects.create(product=product, image=uploaded_file)        

        return redirect('selling')

class ProductPage(View):
    template_name = 'product.html'
    
    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        images = product.images.all()
        context = {
            'product': product,
            'images': images
        }
        return render(request, self.template_name, context)
    
    
@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('selling')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)    
    
def process_image(image, desired_size=(440, 300)):
    """
    Process an uploaded image using Pillow to fit a desired size.
    """
    img = Image.open(image)

    ratio = min(desired_size[0]/img.width, desired_size[1]/img.height)
    new_size = tuple([int(x*ratio) for x in img.size])

    img = img.resize(new_size, Image.LANCZOS)

    new_img = Image.new("RGB", desired_size, "white")
    
    y_offset = (desired_size[1] - img.height) // 2
    x_offset = (desired_size[0] - img.width) // 2
    new_img.paste(img, (x_offset, y_offset))

    return new_img    

class Cart:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, price):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(price), 'quantity': 1}
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()

    def save(self):
        """
        Mark the session as "modified" to ensure it's saved.
        """
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = self.cart.keys()
        # Get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
            self.cart[str(product.id)]['product_id'] = product.id  # Add this line

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Remove the cart from session.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
        
    def contains(self, product):
        """Check if the cart contains a particular product."""
        product_id = str(product.id)
        return product_id in self.cart

    def add(self, product, price):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(price), 'quantity': 1}
            self.save()        


class AddToCartView(View):
    def post(self, request, product_id):
        cart = Cart(request) 
        product = get_object_or_404(Product, id=product_id)

        if not product.is_in_stock():
            messages.warning(request, f"{product.name} is already sold!")
            return redirect('product', slug=product.slug)

        if cart.contains(product):
            messages.warning(request, f"{product.name} is already in your cart!")
            return redirect('product', slug=product.slug)

        cart.add(product, price=product.price)
        messages.success(request, f"{product.name} has been added to your cart!")
        return redirect('cart')


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)  
        return context

class RemoveFromCartView(View):
    def post(self, request, product_id):
        cart = Cart(request)  
        product = get_object_or_404(Product, id=product_id)

        cart.remove(product)

        return redirect('cart')

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)  # Pass the whole request object
        return context
    
    def post(self, request):
        cart = Cart(request)  # Pass the whole request object
        cart.clear()

        return redirect('checkout_success')

    