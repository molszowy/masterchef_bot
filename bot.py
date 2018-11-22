from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

endpoint = EndpointConfig(url='http://localhost:5055/webhook')
interpreter = RasaNLUInterpreter('models/restaurant/nlu')
agent = Agent.load('models/restaurant', interpreter=interpreter, action_endpoint=endpoint)


def handle_incoming_msg(text: str):
    """
    Handle incoming text from user
    :param text:
    :return:
    """
    messages = []
    responses = agent.handle_message(text)
    for r in responses:
        messages.append(r.get("text"))

    return messages


