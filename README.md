# AccuKnox Container Scan GitHub Action

**Description**

This GitHub Action scans Docker images for vulnerabilities and uploads the scan results to the AccuKnox Console. It can be configured with specific inputs to integrate seamlessly into your DevSecOps pipeline, ensuring continuous security compliance.

## Learn More

- [About Accuknox](https://www.accuknox.com/)

## Inputs

```yaml
inputs:
  endpoint:
    description: 'The URL of the CSPM panel to push the scan results to.'
    required: true
    default: 'cspm.demo.accuknox.com'
  token:
    description: 'The token for authenticating with the AccuKnox Console.'
    required: true
  tenant_id:
    description: 'The ID of the tenant associated with the AccuKnox Console.'
    required: true
  label:
    description: "The label created in AccuKnox Console for associating scan results."
    required: true
  image: 
     description: 'Docker image name'
     required: true
  tag:
     description: 'version tag of the image'
     required: true
     default: '${{ github.run_id }}'
  severity:
     description: "Allows selection of severity levels for the scan. Options include UNKNOWN, LOW, MEDIUM, HIGH, and CRITICAL. If specified, the pipeline will exit whenever a vulnerability with the specified severity is detected."
     required: false
```

## Usage

Steps for using Install-action in a workflow yaml file 
- Checkout into the repo using checkout action.
- Utilize the accuknox/container-scan-action repository with version tag v1.

### Token Generation from Accuknox SaaS and Viewing Tenant ID

Navigate to Tokens within the Settings section in the sidebar:
![1](https://github.com/udit-uniyal/container-scan-action/assets/115368361/8f4e188b-d9f3-4404-83af-134d5dc1417a)

Click on Create Token: 
After clicking on 'Create Token,' the Tenant ID will be visible.
![2](https://github.com/udit-uniyal/container-scan-action/assets/115368361/296bc611-acb8-4918-9d6b-3a8ec7733377)

Click on Generate:
![3](https://github.com/udit-uniyal/container-scan-action/assets/115368361/16032af0-bcac-4787-8f2a-a3fa0edc6ec6)


### workflow steps:

```yaml
 - name: Run AccuKnox CSPM Scan
        uses: accuknox/container-scan-action@v1
        with:                      
          token: 
          tenant_id: 
          repository_name:
          endpoint:                        #Optional
          tag:                             #Optional
          severity:                        #Optional
          dockerfile_context:              #Optional
```


## Minimalist Sample Configuration 

```yaml

name: AccuKnox Scan Workflow

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  accuknox-cicd:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@main  
     
      - name: Run AccuKnox CSPM Scan
        uses: accuknox/container-scan-action@v1
        with:
          token: 
          tenant_id: 
          repository_name: 
```
