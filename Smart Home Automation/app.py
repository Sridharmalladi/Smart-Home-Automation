from flask import Flask, request, jsonify

app = Flask(__name__)

def turn_on_light():
    # Replace with actual API call to your smart device
    return "Turning on the lights"

def set_temperature(temp):
    # Replace with actual API call to your smart device
    return f"Setting the temperature to {temp} degrees"

def turn_off_light():
    # Replace with actual API call to your smart device
    return "Turning off the lights"

def set_alarm(time):
    # Replace with actual API call to your smart device
    return f"Setting an alarm for {time}"

def play_music():
    # Replace with actual API call to your smart device
    return "Playing music"

def check_weather():
    # Replace with actual API call to a weather API
    return "The weather is sunny with a chance of rain"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent = req.get('queryResult').get('intent').get('displayName')
    query_text = req.get('queryResult').get('queryText')

    if intent == 'turn_on_lights':
        response_text = turn_on_light()
    elif intent == 'set_temperature':
        parameters = req.get('queryResult').get('parameters')
        temp = parameters.get('temperature')
        response_text = set_temperature(temp)
    elif intent == 'turn_off_lights':
        response_text = turn_off_light()
    elif intent == 'set_alarm':
        parameters = req.get('queryResult').get('parameters')
        time = parameters.get('time')
        response_text = set_alarm(time)
    elif intent == 'play_music':
        response_text = play_music()
    elif intent == 'check_weather':
        response_text = check_weather()
    else:
        response_text = "Sorry, I didn't understand that."

    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(debug=True)
