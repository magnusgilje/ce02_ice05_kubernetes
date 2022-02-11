locals {
  prefix   = (var.prefix == "" ? "" : format("%s-", var.prefix))
  suffix   = (var.suffix == "" ? "" : format("-%s", var.suffix))
  ecr_name = format("%s%s%s", local.prefix, var.environment, local.suffix)
}

resource "aws_ecr_repository" "ecr" {
  name                 = local.ecr_name
  image_tag_mutability = "MUTABLE"
  tags                 = merge(tomap({ "image" = var.environment }), local.default_tags)
}