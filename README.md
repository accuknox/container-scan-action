# AccuKnox Container Scan

🛡️ **Secure Your Container Images Automatically**

The **AccuKnox Container Scan GitHub Action** enables developers and DevSecOps teams to automatically scan container images for known vulnerabilities and generate **Software Bill of Materials (SBOMs)**, with results seamlessly uploaded to the **AccuKnox Console**. This action integrates directly into CI/CD pipelines to help ensure container workloads are secure, compliant, and production-ready.

---

## 🎯 Key Features

- **Automated Container Image Scanning**  
  Detect known vulnerabilities in container images during CI/CD execution.

- **SBOM Generation (Software Bill of Materials)**  
  Generate and upload SBOMs for container images to support supply chain security and compliance requirements.

- **Native GitHub Actions Integration**  
  Easily integrate with GitHub workflows for continuous container security.

- **Centralized Visibility in AccuKnox Console**  
  Upload vulnerability scan results and SBOMs for centralized monitoring and analysis.

- **Severity-Based Enforcement**  
  Fail pipelines or block deployments based on configurable severity thresholds (e.g., HIGH, CRITICAL).



## ⚠️ Prerequisites

Before using this GitHub Action, ensure you have the following:

- **AccuKnox Console Access** – Sign in to your AccuKnox tenant.
- **API Token** – Retrieve the token from the AccuKnox Console  
  (see [Token Generation](https://help.accuknox.com/getting-started/how-to-create-tokens/)).
- **Project Name (from AccuKnox Console UI)** – Create or identify a project in the AccuKnox Console.  
  This is **mandatory only for SBOM generation**.
- **Label Created in Console** – Used for tagging and organizing uploaded scan reports.
- **GitHub Secrets Setup** – Store all sensitive credentials securely using GitHub Secrets.



## 📌 Installation & Usage

### Step 1: Retrieve AccuKnox Credentials

- **Login to AccuKnox Console**
- Navigate to **Settings → Tokens**
- Click **Create Token** and store:
  - `ACCUKNOX_TOKEN`

---

### Step 2 (Optional): Create a Project in AccuKnox Console (Required for SBOM)

> ⚠️ This step is **only required if you plan to generate SBOMs** using `generate_sbom: true`.

To associate SBOM data with the correct entity, you must create a **Project** in the AccuKnox Console.

1. Log in to the **AccuKnox Dashboard**
2. Navigate to **SBOM → Projects**
3. Click **New Project**
4. Fill in the required details:
   - **Name*** – Project name (used as `project_name` in the workflow)
   - **Description** – Short description of the project
   - **Classifier*** – Select **Container**
   - **Tags** – (Optional) Add relevant tags
5. Click **Create**

📌 **Note:**  
The **Project Name** must exactly match the value provided in the GitHub workflow under `project_name`.

---

### Step 3: Define Your GitHub Workflow

Create a workflow file (e.g., `.github/workflows/container-scan.yml`) and add the following configuration:

```yaml
name: AccuKnox Container Scan

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  container-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run AccuKnox Container Scanner
        uses: accuknox/container-scan-action@latest
      
        with:
          accuknox_token: ${{ secrets.ACCUKNOX_TOKEN }}
          accuknox_label: ${{ secrets.ACCUKNOX_LABEL }}
          accuknox_endpoint: ${{ secrets.ACCUKNOX_ENDPOINT }}
          image_name: "your-image"
          tag: "latest"
          severity: "UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL"
          soft_fail: true
          upload_results: true  # (Optional) set true if you want to upload result to Github artefact
          generate_sbom: true   # (Optional) set true to generate SBOM
          project_name: ""      # (Optional) must match the project name created in the dashboard
          dockerfile_context: Dockerfile  # Path to Dockerfile for building image before scan 
```

### ⚙️ Configuration Options (Inputs)

| Input | Description | Required | Default |
|------|------------|----------|---------|
| `accuknox_endpoint` | URL of the AccuKnox Console to upload scan results | ✅ Yes | — |
| `accuknox_token` | API token used to authenticate with the AccuKnox Console | ✅ Yes | — |
| `accuknox_label` | Label used in the AccuKnox Console to tag scan results | ✅ Yes | — |
| `image_name` | Name of the container image to scan | ✅ Yes | — |
| `tag` | Tag of the container image | ❌ No | `latest` |
| `severity` | Vulnerability severities to enforce (e.g., LOW, MEDIUM, HIGH, CRITICAL) | ❌ No | All |
| `soft_fail` | Continue pipeline execution even if vulnerabilities are found | ❌ No | `false` |
| `generate_sbom` | Generate and upload SBOM instead of vulnerability scan | ❌ No | `false` |
| `project_name` | AccuKnox project name (required when SBOM generation is enabled) | ❌ No | — |
| `upload_results` | Upload scan results as GitHub artifact | ❌ No | `true` |
| `dockerfile_context` | Path to Dockerfile for building image before scan | ❌ No | Dockerfile |

---

## 🔍 How It Works

1️⃣ **Container Image is Scanned**  
The AccuKnox Container Scanner analyzes the specified image for known vulnerabilities and security issues.

2️⃣ **Scan Report Generated**  
A detailed JSON scan report is generated containing vulnerability findings.

3️⃣ **Upload to AccuKnox Console**  
Scan results (and SBOMs, if enabled) are securely uploaded to your AccuKnox tenant for centralized visibility.

4️⃣ **Severity Filtering (Optional)**  
If `severity` is configured, the workflow will fail when matching vulnerabilities are detected.

---

## 🛠️ Troubleshooting & Best Practices

❌ **Pipeline Blocked by Vulnerabilities?**

- Adjust the `severity` input to allow less critical findings.
- Review scan results in the AccuKnox Console and remediate identified issues.

🔑 **Authentication Errors?**

- Verify `ACCUKNOX_TOKEN`, `ACCUKNOX_LABEL`, and `ACCUKNOX_ENDPOINT` are correctly stored in GitHub Secrets.
- Regenerate the API token in the AccuKnox Console if required.

🧪 **Best Practices**

- Scan container images on every push and pull request.
- Enable SBOM generation to improve software supply chain visibility.
- Monitor trends and findings in the AccuKnox Console for proactive risk management.

---

## 📖 Support & Documentation

📚 **Read More**: [AccuKnox Docs](https://help.accuknox.com)  
📧 **Contact Support**: [support@accuknox.com](mailto:support@accuknox.com)

---

## 🏁 Conclusion

The **AccuKnox Container Scan GitHub Action** empowers CI/CD pipelines with automated container security scanning and SBOM generation. Identify risks early, enforce security gates, and gain visibility into container vulnerabilities across your environments.

🔐 **Shift Left with AccuKnox – Secure from Build to Runtime!** 🧱

---

