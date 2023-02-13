from typing import List, Dict
from pprint import pformat


def my_hello_application(environ: Dict, start_reponse) -> List:
    responses = []

    if environ['PATH_INFO'] == '/':
        responses.append("Hello You <3 !!!!\n\n")
        start_reponse("200 0K", [])
    else:
        responses.append("Error 400 !!!!\n\n")
        start_reponse("400", [])

    #responses.append(pformat(environ))

    return [item_to_return.encode() for item_to_return in responses]
