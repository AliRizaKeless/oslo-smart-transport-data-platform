variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "rg-oslo-transport-data-dev"
}

variable "location" {
  description = "Azure region for the resources"
  type        = string
  default     = "norwayeast"
}

variable "storage_account_name" {
  description = "Name of the Azure Storage Account"
  type        = string
  default     = "stoslodataplatformdev"
}