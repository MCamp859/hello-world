```text
Copyright (c) 2021-2022 Intel Corporation
SPDX-License-Identifier: MIT
```
# Intelligent Connection Management for Automated Handover

## Overview

Use a deep reinforcement learning (DRL) algorithm with a graph neural network
(GNN) model to implement an intelligent connection management solution for wireless networks. 

Manage the association of mobile user equipment with available radio cells,
optimizing for user throughput, cell coverage maximization, and load balancing. 

Leverage the features of Intel® Smart Edge Open to optimize compute-intensive
operations and decrease network latency. 


To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Developer Experience Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Once you have installed the Intel® Smart Edge Open Developer Experience Kit, select **Configure & Download** to download the reference implementation and the software listed below.  

[**Configure & Download**](https://eshqawebui.intel.com/iot/edgesoftwarehub/download/home/Intelligent_Connection_Management)

**Table 1**

|**Time to Complete**|15 – 20 mins|
| :- | :- |
|**Programming Language**|Python*, Go, C, C++
|<p>**Software**</p><p></p>|<p>[Intel® Smart Edge Open Developer Experience Kit](https://github.com/smart-edge-open/open-developer-experience-kits)</p><p>Open Networking Foundation Software Defined RAN [(SDRAN) Version 1.4](https://docs.sd-ran.org/master/release_notes/sdran_1.4.html)</p><p>Intelligent Connection Management for Automated Handover v3.0</p><p></p>|


## Target System Requirements
### Intel® Smart Edge Open Cluster Nodes
- One of the following processors: 
  - Intel® Xeon® Scalable processor.
- At least 64 GB RAM.
- At least 256 GB hard drive.
- An Internet connection.
- Ubuntu* 20.04.2 LTS Server.

## How It Works


### Connection Management xApp

Connection management (i.e., user-cell association) is an important issue for any wireless network for ensuring smooth and well-balanced operation throughout. Traditional methods for connection management consider sub-optimal solutions, such as the connection of each user to a cell with maximum receive power (max RSRP). However, this may lead to some congested cells, while the precious radio resources of other cells might be underutilized. Here we leverage machine learning and artificial intelligence-based solutions to achieve load balancing through intelligent handover management. 

Intelligent Connection Management xApp was developed based on the O-RAN network architecture to optimize user association and load balancing to improve the quality of service (QoS) requirements of a user equipment (UE). The connection management is formulated as a combinatorial graph optimization problem. A deep reinforcement learning (DRL) solution is proposed to learn the weights of a graph neural network (GNN) for an optimal UE association. The wireless network is modeled as a virtual graph in Intelligent Connection Management xApp as shown in Figure 1 below. The GNN network is trained with [reinforcement learning (RL).](https://arxiv.org/abs/2110.07525)

![Figure 1: GNN Network](./images/GNN_Network.png)

<p align = "center">
Figure 1: GNN Network
</p>


The network architecture proposed by the Open Radio Access Network (O-RAN) alliance is the building block for designing virtualized RAN on programmable hardware with radio access control powered by artificial intelligence (AI).

The main contributions of the O-RAN architecture are:

*   Functionality split of central unit (CU), distributed unit (DU) and radio unit (RU)
*   Standardized interfaces between the various units
*   Introduction of RAN intelligent controller (RIC)

The introduction of RIC allows the xApp developers to leverage AI techniques to work on the network data collected by RIC. The ORAN architecture with distributed controllers is shown in the figure below.

![Figure 2: ORAN Architecture](./images/ORAN_Architecture.png)

<p align = "center">
Figure 2: ORAN Architecture
</p>

### ONF SD-RAN

Open Networking Foundation SD-RAN Version 1.4 is a platform for 3GPP compliant software-defined RAN and is consistent with the O-RAN architecture. The SD-RAN provides a near-real-time RIC (nRT-RIC) and RAN simulator for simulating the RAN and UE.

The Intel® Smart Edge Open Developer Experience Kit platform infrastructure is used to deploy the SD-RAN 1.4 release version of RIC pod, RAN Simulator pod and Intelligent Connection Management xApp pod as shown in the figure below. The CM xApp interacts with the RIC to fetch network data from the RAN simulator and performs handover of UEs across different cells.

![Figure 3: High level Deployment](./images/High_level_Deployment_Diagram.png)

<p align = "center">
Figure 3: High level Deployment
</p>

### Intel® Smart Edge Open Enabling Near RT-RIC and xApp 

Intel® Smart Edge Open is an edge computing software toolkit for building platforms optimized for the edge. Platforms created with Intel® Smart Edge Open can host a wide range of services, from network functions such as 5G RAN and 5G core, to AI, media processing, and security workloads. Edge platforms are resource constrained compared to cloud platforms. They require higher network performance and more autonomy, have strong hardware affinity, and face significantly more threat vectors.  Intel® Smart Edge Open addresses the challenges of creating edge platforms by providing a toolkit of functionality selected from across the cloud-native landscape, extended and optimized for the edge.

Intel® Smart Edge Open Developer Experience kits are built on top of Kubernetes*, a production-grade platform for managing containerized workloads and services. Experience kits customize and extend the Kubernetes control plane and edge node with microservices, third-party applications, extensions, and optimizations. The control plane node and one or more edge nodes form an Intel® Smart Edge Open edge cluster.  

![Figure 4: SE-O node](./images/seo-node.png)

<p align = "center">
Figure 4: SmartEdge Open Edge Node
</p>

The Intel® Smart Edge Open node architecture is specialized for each experience kit, to enable developers to create solutions for specific use cases at a given edge location.

## Supported Features

### Subscription for RSRP/RRC reports with SDRAN RIC v1.4.113
     - SD-RAN v1.4.113 is deployed on Intel® Smart Edge Open Developer Experience Kit which supports the E2SM MHO service model v2.
     - Intelligent Connection Management (CM) xApp interacts with the SD-RAN RIC using GoLang SDK. A Python mediation layer binds the App with the GoLang SDK.
     - CM xApp subscribes to the E2 nodes for the Periodic RSRP reports, A3 event-based RSRP reports and RRC state change indications.
### Connection Management Deployment
     - RAN simulator is simulating 4 E2 nodes in the setup.
     - RAN simulator v1.4.2 simulates 140 UEs across 7 cells. The Model file is part of the ran simulator release.
### Automated Handover using OpenVINO™ Inferencing
     - CM xApp performs the handover for the UEs across cells based on the RIC indications. It uses C++ preprocessing and OpenVINO™ inferencing.
     - CM xApp sends these handover requests to the RIC in the form of Control Requests (CR) to trigger the handovers.
     - The handover request queue at any time in the CM xApp is between 1-10 requests.
### Node Feature Discovery (NFD)
     - NFD feature is enabled in the package to detect the platform capability and OS installation information (Icelake and Ubuntu) and deploy the xApp based on the condition.

### CPU Manager
     - CPU Manager is a Kubernetes feature that enables better placement of workloads in the Kubelet, the Kubernetes node agent, by allocating exclusive CPUs to certain pod containers. For CM xApp container, the CPU request is 2 cores and memory requested is 2GB.

## Get Started

### Prerequisites

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Developer Experience Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Ensure that the following conditions are met properly to ensure a smooth installation process for a reference implementation done through Edge Software Provisioner (ESP) Intel® Smart Edge Open Developer Experience Kit package.

1.	**Hardware Requirements**
</br>Make sure you have a fresh ESP Intel® Smart Edge Open Developer Experience Kit installation with the Hardware specified in the Target System Requirements section.

2. **Install Python dependent libraries**

   ```shell
   pip3 install –-user Cython 
   sudo apt-get install python3-dev
   ```
   
3. **Confirm the steps below were followed for ESP Intel® Smart Edge Open Developer Experience Kit installation:**

   *  Proxy Settings
    
      If you are behind a proxy network, ensure that proxy addresses are configured in the system.  

      ```shell
      export http_proxy=<proxy-address>:<proxy-port>
      export https_proxy=<proxy-address>:<proxy-port>
      ```
      
   *  Ensure the ``/etc/wgetrc`` file is configured with required proxy settings as follows: 
   
      Note: Use your preferred text editor to edit the file, for example, use the command: ``sudo vi /etc/wgetrc`` 
   
      ```shell
      https_proxy=<proxy-address>:<proxy-port> 
      http_proxy=<proxy-address>:<proxy-port> 
      ftp_proxy =<proxy-address>:<proxy-port> 
      use_proxy = on
      ```
      
   *  Date and Time 
   
      Make sure that the date and time are in sync with current local time. 
      
   *  Verify that the ssh public key is installed on the system.

   *  Verify that a non-root user ``smartedge-open`` has been created with password ``smartedge-open``.

 ### Install the Reference Implementation

Select [Configure & Download](https://edgesoftwaretestingwebui.intel.com/iot/edgesoftwarehub/download/home/Intelligent_Connection_Management) to download the reference implementation and then follow the steps below to install it. 

[Configure & Download](https://edgesoftwaretestingwebui.intel.com/iot/edgesoftwarehub/download/home/Intelligent_Connection_Management)

1. Make sure that the Target System Requirements are met properly before proceeding further.  

   *  For single-device mode, only one machine is needed. (Both controller and edge node will be on the same device.)
   *  For multi-device mode, make sure you have at least two machines (one for the controller and the other for Edge Node). 
   *  **NOTE: Multi-device mode is not supported in the current release.** 

2. Confirm target host is configured with ESP Intel® Smart Edge Open Developer Experience Kit as referred to in the Prerequisites section.
3. Move the downloaded zip package to ``/home/<non-root-user>`` folder:

   ```shell
   mv <path-of-downloaded-directory>/Intelligent_Connection_Management.zip /home/<non-root-user>
   ```

4. Go to ``/home/<non-root-user>`` directory using the following command and unzip the RI:

   ```shell
   cd /home/<non-root-user>
   unzip Intelligent_Connection_Management.zip
   ```
5. Go to ``Intelligent_Connection_Management`` directory:
   ```shell
   cd Intelligent_Connection_Management
   ```
6. Change permission of the executable edge software file: 
   ```shell
   chmod 755 edgesoftware 
   ```
7. Run the command below to install the Reference Implementation: 

   ```shell
   ./edgesoftware install 
   ```


8. When the installation is complete, you see the message ``Installation of package complete`` and the installation status for each module.

![Figure 5: Installation Successful](./images/installation_successful.png)

<p align = "center">
Figure 5: Installation Successful
</p>

   **NOTE:** Installation logs will be available at: ``/var/log/esb-cli/Intelligent_Connection_Management_for_Automated_Handover_3.0.0/Intelligent_Connection_Management_for_Automated_Handover/install.log``


9. If Intel® Smart Edge Open is installed, running the following command should show output similar to the image below. All the pods should be either in the running or completed stage. 

```shell
kubectl get pods -A
```
![Figure 6: Pods Status](./images/Pods_status.png)

<p align = "center">
Figure 6: Pods Status
</p>

10. List the reference implementation deployed module using the following command: 

    ```shell
    . /edgesoftware list 
    ```
    
![Figure 7: List of Apps](./images/List_Of_apps.png)

<p align = "center">
Figure 7: List of Apps
</p>


## Application Output

The SD-RAN ran simulator will simulate 140 UEs across 7 cells. 

1. Login to the onos-cli pod and run the following commands to view the UEs and cells:

   ```shell
   kubectl exec -it <onos-cli-pod> -n smartedge-apps -- /bin/bash
   onos ransim get ueCount - This shows 140
   onos ransim get ues - This shows all 140 UEs with their RRC states
   onos ransim get cells - This shows all 7 cells with the TxDB, Neighbours
   exit
   ```
   
   ![Figure 8: UE Information](./images/UE_Information.png)

   <p align = "center">
   Figure 8: UE Information
   </p>

   ![Figure 9: Cell Information](./images/Cell_Information.png)

   <p align = "center">
   Figure 9: Cell Information
   </p>

2. To check the subscriptions, run the following command inside onos-cli:

   ```shell
   kubectl exec -it <onos-cli-pod> -n smartedge-apps -- /bin/bash
   onos e2t list subscriptions
   exit
   ```

   ![Figure 10: Subscrition Information](./images/Subscription_Information.png)

   <p align = "center">
   Figure 10: Subscription Information
   </p>

3. To check the subscription requests to the e2 node, run the following command on the app logs:

   ```shell
   kubectl logs <cm-xapp-pod> -n smartedge-apps -c cm-xapp | grep "Create subscription successful"
   ```

   ![Figure 11: Subscription Logs](./images/Subscription_Logs.png)
   <p align = "center">
   Figure 11: Subscription Logs
   </p>

4. Run the following command on the app logs to confirm that the App is issuing the handover requests: 

   ```shell
   kubectl logs <cm-xapp-pod> -n smartedge-apps -c cm-xapp | grep "Calling control req"
   ```
   ![Figure 12: Handover Logs](./images/Handover_logs.png)
   <p align = "center">
   Figure 12: Handover Logs
   </p>

   The same can be confirmed from the RAN Sim logs that the handover requests issued from xApp are reaching the Ran Simulator.

   ```shell
   kubectl logs <ran-simulator-pod> -n smartedge-apps | grep "HO is done successfully"
   ```
   ![Figure 13: Ran simulator Logs](./images/Ran_sim_logs.png)

   <p align = "center">
   Figure 13: Ran Simulator Logs
   </p>

5. Run the following command on the app logs to confirm that the HO processing time is within 10 ms:

   ```shell
   kubectl logs <cm-xapp-pod> -n smartedge-apps -c cm-xapp | grep "OpenVINO Inference HO processing time"
   ```
   ![Figure 14: HO Processing Time Logs](./images/HO_processing.png)

   <p align = "center">
   Figure 14: HO Processing Time
   </p>

### OpenVINO™ Toolkit Inference Handover Processing Time

In the Intelligent Connection Management for Automated Handover app, Graph Neural Network (GNN) and
RL (Reinforcement Learning) is used for an optimal UE association. The OpenVINO™ toolkit 2022.1 release with GNN
model optimizations improves the latency for handover requests processing to be well under 10 ms.

In this release, OpenVINO™ toolkit is the default inferencing method used. The figure below shows the improvement in the latency with respect to Python latency.

Preprocessing: C++

parallelLoop: true

#### OpenVINO Inference Latency

![Figure 15: LatencyLogs](./images/openVINO_Inference_latency.png)

<p align = "center">
Figure 15: OpenVINO Inference Latency
</p>

#### Python Inference Latency

![Figure 15: LatencyLogs](./images/python_inference_latency.png)

<p align = "center">
Figure 16: Python Inference Latency
</p>



## Node Feature Discovery (NFD) Feature

Node Feature Discovery (NFD) is a Kubernetes* add-on that detects and advertises the hardware and software capabilities of a platform.

Intelligent Connection Manangement xApp uses the Intel® Distribution of OpenVINO™ toolkit, which is optimized for Intel® processors that support special instructions like AVX512VNNI for optimized performance. The deployment of this application will require the node with this feature supported on the node along with Ubuntu OS. This NFD feature ensures to deploy the application on the node supported with these features. 

NFD is installed by Intel® Smart Edge Open Developer Experience Kit and running as two pods on Intel® Smart Edge Open, as shown below.

```shell
$ kubectl get pods -A | grep smartedge-system

smartedge-system   nfd-release-node-feature-discovery-master-8c74cbd95-fnh79   1/1     Running   0             37d
smartedge-system   nfd-release-node-feature-discovery-worker-h68xg             1/1     Running   0             37d

```

During xApp deployment, it discovers platform capability and OS installation information. Only if it satisfies the criteria, will the application pod be deployed.

The following output shows a description of Intelligent Connection Management xApp pod, which shows that it is running successfully with the NFD feature.

```shell
kubectl describe po cm-xapp-74ccd7fcb4-mlm8z -n smartedge-apps
...
...
Node-Selectors:              feature.node.kubernetes.io/cpu-cpuid.AVX512VNNI=true
                             feature.node.kubernetes.io/system-os_release.ID=ubuntu
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
...
```



## CPU Manager

CPU Manager is a Kubernetes feature that enables better placement of workloads in the Kubelet, the Kubernetes node agent, by allocating exclusive CPUs to certain pod containers. CPU manager uses Linux CPUSET mechanism to schedule PODS to invividual CPUs. Kubernetes defines shared pool of CPUs which initially contains all the system CPUs without CPUs reverved for system and kubelet itself.

CPU core allocation to the xApp workload enables optimized performance on Intel processors

Kubernetes CPU Management needs CPU manager policy to be set to static which is a default option in Intel® Smart Edge Open. 

For CM xApp container, the CPU request is **2 cores** and memory requested is **2GB**.


## Uninstallation of the RI

Uninstall the reference implementation module using the following command. Get ``cmxapp-module-id`` from the output of ``./edgesoftware list`` command.

Uninstall the reference implementation module using the following command: 

```shell
. /edgesoftware uninstall <cmxapp-module-id>
```

![Figure 17: Uninstallation Logs](./images/Uninstallation_logs.png)

<p align = "center">
Figure 17: Uninstallation Logs
</p>


## Summary and Next Steps

The Intelligent Connection Management App, when deployed on the Intel® Smart Edge Open Developer Experience Kit, creates an impactful Network AI use case that utilizes the capability of Intel® Smart Edge Open Developer Experience Kit and the SD-RAN to perform intelligent automated handover of UEs across cells efficiently.

## Learn More

To continue learning, see the following guides and software resources:

- 	[Intel® Smart Edge Open Architecture](https://github.com/smart-edge-open/specs/blob/master/doc/architecture.md)
- 	[Connection Management xApp](https://arxiv.org/abs/2110.07525)


## Troubleshooting

**Pods Status Check** 

Verify that the pods are Ready as well as in Running state using the following command:

```shell
kubectl get pods -A
```

If any pods are in ImagePullBackOff state, manually pull the images using:
```shell
docker login
docker pull <image-name>
```

If any pods are not in Running state, use the following command to check the pod failure case:
```shell
kubectl describe -n <namespace> pod <pod_name>
```

**Installation Failure**

If the Intel® Smart Edge Open Developer Experience Kit installation has failed on pulling the namespace pods like Telemetry, reboot the system. After rebooting, execute the following command:
```shell
reboot
su 
swapoff -a 
systemctl restart kubelet (Wait till all pods are in “Running” state.)
./edgesoftware install
```

**Pod Status shows "ContainerCreating" for a long time**

If pod status shows ContainerCreating or Error or CrashLoopBackOff for 5 minutes or more, run the following commands:
```shell
reboot
su 
swapoff -a 
systemctl restart kubelet (Wait till all pods are in “Running” state.)
./edgesoftware install 
```

**Installation and Debug Log Info File Path**

Installation log info of Intelligent Connection Management for Automated Handover module will be available at: 
```shell
var/log/esb-cli/Intelligent_Connection_Management_for_Automated_Handover_3.0.0/Intelligent_Connection_Management_for_Automated_Handover/install.log
```


##  Support Forum

If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).  

Execute the command below to consolidate a list of the log files in tar.gz compressed format, e.g., **Intelligent_Connection_Management.tar.gz.**

```shell
tar -czvf Intelligent_Connection_Management.tar.gz /var/log/esb-cli/Intelligent_Connection_Management_for_Automated_Handover_3.0.0/Intelligent_Connection_Management_for_Automated_Handover
```
