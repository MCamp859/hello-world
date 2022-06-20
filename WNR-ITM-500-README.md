# Wireless Network-Ready Intelligent Traffic Management Reference Implementation
## Overview


Wireless Network-Ready Intelligent Traffic Management is designed to
detect and track vehicles and pedestrians and provides the
intelligence required to estimate a safety metric for an
intersection. In addition, the Intel® Smart Edge Open toolkit
included in the reference implementation could be used to host a 5G
radio access network (RAN) on the same edge device when implemented on a
platform supporting a 5G RAN.

Vehicles, motorcyclists, bicyclists and pedestrians are detected and
located in video frames via object detection deep learning
modules. Object tracking recognizes the same object detected across
successive frames, giving the ability to estimate
trajectories and speeds of the objects. The reference
implementation automatically detects collisions and near-miss
collisions. A real-time dashboard visualizes the intelligence extracted
from the traffic intersection along with annotated video stream(s).

This collected intelligence can be used to adjust traffic light cycling
to optimize the traffic flow of the intersection in near real time, or
to evaluate and enhance the safety of the
intersection. For example, emergency services notifications, i.e, 911
calls, could be triggered by collision detection, reducing emergency
response times. Intersections with higher numbers of collisions and
near-miss collision detections could be
flagged for authority's attention as high-risk intersections.

The data from the traffic cameras in the intersection can be
routed easily using the [SmartEdge-Open high-speed data
plane](https://github.com/open-ness/specs/blob/master/doc/architecture.md#dataplanecontainer-network-interfaces)
for near-real time video analytics in the field.
Further, SmartEdge-Open helps to build and manage the infrastructure to
deploy, monitor, and orchestrate virtualized applications across
multiple edge devices.

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Private Wireless Experience Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).




*  **Time to Complete:**  20 - 25 minutes
*  **Programming Language:**  Python\*
*  **Software:**
   *  Intel® Distribution of OpenVINO™ toolkit 2021 Release
   *  Intel® Smart Edge Open 21.12


## Target System Requirements

### Edge Controller
-   One of the following processors:

    -   Intel® Xeon® Scalable processor.

    -   Intel® Xeon® Processor D.

-   At least 64 GB RAM.

-   At least 256 GB hard drive.

-   An Internet connection.

-   CentOS* 7.9.2009.

-   IP camera or pre-recorded video(s).

### Edge Nodes

-   One of the following processors:

    -   Intel® Xeon® Scalable processor.

    -   Intel® Xeon® Processor D.

-   At least 64 GB RAM.

-   At least 256 GB hard drive.

-   An Internet connection.

-   CentOS* 7.9.2009.

-   IP camera or pre-recorded video(s).

## How It Works

The application uses the inference engine and the Intel® Deep Learning Streamer (Intel® DL Streamer). The solution is
designed to detect and track vehicles and pedestrians by using
Intel® Smart Edge Open Private Wireless Experience Kit (version 21.09).

<img src="images/wnr_itm_1_how_it_works.png" />

Figure 1: How It Works

The Wireless Network-Ready application requires the application pod,
database and a visualizer. Once the installation is successful, the
application is ready to be deployed using helm. After the deployment,
the application pod takes in the virtual/real RTSP stream addresses and
performs inference and sends metadata for each stream to the InfluxDB\*
database. The visualizer in parallel shows the analysis over the
metadata like pedestrians detected, observed collisions and processed
video feed.

The application has capability to perform inferences over as much as 20
channels. In addition, the visualizer is capable to show each feed
separately as well as all the feeds at the same time using Grafana\*. The
user can visualize the output remotely over a browser, provided that
they are in same network.

<img src="images/itm_on_pwek_architecture.png" />


Figure 2: Architecture Diagram

## Get Started

### Prerequisites

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Private Wireless Experience Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Ensure that the following conditions are met properly to ensure a smooth installation process for a reference implementation done through Edge Software Provisioner (ESP) Intel® Smart Edge Open Private Wireless Experience Kit package.

1. Hardware Requirements

   Make sure you have a fresh **CentOS\* 7.9.2009** installation with the
   Hardware specified in the [Target System
   Requirements](#target-system-requirements) section.


### Step 1: Install the Reference Implementation

>**NOTE:** The following sections may use ``<Controller_IP>`` in a URL
or command. Make note of your Edge Controller’s IP address and
substitute it in these instructions.

Select **Configure & Download** to download the reference implementation and
then follow the steps below to install it.

[Configure &
Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/wireless_network_ready_intelligent_traffic_management)

1.  Make sure that the Target System Requirements are met properly
    before proceeding further.


2.  If you are behind a proxy network, be sure that proxy addresses are configured in the system:

    ```
    export http_proxy=proxy-address:proxy-port
    export https_proxy=proxy-address:proxy-port
    ```

3.  Under the user deploy PWEK, for example smartedge-open, download ITM RI package:

    ```
    mkdir path-of-downloaded-directory
    ```

4.  Open a new terminal and move the downloaded .zip package to the ``/home/smartedge-open`` folder:
    ```
    mv path-of-downloaded-directory/wireless_network_ready_intelligent_traffic_management.zip /home/smartedge-open
    ```

5.  Go to the ``/home/smartedge-open`` directory using the following command
    and unzip the RI:
    ```
    cd /home/smartedge-open
    unzip wireless_network_ready_intelligent_traffic_management.zip
    ```

6.  Go to the ``wireless_network_ready_intelligent_traffic_management/``
    directory:
    ```
    cd wireless_network_ready_intelligent_traffic_management
    ```

7.  Change permissions of the executable edgesoftware file to enable
    execution:
    ```
    chmod +x edgesoftware
    ```

8.  Run the command below to install the Reference Implementation:

    ```
    ./edgesoftware install
    ```

9.  During the installation, you will be prompted for the Product Key.
    The Product Key is contained in the email you received from Intel
    confirming your download.

    > **NOTE:** Installation logs are available at path:
    >
    > ``/var/log/esb-cli/Wireless_NetworkReady_Intelligent_Traffic_Management_<version>/<Component_Name>/install.log``


    Figure 3: Product Key


10. When the installation is complete, you see the message “Installation
    of package complete” and the installation status for each module.

    <img src="images/wnr_itm_4_install_success.png" />

    Figure 4: Successful Installation

11. Check the ITM images with the command:

    ```
    docker images
    ```

    <img src="images/itm-images-check.png" />

Figure 5: Check Images

### Step 2: Install the ITM Application

1.  Apply the Network Attachment Definition using the provided
    ``net-sriov-itm.yaml`` file:
    ```
    cd wireless_network_ready_intelligent_traffic_management/Wireless_NetworkReady_Intelligent_Traffic_Management_5.0.0/Wireless_NetworkReady_Intelligent_Traffic_Management/WNR_ITM

    # create Network Attachment Definition
    kubectl create -f net-sriov-itm.yaml
    ```

2.  Apply the network policy using the provided ``itm_network_policy.yaml`` file:
    ```
    cd wireless_network_ready_intelligent_traffic_management/Wireless_NetworkReady_Intelligent_Traffic_Management_5.0.0/Wireless_NetworkReady_Intelligent_Traffic_Management/WNR_ITM

    # create netpol for the ITM
    kubectl create -f itm_network_policy.yaml
    ```

3.  Deploy Grafana and Influxdb pods using Helm:
    ```
    cd WNR_ITM/deploy
    Cluster_ControllerIP=$(kubectl get node -o wide |grep control-plane | awk '{print $6}')
    helm install grafana ./grafana --set hostIP=${Cluster_ControllerIP}
    helm install influxdb ./influxdb

    # check the Grafana and Influxdb pod
    kubectl get pod -n smartedge-apps

    NAME                        READY   STATUS    RESTARTS   AGE
    grafana-796b7f677-lsrh4     1/1     Running   0          44h
    influxdb-585c4b8bb5-8f2lc   1/1     Running   0          44h
    ```

4.  Deploy the ITM application:
    ```
    # Get the Grafana sriov ip
    grafana_pod=$(kubectl get pod -n smartedge-apps |grep grafana | awk '{print $1}')
    sriov_IP=$(kubectl exec -n smartedge-apps ${grafana_pod} -- ip a s net1 | grep inet |awk '{print $2}' | cut -d '/' -f 1)

    # helm install ITM
    cd WNR_ITM/deploy
    grafana_ip=$(kubectl get pod -n smartedge-apps -owide |grep grafana | awk '{print $6}')
    Passwd=admin
    helm install itm ./itm --set hostIP=${Cluster_ControllerIP} --set sriovIP=${sriov_IP} --set grafanaPassword="${Passwd}" --set grafanaHost=${grafana_ip}

    # check the ITM pod
    kubectl get pod -n smartedge-apps

    NAME                   READY   STATUS    RESTARTS   AGE
    itm-75758c684f-cdxt5   1/1     Running   0          44h
    ```

    > NOTE: ``<Cluster_ControllerIP>`` is the cluster controller IP.

5.  Start the nginx service in the Grafana pod by executing the following
    commands on the controller node.
    ```
    kubectl exec -n smartedge-apps ${grafana_pod} -- sudo sed -i "s/try_files \$uri \$uri\/ =404;/proxy_pass http:\/\/${Cluster_ControllerIP}:30300;/"  /etc/nginx/sites-available/default
    kubectl exec -n smartedge-apps ${grafana_pod} -- sudo nginx -g "daemon on;"
    ```

6.  Add routing rule for Grafana on the edge node:
    ```
    # Login to the edge node, and add an additional route rule for Grafana
    [smartedge-open@node]# docker ps | grep k8s_grafana_grafana* | awk '{print $1}'
    32e0eade6b0d

    [smartedge-open@node]# docker inspect -f {{.State.Pid}} 32e0eade6b0d
    86372
    [smartedge-open@node]# sudo nsenter -n -t 86372

   [smartedge-open@node]# sudo ip route add 192.171.1.0/24 via 6.6.6.11

    [smartedge-open@node]# route
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    default         gateway         0.0.0.0         UG    0      0        0 eth0
    6.6.6.0         0.0.0.0         255.255.255.0   U     0      0        0 net1
    gateway         0.0.0.0         255.255.255.255 UH    0      0        0 eth0
    192.171.1.0     6.6.6.11        255.255.255.0   UG    0      0        0 net1
    ```
    > NOTE: The subnet 192.171.1.0/24 is the UE (User Equipment) network segment allocated by 5GC network functions.


7.  Add routing rule in the edge node to add an additional rule for edgeDNS.

    Create a net-attach-def resource for edgeDNS:

    ```shell
    $ cat edgedns-net-attch-def.yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetwork
    metadata:
    name: intel-sriov-edgedns
    namespace: sriov-network-operator
    spec:
    resourceName: intel_sriov_10G_VEDIOSTREAM
    networkNamespace: smartedge-system
    ipam: |-
      {
         "type": "host-local",
         "subnet": "6.6.6.0/24",
         "rangeStart": "6.6.6.66",
         "rangeEnd": "6.6.6.66",
         "routes": [{
            "dst": "0.0.0.0/0"
         }],
         "gateway": "6.6.6.1"
      }

    kubectl apply -f edgedns-net-attch-def.yaml
    ```
    Patch the original edgedns daemonSet with the following patch:
    ```shell
    $ cat edgedns-ds-patch.yaml
    spec:
    template:
       metadata:
          annotations:
          k8s.v1.cni.cncf.io/networks: intel-sriov-edgedns
       spec:
          containers:
          - name: edgedns
          resources:
             limits:
                intel.com/intel_sriov_10G_VEDIOSTREAM: "1"
             requests:
                intel.com/intel_sriov_10G_VEDIOSTREAM: "1"

    kubectl patch ds -n smartedge-system edgedns --patch "$(cat edgedns-ds-patch.yaml)"
    ```
    Login to the edge node, and add an additional route rule for Grafana:
    ```
    [smartedge-open@node]# docker ps | grep edgednssvr* | awk '{print $1}'
    6e4d8ea23ecb

    [smartedge-open@node]# docker inspect -f {{.State.Pid}} 6e4d8ea23ecb
    102569
    [smartedge-open@node]# sudo nsenter -n -t 102569

    [smartedge-open@node]# sudo ip route add 192.171.1.0/24 via 6.6.6.11

    [smartedge-open@node]# route
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    default         gateway         0.0.0.0         UG    0      0        0 eth0
    6.6.6.0         0.0.0.0         255.255.255.0   U     0      0        0 net1
    gateway         0.0.0.0         255.255.255.255 UH    0      0        0 eth0
    192.171.1.0     6.6.6.11        255.255.255.0   UG    0      0        0 net1
    ```

8.  Create a domain name for ITM on the controller node:

    ```
    # Replace sriov-ip with real IP, you can get sriov-ip with command 'echo ${sriov_IP}'
    kubectl edgedns add www.wnr-itm.com:${sriov_IP}
    ```

### Step 3: Data Visualization on Grafana

Check the Grafana dashboard in the UE browser.

1. Input the address "www.wnr-itm.com:3000". Login with user as ``admin`` and
   password as ``admin``. No need to reset password, just skip.

   Click Home --> select one channel to check the ITM data.

2. Click **Home** and Select the **ITM** to open the main dashboard.

   <img src="images/wnr_itm_9_grafana_home_screen.png" />

   Figure 9: Grafana Home Screen

   <img src="images/wnr_itm_10_grafana_dashboard_list.png" />

   Figure 10: Grafana Dashboard list

   <img src="images/wnr_itm_13_grafana_dashboard_individual_camera_feed.png" />

   Figure 11: Grafana Dashboard of an individual camera feed


### Step 4: Uninstall the Application

1. Check installed modules with the following command:
   ```
   cd /home/smartedge-open/wireless_network_ready_intelligent_traffic_management

   ./edgesoftware list
   ```

   All installed modules will be shown as seen in the screen below:

   <img src="images/wnr_itm_15_installed_modules_list.png" />

   Figure 12: Installed Modules List

2. Run the command below to uninstall all the modules:

   ```
   ./edgesoftware uninstall –a
   ```

3. Run the command below to uninstall the Wireless Network Ready ITM reference
   implementation:

   ```
   ./edgesoftware uninstall <itm-id get from step 1>
   ```

   <img src="images/wnr_itm_16_uninstall_modules.png" />

   Figure 13: Uninstall modules


## Node Feature Discovery (NFD) Feature

Wireless Network-Ready Intelligent Traffic Management uses Intel® Distribution
of OpenVINO™ toolkit which is optimized for Intel® processors that support
special instructions like AVX512VNNI for optimized performance. This NFD
feature ensures to deploy the application on the node supported with these
features. NFD is installed by [Intel® Smart Edge Open Developer Experience
Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits)
and running as two pods on [Intel® Smart Edge
Open](https://software.intel.com/content/www/us/en/develop/tools/smart-edge-open.html).


```shell
   $ kubectl get pods -A | grep smartedge-system
   smartedge-system      nfd-release-node-feature-discovery-master-7b94765ccf-9ghjg   1/1    Running   5 (6d18h ago)    7d23h
   smartedge-system      nfd-release-node-feature-discovery-worker-dq4x6              1/1    Running   5 (6d18h ago)    7d23h
```

 Wireless Network-Ready Intelligent Traffic Management pods scheduled and running successfully on [Intel® Smart Edge Open](https://software.intel.com/content/www/us/en/develop/tools/smart-edge-open.html) node based on hardware capabilities of Intel® Xeon® Scalable server.

```shell
   $ kubectl get pods -A | grep smartedge-apps
   smartedge-apps           grafana-cbbb86456-mwn5b               1/1     Running   0             4d17h
   smartedge-apps           influxdb-7d8c95d994-gpwh2             1/1     Running   0             4d17h
   smartedge-apps           itm-68d8b7d497-4hgqg                  1/1     Running   0             4d17h
```

The following output shows a description of Wireless Network-Ready Intelligent Traffic Management pod, which shows that it is running successfully with the NFD feature.

```shell

   $ kubectl describe pod  itm-68d8b7d497-4hgqg -n smartedge-apps
   ...
   ...
   ...
    Node-Selectors:              feature.node.kubernetes.io/cpu-cpuid.AVX512VNNI=true
    Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
```

## Local Build Instructions

After you have installed Intel® Smart Edge Open Developer Experience Kit from Prerequisites, you can build your own Wireless-Network Ready
Intelligent Traffic Management Docker image using the following instructions.

You can proceed with the steps presented using either edgesoftware sources or GitHub sources: WNR-ITM<github_link>

### Setup
Change the directory to repository path with one of the following options.

For Edgesoftware:

```
cd /home/smartedge-open/wireless_network_ready_intelligent_traffic_management/Wireless_NetworkReady_Intelligent_Traffic_Management_5.0.0/Wireless_NetworkReady_Intelligent_Traffic_Management
```


Use your preferred text editor to make the following file updates.

In the next steps, the tag `<REPOSITORY_PATH>` indicates the path to the repository.

In the Change examples, replace the line indicated by - with the line indicated by +


### Optional Steps

#### Stop the Application

To remove the deployment of this reference implementation, run the
following commands.

>**NOTE:** The following commands will remove all the running pods and
the data and configuration stored in the device.

```
helm delete itm
```

## Summary and Next Steps

This application successfully implements Intel® Distribution of
OpenVINO™ toolkit plugins for detecting and tracking vehicles and
pedestrians and may be used for a basis in estimating a safety
metric for an intersection. It can be extended further to provide
support for a feed from a network stream (RTSP or camera device).

As a next step, you can experiment with accuracy/throughput trade-offs
by substituting object detector models and tracking and collision
detection algorithms with alternative ones.

In addition, on an appropriate platform with supporting RAN hardware you
can onboard a 3rd party 5G RAN (Radio Access Network) implementation
that will make it easy to host a private or public 5G small cell. To
perform video analytics wireless IP cameras can be connected through the
small cell, and the video traffic from the cameras can be routed via the
high-speed SmartEdge-Open data plane to the visual intelligence
container. With the 5G RAN and visual intelligence workloads hosted in a
single system, the solution benefits from faster data transfers between
the workloads and a reduced total cost of ownership.

## Learn More

To continue your learning, see the following guides and software
resources:

-   [Intel® Distribution of OpenVINO™ toolkit
    documentation](https://docs.openvinotoolkit.org/2021.1/index.html)

-   [Intel® Smart Edge Open Developer Experience Kit
    Architecture](https://github.com/intel-sandbox/applications.services.smart-edge-open.docs/blob/main/experience-kits/developer-experience-kit.md)

## Troubleshooting

### Pods status check

Verify that the pods are **Ready** as well as in **Running** state
using below command:

```
kubectl get pods -n smartedge-apps
```

If any pods are not in **Running** state, use the following command to get more
information about the pod state:

```
kubectl describe -n smartedge-apps pod <pod_name>
```

### Pod status shows “ContainerCreating” for long time

If Pod status shows “ContainerCreating” or “Error” or “CrashLoopBackOff” for a
while (5 minutes or more), run the following commands:

```
reboot
su
swapoff -a
systemctl restart kubelet  # Wait till all pods are in “Running” state.
./edgesoftware install
```

### Subprocess:32 issue

If you see any error related to subprocess, run the command below:

```
pip install --ignore-installed subprocess32==3.5.4
```

### Grafana Dashboard Not Showing on Browser

Run the following commands:

```
# check the itm pod log
kubectl logs <itm-pod-name> -n smartedge-apps
```

## Support Forum

If you're unable to resolve your issues, contact the [Support
Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).

To attach the installation logs with your issue, execute the command below to consolidate a list
of the log files in tar.gz compressed format, e.g., **ITM.tar.gz**.


```
tar -czvf ITM.tar.gz /var/log/esb-cli/Wireless_NetworkReady_Intelligent_Traffic_Management_<version>/<Component_name>/install.log
```
