#import curlify
import requests


class APIUtils:

    @staticmethod
    def api_caller(json):
        """
        :param json:
         {
            'method': 'GET',
            'params': '',
            'data': '',
            'endpoint': '',
            'headers': {},
            'username': '',
            'password': '',
        }
        :return: response
        """
        authentication = None
        requests.packages.urllib3.disable_warnings()
        response = None
        if json["username"] is not None and json["password"] is not None:
            authentication = (json["username"], json["password"])

        headers = {'X-Requested-With': 'curl'}
        if 'headers' in json:
            headers.update(json['headers'])
        params = json['params'] if 'params' in json else None
        data = json['data'] if 'data' in json else None
        if json["method"] == 'GET':
            print('API is called with these details :', json)
            response = requests.get(json['endpoint'], params=params, headers=headers, verify=False,
                                    auth=authentication)

        if json["method"] == 'POST':
            print('API is called with these details :', json)
            response = requests.post(json['endpoint'], params=params, data=data,
                                     headers=headers, verify=False, auth=authentication)

        if json["method"] == 'PUT':
            print('API is called with these details :', json)
            response = requests.put(json['endpoint'], params=params, data=data, headers=headers,
                                    verify=False, auth=authentication)

        if json["method"] == 'DELETE':
            print('API is called with these details :', json)
            response = requests.delete(json['endpoint'], params=params, data=data,
                                       headers=headers, verify=False, auth=authentication)

        if json["method"] == 'PATCH':
            print('API is called with these details :', json)
            response = requests.patch(json['endpoint'], params=params, data=data,
                                      headers=headers, verify=False, auth=authentication)

        #print(curlify.to_curl(response.request))
        print(response)
        return response

    @staticmethod
    def get_api_request(json):
        json['method'] = 'GET'
        return APIUtils.api_caller(json)

    @staticmethod
    def post_api_request(json):
        json['method'] = 'POST'
        return APIUtils.api_caller(json)

    @staticmethod
    def put_api_request(json):
        json['method'] = 'PUT'
        return APIUtils.api_caller(json)

    @staticmethod
    def patch_api_request(json):
        json['method'] = 'PATCH'
        return APIUtils.api_caller(json)

    @staticmethod
    def delete_api_request(json):
        json['method'] = 'DELETE'
        return APIUtils.api_caller(json)
