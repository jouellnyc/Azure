from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.applications.item.remove_password.remove_password_post_request_body import RemovePasswordPostRequestBody

from uuid import UUID

from creds import tenant_id, client_id, client_secret

async def delete_secret():

    """
    Asynchronously deletes a secret (password) from an Azure AD application using the Microsoft Graph API.

    This function authenticates using a client secret and removes the password associated with a specific key ID
    from the specified application.  It handles potential exceptions during the process.
    """

    try:

        credential = ClientSecretCredential(
                    tenant_id=tenant_id,
                    client_id=client_id,
                    client_secret=client_secret
        )


        scopes = ['https://graph.microsoft.com/.default']
        graph_client = GraphServiceClient(credential, scopes)

        request_body = RemovePasswordPostRequestBody(
            key_id = UUID("$UUID_OF_THE_KEY"),
        )

        result = await graph_client.applications.by_application_id('$APP-ID').remove_password.post(request_body)

    except Exception as e:
        print(f"Error deleting secret: {str(e)}")
        raise

if __name__ == "__main__":
    import asyncio
    asyncio.run(delete_secret())



