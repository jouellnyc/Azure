from msgraph import GraphServiceClient
from msgraph.generated.applications.item.add_password.add_password_post_request_body import AddPasswordPostRequestBody
from msgraph.generated.models.password_credential import PasswordCredential

from azure.identity import ClientSecretCredential
from creds import tenant_id, client_id, client_secret

async def rotate_secret():
    try:
        """
        Rotates the secret for an Azure AD application.

        This function uses the Microsoft Graph API to add a new password to the specified application.
        It then prints the new secret value and key ID.  It's crucial to store the secret securely
        as it won't be retrievable again through the Graph API after creation.

        Raises:
            Exception: If an error occurs during the secret creation process.  The specific error
                       is printed to the console before re-raising the exception.

        Returns:
            PasswordCredential: The newly created PasswordCredential object returned by the Graph API.
                                This contains information about the created password, including the key ID.
                                Note: The actual secret value is only available immediately after creation
                                and is included in the returned object.
        """
        credential = ClientSecretCredential(
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret
        )

        scopes = ['https://graph.microsoft.com/.default']
        graph_client = GraphServiceClient(credential, scopes)

        request_body = AddPasswordPostRequestBody(
            password_credential=PasswordCredential(
                display_name="Display Name",
            ),
        )

        #Object ID
        result = await graph_client.applications.by_application_id(
            '$APP-ID'
        ).add_password.post(request_body)

        print(f"New secret created successfully!")
        print(f"Secret value: {result.secret_text}")  # Print the actual secret
        print(f"Key ID: {result.key_id}")             # Print the key ID

        return result

    except Exception as e:
        print(f"Error creating secret: {str(e)}")
        raise

if __name__ == "__main__":
    import asyncio
    asyncio.run(rotate_secret())
