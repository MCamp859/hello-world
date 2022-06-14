```text
Copyright (c) 2021-2022 Intel Corporation
SPDX-License-Identifier: MIT
```

# Intel® Smart Edge Open Developer Experience Kit

## Overview

Intel® Smart Edge Open Developer Experience Kit provides customized infrastructure deployments for common network and on-premises edge use cases. Combining Intel cloud-native technologies, wireless networking, and high-performance compute, experience kits let you deliver AI, video, and other services optimized for performance at the edge.

The Intel® Smart Edge Open Developer Experience Kit lets you easily install and instantiate an Intel® Smart Edge Open edge cluster.

The Intel® Smart Edge Open Developer Experience Kit installs the Smart Edge Cluster on a single node. The kit solution is built on top of Kubernetes*, which is a production-grade container orchestration environment. A typical Intel® Smart Edge Open Developer Experience Kit-based deployment consists of a Kubernetes Control Plane and an Edge Node.

Once the cluster is installed, you will be able to run edge applications, including reference implementations built on Intel® Smart Edge Open, and become familiar with operating a stand-alone edge node.

Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits)
to download the Intel® Smart Edge Open Developer Experience Kit version 3.0.0. 

This 3.0.0 version is having flexibility to configure deployment in different modes like Lean, Default and Custom using Edge Software Provisioner (ESP) or manual. 

Lean mode deploys basic minimal services [ like calico cni, grafana, nfd, dns, kube-system, cert-manager ] for developers to deploy different kinds of edge applications including reference implementations.

Default mode deploys all services available with developer experience kit and custom mode deploys  microservices like security SGX and PCCS microservices, SRIOV, harbor, telemetry, root_ceph, kubevirt based on enable or disable.

For more information like building blocks, installation steps with security services in the Default mode, see the Intel® [Default Smart Edge Open Developer Experience Kit](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22.03/experience-kits/developer-experience-kit.md)


**Table 1**

|**Time to Complete**|15 – 20 mins|
| :- | :- |
|**Programming Language**|Python, C++, Java Scripts, HTML|
|<p>**Software**</p><p></p>|<p>[Intel® Smart Edge Open Developer Experience Kit](https://github.com/smart-edge-open/open-developer-experience-kits)</p><p>|



## System Requirements 

You will need two machines if you choose ESP-based deployment: a provisioning system where you will build a bootable image of the experience kit, and a target system where you will install the experience kit to create an edge cluster.

If you choose to enable security features either platform attestation using Intel® SecL - DL or application security using Intel® SGX in your installation, you will also need an Amazon* Web Services (AWS) EC2 t2.medium instance or a local standalone VM instance to host the controller node.

### Provisioning System

This is required only for ESP-based deployment.
- Memory: At least 4 GB RAM.
- Hard drive: At least 20 GB.
- USB flash drive.
- Operating system: Ubuntu 20.04 LTS Server.
- Git.
- Docker and Docker Compose.
  - **NOTE:** You must install Docker from the Docker repository. Installation by Docker package is not supported.
Python 3.6 or later, with the PyYAML module installed.
- Internet access.
- **NOTE:** You must add the user account on the provisioning system to /etc/sudoers. 

### AWS EC2 Instance or standalone VM Requirements for security cluster

Installations that enable either platform attestation using Intel® SecL - DC or application security using Intel® SGX will require the following:
- An AWS EC2 t2.medium instance with the following system requirements:
   - Two vCPUs
   - 16 GB RAM
   - 100 GB disk space
   - Ubuntu 20.04 LTS
- A Linux system from which deployment of the controller node is initiated.

#### Target System

Target system where you will install the experience kit to create an edge cluster.
- A server with two sockets, each populated with a 3rd Generation Intel® Xeon® Scalable Processor.
- Memory: At least 16 GB RAM for Lean deploy and 32 GB RAM for default.
- Disc Space: At least 50 GB Free Space.
- Hard drives: Two SATA SSDs, one for booting and one for data caching.
- Network adapters: Two NICs, one connected to each socket.
  - **NOTE:** This configuration was validated using two Intel Corporation Ethernet Controller E810-C for SFP (rev 02) NICs.
- Operating system: Ubuntu* 20.04 LTS.
  - **NOTE:** The provisioning process will install Ubuntu 20.04 LTS on the target machine. Any existing operating system will be overwritten.

View the full specs of the [validated system](https://github.com/smart-edge-open/docs/blob/main/release-notes/release-notes-se-open-DEK-22-03.md). 


## How It Works

The Intel® Smart Edge Open Developer Experience Kit is designed to support a variety of edge computing use cases. Below is the architecture of an edge node instantiated with platform attestation and application security features enabled:

The kit consists of two clusters.

-	Cluster in the cloud or standalone VM, that hosts Intel® SecL - DC and Intel® SGX control plane services. These control plane services enable platform attestation and Secure enclave for Edge applications and services.
-	Cluster at the edge (typically on-premises) that hosts edge services and applications.

![Smart Edge Open Developer Experience Kit - Deployment Diagram](./images/dek-deploy.PNG)

Let us now look at the components stack of DEK edge and cloud cluster.

![Smart Edge Open Developer Experience Kit - Edge Node Component Diagram](./images/dek-node-component-diagram.PNG)

Let us now look at the components stack of Lean DEK edge .

![Smart Edge Open Developer Experience Kit - Lean Edge Node Component Diagram](./images/lean-dek-component-diagram.PNG)

*Developer Experience Kit edge node with Intel® SecL-DC attestation enabled*

The integrated security features require that remote attestation services be deployed on an Amazon Web Services (AWS) EC2 instance or standalone VM. 

![Smart Edge Open Developer Experience Kit - IsecL Controller and SGX DCAP Node Component Diagram](./images/verification-node-component-diagram.PNG)

*Remote attestation services deployed as a controller node on AWS*


## Building Blocks

Building blocks provide specific functionality in the platform you'll deploy. Each experience kit installs a set of building blocks as part of deployment. You can use additional building blocks to customize your platform, or develop your own custom solution by combining building blocks.

Building blocks varies based on mode of deployment. Below is the table of contents briefs on blocks deploy based on mode choosen by user while package install.

| Building Block | Lean SEO-DEK mode | Default SEO-DEK mode | Custom SEO-DEK mode
| :------------- | :------------- | :------------- | :------------- |
|Calico CNI | Enabled | Enabled | Enabled |
Multus CNI | NA | Enabled | Enabled |
SR-IOV Network Operator | NA | Enabled | Enable/Disable |
cert-manager | Enabled | Enabled | Enabled |
Node Feature Discovery (NFD) | Enabled | Enabled | Enabled |
Harbor | NA | Enabled | Enable/Disable |
Intel® SecL-DC | NA | Enable/Disable | Enable/Disable |
Intel® SGX | NA | Enable/Disable | Enable/Disable |
Telemetry grafana | Enabled | Enabled | Enabled |
Telemetry prometheus | NA | Enabled | Enable/Disable |
Telemetry statsd, collectd | NA | Enabled | Enable/Disable |
Telemetry cadvisor | NA | Enabled | Enable/Disable |
Hugepages | NA | Disable | Enable/Disable |
Rook ceph | NA | Disable | Enable/Disable |
Kube-virt | NA | Disable | Enable/Disable |


The Configurable Intel® Smart Edge Open Developer Experience Kit includes the following building blocks. For more information on a component, see that component’s documentation.

### Edge Node Components

| Building Block | Functionality     |
| :------------- | :------------- |
|[Calico CNI](https://docs.projectcalico.org/about/about-calico) | Default container network interface |
[Telemetry](/components/telemetry/telemetry.md) | Remote collection of device data for real-time monitoring|
[Node Feature Discovery (NFD)](/components/resource-management/node-feature-discovery.md) | Detects and advertises the hardware features available in each node of a Kubernetes* cluster |
[cert-manager](https://cert-manager.io/docs/) | Adds certificates and certificate issuers as resource types in the cluster, and simplifies the process of obtaining, renewing and using those certificates | 

### Controller Node Components

| Building Block | Functionality     |
| :------------- | :------------- |
|[Calico CNI](https://docs.projectcalico.org/about/about-calico) | Default container network interface |
[Node Feature Discovery (NFD)](/components/resource-management/node-feature-discovery.md) | Detects and advertises the hardware features available in each node of a Kubernetes* cluster |
[cert-manager](https://cert-manager.io/docs/) | Adds certificates and certificate issuers as resource types in the cluster, and simplifies the process of obtaining, renewing and using those certificates | 

For information on the versions installed, see the Intel® Smart Edge Open Developer Experience Kit [release notes](https://github.com/smart-edge-open/docs/blob/main/release-notes/release-notes-se-open-DEK-22-03.md#package-versions)




## Get Started

### Prerequisite
   
Make sure that [System Requirements](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22.03/experience-kits/developer-experience-kit.md#requirements) met before continuing further. 

### Download and Install Intel® Smart Edge Open Developer Experience Kit
   
Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits)
to download the Intel® Smart Edge Open Developer Experience Kit and then follow the steps below to install it.   

1. Make sure that the Target System requirements are met properly before continuing further. Refer Target system requirements.

2. Confirm the steps below are followed:
- Proxy Settings
    If you are behind a proxy network, ensure that proxy addresses are configured in the system.
    ```
    https_proxy=<proxy-address>:<proxy-port> 
    http_proxy=<proxy-address>:<proxy-port> 
    HTTP_PROXY=<proxy-address>:<proxy-port>
    HTTPS_PROXY=<proxy-address>:<proxy-port>
    ftp_proxy=<proxy-address>:<proxy-port> 
    no_proxy=<list of proxies with your machine ip>
    NO_PROXY=<list of proxies with your machine ip>
    all_proxy=<socks>:<proxy-address>:<port>
    ```
- Date and Time 
    Make sure that the date and time are in sync with the current local time.  
- Make sure the Hostname of the server should follow the DNS label standard as defined in RFC 1123.
    - contain at most 63 characters
    - contain only lowercase alphanumeric characters or '-'
    - start with an alphanumeric character
    - end with an alphanumeric character

3. Create a non-root user, for example username as "smartedge-open" and set the password as "smartedge-open" for the user.

    ```Shell.bash
    - sudo useradd -s /bin/bash -d /home/smartedge-open/ -m -G sudo smartedge-open
    - sudo passwd smartedge-open
    ```

4. Add sudoers permission to "smartedge-open" user

    ```Shell.bash
    echo "smartedge-open ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/smartedge-open
    ```

5. Login to the server as "smartedge-open" user and run the below commands to configure ssh access

    ```Shell.bash
    - ssh-keygen 
    - ssh-copy-id smartedge-open@<server IP>
    ```

6. Copy the downloaded zip package to the Target Server user home directory.

7. Extract the downloaded .zip package with the command:

    ```Shell.bash
    unzip Smart_Edge_Open_Developer_Experience_Kits.zip
    ```

> **NOTE:** If unzip command cannot be found, install using ``sudo apt-get install unzip``

8. Go to the Smart_Edge_Open_Developer_Experience_Kits directory. 

    ```Shell.bash
    cd Smart_Edge_Open_Developer_Experience_Kits
    ```

9. Change permission of the executable edgesoftware file. 

    ```Shell.bash
    chmod 755 edgesoftware 
    ```

10. Run the command below to install the kit: 

    ```Shell.bash
    ./edgesoftware install
    ```

11. During the installation, you will be prompted for the ESP Provisioning option. If you are using Provisioning setup to generate usb bootable image then select "yes" or else if you are using direct deployment in target system then select "No".

    ![Smart Edge Open Developer Experience Kit - ESP field input Diagram](./images/ESP_lean_mode.PNG)

    Figure 1: ESP Lean mode input fields

    ![Smart Edge Open Developer Experience Kit - ESP custom.yml file changes](./images/ESP_custom_config.PNG)

    Figure 2: ESP custom.yml file changes

> **NOTE:** If user selected ESP option as "yes", the deployement of Smart Edge Open Developer Experience Kit will generate custom.yml file and add feature flags based on deploy mode selected under group_vars:groups:all section. Then follow for further steps to prepare ESP bootable image with custom.yml config file [build-and-run-the-provisioning services](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22.03/experience-kits/developer-experience-kit.md#build-and-run-the-provisioning-services)
  
12. Provide user inputs for required fields. As mentioned above, in this Configurable Smart_Edge_Open_Developer_Experience_Kits version 3.0.0, have flexible to choose different deployment modes. 
    1. Lean DEK
        Micro services deployed are
        a. Calico cni service
        b. Certificate manager service
        c. NFD service
        d. Grafana service
        e. Kube-system services dns, api, etc.
    2. Default DEK
        All default available micro services.
    3. Custom DEK
        All Lean DEK services + remaining micro services based on opted while deploy.

Input fields varies based on mode of deployment. 
  - If opted security services, make sure target machine must have proper connectivity to attestation cloud cluster and target machine BIOS upgraded and configured for SGC and PCCS.
  -  If SRIOV opted, make sure all NICs configured for SRIOV in BIOS configuration.

> **NOTE:** If security features enabled in Default/Custom mode, 
1.	BIOS version on target system must be 1.3.8 or higher.

2.	Enable security support in the BIOS by following steps mentioned at [Enable security suport in the BIOS](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22.03/experience-kits/developer-experience-kit.md#optional-enable-security-support-in-the-bios)

3.	Update environment file with proper proxy servers if target machine is behind the proxy.
   - proxy_env:
      ```
      http_proxy: <proxy-address>:<proxy-port>
      https_proxy: <proxy-address>:<proxy-port>
      ftp_proxy: <proxy-address>:<proxy-port>
      no_proxy: <add Provision machine IP>
      all_proxy: socks5://<proxy-address>:<proxy-port>
      ```
   - sgx_pccs_ip: PCCS server IP address (Attestation DEK cloud cluster/ VM IP)
   - pccs_user_token: the exact password provided in attestation DEK cloud cluster/ VM for ``pccs_user_password:`` and ``pccs_admin_password:``
   - isecl_cms_tls_hash: add the hash generated by running the below command on attestation DEK cloud cluster / VM.
       ```
       kubectl exec -n isecl --stdin "$(kubectl get pod -n isecl -l app=cms -o jsonpath="{.items[0].metadata.name}")" -- cms tlscertsha384
       ```
   - isecl_control_plane_ip: <Attestation DEK cloud cluster / VM IP>

13. Provide user input as '1' if wish to deploy in Lean DEK mode as mentioned below.

    ![Smart Edge Open Developer Experience Kit - Lean mode field input Diagram](./images/Lean_mode.PNG)

    Figure 3: Lean DEK mode input fields

    configuration will be saved and will display on subsequent install as 

    ![Smart Edge Open Developer Experience Kit - Lean mode saved config Diagram](./images/lean_mode_found_previous.PNG)

    Figure 4: Lean DEK saved configuration

14. Provide user input as '2' if wish to deploy Default DEK mode as mentioned below.

    ![Smart Edge Open Developer Experience Kit - Default mode input Diagram](./images/default_mode.PNG)

    Figure 5: Default DEK mode input fields

    configuration will be saved and will display on subsequent install as 

    ![Smart Edge Open Developer Experience Kit - Default mode saved config Diagram](./images/default_mode_found_previous.PNG)

    Figure 6: Default DEK saved configuration

15. Provide user input as '3' if wish to deploy Custom mode of DEK deploy as mentioned below.

    ![Smart Edge Open Developer Experience Kit - Custom mode field inputs Diagram](./images/custom_mode.PNG)

    Figure 7: Custom DEK mode input fields

    configuration will be saved and will display on subsequent install as 

    ![Smart Edge Open Developer Experience Kit - Custom mode saved config Diagram](./images/custom_found_previous.PNG)

    Figure 8: Custom DEK saved configuration

16. When the deployement is complete, you see the message ``Installation of package complete`` and the installation status for each module.

    ![Smart Edge Open Developer Experience Kit - Installed Diagram](./images/dek-installed-diagram.PNG)
   
    Figure 9: Installed Successfully

> **NOTE:** Installation logs are available at the following path: 
/var/log/esb-cli/Smart_Edge_Open_Developer_Experience_Kits_3.0.0/Smart_Edge_Open_Developer_Experience_Kits/install.log

17. After the successful deployment of Lean SEO-DEK, you can check running pods by giving below command.

    ```Shell.bash
    kubectl get pods -A
    ```
    ![Smart Edge Open Developer Experience Kit - Pods Status Diagram](./images/dek-pods-status-diagram.PNG)
    
    Figure 10: Pods Status

### Uninstall the Intel® Smart Edge Open Developer Experience Kit 
1. To remove Intel® Smart Edge Open Developer Experience Kit from system:

    ```Shell.bash
    ./edgesoftware uninstall -a
    ```

    ![Smart Edge Open Developer Experience Kit - dek uninstall Diagram](./images/dek-uninstall-diagram.PNG)
   
    Figure 11: Uninstalled Successfully
 

### Summary and Next Steps

In this guide, you installed the Intel® Smart Edge Open Developer Experience Kit. 

*  If you completed the [Create the Installation Image](https://github.com/smart-edge-open/docs/blob/main/experience-kits/developer-experience-kit.md#create-the-installation-image) procedure, then you created an Intel® Smart Edge Open edge node cluster capable of hosting edge applications.
*  Learn how to [onboard a sample application to your cluster](https://github.com/smart-edge-open/docs/blob/main/application-onboarding/application-onboarding-cmdline.md).
*  Download reference implementations from the [Intel® Developer Catalog](https://www.intel.com/content/www/us/en/developer/tools/software-catalog/overview.html?s=Newest).


### Troubleshooting

1.	Operating System (OS) Mismatch
   
    Use only supported OS and version as mentioned in target system requirements. Otherwise, the error ‘not supported’ is displayed.

2.  Changing BIOS settings
   
    The Intel® SGX settings modification in BIOS doesn't work from iDRAC/BMC. You must do this step from the BIOS console if you experience this issue.
    If you set multiple different parameters, then you must reboot for each step.
 
3.  Intel® SGX Enable Issues
   
    In some servers, Intel® SGX may not enable even after following BIOS settings as in [Enable security suport in the BIOS](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22-03/experience-kits/developer-experience-kit.md#optional-enable-security-support-in-the-bios)
    You must reboot the setup after each setting done in BIOS.
    - TPM Advanced Settings -> Memory Encryption -> Disabled (reboot)
    - TPM Advanced Settings -> Memory Encryption -> Single Key (reboot)
    - TPM Advanced Settings -> SGX & SGX factory reset -> On (reboot)
    - TPM Advanced Settings -> PMMR -> 64GB (reboot)

4.  SRIOV Enabling
   
    If SRIOV is enabled in config file, you must enable SRIOV in BIOS globally and on each NIC interface.


###	Support Forum

If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes). 
   
To attach the logs in compressed format, refer to the steps below to create the tar.gz compressed file.

* Execute the command below to consolidate list of the log files in tar.gz format, like ``seo_dek.tar.gz``.

    ```Shell.bash
    tar -czvf seo_dek.tar.gz /var/log/esb-cli/Smart_Edge_Open_Developer_Experience_Kits_3.0.0/Smart_Edge_Open_Developer_Experience_Kits/
    ```

