# Secure & Automated Demos Example
This repo is to demonstrate all the pieces of the Secure & Automated Demo environment. It holds all the pieces to deploy and test a demo environment.

## Deploy This Demo

### Pre-Reqs

- [Azure Subscription](https://aka.ms/azure)
- [Visual Studio Online Plan](https://aka.ms/vso-login)

### Deploy Code Workspace

- [Create VSO Workspace](https://env.new?name=Secure%20Demo%20Example&repo=azure-octo/demo-SecureDemos-Example)

### Deploy Azure Resources

- [Deploy Infrastructure ARM Template](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fazure-octo%2Fdemo-SecureDemos-Example%2Fmaster%2F.infrastructure%2Fazure%2Fazuredeploy.json")

### Deploy Data Factory

- [Deploy Data Factory ARM Template](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fazure-octo%2Fdemo-SecureDemos-Example%2Fmaster%2F.infrastructure%2Fazure%2Fdatafactory-template.json")
