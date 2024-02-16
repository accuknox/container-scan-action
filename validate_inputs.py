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
    if 'SEVERITY' in inputs:
        valid_severities = {'UNKNOWN', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL'}
        severity = inputs['SEVERITY'].upper()
        if severity not in valid_severities:
            errors.append("Invalid severity level provided.")


    if 'CODE' in inputs:
        code = inputs['CODE']
        if code not in {'0', '1'}:
            errors.append("Invalid code value provided.")
    return errors

def main():
    inputs = {
        'DOCKERFILE_CONTEXT': os.getenv('DOCKERFILE_CONTEXT', ''),
        'ENDPOINT': os.getenv('ENDPOINT', ''),
        'TOKEN': os.getenv('TOKEN', ''),
        'TENANT_ID': os.getenv('TENANT_ID', ''),
        'REPOSITORY_NAME': os.getenv('REPOSITORY_NAME', ''),
        'TAG': os.getenv('TAG', ''),
        'SEVERITY': os.getenv('SEVERITY', ''),
        'CODE': os.getenv('CODE', '')
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

