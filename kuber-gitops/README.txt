Step 1: Set Up Minikube on AWS

cd ec2-minikube-aws/
module_three.tf  terraform.tfvars

terraform init
terraform apply

ssh -i /path/to/faribakeypair.pem ec2-userbe_instance_ip>

Step 2: Initial Container Deployment

deployement.yaml

service.yaml

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml


Step 3: GitHub Actions Workflow
Create GitHub Actions Workflow:
Create a GitHub Actions workflow (e.g., in a .github/workflows directory) to automate the deployment of the next semantic version of the container. This should include updating the version number in your deployment manifests.

workflows.yaml


Step 4: ArgoCD Configuration
Install ArgoCD:
Follow the ArgoCD installation instructions to install ArgoCD on your Minikube cluster: ArgoCD Installation Guide.

Create ArgoCD Application:
Define an ArgoCD Application using an Application manifest or through the ArgoCD UI. The Application should reference your GitHub repository and the Kubernetes manifests within it.

Example Application manifest:

manifest.yaml


Set Up GitOps Workflow:
Ensure that changes to your Kubernetes manifests in your Git repository trigger ArgoCD to apply changes to the Minikube cluster.



