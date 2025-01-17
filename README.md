# Azure App Secrets Management Scripts (MSGraph)

This repository contains two Python scripts for managing Azure App Secrets and Python:

* **delete_app_secrets.py:** Deletes existing app secrets from an Azure App Registration.
* **add_app_secrets.py:** Adds new app secrets to an Azure App Registration.

**Prerequisites:**

* **Python:** Install Python 3.x.
* **msgraph-sdk:** Install the Microsoft Graph SDK and Azure Identity using pip:
   ```bash

   python -m venv azureenv

   pip install msgraph-sdk
   pip install azure-identity

These values are either gotten from a file (dev setup) or from an online Vault.

```
from creds import tenant_id, client_id, client_secret
```

