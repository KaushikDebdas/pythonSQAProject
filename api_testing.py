import logging

import requests
import json


# print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

# print('\x1b[0;30;43m' + 'warning!' + '\x1b[0m')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

report = []

# Variables
product_search_title = "ddp"
product_id = 12064
Outlet_phone = "01000000003"
# SR_PHONE = "02000000002"
SR_PHONE = "01789860860"
SR_PASSWORD = "112233"
line_item_id = 1

#outlet_token = "eyJhbGciOiJIUzI1NiJ9.eyJwaG9uZSI6IjAxMDAwMDAwMDAzIiwib3RwIjo4Mzk1MCwiZXhwIjoxNzQwNjUyODczfQ.8pxHQsw9waViOusFj16_Mj7jGrabo910v42NgYnzuW8"
outlet_token= "eyJhbGciOiJIUzI1NiJ9.eyJwaG9uZSI6IjAxMDAwMDAwMDAzIiwib3RwIjo0MzY5NSwiZXhwIjoxNzQxMTc1MDczfQ.x0xt6u7sjp0IeOiJ_dO4j3FPM7KnLfcLEqCSJ0Bt3EY"
variant_id = 13997
variant_id_for_delete = 13998
PARTNER_ID = 5793
PARTNER_ID = 4240
outlet_id = 5794
sr_token = ("eyJhbGciOiJIUzI1NiJ9.eyJyZXRhaWxlcl9pZCI6NjE5LCJ0eXBlIjoiUmV0YWlsZXJBc3Npc3RhbnQiLCJleHAiOjE3Mzk0MzYxNDR9"
            ".dj7WAyF7_2sRkpEswPW1rpa8GIDTBbdRh2rKgTwqyHo")

# Base URL
base_url = "https://mcore-dev.shopoth.net"


# Function to make API requests
def make_request(method, endpoint, headers=None, data=None):
    url = base_url + endpoint
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)

        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None, None


# Function to print response
def print_response(response, status_code):
    if status_code == 200 or status_code == 201:
        print('\x1b[6;30;42m' + '200 Success!' + '\x1b[0m')
        if not response and status_code == 200:  # Check if response is empty
            print('\x1b[0;30;43m' + ' [] empty ' + '\x1b[0m')
        else:
            print(json.dumps(response, indent=4))
    elif status_code == 500:
        print('\x1b[0;30;43m' + '500' + '\x1b[0m')
    elif status_code == 404:
        print('\x1b[0;30;43m' + '404' + '\x1b[0m')
    elif status_code == 422:
        print('\x1b[0;30;43m' + '422' + '\x1b[0m')

    elif status_code == 401:
        print('\x1b[0;30;43m' + '401' + '\x1b[0m')

    elif status_code == 433:
        print('\x1b[0;30;43m' + '433' + '\x1b[0m')
    else:
        print(f"Request failed with status code {status_code}")


# Step 1: Get product list
def get_product_list(outlet_token):
    # outlet_token="eyJhbGciOiJIUzI1NiJ9.eyJwYXJ0bmVyX2lkIjo1Nzk0LCJyZXRhaWxlcl9pZCI6NjE5LCJleHAiOjE3Mzk0MzY3NDF9.wNLQ1pHVKlj1vUU5VockDKG9B-h_MFzJoglJbEbyj-Y"
    # print("eyJhbGciOiJIUzI1NiJ9.eyJwYXJ0bmVyX2lkIjo1Nzk0LCJyZXRhaWxlcl9pZCI6NjE5LCJleHAiOjE3Mzk0MzY3NDF9.wNLQ1pHVKlj1vUU5VockDKG9B-h_MFzJoglJbEbyj-Y",outlet_token)
    endpoint = "/sales_app/api/v1/products?page=1"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)
    # print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    # print('\x1b[0;30;41m' + 'Failed!' + '\x1b[0m')
    # print('\x1b[0;30;43m' + 'warning!' + '\x1b[0m')

    new_object = {
        "name": "get_product_list",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)

    # Adding the new object to t

    if status_code == 200 or status_code == 201:
        # print('\x1b[6;30;42m' + 'status_code!' + status_code + '\x1b[0m')
        print('\x1b[6;30;42m' + '200 Success!' + '\x1b[0m')
    else:
        print('\x1b[6;30;42m' + 'status ' + str(status_code) + '\x1b[0m')

    return response


# Step 2: Clear cart
def clear_cart():
    endpoint = "/partner/api/v1/carts/delete"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("DELETE", endpoint, headers)
    print_response(response, status_code)

    new_object = {
        "name": "clear_cart",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)


# Step 3: Check cart item count
def get_cart_item_count():
    endpoint = "/partner/api/v1/carts/items"
    print(" checking endpoint " + endpoint)
    logger.info(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)
    new_object = {
        "name": "get_cart_item_count",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)

    return response.get("items")


# Step 4: Add to cart
def add_to_cart(variant_id):
    endpoint = "/partner/api/v1/carts"
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    print(" checking endpoint " + endpoint)
    payload = {"variant_id": variant_id, "quantity": 1}
    response, status_code = make_request("POST", endpoint, headers, payload)
    print_response(response, status_code)
    new_object = {
        "name": "add_to_cart",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)
    return response


# Step 5: Check cart line item count
def check_cart_line_item_count():
    cart_items = get_cart_item_count()
    return len(cart_items)


# Step 6: Save line item ID and quantity
def save_line_item_details(data):
    global line_item_id
    try:
        line_item_id = data['cart_items'][0]['items'][0]['shopoth_line_item_id']
    except KeyError:
        print("shopoth_line_item_id: ", line_item_id)

    print("shopoth_line_item_id: ", line_item_id)
    return line_item_id


# Step 7: Increase quantity
def increase_quantity(line_item_id):
    endpoint = f"/partner/api/v1/carts/shopoth_line_items/{line_item_id}/add-one"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("PUT", endpoint, headers)
    print_response(response, status_code)
    new_object = {
        "name": "increase_quantity",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)


# Step 8: Decrease quantity
def decrease_quantity(line_item_id):
    endpoint = f"/partner/api/v1/carts/shopoth_line_items/{line_item_id}/dec-one"
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("PUT", endpoint, headers)
    print_response(response, status_code)
    new_object = {
        "name": "decrease_quantity",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)


def dash_board():
    endpoint = "/sales_app/api/v1/dashboard/"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": sr_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)

    new_object = {
        "name": "decrease_quantity",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)


def get_outlet_history():
    endpoint = "/sales_app/api/v1/partners/history"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": sr_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)


def targets():
    endpoint = "/sales_app/api/v1/targets"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": sr_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)


def ohs():
    endpoint = "/sales_app/api/v1/dashboard/ohs"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)


def get_outlet_promo_text():
    endpoint = f"/sales_app/api/v1/partners/{outlet_id}/promotions"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)


def sr_dashboard_promo_slider():
    endpoint = '/sales_app/api/v1/sliders?image_type=sales_app_promotion'
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": sr_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)


def lastCall(call_number):
    endpoint = "/partner/api/v1/sales_history?start_date=11-11-2-24&end_date=11-11-2024&sell_call=1"
    # endpoint = (f"/partner/api/v1/sales_history?start_date=%E0%A7%A8%E0%A7%A6%E0%A7%A8%E0%A7%AA-%E0%A7%A6%E0%A7%A8-%E0"
    #             f"%A7%A7%E0%A7%A9&end_date=%E0%A7%A8%E0%A7%A6%E0%A7%A8%E0%A7%AA-%E0%A7%A6%E0%A7%A8-%E0%A7%A7%E0%A7%AA"
    #             f"&sell_call=1")
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print(response, status_code)
    print_response(response, status_code)


def get_surveys():
    endpoint = "/sales_app/api/v1/surveys"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)


def post_survey():
    endpoint = "/sales_app/api/v1/surveys/store_survey"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}

    payload = {
        "outlet_id": outlet_id,
        "survey_data": [
            {"variant_id": variant_id, "remaining_quantity": 10}
        ]
    }
    response, status_code = make_request("POST", endpoint, headers, payload)
    print_response(response, status_code)
    print(" ##---- post_survey end ---##")


# Step 9: Check cart details

def get_last_line_item_from_cart(response_data):
    line_items = response_data.get("shopoth_line_items", [])
    shopoth_line_item_id = 0
    if line_items:
        first_item = line_items[0]
        shopoth_line_item_id = first_item.get("shopoth_line_item_id")

    return shopoth_line_item_id


def cart_details(outlet_token):
    endpoint = "/partner/api/v1/carts/details"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)
    return response


# partner/api/v1/product/search?title=d
def product_details(product_id):
    # 12064
    endpoint = f"/partner/api/v1/product/{product_id}/details"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)

    new_object = {
        "name": "product_details",
        "endpoint": endpoint,
        "status": status_code
    }

    # Adding the new object to the list
    report.append(new_object)
    return response


def product_search(title):
    endpoint = f"/partner/api/v1/product/search?title={title}"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)

    new_object = {
        "name": "product_search",
        "endpoint": endpoint,
        "status": status_code
    }

    # Adding the new object to the list
    report.append(new_object)
    print_response(response, status_code)
    return response


def check_cart_details(outlet_token):
    endpoint = "/partner/api/v1/carts/details"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)

    new_object = {
        "name": "check_cart_details",
        "endpoint": endpoint,
        "status": status_code
    }

    # Adding the new object to the list
    report.append(new_object)

    if response.get("message"):
        print("Cart is empty")
        return 0, 0, 0, 0, response.get("variant_id", 0), 0

    is_available, shopoth_line_item_id, quantity, price, variant_id, size = extract_cart_details(response)

    return is_available, shopoth_line_item_id, quantity, price, variant_id, size


# Step 10: Delete line item
def delete_line_item(line_item_id):
    endpoint = f"/partner/api/v1/carts/shopoth_line_items/{line_item_id}"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    response, status_code = make_request("DELETE", endpoint, headers)

    new_object = {
        "name": "delete_line_item",
        "endpoint": endpoint,
        "status": status_code
    }

    # Adding the new object to the list
    report.append(new_object)

    print_response(response, status_code)


# Step 11: Add line item again with more than available quantity
def add_line_item_with_more_quantity():
    endpoint = "/partner/api/v1/carts"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}

    payload = {
        "outlet_id": 4073,
        "survey_data": [
            {"variant_id": 12736, "remaining_quantity": 10}
        ]
    }
    payload = {"variant_id": variant_id, "quantity": 100}  # Quantity higher than available
    response, status_code = make_request("POST", endpoint, headers, payload)

    new_object = {
        "name": "add_line_item_with_more_quantity",
        "endpoint": endpoint,
        "status": status_code
    }

    # Adding the new object to the list
    report.append(new_object)
    print_response(response, status_code)


# Step 12: Add line item with valid quantity
def add_line_item_with_valid_quantity():
    endpoint = "/partner/api/v1/carts"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    payload = {"variant_id": variant_id, "quantity": 1}
    response, status_code = make_request("POST", endpoint, headers, payload)
    print(" ##---- add_line_item_with_valid_quantity end ---##")
    print_response(response, status_code)

    print(" ##---- add_line_item_with_valid_quantity end ---##")


# Step 13: Place order
def place_order():
    endpoint = "/partner/api/v1/order/place"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token, "Business-Type": "multicat"}
    payload = {"phoneNo": Outlet_phone}
    response, status_code = make_request("POST", endpoint, headers, payload)

    new_object = {
        "name": "place_order",
        "endpoint": endpoint,
        "status": status_code
    }

    # Adding the new object to the list
    report.append(new_object)

    print_response(response, status_code)
    print(" ##---- place_order end ---##")


def extract_cart_details(response_data):
    line_items = response_data.get("shopoth_line_items", [])
    cart_item_size = len(response_data.get('cart_items')) or 0

    # Initialize variables
    is_available = None
    quantity = None
    price = None
    variant_id = None
    shopoth_line_item_id = 0

    # Extract the first item if it exists
    if line_items:
        first_item = line_items[0]
        is_available = first_item.get("is_available")
        shopoth_line_item_id = first_item.get("shopoth_line_item_id")
        quantity = first_item.get("quantity")
        price = first_item.get("price")
        variant_id = first_item.get("variant_id")

    # Return the extracted values
    return is_available, shopoth_line_item_id, quantity, price, variant_id, cart_item_size


def sales_login():
    endpoint = "/partner/api/v1/login"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": outlet_token}

    payload = {"phone": '02000000002', "password": "112233"}  # Quantity higher than available
    response, status_code = make_request("POST", endpoint, headers, payload)
    print_response(response, status_code)
    # sr_token = response.get("auth_token")

    new_object = {
        "name": "sales_login",
        "endpoint": endpoint,
        "status": status_code
    }

    # Adding the new object to the list
    report.append(new_object)

    if status_code == 200:
        # data = json.loads(response)
        global sr_token
        sr_token = response.get("auth_token")
        # print(sr_token)
    # return sr_token


def get_outlet_list(sr_token):
    endpoint = "/sales_app/api/v1/partners"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": sr_token, "Business-Type": "multicat"}
    response, status_code = make_request("GET", endpoint, headers)
    print_response(response, status_code)

    new_object = {
        "name": "get_outlet_list",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)


def outlet_login(sr_token):
    print("--outlet-login")
    endpoint = f"/partner/api/v1/otps/{outlet_id}/send"
    print(" checking endpoint " + endpoint)
    headers = {"Authorization": sr_token, "Business-Type": "multicat"}
    response, status_code = make_request("POST", endpoint, headers)
    print_response(response, status_code)
    new_object = {
        "name": "outlet_login",
        "endpoint": endpoint,
        "status": status_code
    }
    report.append(new_object)

    if status_code == 201:
        global outlet_token
        outlet_token = response.get("message")
        print("---Outlet--" + response.get("message"))
        return response.get("message")

    elif response.get("status_code"):
        # print()
        pass

        # Add appropriate handling for status code 201
    else:
        print("Unexpected status code:", status_code)  # Handle other status codes if needed


def check_cart():
    global line_item_id

    is_available, line_item_id, quantity, price, variant_id, cart_item_size = check_cart_details(outlet_token)
    print(str(line_item_id) + "check_cart")
    # # Step 3: Check cart item count
    cart_items_before_adding = int(get_cart_item_count())

    cart_items_before_adding = get_cart_item_count()

    if cart_item_size == int(cart_item_size):

        print(
            f"\x1b[6;30;42m' + '200 Success!'  cart_items_before_adding {cart_items_before_adding} == cart_item_size {cart_item_size} '\x1b[0m'")
    else:
        print('\x1b[0;30;41m' + 'Cart Item is not same!' + '\x1b[0m')


# Main function to test order cycle
def test_order_cycle():
    # SR DASHBOARD
    dash_board()
    sr_dashboard_promo_slider()
    targets()
    #
    # get_outlet_list(sr_token)
    get_outlet_history()

    outlet_login(sr_token)
    # Outlet Dashboard
    ohs()
    get_surveys()
    post_survey()
    # lastCall(1)
    #
    get_product_list(outlet_token)
    product_details(product_id)
    product_search(product_search_title)

    get_cart_item_count()
    # clear_cart()

    check_cart_details(outlet_token)
    add_to_cart(variant_id)

    # line_item_id = get_last_line_item_from_cart(cart_details(outlet_token))
    #
    # increase_quantity(line_item_id)
    # decrease_quantity(line_item_id)

    # delete_line_item(line_item_id)

    # place_order()


def test_order_cycle_and_generate_report():
    # Test the order cycle
    test_order_cycle()
    print(report)
    return report


# Run the test and generate report
test_order_cycle_and_generate_report()
