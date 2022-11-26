# applications.services.esh.multi-access-with-private-5g
## Overview

As the mobile industry evolves towards 5G/5G+, it is becoming clear that no
single radio technology will be able to meet a great variety of requirements for
human and machine communications. On the other hand, driving more data through a
scarce and finite radio spectrum becomes a real challenge, and spectrum
efficiency is approaching a plateau and will not deliver the needed increase in
bandwidth improvement itself. Therefore, 5G is likely to utilize frequencies
below 6 GHz as well as mmWave, in both licensed and unlicensed bands.

Use a new software-defined, access-agnostic and high-performance reference
implementation (RI) to enable seamless integration of multiple access networks
at the edge. The Generic Multi-Access (GMA) RI can be used with no impact to
cellular or Wi-Fi* radio protocols (PDCP, RRC, Ethernet, and
others) or network protocols (IP, TCP, UDP, and others).

To run the reference implementation, you will need to first download and install
the [Intel® Smart Edge Open Private Wireless Experience
Kit](https://intelsmartedge.github.io/docs/experience-kits/private-wireless-experience-kit/#overview).

Once you have installed the Intel® Smart Edge Open Private Wireless Experience
Kit, select **Configure & Download** to download the reference implementation
and then follow the steps below to install it.

[Configure &
Download](https://software.intel.com/iot/edgesoftwarehub/download/home/multi-access-with-private-5g)

*  **Time to Complete:**  120 - 150 minutes
*  **Programming Language:**  Python\*
*  **Software:** Intel® Smart Edge Open 22.04.01 PWEK Release

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

### Client Device

-   Laptop supporting Wi-Fi and cellular (or Wi-Fi + cellular/USB tethering)

-   Ubuntu* 20.04

-   Wi-Fi AP

## How It Works

The Generic Multi-Access (GMA) client connects to the GMA server over cellular
and Wi-Fi. At the very beginning, the client has only one delivery connection
established (e.g. cellular) and will try to make the second delivery connection.
After both delivery connections are established, the client will then establish
a websocket-based secure connection between client and server to exchange
messages. A new protocol layer for GMA convergence is introduced to handle all
multi-path related operations, for example, splitting, reordering, duplication,
elimination measurements, etc.

![The architecture is represented by a complex block diagram.](/images/multi-access-with-private-5g-arch-diagram.png)

Figure 1: Architecture Diagram


## Get Started
### Prerequisites

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Private Wireless Experience Kit](https://smart-edge-open.github.io/docs/experience-kits/private-wireless-experience-kit/).

Ensure that the following conditions are met properly to ensure a smooth installation process for a reference implementation done through Edge Software Provisioner (ESP) Intel® Smart Edge Open Private Wireless Experience Kit package.

1. Hardware Requirements

   Make sure you have a fresh **CentOS\* 7.9.2009** installation with the
   Hardware specified in the [Target System
   Requirements](#target-system-requirements) section.

2. Network connections

    - Laptop connected to Wi-Fi through Wi-Fi AP which is connected to 100GbE
      Intel® Ethernet Network Adapter E810.

    - Laptop connected to cellular network through cellular tethering.

### Step 1: Install the Reference Implementation

>**NOTE:** The following sections may use ``<Controller_IP>`` in a URL
or command. Make note of your Edge Controller’s IP address and
substitute it in these instructions.

Select **Configure & Download** to download the reference implementation and
then follow the steps below to install it.

[Configure &
Download](https://software.intel.com/iot/edgesoftwarehub/download/home/multi-access-with-private-5g)

1.  Make sure that the Target System Requirements are met properly
    before proceeding further.


2.  If you are behind a proxy network, be sure that proxy addresses are configured in the system:

    ```bash
    export http_proxy=proxy-address:proxy-port
    export https_proxy=proxy-address:proxy-port
    ```

3.  Under the user deploy PWEK, for example smartedge-open, download the GMA RI package:

    ```bash
    mkdir path-of-downloaded-directory
    ```

4.  Open a new terminal and move the downloaded .zip package to the ``/home/smartedge-open`` folder:

    ```bash
    mv path-of-downloaded-directory/multi-access-with-private-5g.zip /home/smartedge-open
    ```

5.  Go to the ``/home/smartedge-open`` directory using the following command
    and unzip the RI:

    ```bash
    cd /home/smartedge-open
    unzip multi-access-with-private-5g.zip
    ```

6.  Go to the ``multi-access-with-private-5g/``
    directory:

    ```bash
    cd multi-access-with-private-5g

    openssl genrsa -out server.key 3072
    openssl req -new -key server.key -out server.csr (input user info)
    openssl x509 -req -in server.csr -out server.crt -signkey server.key -days 3650
    ```
    Three files will be generated: server.key, server.csr and server.crt.

7.  Apply the Network Attachment Definition and network policy:

    ```bash
    cd MultiAccess_with_Private_5G_Reference_Implementation_1.0.0/MultiAccess_with_Private_5G/GMA/deploy
    kubectl apply -f gma5g-net.yaml
    kubectl apply -f gmawifi-net.yaml
    kubectl apply -f gmanet-policy.yaml
    ```

8.  Change permissions of the executable edgesoftware file to enable
    execution:

    ```bash
    cd ../../../..
    chmod +x edgesoftware
    ```

9.  Run the command below to install the Reference Implementation:

    ```bash
    ./edgesoftware install
    ```

    > **NOTE:** Installation logs are available at path:
    >
    > ``/var/log/esb-cli/Multi-access-with-private-5g_<version>/<Component_Name>/install.log``


10. When the installation is complete, you see the message “Installation
    of package complete” and the installation status for each module.

    ![A console window showing system output during the install process. At the
    end of the process, the system displays the message "Installation of
    package complete" and the installation status for each
    module.](images/multi-access-with-private-5g-install-success.png)

    Figure 2: Successful Installation


    >**NOTE:** If the pods have a status of “ContainerCreating”, please wait
  for some time, since Kubernetes* will pull the images from the registry
  and then deploys them. This happens only the first time the containers
  are deployed, and the wait time will depend upon the network bandwidth
  available.

11. Check the GMA pods with the command:

    ```bash
    kubectl get pods -n smartedge-apps
    ```

    ![A console window showing system output after running the "kubectl get
    pods" command. The system displays a list of all the pods and the pod
    status. The expected status is "Running" or
    "Completed".](images/multi-access-with-private-5g-status-of-pods.png)

    Figure 3: Status of pods

12. Get the **Container ID** of gmaserver with the command:

    ```bash
    kubectl describe pod <gma-pod> -n smartedge-apps | grep "Container ID"
    ```

13. Copy the SSL certificate to the GMA container:

    ```bash
    docker cp ./server.key <gma-pod>:/home/python
    docker cp ./server.csr <gma-pod>:/home/python
    docker cp ./server.crt <gma-pod>:/home/python
    ```
    > **NOTE:** Run the command on Kubernetes node.

14. Run the gmaserver application:

    ```bash
    docker exec -itd <gma-container-id> bash -c "sudo ./rungma.sh"
    ```

    > **NOTE:** Run the command on Kubernetes node.

15. Install test tools of gmaserver:

    ```bash
    docker exec -itd <gma-container-id> bash -c "sudo apt-get update && sudo apt-get install iperf3 -y"
    ```
    > **NOTE:** Run the command on Kubernetes node.

### Step 2: Check the Application

1. Set up GMA client on the GMA client device, which is the laptop:

    ```bash
    git clone https://github.com/IntelLabs/gma.git

    sudo apt-get install libboost-all-dev
    sudo apt-get install libssl-dev
    sudo apt-get update
    sudo apt-get install net-tools
    sudo apt install screen speedometer iw -y
    ```

   Change client key to generated key. Use ``server.csr`` which was generated in [Step 1](#step-1-install-the-reference-implementation).

    ```bash
    cp /path/to/server.crt /path/to/gma
    cd gma
    sed '/./{s/^/        "&/;s/$/&\\n"/}' server.crt > client.crt
    ```
   Copy the contents of ``client.crt`` to ``path/to/gma/client/root_certificates.hpp`` to replace std::string const cert content.

   Compile the GMA client:

     ```bash
     cd ./GMAlib/lib
     make -B
     cd ../../client
     make -B
     ```

   Install the GMA client:

     ```bash
     sudo mkdir /home/gmaclient
     sudo chmod 777 ./gmaclient
     cd ./client
     cp ./gmaclient /home/gmaclient/
     cp ./config.txt /home/gmaclient/
     ```

   Configure the GMA client using the command below, where:

    ``wlan0``: network interface for Wi-Fi

    ``wwan0``: network interface for cellular

    ``gmaserver.apps.local``: local DNS name for GMA service running at Edge

    ``a.b.c.d``: GMA service IP address at the edge node via LTE

     ```bash
     SERVER_NCM_IP=a.b.c.d
     WLAN_INTERFACE_CONFIG=wlan0
     LTE_INTERFACE_CONFIG=wwan0
     ```

   Start the GMA client:

     ```bash
     cd /home/gmaclient
     sudo ./gmaclient
     ```

 2. Ping the GMA server. You will do tun setup after connection setup.

    ```bash
    ping 10.8.0.1

    PING 10.8.0.1 (10.8.0.1) 56(84) bytes of data.
    64 bytes from 10.8.0.1: icmp_seq=1 ttl=64 time=0.847 ms
    64 bytes from 10.8.0.1: icmp_seq=2 ttl=64 time=0.824 ms
    64 bytes from 10.8.0.1: icmp_seq=3 ttl=64 time=0.903 ms
    64 bytes from 10.8.0.1: icmp_seq=4 ttl=64 time=0.871 ms
    64 bytes from 10.8.0.1: icmp_seq=5 ttl=64 time=0.807 ms
    64 bytes from 10.8.0.1: icmp_seq=6 ttl=64 time=0.830 ms
    ```

 3. Run Demo Tests. Install test tools in server and log in to GMA Docker.

    ```bash
    kubectl exec -it <GMA-pod> -c gma -n smartedge-apps /bin/bash
    iperf3 -s -i 5
    ```

### Step 3: Check Seamless Mobility

1. Run demo test tools on the GMA client device:
    ```bash
    iperf3 -c 10.8.0.1 -t 1000 -i 5 -b 2M -u -l 1000
    speedometer -t tun0 -t wlp0s20f3 -t enx000ec6d75f05 -b -s -l -n 0 -m 400000
    ```

    ![Two console windows displayed side by side. The left window shows output of the "iperf3" command. The right window shows output of the speedometer tool.](/images/seamless_mobility/multi-access-with-private-5g-seamless-scene1-1.png)

    Figure 4: Start Demo Test Tools

2. Disconnect the Wi-Fi path:
    ```bash
    nmcli device disconnect <wifi-interface>
    ```
    Now the flow is transferred from Wi-Fi to cellular:

    ![Speedometer output showing data flow transfer from Wi-Fi to cellular.](/images/seamless_mobility/multi-access-with-private-5g-seamless-scene1-2.png)

    Figure 5: Disconnect the Wi-Fi Path

3. Reconnect the Wi-Fi path:
    ```bash
    nmcli device connect <wifi-interface>
    ```

    Now the flow is transferred to Wi-Fi again:

    ![Speedometer output showing data flow transfer from cellular to Wi-Fi.](/images/seamless_mobility/multi-access-with-private-5g-seamless-scene1-3.png)

    Figure 6: Reconnect the Wi-Fi Path

### Step 4: Check Uplink Redundancy

1. Run demo test. Install test tools on the GMA client device:

    ```bash
    iperf3 -c 10.8.0.1 -t 1000 -i 5 -b 2M -u -l 1000
    speedometer -t tun0 -t wlp0s20f3 -t enx000ec6d75f05 -b -s -l -n 0 -m 400000
    ```

2. Set the packet loss rate to 50% for both Wi-Fi and cellular:

    ```bash
    tc qdisc add dev <cellular-interface> root netem loss 50%
    tc qdisc add dev <wifi-interface> root netem loss 50%
    ```

    ![Speedometer output showing packet loss rate.](/images/uplink_redundancy/multi-access-with-private-5g-uplink-scene2-1.png)

    Figure 7: Status of Packet Loss Rate

    ![iperf output showing packet loss rate.](/images/uplink_redundancy/multi-access-with-private-5g-uplink-scene2-2.png)

    Figure 8: Status of Packet Loss Rate

3. Run GMA controller and enable uplink redundancy:

    ```bash
    ./gmactrl
    tfc 2 1 2 0 65520
    ```
    Now the packet loss rate of tun is decreased from 50% to about 25%:

    ![Speedometer output showing real time transmission status.](/images/uplink_redundancy/multi-access-with-private-5g-uplink-scene2-4.png)

    Figure 9: Real Time Transmission Status

    ![iperf output showing status of packet loss rate.](/images/uplink_redundancy/multi-access-with-private-5g-uplink-scene2-5.png)

    Figure 10: Status of Packet Loss Rate

4. Disable Uplink Redundancy:

    ```bash
    tfc 2 1 0 0 0
    ```
    Now the packet loss rate of tun is increased to 50% again:

    ![iperf output showing packet loss rate.](/images/uplink_redundancy/multi-access-with-private-5g-uplink-scene2-6.png)

    Figure 11: Status of Packet Loss Rate

    ![Speedometer output showing real time transmission status.](/images/uplink_redundancy/multi-access-with-private-5g-uplink-scene2-7.png)

    Figure 12: Real Time Transmission Status

### Step 5: Uninstall the Application

1. Check installed modules with the following command:

    ```bash
    cd /home/smartedge-open/multi-access-with-private-5g
    ./edgesoftware list
    ```

    ![A console window showing the output of the "edgesoftware list" command. The installed modules are listed.](/images/multi-access-with-private-5g-modules-list.png)

    Figure 13: Installed Modules List


2. Run the command below to uninstall all the modules:

    ```bash
    ./edgesoftware uninstall -a
    ```

3. Run the command below to uninstall the Multi Access with Private 5G reference
   implementation:

    ```bash
    ./edgesoftware uninstall <gma-id>
    ```

    ![A console window showing the output of the "edgesoftware uninstall" command. The system displays output during the uninstall process. At the end of the process, the system displays the message “Uninstall finished” and the uninstallation status for each module.](/images/multi-access-with-private-5g-uninstall.png)

    Figure 14: Uninstalled Modules


## Local Build Instructions

After you have installed Intel® Smart Edge Open Private Wireless Experience Kit, you can build your own Multi Access with Private 5G image using the following instructions. You can proceed with the steps presented using either edgesoftware sources or GitHub* sources.

### Setup

Change the directory to repository path with one of the following options.

For Edgesoftware:

```bash
cd /home/smartedge-open/multi-access-with-private-5g/MultiAccess_with_Private_5G_Reference_Implementation_1.0.0/MultiAccess_with_Private_5G
```

For GitHub:

```bash
git clone <gma-repo>
cd /home/smartedge-open/applications.services.esh.multi-access-with-private-5g/
```

Use your preferred text editor to make the following file updates.

In the next steps, the tag `<REPOSITORY_PATH>` indicates the path to the repository.

In the Change examples, replace the line indicated by - with the line indicated by +

1. ``<REPOSITORY_PATH>/GMA/gmaserver/dockerbuild.sh`` - update the tag and version for the image.

    ```bash
    Change example:
    -    -t docker build -f ./dockerfile . -t generic-multi-access-network-virtualization:1.0
    +    -t docker build -f ./dockerfile . -t <local_tag>/generic-multi-access-network-virtualization:<version> 
    ```

2. ``<REPOSITORY_PATH>/GMA/deploy/gma/templates/deployment.yaml`` - update image deployment
   tag.

    ```bash
    Change example:
    - image: "intel/{{ .Values.image.repository }}:{{ .Values.image.Version }}"
    + image: "<local_tag>/{{ .Values.image.repository }}:{{ .Values.image.Version }}"
    ```

3. ``<REPOSITORY_PATH>/GMA/deploy/gma/values.yaml`` - update version.

    ```bash
    Change example:
    -  Version: "1.0"
    +  Version: "<version>"
    ```

### Build and Install

Build the Docker image with the following commands:

```bash
cd <REPOSITORY_PATH>/GMA/gmaserver
./dockerbuild.sh   # The local Docker image will be built on the Ubuntu machine.
```

Install Helm with the following commands:

1. Apply the Network Attachment Definition:

    ```bash
    cd <REPOSITORY_PATH>/GMA/deploy
    kubectl apply -f gma5g-net.yaml
    kubectl apply -f gmawifi-net.yaml
    ```

2. Apply the network policy:

    ```bash
    kubectl apply -f gmanet-policy.yaml
    ```

3. Run the following Helm installation command:

    ```bash
    helm install gma ./gma
    ```

After step 3 completes, run the GMA client application on client machine to test
the connectivity.

## Summary and Next Steps

*OPEN: Provide 2-3 line description of what they have successfully done and
where they should go to as the next step.*

## Learn More

To continue learning, see the following guides and software resources:

-  [Intel® Smart Edge Open Private Wireless Experience
Kit](https://intelsmartedge.github.io/docs/experience-kits/private-wireless-experience-kit/#overview)
-  [relevant link title](URL) *OPEN*
-  [relevant link title](URL) *OPEN*


## Troubleshooting

### Setting packet loss rate of Wi-Fi and cellular interface

If the loss rate can't be added and you see this error:

```bash
tc qdisc add dev <wifi-interface> root netem loss 50%
Error: Exclusivity flag on, cannot modify.
```
Use the following command instead:

```bash
tc qdisc change dev <wifi-interface> root netem loss 50%
```

### Support Forum

If you're unable to resolve your issues, contact the [Support
Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).