import base64
import requests



class UtilsAuto:
    @staticmethod
    def post_api_call(server, uri, user_name, password, api_request_data):
        server_url = server + uri
        enc_usr_pass = str(user_name) + ':' + str(password)
        b64Val = base64.b64encode(enc_usr_pass.encode("ascii")).decode("ascii")
        headers = {
            'X-Requested-With': 'curl demo2',
            'Authorization': "Basic %s" % b64Val
        }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=server_url, params=api_request_data, headers=headers, verify=False)
        contents = r.content
        # print(contents)
        return contents

    @staticmethod
    def post_api_call_with_body(server, uri, payloadRecieved, content_type, user_name, password):
        server_url = server + uri
        enc_usr_pass = str(user_name) + ':' + str(password)
        b64Val = base64.b64encode(enc_usr_pass.encode("ascii")).decode("ascii")
        if content_type is None:
            headers = {
                'X-Requested-With': 'curl demo2',
                'Authorization': "Basic %s" % b64Val
            }
        else:
            headers = {
                'X-Requested-With': 'curl demo2',
                'Authorization': "Basic %s" % b64Val,
                'Content-Type': content_type
            }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=server_url, headers=headers, data=payloadRecieved, verify=False)
        contents = r.content
        return contents

    @staticmethod
    def get_api_call(server, uri, user_name, password, api_request_data):
        server_url = server + uri
        enc_usr_pass = str(user_name) + ':' + str(password)
        b64Val = base64.b64encode(enc_usr_pass.encode("ascii")).decode("ascii")
        headers = {
            'X-Requested-With': 'curl demo2',
            'Authorization': "Basic %s" % b64Val
        }
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url=server_url, params=api_request_data, headers=headers, verify=False)
        contents = r.content
        # print(contents)
        return contents

    @staticmethod
    def DELETE_CALL_WITH_BODY(server, contentType, payloadProvided, user_name, password):
        url = server
        payload = payloadProvided
        enc_usr_pass = str(user_name) + ':' + str(password)
        b64Val = base64.b64encode(enc_usr_pass.encode("ascii")).decode("ascii")

        headers = {
            'X-Requested-With': 'curl demo2',
            'Authorization': "Basic %s" % b64Val,
            'Content-Type': contentType
        }

        requests.packages.urllib3.disable_warnings()
        response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)
        contents = response.content
        return contents
