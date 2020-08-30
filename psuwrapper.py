## PSU Wrapper By Retarded Stroketon
import requests
class obfuscator_error(Exception):
    def __init__(self, error_type, message):
        self.type = error_type
        self.message = message

def is_api_response(res):
    if (res.headers and res.headers.get("Content-Type") == "application/json" and res.json().get("error")):
        return True
    else:
        return False

class obfuscator:
    def __init__(self, key=str):
        self.key = key
    def obfuscate(self, script, options=None):
        request_body = {
            "script": script,
            "options": "",
            "key": self.key
        }

        if options:
            request_body["options"] = (",").join(options)

        try:
            api_response = requests.post("https://psu.dev/postapi", json=request_body)
            api_response.raise_for_status()
            api_response_json = api_response.json()
            return api_response_json.get("script")
        except requests.exceptions.HTTPError:
            api_error_type = is_api_response(api_response) and "api-error" or "request-error"
            api_error_message = is_api_response(api_response) and api_response_json.error or api_response.text
            raise obfuscator_error(api_error_type, api_error_message)
