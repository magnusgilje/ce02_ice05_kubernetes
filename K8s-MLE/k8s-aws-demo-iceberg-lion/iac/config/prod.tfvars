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
    userarn  = "arn:aws:iam::411447780843:group/kubernetes_dev"
    username = "kubernetes_dev"
    groups   = ["system:masters"]
  },
]