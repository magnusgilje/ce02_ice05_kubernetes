environment = "prod"
cohort      = 2
dns         = "kubrickgroup.training"
map_accounts = [
  "411447780843"
]
map_roles = [
]
map_users = [
  {
    userarn  = "arn:aws:iam::411447780843:user/ce02-AWS-Terraform-prod"
    username = "ce02-AWS-Terraform-prod"
    groups   = ["system:masters"]
  },
  {
    userarn  = "arn:aws:iam::411447780843:user/ce02-AWS-prod"
    username = "ce02-AWS-prod"
    groups   = ["system:masters"]
  },
  {
    userarn  = "arn:aws:iam::411447780843:user/MartinPalmer"
    username = "MartinPalmer"
    groups   = ["system:masters"]
  },
]