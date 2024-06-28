import os
import yaml
import sys


parameters = {
    'inputs': {},
    'outputs': {}
}


action_file = '.github/actions/jakies-cos/action.yml'
with open(action_file, 'r') as file:
    action_data = yaml.safe_load(file)
if 'inputs' in action_data:
    for input_name, input_details in action_data['inputs'].items():
        parameters['inputs'][input_name] = {
            'description': input_details.get('description', ''),
            'required': input_details.get('required', False),
            'default': input_details.get('default', None)
        }
if 'outputs' in action_data:
    for output_name, output_details in action_data['outputs'].items():
        parameters['outputs'][output_name] = {
            'description': output_details.get('description', '')
        }

print('Inputs:')
for input_name, details in parameters['inputs'].items():
    print(f'Input: {input_name}')
    print(f'Description: {details["description"]}')
    print(f'Required: {details["required"]}')
    print(f'Default: {details["default"]}')
    print()

print('Outputs:')
for output_name, details in parameters['outputs'].items():
    print(f'Output: {output_name}')
    print(f'Output value: sys.argv[1]')
    print(f'Description: {details["description"]}')
    print()

print(f'sys.argv: {sys.argv}')

with open(os.getenv('GITHUB_OUTPUT'), 'a') as f:
    f.write(f'wynik={parameters['inputs']['jakies-cos']}\n')
