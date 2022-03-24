import json

from sudoku.api.event_validator import EventHandler


def lambda_handler(event, context):
    print(event)
    body = json.loads(event['body'])
    print(body)
    errors = EventHandler.validate_event(body)
    if errors:
        print("Errors!")
        return json.dumps(EventHandler.handle_errors(errors))
    print("No Errors!")
    return json.dumps(EventHandler.handle_event(body))
