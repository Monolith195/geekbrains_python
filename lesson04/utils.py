from datetime import datetime

response_dict = {
    "OK": {
        "response": 200,
    },
    "Bad Request": {
        "response": 400,
        "error": 'Bad Request'
    }
}

presence_d = {
    "action": "presence",
    "time": datetime.now().isoformat(),
    "type": "status",
    "user": {
        "account_name": "test",
        "status": "I'm here"
    }
}

receive_size = 1000
