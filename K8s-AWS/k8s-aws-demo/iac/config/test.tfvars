environment = "test"
cohort      = 2
dns         = "kubrickgroup.training"
map_accounts = [
  "411447780843"
]
map_roles = [
]
map_users = [
  {
    userarn  = "arn:aws:iam::411447780843:user/ce02-AWS-Terraform-test"
    username = "ce02-AWS-Terraform-test"
    groups   = ["system:masters"]
  },
  {
    userarn  = "arn:aws:iam::411447780843:user/ce02-AWS-test"
    username = "ce02-AWS-test"
    groups   = ["system:masters"]
  },
  {
    userarn  = "arn:aws:iam::411447780843:user/MartinPalmer"
    username = "MartinPalmer"
    groups   = ["system:masters"]
  },
]