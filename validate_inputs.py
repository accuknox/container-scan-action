import os
import json
import sys

def validate_inputs(inputs):
    errors = []


    if 'TOKEN' not in inputs or not inputs['TOKEN']:
        errors.append("Token is required.")
    if 'TENANT_ID' not in inputs or not inputs['TENANT_ID']:
        errors.append("Tenant ID is required.")

    if 'REPOSITORY_NAME' not in inputs or not inputs['REPOSITORY_NAME']:
        errors.append("Repository name is required.")

def main():
    inputs = {
        'ENDPOINT': os.getenv('ENDPOINT', ''),
        'TOKEN': os.getenv('TOKEN', ''),
        'TENANT_ID': os.getenv('TENANT_ID', ''),
        'REPOSITORY_NAME': os.getenv('REPOSITORY_NAME', ''),
        'TAG': os.getenv('TAG', ''),
        'SEVERITY': os.getenv('SEVERITY', ''),
        'CODE': os.getenv('CODE', '')
        'IGNORE_UNFIXED': os.getenv('IGNORE_UNFIXED', ' '),
    }


    errors = validate_inputs(inputs)


    if errors:
        print("Input validation failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("Input validation passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()

