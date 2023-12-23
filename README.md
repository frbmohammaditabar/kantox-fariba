# kantox-fariba
My Repository for kantox challenge.

The Jedi Council: Secrets of the Galaxy
Welcome to the first challenge! In this game-challenge you are a Jedi with the mission to find
out the location of other Jedis.
Introduction
You are a Jedi on a secret mission to locate other powerful Jedi across the galaxy. The Jedi
Council has entrusted you with the task of finding these hidden heroes and safeguarding
their locations. You'll receive from time to time a Manifest, a JSON file containing the names
and locations of strong Jedi and a specific mission to locate one of them.
{
"98721": {
"name": "Yoda",
"planet": "Dagobah",
"power_level": 90
},
"54832": {
"name": "Obi-Wan Kenobi",
"planet": "Stewjon",
"power_level": 85
},
"12345": {
"name": "Mace Windu",
"planet": "Haruun Kal",
"power_level": 87
},
"78965": {
"name": "Rey",
"planet": "Jakku",
"power_level": 75
},
"63421": {
"name": "Qui-Gon Jinn",
"planet": "Coruscant",
"power_level": 82
},
"25689": {
"name": "Ahsoka Tano",
"planet": "Shili",
"power_level": 78
},
"86420": {
"name": "Kit Fisto",
"planet": "Glee Anselm",
"power_level": 76
},
"51234": {
"name": "Plo Koon",
"planet": "Dorin",
"power_level": 83
},
"93571": {
"name": "Ki-Adi-Mundi",
"planet": "Cerean",
"power_level": 81
},
"32698": {
"name": "Shaak Ti",
"planet": "Shili",
"power_level": 79
},
"74623": {
"name": "Luminara Unduli",
"planet": "Mirial",
"power_level": 77
}
}
Objective
Your objective is to locate and safeguard the location of the Jedi identified in the mission
while keeping their identity secret. To achieve this, store the Jedi's ID requested by the
Council as your own encrypted secret (for example “63421”), and then log the Jedi
information requested by the Council everytime you receive a new Manifest with the update
of the locations and new Jedis.
May the Force guide you in your quest to protect the Jedi and preserve their secrets. The
galaxy depends on your skills and discretion!
We expect:
● A working example using Terraform
● Use your CMK
● PoC documentation
● Serverless
● Cost-effective
● Event-driven architecture
We will value positively:
● Clean terraform code and best practices
● Use of modules


KubeOps Challenge: Prove Your Kubernetes &
GitOps Mastery
Welcome to the KubeMaster Challenge, where you'll prove your Kubernetes skills by
deploying a Minikube Kubernetes cluster with a "Hello world" container. What makes this
challenge exciting? You'll continually update the container version, showing off your
expertise in continuous deployment and GitOps using GitHub Actions and ArgoCD. Are you
up for the task?
Challenge Objectives
● Deploy Minikube Cluster: Set up a Minikube Kubernetes cluster on your local
machine.
● Initial Container Deployment: Deploy the initial version of the "Hello world" container
using Kubernetes manifests (Service and Deployment).
● GitHub Action Workflow: Create a GitHub Actions workflow to automate the
deployment of the next semantic version of the container. This should include
updating the version number.
● ArgoCD Configuration: Implement ArgoCD for continuous delivery and set up a
GitOps workflow for your Kubernetes cluster. Your ArgoCD configuration should be
based on a template.
We expect:
● A working example
● Deploy a next version of the app using github action workflow and ArgoCD
● K8s manifest
● ArgoCD configuration ( projects, apps)
We will value positively:
● Deploy without outage
● Multi environments (for example staging, production)
● ArgoCD configuration based on templates
● Zero downtime deployment
