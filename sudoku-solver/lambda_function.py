import json

from sudoku.api.event_handler import EventHandler


def lambda_handler(event, context):
    print(event)
    body = json.loads(event['body'])
    print(body)
    errors = EventHandler.validate_event(body)
    if errors:
        print("Errors!")
        resp = EventHandler.handle_errors(errors)
        print(resp)
        return resp
    print("No Errors!")
    resp = EventHandler.handle_event(body)
    print(resp)
    return resp
