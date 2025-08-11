from django.shortcuts import render
def menu_items_view(request):
    menu_items=[
        {'name':'pizza','price':10.99},
        {'name':'Burger','price':7.99},
        {'name':'Salad','price':5.99},
        {'name':'Pasta','price':8.99},

    ]
    return render(request,'MENU_ITEMS.html',{'MENU_ITEMS':MENU_ITEMS})