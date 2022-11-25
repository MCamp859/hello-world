# applications.services.esh.multi-access-with-private-5g
## Overview

As the mobile industry evolves towards 5G/5G+, it is becoming clear that no single radio technology will be able to meet a great variety of requirements for human and machine communications. On the other hand, driving more data through a scarce and finite radio spectrum becomes a real challenge, and spectrum efficiency is approaching a plateau and will not deliver the needed increase in bandwidth improvement itself. Therefore, 5G is likely to utilize frequencies below 6GHz as well as mmWave, in both licensed and unlicensed bands. We developed a new  Software-Defined  & Access-Agnostic & High-Performance solution – “Generic Multi-Access (GMA)” to enable seamless integration of multiple access networks at the edge, with no impact to legacy (cellular or Wi-Fi) radio protocols, e.g. PDCP, RRC, Ethernet, etc., or network protocols, e.g. IP, TCP, UDP, etc.

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Private Wireless Experience Kit](https://smart-edge-open.github.io/docs/experience-kits/private-wireless-experience-kit).

*  **Time to Complete:**  120 - 150 minutes
*  **Programming Language:**  Python\*
*  **Software:**

   *  Intel® Smart Edge Open 22.04.01 PWEK Release
   
   
## Target System Requirements

### Edge Controller
-   One of the following processors:

    -   Intel® Xeon® Scalable processor.

    -   Intel® Xeon® Processor D.

-   At least 64 GB RAM.

-   At least 256 GB hard drive.

-   An Internet connection.

-   CentOS* 7.9.2009.

### Edge Nodes

-   One of the following processors:

    -   Intel® Xeon® Scalable processor.

    -   Intel® Xeon® Processor D.

-   At least 64 GB RAM.

-   At least 256 GB hard drive.

-   An Internet connection.

-   CentOS* 7.9.2009.

### Client devices

-   Laptop support Cellular / WIFI (or Wi-Fi + Cellular/USB tethering) 

-   Ubuntu* 20.04

-   Wifi AP

## How It Works

GMA client will connect to GMA server over Celluar and Wifi, At the very beginning, client has only one delivery connection (e.g. celluar) established,and will try getting the second delivery connection. After both delivery connections are established, will then establish a websocket,A websocket-based secure connection is established between client and server to exchange messages, A new protocol layer – GMA convergence is introduced to handle all multi-path related operations, e.g. splitting, reordering, duplication, elimination measurements, etc.

<img src="images/GMA.png" />
<div align=center>Figure 1: Architecture Diagram</div>

## Get Started
### Prerequisites

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Private Wireless Experience Kit](https://smart-edge-open.github.io/docs/experience-kits/private-wireless-experience-kit/).

Ensure that the following conditions are met properly to ensure a smooth installation process for a reference implementation done through Edge Software Provisioner (ESP) Intel® Smart Edge Open Private Wireless Experience Kit package.

1. Hardware Requirements

   Make sure you have a fresh **CentOS\* 7.9.2009** installation with the
   Hardware specified in the [Target System
   Requirements](#target-system-requirements) section.
2. Network connection

   Laptop connect to wifi through Wifi AP which is connected to E810 nic
   
   Laptop connect to celluar through Cellular tethering

### Step 1: Install the Reference Implementation

>**NOTE:** The following sections may use ``<Controller_IP>`` in a URL
or command. Make note of your Edge Controller’s IP address and
substitute it in these instructions.

Select **Configure & Download** to download the reference implementation and
then follow the steps below to install it.

[Configure &
Download](https://eshqawebui.intel.com/iot/edgesoftwarehub/download/home/multi-access-with-private-5g)

1.  Make sure that the Target System Requirements are met properly
    before proceeding further.


2.  If you are behind a proxy network, be sure that proxy addresses are configured in the system:

    ```
    $ export http_proxy=proxy-address:proxy-port
    $ export https_proxy=proxy-address:proxy-port
    ```

3.  Under the user deploy PWEK, for example smartedge-open, download GMA RI package:

    ```
    $ mkdir path-of-downloaded-directory
    ```

4.  Open a new terminal and move the downloaded .zip package to the ``/home/smartedge-open`` folder:
    ```
    $ mv path-of-downloaded-directory/multi-access-with-private-5g.zip /home/smartedge-open
    ```

5.  Go to the ``/home/smartedge-open`` directory using the following command
    and unzip the RI:
    ```
    $ cd /home/smartedge-open
    $ unzip multi-access-with-private-5g.zip
    ```

6.  Go to the ``multi-access-with-private-5g/``
    directory:
    ```
    $ cd multi-access-with-private-5g

    $ openssl genrsa -out server.key 3072
    $ openssl req -new -key server.key -out server.csr (input user info)
    $ openssl x509 -req -in server.csr -out server.crt -signkey server.key -days 3650
    ```
    Three files will be generated, server.key, server.csr and server.crt.

7.  Apply the Network Attachment Definition and network policy:
    ```
    $ cd MultiAccess_with_Private_5G_Reference_Implementation_1.0.0/MultiAccess_with_Private_5G/GMA/deploy
    $ kubectl apply -f gma5g-net.yaml
    $ kubectl apply -f gmawifi-net.yaml
    $ kubectl apply -f gmanet-policy.yaml
    ```

8.  Change permissions of the executable edgesoftware file to enable
    execution:
    ```
    $ cd ../../../..
    $ chmod +x edgesoftware
    ```

9.  Run the command below to install the Reference Implementation:

    ```
    $ ./edgesoftware install
    ```

    > **NOTE:** Installation logs are available at path:
    >
    > ``/var/log/esb-cli/Multi-access-with-private-5g_<version>/<Component_Name>/install.log``


10. When the installation is complete, you see the message “Installation
    of package complete” and the installation status for each module.

    <div align=center><img src="images/Successful Installation.png" /></div>
    <div align=center>Figure 2: Successful Installation</div>

    >**NOTE:** If the pods have a status of “ContainerCreating”, please wait
  for some time, since Kubernetes will pull the images from the registry
  and then deploys them. This happens only the first time the containers
  are deployed, and the wait time will depend upon the network bandwidth
  available.

11. Check the GMA pods with the command:

    ```
    $ kubectl get pods -n smartedge-apps
    ```

  <div align=center><img src="images/Status of pods.png" width="600" height="50"/></div>
  <div align=center>Figure 3: Status of Pods</div>
  <br/>
      
12. Get **Container ID** of gmaserver with the command:
    ```
    $ kubectl describe pod <gma-pod> -n smartedge-apps | grep "Container ID"
    ```
    
13. Copy the ssl certificate to the gma container:
    ```
    $ docker cp ./server.key <gma-pod>:/home/python
    $ docker cp ./server.csr <gma-pod>:/home/python
    $ docker cp ./server.crt <gma-pod>:/home/python
    ```
    > **NOTE:** Run the command on k8s node.

14. Run the gmaserver application:
    ```
    $ docker exec -itd <gma-container-id> bash -c "sudo ./rungma.sh"
    ```
    > **NOTE:** Run the command on k8s node.
    
15. Install test tools of gmaserver:
    ```
    $ docker exec -itd <gma-container-id> bash -c "sudo apt-get update && sudo apt-get install iperf3 -y"
    ```
    > **NOTE:** Run the command on k8s node.
    
### Step 2: Check the Application
1. Setup GMA client
   on the GMA client device, which is the laptop: 
    ```
    $ git clone https://github.com/IntelLabs/gma.git
  
    $ sudo apt-get install libboost-all-dev
    $ sudo apt-get install libssl-dev
    $ sudo apt-get update
    $ sudo apt-get install net-tools
    $ sudo apt install screen speedometer iw -y
  
    ```
   Change client key to generated Key,use server.csr which generate in step 1:
  
     ```
     cp /path/to/server.crt /path/to/gma
     cd gma
     sed '/./{s/^/        "&/;s/$/&\\n"/}' server.crt > client.crt
     ```
   Copy client.crt's content to path/to/gma/client/root_certificates.hpp to replace std::string const cert content,Compile GMA client:
  
     ```
     $ cd ./GMAlib/lib
     $ make -B
     $ cd ../../client
     $ make -B
     ```
  
   Install GMA client:
     
     ```
     $ sudo mkdir /home/gmaclient
     $ sudo chmod 777 ./gmaclient
     $ cd ./client
     $ cp ./gmaclient /home/gmaclient/
     $ cp ./config.txt /home/gmaclient/
     ``` 
  
   Config GMA client(wlan0: network interface for wifi, wwan0: network interface for cellular, gmaserver.apps.local: local DNS name for GMA service running at Edge,    a.b.c.d is the (GMA service) IP address at the edge node via LTE)
  
     ``` 
     SERVER_NCM_IP=a.b.c.d

     WLAN_INTERFACE_CONFIG=wlan0

     LTE_INTERFACE_CONFIG=wwan0
     ``` 
  
   Start GMA client
  
     ``` 
     $ cd /home/gmaclient
     $ sudo ./gmaclient
     ``` 
  
 2. ping GMA server
   there will be tun setup after connection setup
    ```
    $ ping 10.8.0.1
    PING 10.8.0.1 (10.8.0.1) 56(84) bytes of data.
    64 bytes from 10.8.0.1: icmp_seq=1 ttl=64 time=0.847 ms
    64 bytes from 10.8.0.1: icmp_seq=2 ttl=64 time=0.824 ms
    64 bytes from 10.8.0.1: icmp_seq=3 ttl=64 time=0.903 ms
    64 bytes from 10.8.0.1: icmp_seq=4 ttl=64 time=0.871 ms
    64 bytes from 10.8.0.1: icmp_seq=5 ttl=64 time=0.807 ms
    64 bytes from 10.8.0.1: icmp_seq=6 ttl=64 time=0.830 ms
    ```
 3. Run demo Test
   Install test tools in server, login to GMA docker
    
    ```
    $ kubectl exec -it <GMA-pod> -c gma -n smartedge-apps /bin/bash
    $ iperf3 -s -i 5 
    ```
   
### Step 3: Check Seamless Mobility
1. Run demo test tools on GMA client device:
    ```
    $ iperf3 -c 10.8.0.1 -t 1000 -i 5 -b 2M -u -l 1000
    $ speedometer -t tun0 -t wlp0s20f3 -t enx000ec6d75f05 -b -s -l -n 0 -m 400000
    ```
  <div align=center><img src="images/seamless_mobility/scene1_1.png" /></div>
  <div align=center>Figure 4: Start Demo Test Tool</div>
  
2. Disconnect the wifi path:
    ```
    $ nmcli device disconnect <wifi-interface>
    ```
    Now the flow is transferred from wifi to cellular:
    <div align=center><img src="images/seamless_mobility/scene1_2.png" width="600" height="400"/></div>
    <div align=center>Figure 5: Disconnect the Wifi Path</div>

3. Re-connect the wifi path:
    ```
    $ nmcli device connect <wifi-interface>
    ```
    Now the flow is transferred to wifi again:
    <div align=center><img src="images/seamless_mobility/scene1_3.png" width="600" height="400"/></div>
    <div align=center>Figure 6: Re-connect the Wifi Path</div>

### Step 4: Check Uplink Redundancy
1. Run demo Test Install test tools on GMA client device:
    ```
    $ iperf3 -c 10.8.0.1 -t 1000 -i 5 -b 2M -u -l 1000
    $ speedometer -t tun0 -t wlp0s20f3 -t enx000ec6d75f05 -b -s -l -n 0 -m 400000
    ```
  
2. Set the packet loss rate to 50% for both wifi and cellular:
    ```
    $ tc qdisc add dev <cellular-interface> root netem loss 50%
    $ tc qdisc add dev <wifi-interface> root netem loss 50%
    ```
    <div align=center><img src="images/uplink_redundancy/scene2_1.png" width="600" height="400"/></div>
    <div align=center>Figure 7: Status of Packet Loss Rate</div>
    <br/>
    <div align=center><img src="images/uplink_redundancy/scene2_2.png" width="400" height="150"/></div>
    <div align=center>Figure 8: Status of Packet Loss Rate</div>
  
3. Run GMA controller and enable uplink redundancy:
    ```
    $ ./gmactrl
    tfc 2 1 2 0 65520
    ```
    Now the packet loss rate of tun is decreased from 50% to about 25%:
    <div align=center><img src="images/uplink_redundancy/scene2_4.png" width="600" height="400"/></div>
    <div align=center>Figure 9: Real Time Transmission Status</div>
    <br/>
    <div align=center><img src="images/uplink_redundancy/scene2_5.png" width="400" height="150"/></div>
    <div align=center>Figure 10: Status of Packet Loss Rate</div>
  
4. Disable Uplink Redundancy:
    ```
    tfc 2 1 0 0 0
    ```
    Now the packet loss rate of tun is increased to 50% again:
    <div align=center><img src="images/uplink_redundancy/scene2_6.png" width="400" height="150"/></div>
    <div align=center>Figure 11: Status of Packet Loss Rate</div>
    <br/>
    <div align=center><img src="images/uplink_redundancy/scene2_7.png" width="600" height="400"/></div>
    <div align=center>Figure 12: Real Time Transmission Status</div>

### Step 5: Uninstall the Application
1. Check installed modules with the following command:
    ```
    $ cd /home/smartedge-open/multi-access-with-private-5g
    $ ./edgesoftware list
    ```
     <div align=center><img src="images/list.png" width="500" height="80"/></div>
     <div align=center>Figure 13: Installed Modules List</div>
2. Run the command below to uninstall all the modules:
    ```
    $ ./edgesoftware uninstall -a
    ```
3. Run the command below to uninstall the Multi Access with Private 5g reference implementation:
    ```
    $ ./edgesoftware uninstall <gma-id>
    ```
    <div align=center><img src="images/uninstall.png" /></div>
    <div align=center>Figure 14: Uninstalled Modules </div>


## Local Build Instructions

After you have installed Intel® Smart Edge Open Private Wireless Experience Kit, you can build your own Multi Access with Private 5g image using the following instructions. You can proceed with the steps presented using either edgesoftware sources or GitHub sources.

### Setup
Change the directory to repository path with one of the following options.

For Edgesoftware:

```
$ cd /home/smartedge-open/multi-access-with-private-5g/MultiAccess_with_Private_5G_Reference_Implementation_1.0.0/MultiAccess_with_Private_5G
```

For GitHub:

```
$ git clone <gma-repo>
$ cd /home/smartedge-open/applications.services.esh.multi-access-with-private-5g/
```

Use your preferred text editor to make the following file updates.

In the next steps, the tag `<REPOSITORY_PATH>` indicates the path to the repository.

In the Change examples, replace the line indicated by - with the line indicated by +

1. <REPOSITORY_PATH>/GMA/gmaserver/dockerbuild.sh - update the tag and version for the image.
  ```
   Change example:
   -    -t docker build -f ./dockerfile . -t generic-multi-access-network-virtualization:1.0
   +    -t docker build -f ./dockerfile . -t <local_tag>/generic-multi-access-network-virtualization:<version> 
   ```
2. <REPOSITORY_PATH>/GMA/deploy/gma/templates/deployment.yaml - update image deployment
   tag.
   ```
   Change example:
   - image: "intel/{{ .Values.image.repository }}:{{ .Values.image.Version }}"
   + image: "<local_tag>/{{ .Values.image.repository }}:{{ .Values.image.Version }}"
   ```
3. <REPOSITORY_PATH>/GMA/deploy/gma/values.yaml - update version.
   ```
   Change example:
   -  Version: "1.0"
   +  Version: "<version>"
   ```

### Build and Install

Build the Docker image with the following commands:

```
$ cd <REPOSITORY_PATH>/GMA/gmaserver
$ ./dockerbuild.sh   # The local Docker image will be built on the Ubuntu machine.
```

Install Helm with the following commands:

1. Apply the Network Attachment Definition:
```
$ cd <REPOSITORY_PATH>/GMA/deploy
$ kubectl apply -f gma5g-net.yaml
$ kubectl apply -f gmawifi-net.yaml
```

2. Apply the network policy:
```
$ kubectl apply -f gmanet-policy.yaml
```

3. Run the following Helm installation command:
```
$ helm install gma ./gma
```

After step 3 completes, run GMA client application on client machine to test the connectivity.



## Troubleshooting

### Setting packet loss rate of wifi and cellular interface
If the loss rate can't be added:
```
$ tc qdisc add dev <wifi-interface> root netem loss 50%
Error: Exclusivity flag on, cannot modify.
```
Please using the following command instead:
```
$ tc qdisc change dev <wifi-interface> root netem loss 50%
```
