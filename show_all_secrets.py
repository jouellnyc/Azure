from msgraph import GraphServiceClient

from azure.identity import ClientSecretCredential
from creds import tenant_id, client_id, client_secret

async def show_secrets():
    """
    Retrieves and displays the password credentials (secrets) for a given Azure AD application.

    This function uses the Microsoft Graph API to fetch the secret information.  It requires
    credentials to be provided via environment variables or a separate 'creds.py' file (as in this example).

    Raises:
        Exception: If an error occurs during the process, it will be caught and the error message printed.
    """
    try:
        credential = ClientSecretCredential(
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret
        )

        scopes = ['https://graph.microsoft.com/.default']
        graph_client = GraphServiceClient(credential, scopes)

        result = await graph_client.applications.by_application_id($APP_OBJECT_ID).get()
        for credential in result.password_credentials:
            print(f"Display Name: {credential.display_name}, Key ID: {credential.key_id}, End Date: {credential.end_date_time}")

    except Exception as e:
        print(f"Error creating secret: {str(e)}")
        raise

if __name__ == "__main__":
    import asyncio
    asyncio.run(rotate_secret())
