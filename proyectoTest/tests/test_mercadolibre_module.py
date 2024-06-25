import pytest  # Importa la biblioteca pytest para realizar pruebas unitarias
import requests  # Importa la biblioteca requests para realizar solicitudes HTTP
from requests.exceptions import RequestException  # Importa la excepción RequestException de requests
import requests_mock  # Importa requests_mock para simular solicitudes HTTP
from mercadolibre_module import get_product_details  # Importa la función get_product_details del módulo mercadolibre_module

# Definición del primer caso de prueba
def test_get_product_details_success(requests_mock):
    # Define el ID del producto y la respuesta simulada
    product_id = "MLA16060760"
    mock_response = {
        "id": product_id,
        "site_id": "MLA",
        "title": "Sillón Mesh Ejecutivo Respaldo Alto",
        "subtitle": None,
        "seller_id": 123456789,
        "category_id": "MLA1055",
        "price": 1000.0,
        "currency_id": "ARS",
        "available_quantity": 10,
        "sold_quantity": 2,
        "buying_mode": "buy_it_now",
        "listing_type_id": "gold_special",
        "start_time": "2023-01-01T00:00:00.000Z",
        "stop_time": "2023-12-31T23:59:59.000Z",
        "condition": "new",
        "permalink": "http://www.mercadolibre.com.ar/sillon-mesh-ejecutivo-respaldo-alto-silla-escritorio-baires4-colo",
        "thumbnail": "http://http2.mlstatic.com/D_12345-MLA1234567890_12345-O.jpg",
        "accepts_mercadopago": True,
        "shipping": {
            "mode": "me2",
            "free_shipping": True,
            "tags": [],
            "logistic_type": "drop_off",
            "store_pick_up": False
        },
        "seller_address": {
            "city": {
                "name": "Buenos Aires"
            },
            "state": {
                "name": "Capital Federal"
            },
            "country": {
                "id": "AR",
                "name": "Argentina"
            },
            "search_location": {
                "neighborhood": {
                    "id": "TUxBQlZJTDY3Nzk",
                    "name": "Villa Urquiza"
                },
                "city": {
                    "id": "TUxBQ0NBUGZlZG1sYQ",
                    "name": "Capital Federal"
                },
                "state": {
                    "id": "TUxBUENBUGw3M2E1",
                    "name": "Capital Federal"
                }
            },
            "id": 123456789
        },
        "attributes": [
            {
                "id": "BRAND",
                "name": "Marca",
                "value_id": "27471",
                "value_name": "Genérico",
                "value_struct": None,
                "values": [
                    {
                        "id": "27471",
                        "name": "Genérico",
                        "struct": None
                    }
                ],
                "attribute_group_id": "OTHERS",
                "attribute_group_name": "Otros"
            }
        ]
    }
    # Construye la URL de la API con el ID del producto
    url = f"https://api.mercadolibre.com/items/{product_id}"
    # Configura requests_mock para responder con mock_response cuando se haga una solicitud GET a la URL
    requests_mock.get(url, json=mock_response, status_code=200)
    
    # Llama a la función get_product_details con el ID del producto
    response = get_product_details(product_id)
    
    # Verifica que la respuesta de get_product_details sea igual a mock_response
    assert response == mock_response

# Definición del segundo caso de prueba
def test_get_product_details_not_found(requests_mock):
    # Define el ID del producto y la URL de la API
    product_id = "MLA16060760"
    url = f"https://api.mercadolibre.com/items/{product_id}"
    # Configura requests_mock para responder con un código de estado 404 cuando se haga una solicitud GET a la URL
    requests_mock.get(url, status_code=404)
    
    # Llama a la función get_product_details con el ID del producto
    response = get_product_details(product_id)
    
    # Verifica que la respuesta de get_product_details sea None (producto no encontrado)
    assert response is None

# Definición del tercer caso de prueba
def test_get_product_details_server_error(requests_mock):
    # Define el ID del producto y la URL de la API
    product_id = "MLA16060760"
    url = f"https://api.mercadolibre.com/items/{product_id}"
    # Configura requests_mock para responder con un código de estado 500 (error del servidor) cuando se haga una solicitud GET a la URL
    requests_mock.get(url, status_code=500)
    
    # Llama a la función get_product_details con el ID del producto
    response = get_product_details(product_id)
    
    # Verifica que la respuesta de get_product_details sea None (error del servidor)
    assert response is None

# Definición del cuarto caso de prueba
def test_get_product_details_request_exception(monkeypatch: pytest.MonkeyPatch):
    # Define el ID del producto
    
    product_id = "MLA16060760"
    
    # Define una función de simulación que genera una RequestException
    def mock_get(*args, **kwargs):
        raise RequestException("Error de red")
    
    # Aplica el mock de la función requests.get usando monkeypatch
    monkeypatch.setattr(requests, "get", mock_get)
    
    # Llama a la función get_product_details con el ID del producto
    response = get_product_details(product_id)
    
    # Verifica que la respuesta de get_product_details sea None (error de solicitud)
    assert response is None
