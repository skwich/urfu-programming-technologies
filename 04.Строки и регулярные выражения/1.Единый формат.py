import json
import re

def format_text(header: str, text: str):
    match header:
        case 'description':
            return format_description(text)
        case 'salary':
            return format_salary(text)
        case 'key_phrase':
            return format_key_phrase(text)
        case 'addition':
            return format_addition(text)
        case 'company_info':
            return format_company_info(text)
        case 'key_skills':
            return format_key_skills(text)

def get_field(key: str):
    start_index = text.find(f'{key}: ')
    if start_index == -1:
        return None
    end_index = text.find(';', start_index)
    return text[start_index+len(f'{key}: ') : end_index]

def format_description(text: str):
    description = get_field('description')
    format_words = []
    for word in description.split('. '):
        format_words.append(word.capitalize())
    return '. '.join(format_words)

def format_salary(text: str):
    salary = get_field('salary')
    return '{:.2f}'.format(round(float(salary), 2))

def format_key_phrase(text: str):
    key_phrase = get_field('key_phrase')
    return key_phrase.upper() + '!'

def format_addition(text: str):
    addition = get_field('addition')
    return '..' + addition.lower() + '..'

def format_company_info(text: str):
    company_info = get_field('company_info')
    while '(' in company_info:
        company_info = re.sub(r"\([^()]*\)", '', company_info)
    return company_info

def format_key_skills(text: str):
    key_skills = get_field('key_skills')
    return key_skills.replace('&nbsp', ' ')

text = input()
headings = input()
result = {}

for header in headings.split(', '):
    if header in text:
        result[header] = format_text(header, text)

print(json.dumps(result))