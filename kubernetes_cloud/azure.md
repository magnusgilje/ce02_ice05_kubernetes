# Azure Deployment from Command Line

## Create the container image

1. Create a container image

    Start within the `hellokubrickfromkubernetes` folder

    Check the folder has the following files:
    * `Dockerfile`
    * `main.go`
    * `go.mod`
  
    ``` cmd
        dir
    ```

    Now build the docker image

    ``` cmd
    docker build . -t hellokubrick
    docker images
    ```

1. Test the image locally

    ``` cmd
    docker run -p 8080:8080 hellokubrick:latest
    ```

1. In a separate terminal, access the container

    ``` cmd
    curl http://localhost:8080
    ```

1. Now clean up and close the container image

    ``` cmd
    curl http://localhost:8080
    docker container ls --format "{{.ID}} {{.Image}}"
    docker stop <container id>
    ```

## Update the azure cli tooling and login

1. Download aks cli

    Install kubectl locally using the az aks install-cli command:

    ``` cmd
    az aks install-cli
    ```

1. Login to the Azure infrastructure

    1. Log into  "Kubrick Training"

        ``` cmd
        az login --tenant c56ac403-160c-4cd5-937a-d9154c81466b
        ```

    1. Use the `training_ce02` subscription

        ``` cmd
        az account set --subscription f92c3804-6fcc-478e-a9cc-0304683d131f
        ```

    1. Check the account details

        ``` cmd
        az account show
        ```

## Set up the cloud infrastructure

1. Create Azure resource group

    We will be using the azure resource group `rg-kubrick-k8s` for this example

    ``` cmd
    az group create --location northeurope --resource-group rg-kubrick-k8s
    ```

1. Create a tagged image for our container registry

    ``` cmd
    docker build . -t acrdockerdevguest.azurecr.io/hellokubrick:v1
    docker images
    ```

1. Upload the container to the container registry

    ``` cmd
    az acr login -n acrdockerdevguest.azurecr.io
    docker push acrdockerdevguest.azurecr.io/hellokubrick:v1
    ```

    Check with [Artifact Registry](https://portal.azure.com/#@kubrickgrouptraining.onmicrosoft.com/resource/subscriptions/f92c3804-6fcc-478e-a9cc-0304683d131f/resourceGroups/rgce02dockerdev01/providers/Microsoft.ContainerRegistry/registries/acrdockerdevguest/repository)

## Create Kubernetes instance in Azure

1. Create the Azure Kubernetes Cluster (AKS)

   The cluster we will use will be called `hello-cluster` and deployed into our resource group `rg-kubrick-k8s`.

   ``` cmd
    az aks create --resource-group rg-kubrick-k8s --name hello-cluster --node-count 2 --enable-addons monitoring --generate-ssh-keys --attach-acr acrdockerdevguest
   ```

1. Get the access credentials for our cluster credentials

    ``` cmd
    az aks get-credentials --resource-group rg-kubrick-k8s --name hello-cluster
    ```

1. Deploy our container

   Use the tagged image `hellokubrick:v1` from the register `acrdockerdevguest` to port `8080`

    ``` cmd
    kubectl run hello-cluster --image=acrdockerdevguest.azurecr.io/hellokubrick:v1 --port 8080

    ```

---

## Now onto `Kubectl`

1. Check the container is running, and get its service information

    ``` cmd
    kubectl get pods
    ```

   This will present a table on the kubernetes pods

    |NAME|READY|STATUS|RESTARTS|AGE|
    |-|-|-|-|-|
    |hello-cluster|1/1|Running|0|2m13s|

1. Check the current status

    ``` cmd
    kubectl get svc
    ```

    This shows a table of the networking for the kubernetes cluster

    |NAME|TYPE|CLUSTER-IP|EXTERNAL-IP|PORTS|AGE|
    |-|-|-|-|-|-|
    |kubernetes|ClusterIP|10.24.0.1|24\<none\>|443/TCP| 1m12s

## Create a deployment and expose to the internet

1. Check the current status

    ``` cmd
    kubectl get svc
    ```

    This shows a table of the networking for the kubernetes cluster

    |NAME|TYPE|CLUSTER-IP|EXTERNAL-IP|PORTS|AGE|
    |-|-|-|-|-|-|
    |kubernetes|ClusterIP|10.24.0.1|24\<none\>|443/TCP|

1. Create a deployment and use a load balancer as a front
   1. Our deployment will be called `hello-kubrick` for our tagged container:

        ``` cmd
        kubectl create deployment hello-kubrick --image=acrdockerdevguest.azurecr.io/hellokubrick:v1     
        ```

    1. Use port 80 (http) to be on the front of the load balancer

        ``` cmd
        kubectl expose deployment hello-kubrick --type=LoadBalancer --port 80 --target-port 8080
        ```

3. Now re-check the network status

    ``` cmd
    kubectl get svc
    ```

    This shows a table of the networking for the kubernetes cluster

    |NAME|TYPE|CLUSTER-IP|EXTERNAL-IP|PORTS|AGE|
    |-|-|-|-|-|-|
    |hello-kubrick|LoadBalancer|10.0.149.234|20.67.206.36|80:32127/TCP| 12m|
    |kubernetes|ClusterIP|10.0.0.1|\<none\>|443/TCP| 12m

4. Re-Run our curl command from earlier with our new `external ip address`

    ``` cmd
    curl http://20.67.206.36
    ```

---

## Clean up our resources

   1. Delete Deployed service

      ``` cmd
      kubectl delete service hello-kubrick
      ```

   2. Remove our kubernetes cluster

      ``` cmd
      az aks delete --resource-group rg-kubrick-k8s --name hello-cluster
      ```
