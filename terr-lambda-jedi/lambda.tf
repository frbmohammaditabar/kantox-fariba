locals {
    lambda_zip_location = "/home/user01/terr-lambda-jedi/outputs/functionjedi.zip"
}

data "archive_file" "init" {
  type        = "zip"
  source_file = "/home/user01/terr-lambda-jedi/functionjedi.py"
  output_path = "/home/user01/terr-lambda-jedi/outputs/functionjedi.zip"
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "/home/user01/terr-lambda-jedi/outputs/functionjedi.zip"
  function_name = "functionjedi"
  role          = aws_iam_role.lambda_role.arn
  handler       = "functionjedi.main"

# This is for changing the function
  source_code_hash = data.archive_file.init.output_base64sha256

  runtime = "python3.10"
  
  environment {
    variables = {
      MANIFEST_S3_BUCKET = aws_s3_bucket.manifest.bucket
    }
  }
}
resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.test_lambda.function_name
  principal     = "s3.amazonaws.com"
}

resource "aws_s3_bucket" "manifest" {
  bucket = "jedibucketfariba"  # Change this to your desired S3 bucket name
}
