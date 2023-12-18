How to deploy AWS Lambda Function using Terraform

1. Create Terraform provider for region us-east-1
2. Create lambda funtion basic using python
functionjedi.py
3. Create IAM Role
  2.1: Create IAM Role Policy
     https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy
     https://awspolicygen.s3.amazonaws.com/policygen.html
     IAM Policy > Amazon CloudWatch Logs > All Services> Add statement> Generate Policy

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1702550400569",
      "Action": "*",
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}


 Policy = I will open for AWS CloudWatch Logs
 We using JSON and file to call policy

  
  2.2: Create Assume Policy

https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function


4. Write Lambda function terraform
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function

5. Zip filehttps://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file

We have 2 outputs/functionbasic.zip
We will use locals to 

6. Run apply terraform

terraform init
terraform plan
terraform apply

7. Testing lambda function and check CloudWatch Logs

Access key:
AKIAUSBC7FPAMZARS5AT
Secret Key:
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
8. Delete

terraform destroy  
