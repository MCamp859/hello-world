# Quantization-Aware Training and Inference using OpenVINO™ Toolkit

## Overview

Create an end-to-end AI/ML (Artificial Intelligence/Machine Learning) pipeline
demonstrating Quantization-Aware Training and Inference using a wide array of
Intel® software including the OpenVINO™ toolkit. The workflow is deployed
through Helm* by using microservices and Docker* images, which are built or
taken from Microsoft Azure* Marketplace.†

Select **Configure & Download** to download the workflow.

[Configure & Download](https://www.intel.com/iot/edgesoftwarehub/download/home/ri/quantization_aware_training_and_inference)


-  **Time to Complete:** 10 minutes
-  **Programming Language:** Python*
-  **Available Software:** OpenVINO™ toolkit, OpenVINO™ Integration with
   Optimum\*, Docker\*, Kubernetes\*, Helm\*


## How It Works

![The workflow is represented by a complex block diagram.](quantization-aware-training-usecase-flow.png)

Figure 1: Flow Diagram

The workflow executes as follows:

1. The Pipeline triggers Quantization-Aware Training of a Natural Language
   Processing (NLP) model from Hugging Face. The output of this container is the
   INT8 optimized model stored on a local/cloud storage.
2. Once the model is generated, then inference applications can be deployed with
   one of the following APIs:

    *  Inference using Hugging Face API with Optimum Intel
    *  Inference using Hugging Face API with Optimum ONNX Runtime
    *  Deploy the model using OpenVINO™ Model Server and send in grpc requests

The workflow architecture is shown below.

![The architecture is represented by a complex block diagram.](quantization-aware-training-usecase-architecture.png)

Figure 2: Architecture Diagram



## Get Started

### Prerequisites

You need a Kubernetes* cluster that meets the Edge Node and Software requirements described below.

#### Edge Node Requirements

-  One of the following processors:

    -  Intel® Xeon® Platinum 8370C Processor @ 2.80GHz (16 vCPUs).
    -  Intel® Xeon® Processor with NVIDIA* GPU.

-  At least 64 GB RAM.

-  At least 256 GB hard drive.

-  An Internet connection.

-  Ubuntu\* 20.04 LTS

#### Software Requirements

-  [Docker & Docker Compose installation](https://docs.docker.com/engine/install/ubuntu/)

-  Any flavor of Kubernetes variations.

   This project uses [Rancher* K3S* installation](https://rancher.com/docs/k3s/latest/en/installation/install-options/#options-for-installation-with-script).


    ```bash
    curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
    export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
    ```

-  Helm installation on master node.

   Simple commands are listed below. For details, see [Helm installation instructions](https://helm.sh/docs/intro/install/).

    ```bash
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
    ```

-  This project uses the
   `bert-large-uncased-whole-word-masking-finetuned-squad` model for `Question
   Answering` use case through quantization-aware training and inference. Training and inference scripts are included in the respective folders.

## Step 1: Install and Run the Workflow

### Download Source Code

Choose one of the following options:


*  Select **Configure & Download** to download the workflow.

    [Configure & Download](https://www.intel.com/iot/edgesoftwarehub/download/home/ri/quantization_aware_training_and_inference)


*  Or, run the command:

    ```bash
    git clone https://github.com/intel/nlp-training-and-inference-openvino/tree/main/question-answering-bert-qat
    cd nlp-training-and-inference-openvino/question-answering-bert-qat
    ```



### Modify Helm Chart Values

Edit the ``helmchart/qat/values.yaml`` file as follows:

* Replace ``<current_working_gitfolder>`` under ``mountpath:`` with the current working repo directory. 

    >**Note:** Relative paths do not work with Helm.

* Edit the `helmchart/qat/values.yaml` file for the `<train_node>` and `<inference_node>` values under `'nodeselector'` key.  
    
    Pick any of the available nodes for training and inference with the nodename of this command.

    ```bash 
      kubectl get nodes --show-labels
    ```

   `values.yaml`

    ```bash
    nodeselector:
       trainingnode: <train_node>
       inferencenode: <inference_node>
    ```

   
*  Edit `helmchart/qat/values.yaml` file with higher values of `MAX_TRAIN_SAMPLES`
   and `MAX_EVAL_SAMPLES` parameters for better finetuning of data. Default value
   is 50 samples.
  * Find details on all the parameters in the [Parameters Table](https://github.com/intel/nlp-training-and-inference-openvino/tree/main/question-answering-bert-qat/docs/params_table.md).

## Step 2: Run Helm Charts

This section contains step-by-step details to install specific Helm charts with both training and inference. [Learn more about Helm commands.](https://helm.sh/docs/helm/helm_install/)


### Use Case 1: QAT with Inference using OpenVINO™ Integration with Optimum*

We have options to run inference in two ways:

1.  Using Input CSV file (Default).
2.  Using Arguments (Optional) - Question and Context Argument. We need to edit `deployment_optimum.yaml` to run inference based on question and context argument. We need to pass question and context as below in `deployment_optimum.yaml`:  

    ```bash
    args: ["-c", "chown openvino -R /home/inference && cd /home/inference && ./run_onnx_inference.sh 'Who is sachin' 'Sachin is a cricket player'"]
    ```

The Training pod is deployed through `pre_install_job.yaml`.
The Inference pod is deployed through `deployment_optimum.yaml`.


```bash
cd helmchart
helm install qatchart qat  --timeout <time>
```
The `<time>` value has the format ``nnns``, where **s** indicates seconds. For the above hardware configuration and with
``MAX_TRAIN_SAMPLES=50``, we recommend you set the `<time>` value as ``480s``. You can increase the value
for reduced hardware configuration. Refer to [Troubleshooting](#Troubleshooting)
in case of timeout errors.


Confirm if the training has been deployed.

```bash
kubectl get pods
```

If the training pod is in "Running" state then the pod has been deployed.
Otherwise, check for any errors by running the command:

```bash
kubectl describe pod <pod_name>
```

The training pod will be in "Completed" state after it finishes training. Refer
to the [Training Output section](#training-output) for details.

Once the training is completed, the inference pod gets deployed automatically.
The inference pod uses OpenVINO™ Runtime as a backend to Hugging Face APIs and
takes in model generated from training pod as input.

#### Optimum Inference Output

1. Input to the inference pod will be taken from the `openvino_optimum_inference/data` folder.

2. Output of the OpenVINO™ Integration with Optimum* inference pod will be
   stored in the `openvino_optimum_inference/logs.txt` file.

3. View the logs using:

    ```bash
    kubectl logs <pod_name>
    ```


### Use Case 2: QAT with Inference using OpenVINO™ Model Server

The Training pod is deployed through `pre_install_job.yaml`.
The OpenVINO™ Model Server pod is deployed through `deployment_ovms.yaml`.

Copy `deployment_ovms.yaml` from `helmchart/deployment_yaml` folder into
`helmchart/qat/templates`. Make sure there is only one `deployment_*.yaml` file
in the templates folder for single deployment.

Follow the same instructions as [Use Case 1](#use-case-1-qat-with-inference-using-openvino™-integration-with-optimum).


#### OpenVINO™ Model Server Inference Output
1. OpenVINO™ Model Server deploys optimized model from training container. View
   the logs using the command:

    ```bash
    kubectl logs <pod_name>
    ```

2. The client can send in grpc request to server using OpenVINO™ APIs.
  
   Find more details on the [OpenVINO™ Model Server Adapter API](https://docs.openvino.ai/latest/omz_model_api_ovms_adapter.html).

3. Run a sample OpenVINO™ client application as below. 
  
   Open a new terminal to run the client application. Change the `<hostname>` in the command below before running.
 
   ``<hostname>`` hostname of the node where the OpenVINO™ Model Server has been deployed.  
 ```bash
 kubectl get nodes  
     
 azureuser@SRDev:~/nlp-training-and-inference-openvino/question-answering-bert-qat/openvino_optimum_inference$ kubectl get nodes  
 NAME    STATUS   ROLES                  AGE   VERSION  
 srdev   Ready    control-plane,master   16d   v1.24.6+k3s1   
 ```
 
   In this case, hostname should be `srdev`.
   

#### Run Client Application to Send Request to OpenVINO™ Model Server

This will download inference script from open_model_zoo and serve inference using ovms server.
    
```bash
   cd <gitrepofolder>/openvino_inference
    docker run -it --entrypoint /bin/bash -v "$(pwd)":/home/inference -v "$(pwd)"/../quantization_aware_training/models/bert_int8/vocab.txt:/home/inference/vocab.txt --env VOCAB_FILE=/home/inference/vocab.txt --env  INPUT="https://en.wikipedia.org/wiki/Bert_(Sesame_Street)" --env MODEL_PATH=<hostname>:9000/models/bert openvino/ubuntu20_dev:2022.2.0  -c /home/inference/run_ov_client.sh
```
   
The client application will trigger a interactive terminal to ask questions based on the context for "https://en.wikipedia.org/wiki/Bert_(Sesame_Street)" as this is given as input. Please input a question.

### Use Case 3: QAT with Inference using OpenVINO™ Execution Provider

The Training pod is deployed through `pre_install_job.yaml`.

The Optimum ONNX Runtime with OpenVINO™ Execution Provider pod is deployed through `deployment_onnx.yaml`. 

Copy `deployment_onnx.yaml` from `helmchart/deployment_yaml` folder into `helmchart/qat/templates`. Make sure there is only one deployment_*.yaml file in the templates folder.

Follow the same instructions as [Use Case 1](#use-case-1-qat-with-inference-using-openvino™-integration-with-optimum).

#### Onnxruntime Inference Output
1. Input to the inference pod will be taken from the `onnxovep_optimum_inference/data` folder.

2. Output of the onnxruntime inference pod will be stored in the `onnxovep_optimum_inference/logs.txt` file. 

3. View the logs using: 
    ```bash
    kubectl logs <pod_name>
    ```

### Use Case 4: Inference Only

Before triggering the inference, make sure you have access to the model file and
also edit the model path in the `qat/values.yaml` file.

Keep only one deployment-*.yaml file in the `qat/templates` folder to deploy
just one inference application.

*  For Onnxruntime with OpenVINO-EP, use `deployment_onnx.yaml` file. Model
   format acceptable is .onnx

*  For Huggingface API  with OpenVINO™ runtime, use `deployment_optimum.yaml`.
   Model format acceptable is pytorch or IR.xml

*  For OpenVINO™ model server, use `deployment-ovms.yaml`. Model format
   acceptable is IR.xml


To run inference, use the following commands:

```bash
cd helmchart
helm install qatchart qat --no-hooks
```
### Clean Up

After you run a use case, clean up resources using the command:

```bash
helm uninstall qatchart
```

### Useful Commands

Uninstalling Helm: (If required)
```bash
sudo rm -rf /usr/local/bin/helm
```

Uninstalling K3S: (If required)
```bash
/usr/local/bin/k3s-uninstall.sh
```
Refer to [Steps to uninstall Rancher K3S](https://rancher.com/docs/k3s/latest/en/installation/uninstall/#:~:text=If%20you%20installed%20K3s%20using,installation%20script%20with%20different%20flags).


## Step 3: Evaluate Use Case Output

View the pods that are deployed through Helm Chart with the command below:

```bash
kubectl get pods
```
Take the pod_name from the list of pods, run:

```bash
kubectl logs <pod_name>
```

If the pods are in completed state, it means they have completed the running
task.

### Training Output

1. Output of the training container will be an optimized INT8 model generated in
   the `quantization_aware_training/model` folder.
2. Verify if all the model files are generated in the `<output>` folder.
3. A `logs.txt` file is generated to store the logs of the training container
   which will have accuracy details.

### Inference Output

1. Output of the inference will be inference time and the answer to the question pertraining to a context file that is given as input
2. Log file is generated named logs.txt in the inference folder



## Set Up Azure Storage (Optional)

Use Azure Storage for multi-node Kubernetes setup if you want to use the same
storage across all the nodes.

### Azure References
  * [Azure File Storage](https://docs.microsoft.com/en-us/previous-versions/azure/virtual-machines/linux/mount-azure-file-storage-on-linux-using-smb)

### Setup Steps

1. Open Azure CLI terminal on Azure Portal.
2. Create a resource group:

    ```bash
    az group create --name myResourceGroup --location eastus
    ```

3. Create Storage Account:

    ```bash
    STORAGEACCT=$(az storage account create \
     --resource-group "myResourceGroup" \
     --name "mystorageacct$RANDOM" \
     --location eastus \
     --sku Standard_LRS \
     --query "name" | tr -d '"')
    ```

4. Create Storage Key:

    ```bash
    STORAGEKEY=$(az storage account keys list \
       --resource-group "myResourceGroup" \
       --account-name $STORAGEACCT \
       --query "[0].value" | tr -d '"')
    ```

5. Create a file share:

    ```bash
    az storage share create --name myshare \
       --quota 10 \
       --account-name $STORAGEACCT \
       --account-key $STORAGEKEY
    ```

6. Create a mount point:

    ```bash
    mkdir -p /mnt/MyAzureFileShare
    ```

7. Mount the share:

    ```bash
    sudo mount -t cifs //$STORAGEACCT.file.core.windows.net/myshare /mnt/MyAzureFileShare -o vers=3.0,username=$STORAGEACCT,password=$STORAGEKEY,serverino
    ```

### Use Azure Storage in Helm Chart

1. Clone the git_repo in /mnt/MyAzureFileShare and make it as your working
   directory.
2. Edit `<current_working_directory>` in `./helmchart/qat/values.yaml` file to
   reflect the same.
3. All other instructions will be same as in above steps to install the Helm
   chart and trigger the pipeline.
4. Once the training is completed, you can view the Azure Portal and check in
   your fileshare that the model has been generated.

## Learn More

To continue your learning, see the following guides and software resources:

* [OpenVINO™ Integration with Hugging Face Optimum](https://github.com/openvinotoolkit/openvino_contrib/tree/master/modules/optimum)
* [Neural Network Compression Framework (NNCF)](https://github.com/openvinotoolkit/nncf)
* [Hugging Face Transformers training pipelines](https://github.com/huggingface/transformers/tree/main/examples/pytorch)
* [OpenVINO™ Execution Provider](https://onnxruntime.ai/docs/execution-providers/OpenVINO-ExecutionProvider.html)

## Troubleshooting

### Connection Refused
If you encounter a connection refused message as shown below:

```bash
Error: INSTALLATION FAILED: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
```
Set the environment variable:
```bash
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

### Helm Installation Failed

If you see this error message:
```bash
Error: INSTALLATION FAILED: cannot re-use a name that is still in use
```
Run the command:
```bash
helm uninstall qatchart
```

Then install it again:
```bash
helm uninstall qatchart
```
### Helm Timeout
If the training is taking a long time, you may see a timeout error during helm
install command, similar to the text below:
```bash
Error: INSTALLATION FAILED: failed pre-install: timed out waiting for the condition
```
#### Workaround 1
Based on the system performance, add `--timeout <seconds>` to the helm command:
```bash
helm install qatchart qat --timeout <time>
```
The `<time>` value has the format ``nnns``, where **s** indicates seconds. For
the above hardware configuration and with ``MAX_TRAIN_SAMPLES=50``, we recommend
you set the `<time>` value as ``480s``. Increase the timeout if you need to
finetune on the whole dataset.

#### Workaround 2


1. Even if Helm issues an error, the training pod will get schedule and will
   keep running and finish its job. Verify ``kubectl logs <training_pod>``
   when the pod is completed.

2. Run the command:
    ```bash
    helm uninstall qatchart
    ```
3. Install the qatchart with just inference as training has completed:
    ```bash
    helm install qatchart qat --no-hooks
    ```




### Support Forum

If you're unable to resolve your issues, contact the 
[Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).


†  You are responsible for payment of all third-party charges, including payment
for use of Microsoft Azure services.

For the most up-to-date information on Microsoft® Azure products, see the
Microsoft Azure [website](https://azure.microsoft.com/en-us/).

