mport base64
import json
import requests

AUTH_URL = '/oauth2/token'
MATERIALS_URL = '/materials/v1'
MODEL_URL = '/model/v1'
ORDER_URL = '/orders/v1'


class ShapewaysOauth2Client():
    """
    Shapeways API client, supporting Oauth2 Bearer Token
    """

    def __init__(self, api_url=None):
        self.access_token = None
        if not api_url:
            self.api_url = 'https://api.shapeways.com'

    def authenticate(self, client_id, client_secret):
        """
        Authenticate your application and retrieve a bearer token

        :type client_id: str
        :type client_secret: str
        :return: True for success, false for Failure
        :rtype: bool
        """
        auth_post_data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(url=self.api_url + AUTH_URL, data=auth_post_data, auth=(client_id, client_secret))
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            return True
        print("Error: status code " + str(response.status_code))
        print(response.content)
        return False

    def _validate_response(self, content):
        """
        Internal function - validate results
        :rtype: list()
        """
        try:
            if content['result'] == 'success':
                return content
            else:
                raise RuntimeError(content)
        except:
            raise RuntimeError(content)

    def _execute_get(self, url, **params):
        """
        Internal function - execute get request and validate
        :param url:
        :param params:
        :rtype: list()
        """
        response = requests.get(url=url, **params)
        return self._validate_response(response.json())

    def _execute_post(self, url, **params):
        """
        Internal function - execute get request and validate
        :param url:
        :param params:
        :rtype: list()
        """
        response = requests.post(url=url, **params)
        return self._validate_response(response.json())

    def get_materials(self):
        """
        Use your bearer token to retrieve our material list

        :return: list of materials
        :rtype: list()
        """

        if not self.access_token:
            raise RuntimeError("Access token not defined: be sure to call .authenticate() first!")

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        content = self._execute_get(url=self.api_url + MATERIALS_URL, headers=headers)
        return content['materials']

    def get_models(self, page_count=1):
        """
        Use your bearer token to retrieve a list of your models

        :return: list of materials
        :rtype: list()
        """

        if not self.access_token:
            raise RuntimeError("Access token not defined: be sure to call .authenticate() first!")

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        content = self._execute_get(url=self.api_url + MODEL_URL + '?page=' + str(page_count), headers=headers)
        return content['models']

    def upload_model(self, path_to_model):
        """
        Upload a model to Shapeways

        :param path_to_model: path to model on your local filesystem
        :type path_to_model: str
        :return:
        """
        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        with open(path_to_model, 'rb') as model_file:
            model_file_data = model_file.read()

        model_upload_post_data = {
            'fileName': 'cube.stl',
            'file': base64.b64encode(model_file_data).decode('utf-8'),
            'description': 'Someone call a doctor, because this cube is SIIIICK.',
            'hasRightsToModel': 1,
            'acceptTermsAndConditions': 1
        }

        content = self._execute_post(url=self.api_url + MODEL_URL, headers=headers, data=json.dumps(model_upload_post_data))
        return content

    def order_model(self, model_id, material_id, payment_verification_id):
        """
        Order a model.

        :type model_id: int
        :type material_id: int
        :type payment_verification_id: str
        :return:
        """

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }

        items = [{
            'materialId': material_id,
            'modelId': model_id,
            'quantity': 1
        }]

        order_data = {
            'items': items,
            'firstName': 'my',
            'lastName': 'dude',
            'country': 'US',
            'state': 'NY',
            'city': 'New York',
            'address1': '419 Park Ave South',
            'address2': '9th Floor',
            'zipCode': '10016',
            'phoneNumber': '1234567890',
            'paymentVerificationId': payment_verification_id,
            'paymentMethod': 'credit_card',
            'shippingOption': 'Cheapest'
        }

        content = self._execute_post(url=self.api_url + ORDER_URL, headers=headers, data=json.dumps(order_data))
        return content
