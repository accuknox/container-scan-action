# AccuKnox Container Scan

🛡️ **Secure Your Container Images Automatically**

The **AccuKnox Container Scan GitHub Action** enables developers and DevSecOps teams to perform automated vulnerability scans on container images and seamlessly upload results to the AccuKnox Console. Ensure your container workloads are compliant, secure, and free from known vulnerabilities.

---

## 🎯 Key Features

- **Automated Container Image Scanning** – Detects known vulnerabilities in containerized workloads.
- **Seamless GitHub Actions Integration** – Plug directly into your CI/CD pipelines.
- **Centralized Results** – Scan reports are uploaded to the AccuKnox Console for review and tracking.
- **Severity Enforcement** – Block deployments with high/critical vulnerabilities.
- **Custom Labels and Metadata** – Tag scan reports using labels in AccuKnox Console.

---

## ⚠️ Prerequisites

Before using this GitHub Action, ensure you have the following:

- **AccuKnox Console Access** – Sign in to your AccuKnox tenant.
- **API Token & Tenant ID** – Retrieve these from the AccuKnox Console. (see [Token Generation](https://help.accuknox.com/getting-started/how-to-create-tokens/)).
- **Label Created in Console** – For tagging the uploaded scan reports.
- **GitHub Secrets Setup** – Store credentials securely using GitHub Secrets.

---

## 📌 Installation & Usage

### Step 1: Retrieve AccuKnox Credentials

* **Login to AccuKnox Console**
* Navigate to **Settings → Tokens**
* Click **"Create Token"** and store:

  * `accuknox_token`

### Step 2: Define Your GitHub Workflow

Create a workflow file (e.g., `.github/workflows/container-scan.yml`) and add the following configuration:

```yaml
name: AccuKnox Container Scan

on:
  push:
    branches:
      - main

jobs:
  container-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run AccuKnox Container Scanner
        uses: accuknox/container-scan-action@v1.0.0
        with:
          soft_fail: false          # set false to fail workflow if vulnerabilities are found
          endpoint: ${{ secrets.ACCUKNOX_ENDPOINT }}
          label: ${{ secrets.ACCUKNOX_LABEL }}
          token: ${{ secrets.ACCUKNOX_TOKEN }}
          image: "your-image-name"
          tag: "latest"             # optional
          severity: "LOW, MEDIUM, HIGH, CRITICAL, UNKNOWN"
          
```

---

## ⚙️ Configuration Options (Inputs)

| Input       | Description                                                                 | Required | Default                  |
| ----------- | --------------------------------------------------------------------------- | -------- | ------------------------ |
| `endpoint`  | URL of the AccuKnox Console to push scan results                            | ✅ Yes    | `cspm.demo.accuknox.com` |
| `token`     | API token to authenticate with the AccuKnox Console                         | ✅ Yes    | —                        |
| `image`     | Name of the container image to scan                                         | ✅ Yes    | —                        |
| `tag`       | Version tag for the container image                                         | ✅ Yes    | `${{ github.run_id }}`   |
| `severity`  | (Optional) Severity levels to block pipeline (`LOW`, `MEDIUM`, `HIGH`, etc) | ❌ No     | —                        |
| `label`     | Label used in AccuKnox Console to tag scan results                          | ✅ Yes    | —                        |

---

## 🔍 How It Works

1️⃣ **Container Image is Scanned**
AccuKnox Container Vulnerability Scanner analyzes the specified image for CVEs and misconfigurations.

2️⃣ **Scan Report Generated**
A JSON scan report is produced with detailed findings.

3️⃣ **Upload to AccuKnox Console**
The report is securely sent to your tenant's dashboard for centralized review and tracking.

4️⃣ **Severity Filtering (Optional)**
If `severity` is defined, the workflow will block if matching vulnerabilities are found.

---

## 🛠️ Troubleshooting & Best Practices

❌ **Pipeline Blocked by Vulnerabilities?**

* Adjust the `severity` input to allow less critical findings.
* Review scan reports in the AccuKnox Console to triage issues.

🔑 **Authentication Errors?**

* Verify your `token` and `tenant_id` are correctly stored in GitHub Secrets.
* Regenerate credentials in AccuKnox Console if needed.

🧪 **Best Practices**

* Scan every push and release candidate.
* Monitor trends via AccuKnox Console for proactive risk management.

---

## 📖 Support & Documentation

📚 **Read More**: [AccuKnox Docs](https://help.accuknox.com)
📧 **Contact Support**: [support@accuknox.com](mailto:support@accuknox.com)

---

## 🏁 Conclusion

The **AccuKnox Container Scan GitHub Action** empowers your CI/CD pipelines with automated container security scanning. Identify critical issues early, enforce deployment security gates, and gain visibility into vulnerabilities across container workloads.

🔐 **Shift Left with AccuKnox – Secure from Build to Runtime!** 🧱

---
