variable "region" {
  description = "AWS region to be deployed into."
  type        = string
}

variable "environment" {
  type = string
}

variable "prefix" {
  type    = string
  default = ""
}

variable "suffix" {
  type    = string
  default = ""
}

variable "project" {
  type = string
}

variable "cohort" {
  type = string
}