```text
Copyright (c) 2021-2022 Intel Corporation
SPDX-License-Identifier: MIT
```

# Intel® Smart Edge Open Developer Experience Kit

## Overview

Intel® Smart Edge Open Developer Experience Kit provides customized
infrastructure deployments for common network and on-premises edge use cases.
Combining Intel Cloud Native technologies, and high-performance compute, this
kit provide a blueprint to help building AI, video and edge services covering
diverse IoT segments with diverse optimization at the edge.

The Intel® Smart Edge Open Developer Experience Kit enables you to install and
instantiate an Intel® Smart Edge Open edge cluster on a single node. A typical
Intel® Smart Edge Open Developer Experience Kit-based deployment consists of a
Kubernetes Control Plane and an Edge Node.

Once the cluster is installed, you will be able to run edge applications,
including reference implementations built on Intel® Smart Edge Open, and become
familiar with operating a stand-alone edge node.

The Intel® Smart Edge Open Developer Experience Kit 22.03.01, with ESH SW package
version v3.0.0, provides flexible installation options using Edge Software
Provisioner (ESP) or manual configuration.

*  **Default Installation**, which deploys the full capabilities of Intel® Smart
   Edge Open Developer Experience Kit including the security capabilities. 

*  **Installation without Security features**, which deploys Intel® Smart Edge
   Open Developer Experience Kit without the security building blocks 
   (SGX, ISecL, KMRA).

*  **Installation with building blocks selection**, which deploys a set of
   building blocks required for basic services operation (like Calico/Multus CNI,
   SR-IOV Network Operator, Grafana*, Prometheus, stasd, telegraf, cadvisor, NFD,
   DNS, huge-pages, rook-ceph, Harbor, kube-system, kube-vert, cert-manager) for
   developers to deploy different kind of edge applications including reference
   implementations helping the case of limited resources for the platforms.


Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits)
to download the Intel® Smart Edge Open Developer Experience Kit. 


*  **Time to Complete:**  15 – 20 minutes
*  **Programming Language:**  Python, C++, Java Scripts, HTML
*  **Software:**  Intel® Smart Edge Open Developer Experience Kit



## System Requirements

You will need two machines if you choose ESP-based deployment: a provisioning
system where you will build a bootable image of the experience kit, and a target
system where you will install the experience kit to create an edge cluster.

When you do default installation, where the security features will be included,
either platform attestation using Intel® SecL - DL or application security using
Intel® SGX in your installation, you will also need an Amazon* Web Services (AWS)
EC2 t2.medium instance or a local standalone VM instance to host the controller node.

### Provisioning System

This is required only for ESP-based deployment.

- Memory: At least 4 GB RAM.
- Hard drive: At least 20 GB.
- USB flash drive.
- Operating system: Ubuntu* 20.04 LTS Server.
- Git.
- Docker* and Docker Compose.

  **NOTE:** You must install Docker from the Docker repository. Installation by Docker package is not supported.

- Python 3.6 or later, with the PyYAML module installed.
- An Internet connection.

**NOTE:** You must add the user account on the provisioning system to
`/etc/sudoers`.

### Security Cluster Requirements

The default installation of Developer Experience Kit that enable either platform attestation using
Intel® SecL - DC or application security using Intel® SGX will require the following:
- An AWS EC2 t2.medium instance with the following system requirements:

   - Two vCPUs.
   - 16 GB RAM.
   - 100 GB disk space.
   - Ubuntu 20.04 LTS.

- A Linux* system from which deployment of the controller node is initiated.

### Target System

Target system where you will install the Intel® Smart Edge Open Developer
Experience Kit to create an edge cluster.
- A server with two sockets, each populated with a 3rd Generation Intel® Xeon® Scalable Processor.
- Memory: At least 16 GB RAM for Lean mode and 32 GB RAM for default installation.
- Disk Space: At least 50 GB free space.
- Hard drives: Two SATA SSDs, one for booting and one for data caching.
- Network adapters: Two NICs, one connected to each socket.

  **NOTE:** This configuration was validated using two Intel® Ethernet Controller E810-C for SFP (rev 02) NICs.

- Operating system: Ubuntu* 20.04 LTS.

  **NOTE:** The provisioning process will install Ubuntu 20.04 LTS on the target machine. Any existing operating system will be overwritten.

View the full specs of the [validated system](https://github.com/smart-edge-open/docs/blob/main/release-notes/release-notes-se-open-DEK-22-03.md).


## How It Works

The Intel® Smart Edge Open Developer Experience Kit uses [Edge Software
Provisioner](https://github.com/intel/Edge-Software-Provisioner), which
automates the process of provisioning bare-metal or virtual machines with an
operating system and software stack. Intel® Smart Edge Open provides a fork of
the [Ubuntu OS ESP Profile](https://github.com/intel/rni-profile-base-ubuntu)
tailored for its specific needs.

The Intel® Smart Edge Open Developer Experience Kit is designed to support a variety
of edge computing use cases. Below is the architecture of an edge node instantiated
with platform attestation and application security features enabled:

Intel® Smart Edge Open Developer Experience Kit consists of two clusters, as shown
in the diagram below.

-	Cluster in the cloud or standalone VM, that hosts Intel® SecL - DC and Intel® SGX
   control plane services. These control plane services enable platform attestation
   and secure enclave for Edge applications and services. This Cluster will be needed
   if the default installation is used, which has the security features.
-	Cluster at the edge (typically on-premises) that hosts edge services and applications.

![Smart Edge Open Developer Experience Kit - Deployment Diagram](./images/dek-deploy.png)

Figure 1: Deployment Architecture

The following diagram shows the component stack of Intel® Smart Edge Open Developer
Experience Kit edge and cloud cluster.

![Smart Edge Open Developer Experience Kit - Edge Node Component Diagram](./images/dek-node-component-diagram.png)

Figure 2: Components of the Intel® Smart Edge Open Developer Experience Kit

The integrated security features require that remote attestation services be deployed on an 
Amazon Web Services (AWS) EC2 instance or standalone VM, as shown in the following diagram.

![Smart Edge Open Developer Experience Kit - IsecL Controller and SGX DCAP Node Component Diagram](./images/verification-node-component-diagram.png)

Figure 3: Verification Node Components

Intel® Smart Edge Open Developer Experience Kit includes the following building blocks.
For more information on a component, see that component’s documentation.

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

For information on the versions installed, see the Intel® Smart Edge Open Developer Experience Kit [Release Notes](https://github.com/smart-edge-open/docs/blob/main/release-notes/release-notes-se-open-DEK-22-03.md#package-versions).




## Get Started

### Prerequisite

Make sure that [Intel® Smart Edge Open Developer Experience Kit
System Requirements](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22.03/experience-kits/developer-experience-kit.md#requirements)
are met before continuing further.

### Download and Install Intel® Smart Edge Open Developer Experience Kit

Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits)
to download the Intel® Smart Edge Open Developer Experience Kit and then follow the steps below to install it.

1. Make sure that the Target [System Requirements](#system-requirements) are met
   properly before continuing further.

2. Confirm the steps below are followed:
   -  Proxy Settings

      If you are behind a proxy network, ensure that proxy addresses are configured in the system.

      ```Shell.bash
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

   - Make sure the Hostname of the server should follow the DNS label standard
     as defined in RFC 1123.
      - Contain at most 63 characters
      - Contain only lowercase alphanumeric characters or ``-``
      - Start with an alphanumeric character
      - End with an alphanumeric character

3. Create a non-root user. For example, set username as ``smartedge-open`` and
   set the password as ``smartedge-open`` for the user:

    ```Shell.bash
    sudo useradd -s /bin/bash -d /home/smartedge-open/ -m -G sudo smartedge-open
    sudo passwd smartedge-open
    ```

4. Add sudoers permission to ``smartedge-open`` user:

    ```Shell.bash
    echo "smartedge-open ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/smartedge-open
    ```

5. Login to the server as ``smartedge-open`` user and run the below commands to
   configure ssh access:

    ```Shell.bash
    ssh-keygen
    ssh-copy-id smartedge-open@<server IP>
    ```

6. Copy the downloaded zip package to the Target Server user home directory.

7. Extract the downloaded .zip package with the command:

    ```Shell.bash
    unzip Smart_Edge_Open_Developer_Experience_Kits.zip
    ```

   > **NOTE:** If the unzip command cannot be found, install it using the ``sudo apt-get install unzip`` command.

8. Go to the ``Smart_Edge_Open_Developer_Experience_Kits`` directory:

    ```Shell.bash
    cd Smart_Edge_Open_Developer_Experience_Kits
    ```

9. Change permission of the executable edgesoftware file:

    ```Shell.bash
    chmod 755 edgesoftware
    ```

10. Run the command below to install the kit:

    ```Shell.bash
    ./edgesoftware install
    ```

11. During the installation, you will be prompted for the ESP Provisioning option. 
    If you are using Provisioning setup to generate a USB bootable image, then 
    select "Yes". If you are using direct deployment in target system, then select "No".
    ![Smart Edge Open Developer Experience Kit - ESP default mode input Diagram](./images/ESP_default_mode.png)

    Figure 4: ESP method with Default Installation mode

    ![Smart Edge Open Developer Experience Kit - ESP field input Diagram](./images/ESP_lean_mode.png)

    Figure 5: ESP method with Selective building blocks installation mode

    ![Smart Edge Open Developer Experience Kit - ESP custom.yml file changes](./images/ESP_custom_config.png)

    Figure 6: ESP method configuration file

      > **NOTE:** If you selected the ESP option as "Yes", the deployment of the Intel® Smart Edge Open Developer Experience Kit will pull the latest repo, generate a ``custom.yml`` file, and add feature flags based on installation selected under the  ``group_vars:groups:all`` section. To prepare an ESP bootable image with custom.yml config file, follow the steps here:  [build-and-run-the-provisioning services](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22.03/experience-kits/developer-experience-kit.md#build-and-run-the-provisioning-services)

12. Provide user inputs for required fields. As mentioned above, you can choose
    based on required installation type. The input fields vary depending on
    which installation you choose.

      * If you selected security services, make sure the target machine has
        proper connectivity to attestation cloud cluster and the target machine
        BIOS is upgraded and configured for SGC and PCCS.

      * If you selected SR-IOV, make sure all NICs configured for SR-IOV in BIOS
        configuration.

      * If security features are enabled:

         * BIOS version on target system must be 1.3.8 or higher.
         * Enable security support in the BIOS by following steps mentioned at:
           [Enable security suport in the BIOS](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22.03/experience-kits/developer-experience-kit.md#optional-enable-security-support-in-the-bios)
         * Update ``proxy_env`` environment file with proper proxy servers if target machine
           is behind a proxy:

            ```
            http_proxy: <proxy-address>:<proxy-port>
            https_proxy: <proxy-address>:<proxy-port>
            ftp_proxy: <proxy-address>:<proxy-port>
            no_proxy: <add Provision machine IP>
            all_proxy: socks5://<proxy-address>:<proxy-port>
            ```
         - sgx_pccs_ip: PCCS server IP address (Attestation DEK cloud cluster/ VM IP)
         - pccs_user_token: The exact password provided in attestation DEK cloud cluster/ VM for ``pccs_user_password:`` and ``pccs_admin_password:``
         - isecl_cms_tls_hash: Add the hash generated by running the below command on attestation DEK cloud cluster / VM.
            ```
            kubectl exec -n isecl --stdin "$(kubectl get pod -n isecl -l app=cms -o jsonpath="{.items[0].metadata.name}")" -- cms tlscertsha384
            ```
         - isecl_control_plane_ip: ``<Attestation DEK cloud cluster / VM IP>``
  

13. Enter ``1`` if you wish to deploy selective building blocks with limited resource as mentioned below.

    ![Smart Edge Open Developer Experience Kit - Lean mode field input Diagram](./images/Lean_mode.png)

    Figure 7: Selective building blocks with limited resource Input Fields

    The configuration will be saved and will display on subsequent install as shown below.

    ![Smart Edge Open Developer Experience Kit - Lean mode saved config Diagram](./images/lean_mode_found_previous.png)

    Figure 8: Selective building blocks with limited resource Saved Configuration

14. Enter ``2`` if you wish to deploy Default installation as mentioned below.

    ![Smart Edge Open Developer Experience Kit - Default mode input Diagram](./images/default_mode.png)

    Figure 9: Default installation Input Fields

    The configuration will be saved and will display on subsequent install as shown below.

    ![Smart Edge Open Developer Experience Kit - Default mode saved config Diagram](./images/default_mode_found_previous.png)

    Figure 10: Default Installation Saved Configuration

15. Enter ``3`` if you wish to deploy Selective building blocks as mentioned below.

    ![Smart Edge Open Developer Experience Kit - Custom mode field inputs Diagram](./images/custom_mode.png)

    Figure 11: Selective building blocks Input Fields

    The configuration will be saved and will display on subsequent install as shown below.

    ![Smart Edge Open Developer Experience Kit - Custom mode saved config Diagram](./images/custom_found_previous.png)

    Figure 12: Selective building blocks Saved Configuration

      > **NOTE:** Telemetry telegraf feature is dependent on Harbor registry. Can choose enable/disable only if Harbor registry enabled.

16. When the installation and deployment is complete, you see the message 
    ``Installation of package complete`` and the installation status for each module.

    ![Smart Edge Open Developer Experience Kit - Installed Diagram](./images/dek-installed-diagram.png)
   
    Figure 13: Installed Complete

> **NOTE:** Installation logs are available at the following path:
``/var/log/esb-cli/Smart_Edge_Open_Developer_Experience_Kits_<version>/Smart_Edge_Open_Developer_Experience_Kits/install.log``
>
> Where ``<version>`` indicates the package version downloaded.

17. After the successful deployment, you can check running pods using the command:

    ```Shell.bash
    kubectl get pods -A
    ```
    ![Smart Edge Open Developer Experience Kit - Pods Status Diagram](./images/dek-pods-status-diagram.png)
    
    Figure 14: Pods Status

### Uninstall the Intel® Smart Edge Open Developer Experience Kit

To remove the Intel® Smart Edge Open Developer Experience Kit, run the command:

```Shell.bash
./edgesoftware uninstall -a
```

You will see output similar to:

![Smart Edge Open Developer Experience Kit - dek uninstall Diagram](./images/dek-uninstall-diagram.png)

Figure 15: Uninstalled Successfully


If the uninstall operation fails, you will see output similar to: 

![Smart Edge Open Developer Experience Kit - dek uninstall fail Diagram](./images/dek-uninstall-failure.png)
   
Figure 16: Uninstall Failed

 
> **NOTE:** If you selected ESP option as "NO" (manual deployment), this uninstall/cleanup will FAIL, as the Intel® Smart Edge Open Developer Kit does not support uninstall/cleanup. Have to reflash the server with the Ubuntu 20.04 LTS OS as per the pre-requisites to continue.


### Summary and Next Steps

In this guide, you installed the Intel® Smart Edge Open Developer Experience Kit. 

*  If you completed the [Create the Installation Image](https://github.com/smart-edge-open/docs/blob/main/experience-kits/developer-experience-kit.md#create-the-installation-image) procedure, then you created an Intel® Smart Edge Open edge node cluster capable of hosting edge applications.
*  Learn how to [onboard a sample application to your cluster](https://github.com/smart-edge-open/docs/blob/main/application-onboarding/application-onboarding-cmdline.md).
*  Download reference implementations from the [Intel® Developer Catalog](https://www.intel.com/content/www/us/en/developer/tools/software-catalog/overview.html?s=Newest).


### Troubleshooting

#### Operating System (OS) Mismatch

Use only supported OS and version as mentioned in [System Requirements](#system-requirements). Otherwise, the error ``not supported`` is displayed.

#### Changing BIOS Settings

The Intel® SGX settings modification in BIOS doesn't work from iDRAC/BMC. You
must do this step from the BIOS console if you experience this issue. If you set
multiple different parameters, then you must reboot for each step.

#### Intel® SGX Enable Issues

In some servers, Intel® SGX may not enable even after following BIOS settings as in [Enable security suport in the BIOS](https://github.com/smart-edge-open/docs/blob/smart-edge-open-22-03/experience-kits/developer-experience-kit.md#optional-enable-security-support-in-the-bios)

You must reboot the setup after each setting done in BIOS.

- TPM Advanced Settings -> Memory Encryption -> Disabled (reboot)
- TPM Advanced Settings -> Memory Encryption -> Single Key (reboot)
- TPM Advanced Settings -> SGX & SGX factory reset -> On (reboot)
- TPM Advanced Settings -> PMMR -> 64GB (reboot)

#### SR-IOV Enabling

If SR-IOV is enabled in the config file, you must enable SR-IOV in BIOS globally
and on each NIC interface.


###	Support Forum

If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).

To attach the installation logs with your issue, execute the command below to
consolidate a list of the log files in tar.gz compressed format, e.g.,
``seo_dek.tar.gz``

```Shell.bash
tar -czvf seo_dek.tar.gz /var/log/esb-cli/Smart_Edge_Open_Developer_Experience_Kits_<version>/Smart_Edge_Open_Developer_Experience_Kits/
```

Where `<version>` is the package version downloaded.
