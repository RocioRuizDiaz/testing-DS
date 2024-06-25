import requests  # Importa la biblioteca requests para realizar solicitudes HTTP

def get_product_details(product_id):
    """
    Obtiene los detalles de un producto desde la API de MercadoLibre.

    Args:
        product_id (str): El ID del producto en MercadoLibre.

    Returns:
        dict or None: Un diccionario con los detalles del producto si la solicitud fue exitosa,
                      o None si ocurrió un error durante la solicitud.
    """
    url = f"https://api.mercadolibre.com/items/{product_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Retorna los detalles del producto en formato JSON
        else:
            return None  # Retorna None si la respuesta no fue exitosa (código de estado distinto de 200)
    except requests.exceptions.RequestException:
        return None  # Retorna None si ocurre una excepción durante la solicitud HTTP

def display_product_details(product_id):
    """
    Muestra los detalles de un producto en la consola.

    Args:
        product_id (str): El ID del producto en MercadoLibre.
    """
    product_details = get_product_details(product_id)
    if product_details:
        for key, value in product_details.items():
            print(f"{key}: {value}")  # Imprime cada clave y valor del diccionario de detalles del producto
    else:
        print("No se encontraron detalles para el producto.")  # Mensaje si no se encontraron detalles

# Ejemplo de uso con un ID de producto real
product_id = "MLA16060760"
display_product_details(product_id)
print("mostrar detalles")  # Mensaje adicional al final del script







