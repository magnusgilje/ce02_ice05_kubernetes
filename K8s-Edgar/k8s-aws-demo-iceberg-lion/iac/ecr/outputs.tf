output "ecr_shortname" {
  value = aws_ecr_repository.ecr.name
}

output "repository_url" {
  value = aws_ecr_repository.ecr.repository_url
}