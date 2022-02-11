environment = "dev"

map_accounts = [
  "411447780843"
]
map_roles = [
]
map_users = [
  {
    userarn  = "arn:aws:iam::411447780843:user/ce02-AWS-Terraform-dev"
    username = "ce02-AWS-Terraform-dev"
    groups   = ["system:masters"]
  },
  {
    userarn  = "arn:aws:iam::411447780843:user/ce02-AWS-dev"
    username = "ce02-AWS-dev"
    groups   = ["system:masters"]
  },
  {
    userarn  = "arn:aws:iam::411447780843:user/MartinPalmer"
    username = "MartinPalmer"
    groups   = ["system:masters"]
  },
  {
    userarn  = "arn:aws:iam::411447780843:group/kubernetes_dev"
    username = "kubernetes_dev"
    groups   = ["system:masters"]
  },
]