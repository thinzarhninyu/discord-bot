def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'yo sup'
    
    if p_message == 'nice to meet you':
        return 'good to see you too!'
    
    return 'huh?'