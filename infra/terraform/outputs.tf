output "resource_group_name" {
  description = "Name of the created Azure Resource Group"
  value       = azurerm_resource_group.main.name
}

output "resource_group_location" {
  description = "Location of the created Azure Resource Group"
  value       = azurerm_resource_group.main.location
}

output "storage_account_name" {
  description = "Name of the Azure Storage Account"
  value       = azurerm_storage_account.main.name
}

output "raw_container_name" {
  description = "Name of the raw data container"
  value       = azurerm_storage_container.raw.name
}