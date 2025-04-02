

#  **AccuKnox Container Scan GitHub Action**  

### **Enhance Your Container Security with Automated Vulnerability Scanning**  

The **AccuKnox Container Scan GitHub Action** allows you to **automatically scan Docker images for security vulnerabilities** and upload scan results to the **AccuKnox Console**. This action integrates seamlessly into your **CI/CD pipeline**, ensuring **continuous security compliance** and enabling teams to proactively detect and remediate vulnerabilities before deployment.  

---

## 🎯 **Key Features**  

✅ **Automated Security Scanning** – Scans Docker images for vulnerabilities during the build and deployment process.  
✅ **Customizable Severity Levels** – Define threshold levels (UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL) to block builds based on vulnerability severity.  
✅ **Seamless CI/CD Integration** – Works effortlessly within GitHub Actions workflows.  

---

## ⚠️ **Prerequisites**  

Before using this GitHub Action, ensure the following:  

1️⃣ **An AccuKnox Account** – Connect with the AccuKnox Support team at [support@accuknox.com](mailto:support@accuknox.com).  
2️⃣ **AccuKnox API Token & Tenant ID** – Required for authentication (see [Token Generation](https://help.accuknox.com/getting-started/how-to-create-tokens/)).  
3️⃣ **Docker Image Available** – Ensure your container image is created or available before scanning.  
4️⃣ **GitHub Repository with Actions Enabled** – Required for running workflows.  

---

## 📌 **Installation & Usage**  

To integrate this action into your GitHub workflow:  

### **Step 1: Define the Workflow in `.github/workflows/container-scan.yml`**  

Create a new workflow file inside your GitHub repository:  

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
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Build Docker Image
        run: |
          docker build -t my-docker-repo/image-name:latest .

      - name: Run AccuKnox CSPM Scan
        uses: accuknox/container-scan-action@v1
        with:
          token: ${{ secrets.ACCUKNOX_TOKEN }}
          tenant_id: ${{ secrets.ACCUKNOX_TENANT_ID }}
          image: my-docker-repo/image-name
          tag: latest
          severity: HIGH
```

---

## ⚙️ **Configuration Options (Inputs)**  

This GitHub Action supports the following inputs:  

| **Input Parameter** | **Description** | **Required** | **Default Value** |
|----------------------|----------------|--------------|-------------------|
| `endpoint` | The URL of the CSPM panel where scan results are uploaded. | ✅ Yes | `cspm.demo.accuknox.com` |
| `token` | Authentication token for AccuKnox API. | ✅ Yes | None |
| `tenant_id` | Tenant ID for the AccuKnox Console. | ✅ Yes | None |
| `label` | Label to categorize scan results in AccuKnox Console. | ✅ Yes | None |
| `image` | Name of the Docker image to scan. | ✅ Yes | None |
| `tag` | Tag/version of the Docker image. | ✅ Yes | `${{ github.run_id }}` |
| `severity` | Minimum vulnerability severity that will trigger a failure (UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL). | ❌ No | None |

---

## 🔍 **How It Works?**  

### **Step 1: Checkout Your Repository**  
The workflow starts by pulling your source code from GitHub.  

### **Step 2: Build the Docker Image**
Build the Docker image for scanning in later stages via AccuKnox Container Scan plugin. 

### **Step 3: Run AccuKnox Container Scan**  
- The scan is executed using the `accuknox/container-scan-action@v1` GitHub Action.  
- The provided **Docker image** is analyzed, and results are generated.  

### **Step 4: Scan Results Uploaded**  
- The scan results are securely uploaded to the **AccuKnox Console**.  
- The pipeline can fail based on detected vulnerabilities and the configured **severity level**.  

---

## 🛠️ **Troubleshooting & Best Practices**  

### ❌ **Pipeline Failing Due to Vulnerabilities?**  
- Adjust the **severity level** to allow certain vulnerabilities.  
- Use **`severity: CRITICAL`** to fail only on critical vulnerabilities.  

### 🔑 **Invalid Token Error?**  
- Ensure the **token is correctly set** in GitHub Secrets.  
- **Regenerate** the token from the AccuKnox Console if needed.  

---

## 🔒 **Security Best Practices**  

- **Regular Scans** – Automate scanning on every pull request & deployment.  
- **Enforce Policies** – Set **severity thresholds** to prevent high-risk vulnerabilities from reaching production.  
- **Least Privilege Access** – Store secrets securely in GitHub and avoid exposing credentials in workflow files.  

---

## 📖 **Support & Documentation**  

📚 **Read More:** [AccuKnox Docs](https://www.accuknox.com/)  
📧 **Contact Support:** [support@accuknox.com](mailto:support@accuknox.com)  

---

## 🏆 **Conclusion**  

The **AccuKnox Container Scan GitHub Action** empowers teams to **detect security vulnerabilities early**, enforce security compliance, and **streamline DevSecOps workflows**. By integrating this action into your CI/CD pipeline, you can ensure that only **secure** containers are deployed.  

> 🔹 **Secure your containers with AccuKnox – Start Today!** 🔒  


