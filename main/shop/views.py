from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json

# Create your views here.


def index(request):
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'products': products}
    # allProds = [[products, range(1, nSlides), nSlides], [
    #     products, range(1, nSlides), nSlides]]

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    query = query.lower()
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    allProds = []
    query = request.GET.get('search')
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds, 'found': True}

    if len(allProds) == 0 or len(query) < 4:
        params = {'allProds': allProds, 'found': False}

    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', 'dummy@dummy.com')
        desc = request.POST.get('text', '')
        # print(name, phone, email, desc)

        contact = Contact(name=name, phone=phone, email=email, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', "")
        email = request.POST.get('email', "")
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status": "success",
                                           "updates": updates,
                                           "itemsJson": order[0].items_json
                                           },
                                          default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "noitem"}')
        except Exception as e:
            return HttpResponse('{"status": "error"}')
    return render(request, 'shop/tracker.html')

    # this was wriiten for an excercise and need to be placed in productview function along with rendering
    # index2.html as well which got deleted so i need to build it again and passing the dictionary context as a parameter in render function
    ''' context = {"product_list": product_list} 
        product_list = Product.objects.all()
    '''

# myid paramter gets it value from the URL in the urls.py file


def productView(request, myid):
    # Fetch the product using its id
    product = Product.objects.filter(id=myid)
    # print(product)

    # Here product is a list but for each id we have only one product thats why we will
    # pass first or the only object of that list
    return render(request, 'shop/prodView.html', {'item': product[0]})


def checkout(request):
    thanks = False
    id = 0
    if request.method == "POST":
        json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', ' ')
        thanks = True
        print(name, email, phone, city, address, zip_code)
        order = Order(items_json=json, name=name, phone=phone, email=email,
                      address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        id = order.order_id

        # Creating Order Update from here
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The order has been placed")
        update.save()

        params = {'thanks': thanks, 'id': id}
        return render(request, 'shop/checkout.html', params)
    return render(request, 'shop/checkout.html')
