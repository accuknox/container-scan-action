# Automate Container Image Security Scanning with AccuKnox GitHub Action

## Learn More

- [About Accuknox](https://www.accuknox.com/)

| Input Values       | Description                                                                                            | Optional/Required | Default Values                         |
| ------------------ | ------------------------------------------------------------------------------------------------------ | ----------------- | -------------------------------------- |
| dockerfile_context | The context of the Dockerfile to use for building the image.                                           | Optional          | Dockerfile                             |
| endpoint           | The URL of the CSPM panel to push the scan results to.                                                 | Optional          | `cspm.demo.accuknox.com`               |
| token              | The token for authenticating with the CSPM panel.                                                      | Required          | -                                      |
| tenant_id          | The ID of the tenant associated with the CSPM panel.                                                   | Required          | -                                      |
| repository_name    | Docker image repository name.                                                                          | Required          | -                                      |
| tag                | Add version tag to the repository.                                                                     | Optional          | `${{ github.run_id }}`                 |
| severity           | Allows selection of severity level for the scan. Options include UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL. | Optional          | `UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL` |
| exit_code          | Specifies pipeline behavior upon detecting specified severity level. '0' (continue) or '1' (halt).     | Optional          | 0                                      |
| label              | The label created in AccuKnox SaaS for associating scan results.                                       | Required          | -                                      |

## Usage

Steps for using Install-action in a workflow yaml file

- Checkout into the repo using checkout action.
- Utilize the accuknox/container-scan-action repository with version tag v0.0.1.

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
        uses: accuknox/container-scan-action@v0.0.1
        with:
          token:
          tenant_id:                       #Required
          repository_name:                 #Required
          label:                           #Required
          endpoint:                        #Optional
          tag:                             #Optional
          exit_code:                       #Optional
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
        uses: accuknox/container-scan-action@v0.0.1
        with:
          token: ${{ secrets.TOKEN }}
          tenant_id: ${{ secrets.TENANT_ID }}
          repository_name: ${{ github.repository }}
          label: ${{ secrets.LABEL }}
```
