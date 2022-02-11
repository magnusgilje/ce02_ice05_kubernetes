terraform {
  backend "s3" {
  }
}

locals {
  cluster_name = format("%s_ce%02d_aks_cluster_demo", var.environment, var.cohort)

  default_tags = tomap({
    "environment" = var.environment
    "project"     = var.project
    "purpose"     = "eks"
    }
  )
}

provider "aws" {
  region = var.region
}

provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
  token                  = data.aws_eks_cluster_auth.cluster.token
}

data "aws_eks_cluster" "cluster" {
  name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_id
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "17.1.0"

  # cluster_security_group_id = aws_security_group.ingress.id
  cluster_name    = local.cluster_name
  cluster_version = "1.21"
  subnets         = module.vpc.private_subnets
  enable_irsa     = true
  vpc_id          = module.vpc.vpc_id

  workers_group_defaults = {
    root_volume_type = "gp2"
  }

  # cluster_endpoint_private_access = "true"
  # cluster_endpoint_public_access  = "true"

  worker_groups = [
    {
      name                          = "worker-group-1"
      instance_type                 = "t2.large"
      asg_desired_capacity          = 1
      additional_security_group_ids = [aws_security_group.worker_group_mgmt_one.id]
    },
    {
      name                          = "worker-group-2"
      instance_type                 = "t2.large"
      additional_security_group_ids = [aws_security_group.worker_group_mgmt_two.id]
      asg_desired_capacity          = 1
    },
  ]

  worker_additional_security_group_ids = [aws_security_group.all_worker_mgmt.id]
  map_roles                            = var.map_roles
  map_users                            = var.map_users
  map_accounts                         = var.map_accounts
}