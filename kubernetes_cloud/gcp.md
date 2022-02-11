# GCP Deployment from Command Line

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

2. Test the image locally

    ``` cmd
    docker run -p 8080:8080 hellokubrick:latest
    ```

3. In a separate terminal, access the container

    ``` cmd
    curl http://localhost:8080
    ```

4. Now clean up and close the container image

    ``` cmd
    docker container ls --format "{{.ID}} {{.Image}}"
    docker stop <container id>
    ```

## Login to Google Cloud

Note well be in the `ce02-330213` google account for this exercise and using the `europe-west2-c` zone.

``` cmd
    gcloud init
```

## Set up the cloud infrastructure

1. Create a tagged image for our container registry

    ``` cmd
    docker build . -t gcr.io/ce02-330213/hellokubrick:v1
    docker images
    ```

1. Upload the container to the container registry

    ``` cmd
    gcloud auth configure-docker
    docker push gcr.io/ce02-330213/hellokubrick:v1
    ```

    Check with [Artifact Registry](https://console.cloud.google.com/gcr/images/ce02-330213?project=ce02-330213)

## Create Kubernetes instance in Google Cloud Platform

1. Create the Google Kubernetes Cluster (GKS)

   The cluster we will use will be called `hello-cluster`

    ```cmd
    gcloud container clusters create hello-cluster --num-nodes=2 --zone=europe-west2-c 
    ```

1. Get the access credentials for our cluster credentials

    ``` cmd
    gcloud container clusters get-credentials hello-cluster --region=europe-west2-c
    ```

1. Deploy our container

    Use the tagged image `hellokubrick:v1` from the register `gcr.io/ce02-330213` to port `8080`

    ``` cmd
    kubectl run hello-cluster --image=gcr.io/ce02-330213/hellokubrick:v1 --port 8080
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
    |hello-cluster|1/1|Running|0|2m34s|

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
    |kubernetes|ClusterIP|10.24.0.1|\<none\>|443/TCP| 6m12s

1. Create a deployment and use a load balancer as a front
   1. Our deployment will be called `hello-kubrick` for our tagged container:

        ``` cmd
        kubectl create deployment hello-kubrick --image=gcr.io/ce02-330213/hellokubrick:v1
        ```

   1. Use port 80 (http) to be on the front of the load balancer

        ``` cmd
        kubectl expose deployment hello-kubrick --type=LoadBalancer --port 80 --target-port 8080
        ```

1. Now re-check the network status

    ``` cmd
    kubectl get svc
    ```

    This shows a table of the networking for the kubernetes cluster

    |NAME|TYPE|CLUSTER-IP|EXTERNAL-IP|PORTS|AGE|
    |-|-|-|-|-|-|
    |hello-kubrick|LoadBalancer|10.24.1.191|34.89.63.241|80:32204/TCP| 51s|
    |kubernetes|ClusterIP|10.24.0.1|\<none\>|443/TCP| 12m

1. Re-Run our curl command from earlier with our new `external ip address`

    ``` cmd
    curl http://34.89.63.241
    ```

## Clean up our resources

   1. Delete Deployed service

    ``` cmd
    kubectl delete service hello-kubrick
    kubectl get svc
    gcloud container clusters delete hello-cluster --region=europe-west2-c
    ```
