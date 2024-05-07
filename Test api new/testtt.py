import re

def lexical_analyzer(expression):
    word_pattern = r'\b\w+\b'
    number_pattern = r'\b\d+\b'
    special_char_pattern = r'[^\w\s\d]'

    tokens = re.findall(word_pattern + '|' + number_pattern + '|' + special_char_pattern, expression)

    categorized_tokens = []
    for token in tokens:
        if re.match(word_pattern, token):
            categorized_tokens.append(('word', token)) 
        elif re.match(number_pattern, token):
            categorized_tokens.append(('number', token))  
        elif re.match(special_char_pattern, token):
            categorized_tokens.append(('special_char', token))  

    return categorized_tokens

example_expression = "Hello! This is a 123 sample text, with %^& some $pecial characters and punctuations."
tokens = lexical_analyzer(example_expression)

print("Tokens:")
for token in tokens:
    print(token)
