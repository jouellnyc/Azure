from creds import tenant_id, client_id, client_secret, object_id

import msal
import requests


def remove_application_secrets(tenant_id, client_id, client_secret, secret_ids):
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = msal.ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret
    )

    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    if "access_token" not in result:
        print(result.get("error"))
        print(result.get("error_description"))
        return

    # Remove each secret
    headers = {
        'Authorization': 'Bearer ' + result['access_token'],
        'Content-Type': 'application/json'
    }

    for secret_id in secret_ids:
        try:
            # Microsoft Graph API endpoint for removing password
            url = f"https://graph.microsoft.com/v1.0/applications/{object_id}/removePassword"

            # Payload with the specific secret ID to remove
            payload = {"keyId": secret_id}

            # Send POST request to remove the password
            response = requests.post(url, headers=headers, json=payload)

            # Check response
            if response.status_code == 204:
                print(f"Successfully removed secret with ID: {secret_id}")
            else:
                print(f"Failed to remove secret {secret_id}. Status code: {response.status_code}")
                print(response.text)

        except Exception as e:
            print(f"Error removing secret {secret_id}: {str(e)}")

remove_application_secrets(
    client_id=client_id,
    tenant_id=tenant_id,
    client_secret=client_secret,
    secret_ids=['blah1', 'blah2']
)

