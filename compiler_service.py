import requests
import time
gfg_compiler_api_endpoint = "https://ide.geeksforgeeks.org/main.php"
gfg_result_api_endpoint = "https://ide.geeksforgeeks.org/submissionResult.php"
languages = ['C', 'Cpp', 'Cpp14', 'Java', 'Python', 'Python3', 'Scala', 'Php', 'Perl', 'Csharp']

def compile(lang, code, _input=None, save=False):
    data = {
      'lang': lang,
      'code': code,
      'input': _input,
      'save': save
    }
    r = requests.post(gfg_compiler_api_endpoint, data=data)
    return r.json()
def get_output (sid):
    return requests.post(gfg_result_api_endpoint, {"requestType":"fetchResults", "sid":sid}).json()