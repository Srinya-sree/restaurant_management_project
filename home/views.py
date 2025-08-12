from django.shortcuts import render  # Import Django's render function for rendering templates

# View function to display a list of menu items
def menu_items_view(request):
    # Hardcoded list of menu items with their name and price
    menu_items = [
        {'name': 'Pizza', 'price': 10.99},
        {'name': 'Burger', 'price': 7.99},
        {'name': 'Salad', 'price': 5.99},
        {'name': 'Pasta', 'price': 8.99},
    ]
    
    # Render the 'menu_items.html' template and pass menu_items as context data
    return render(request, 'menu_items.html', {'menu_items': menu_items})
