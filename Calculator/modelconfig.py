#
# def chatbot_function(input_json):
#     chatbot_engine.classify(input_json)
#     return output_json

def sum(input_json):
    output_json="analyzed: sum"+input_json
    return output_json

def diff(input_json):
    output_json="analyzed: diff"+input_json
    return output_json



models = {
    "add": sum,
    "sub": diff,
    # "chatbot": chatbot_function
}
