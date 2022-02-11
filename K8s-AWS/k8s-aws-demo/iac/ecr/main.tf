terraform {
  backend "s3" {
  }
}

provider "aws" {
  region = var.region
}

locals {
  default_tags = tomap({
    "environment" = var.environment
    "project"     = var.project
    "purpose"     = "ecr"
    }
  )
}