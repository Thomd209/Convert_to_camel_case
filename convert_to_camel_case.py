def convert_to_camel_case(s):
    camel_case = s.split('_')
    camel_case = [camel_case[i].capitalize() for i in range(len(camel_case))]
    return camel_case


snake_case = input()
result = convert_to_camel_case(snake_case)
print(''.join(result))
