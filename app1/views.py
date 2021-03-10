from django.shortcuts import render
from app1.models import Product
from app1.contact import ContactForm
from app1.forms import DetailsForm

# Create your views here.

def fetch_data(request):
    product_list=Product.objects.all()


    item_name=request.GET.get('item_name')#item_name=pedigree
    if item_name!='' and  item_name!=None:
        product_list=product_list.filter(name__contains=item_name)






    my_dict={'product_list':product_list}
    return render(request,"home.html",my_dict)







def displayView(request):
    form=DetailsForm()
    my_dict={'form':form}
    return render(request,"detail.html",my_dict)






def order(request):
    order_amount = 50000
    order_currency = '$'
    client=razorpay.Client(auth=('rzp_test_BH0ieRU3OLHvF9','kFzv0RhDgVcHzF2uoF4Sr4M4'))

    client.order.create(amount=order_amount, currency=order_currency)




def success(request):
    return render(request,"success.html")



def contact(request):
    form_class = ContactForm

    return render(request, 'contact.html', {
        'form':form_class,
    })

def about(request):
    return render(request,'about.html')
