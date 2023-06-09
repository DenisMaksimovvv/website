from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
    
class ProductPageView(TemplateView):
    template_name = "product.html"

class StorePageView(TemplateView):
    template_name = "store.html"
    
    