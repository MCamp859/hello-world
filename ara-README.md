# Address Recognition and Analytics Reference Implementation
## Overview

Based on Intel® Edge Insights for Fleet (EIF) framework, Address Recognition and
Analytics Reference Implementation delivers DL models, computer vision
algorithms, OpenVINO™ toolkit, Edge2Cloud connectivity, and other software
dependencies that will detect address plaques on the surfaces of buildings and
records the addresses on the plaques.

Select **Configure & Download** to download the reference implementation and the
software listed below.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/address_recognition_and_analytics)

>**NOTE:** This software package will not work on the People's Republic of China
>(PRC) network.

>**Legal Disclaimers**\
Recipient is solely responsible for compliance with all applicable regulatory standards and safety, privacy, and security related requirements concerning Recipient's use of the Intel hardware and software.\
Recipient is solely responsible for any and all integration tasks, functions, and performance in connection with use of the Intel hardware or software as part of a larger system. Intel does not have sufficient knowledge of any adjoining, connecting, or component parts used with or possibly impacted by the Intel hardware or software or information about operating conditions or operating environments in which the Intel hardware or software may be used by Recipient.  Intel bears no responsibility, liability, or fault for any integration issues associated with the inclusion of the Intel hardware or software into a system.  It is Recipient’s responsibility to design, manage, and assure safeguards to anticipate, monitor, and control component, system, quality, and or safety failures.


-   **Time to Complete:**  Approximately 60 minutes
-   **Programming Language:**  Python*
-   **Available Software:**  Intel® Distribution of OpenVINO™ toolkit 2021.4.2 Release


### Recommended Hardware

The below hardware is recommended for use with this reference implementation.
For other suggestions, see [Recommended
Hardware](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/hardware.html?s=Newest).

-   [ADLINK MXE-5500 Series](https://www.adlinktech.com/Products/Industrial_PCs_Fanless_Embedded_PCs/IntegratedFanlessEmbeddedComputers/MXE-5500_Series?lang=en)

-   [NEXCOM VTC 7252-7C4IP](https://www.nexcomusa.com/Products/mobile-computing-solutions/in-vehicle-pc/security-vtc/in-vehicle-computer-vtc-vtc-7252-7c4ip)

## Target System Requirements

-   Ubuntu* 20.04 LTS

-   6th to 10th Generation Intel® Core™ processors with Intel® Iris® Plus
    graphics or Intel® HD Graphics

## How It Works

The reference implementation contains a full pipeline of analytics on video
streams from a camera that is mounted on the side of a last mile delivery
vehicle. The camera is connected to an in-vehicle Edge PC based on the Intel®
Core™ processor or Intel Atom® processor. When the vehicle stops, it detects
address plaques on the surfaces of buildings and records the addresses on the
plaques.

This reference implementation contains a notification subsystem which includes a
cloud dashboard and a cloud storage.

![The architecture is represented by a complex block diagram.](docs/address-recognition-and-analytics-ri-arch.png)

Figure 1: Architecture Diagram

## Get Started

### Step 1: Install the Reference Implementation

Select **Configure & Download** to download the reference implementation and
then follow the steps below to install it.

>**NOTE:** The images provided in the reference implementation are ONLY to be used
for validating the accuracy of detection events.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/address_recognition_and_analytics)

>**NOTE:** If the host system already has Docker* images and containers,
you might encounter errors while building the reference implementation
packages. If you do encounter errors, refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document before starting the reference
implementation installation.

1. Open a new terminal, go to the downloaded folder and unzip the downloaded RI package.

    ```bash
    unzip address_recognition_and_analytics.zip
    ```

2. Go to the `address_recognition_and_analytics.zip/` directory.

    ```bash
    cd address_recognition_and_analytics.zip/
    ```

3. Change permission of the executable `edgesoftware` file.

    ```bash
    chmod 755 edgesoftware
    ```

4. Run the command below to install the Reference Implementation.

    ```bash
    ./edgesoftware install
    ```

5. During the installation, you will be prompted for the **Product Key**. The
   **Product Key** is contained in the email you received from Intel confirming
   your download.

    ![A console window showing a system prompt to enter the product key.](docs/address-recognition-and-analytics-recognition-ri-product-key.png)

    Figure 2: Product Key

6. When the installation is complete, you see the message "Installation of
   package complete" and the installation status for each module.

    ![A console window showing system output during the install process. At the end of the process, the system displays the message “Installation of package complete” and the installation status for each module. ](docs/address-recognition-and-analytics-recognition-ri-install.png)

   Figure 3: Installation Success

    >**NOTE:** If you encounter any issues, please refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document. Installation failure logs will be
available at the path:
`/var/log/esb-cli/Address_Recognition_And_Analytics_2022.2/output.log`

7. To start the application, you need to change the directory using the cd
   command printed at the end of the installation process:

    ```bash
    cd <INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.2/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase
    ```

### Step 2: Run the Application

#### Prerequisites

- [Set Up ThingsBoard* Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-thingsboard-cloud-data.html)
- [Set Up Amazon Web Services* Cloud Storage](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-amazon-web-services-cloud-storage.html)

1. Run the application. Copy and run the `make webui` command from the end of
   the installation log:

    ```bash
    make webui EII_BASE=<INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_<version>/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_<version>/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase
    ```

   For example:

    ```bash
   make webui EII_BASE=/home/intel/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.2/IEdgeInsights REPO_FOLDER=/home/intel/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.2/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase
    ```

2. Open the Web UI: Go to **127.0.0.1:9097** on your web browser.

    ![A browser window showing the reference implementation dashboard.](docs/address-recognition-and-analytics-recognition-ri-open-webgui.png)

    Figure 4: Reference Implementation Dashboard

3. If you installed your ThingsBoard Cloud Server and you have enabled S3 Bucket
   Server on your AWS account, you can provide your configured **AWS Access Key
   ID**, **AWS Secret Access Key**, **Thingsboard IP**, **Thingsboard Port** and
   **Thingsboard Device token** on the **Cloud Data Configuration** tab.

   After you complete the Cloud configuration, make sure you click on the **Save
   Credentials** and **Save Token** buttons. Now you can import the ThingsBoard
   dashboard as described at the end of the [Set Up ThingsBoard* Cloud
   Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-thingsboard-cloud-data.html)
   to enable all dashboard features, including the cloud storage.

    ![A web app dashboard showing the Configuration tab. Certain fields are
   covered with a blue bar for security](docs/address-recognition-and-analytics-recognition-ri-aws.png)

   Figure 5: Configuration Tab Contents


   > **NOTE:** If you don't have an AWS account, you will not be able to access Storage Cloud. You can still enable the ThingsBoard Cloud Data if you configured it locally or on another machine.

4. Access the Address Recognition and Analytics Dashboard with the following steps.

      -   Go to sidebar and select **Run Use Case**.

         ![A web app dashboard showing the Run Use Case tab.](docs/address-recognition-and-analytics-recognition-ri-run-usecase.png)

         Figure 6: Select Run Use Case Tab

      -   Configure the use case by selecting the video sample and the device for the UDF model.
      -   Enter a target address value (for example, 30) to generate the target address reached alert.
      -   Optionally, you can also set the simulation data that you want to use. You
      can choose between using the [KnowGo
      Simulator](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-know-go-simulator.html)
      or simply use the CSV pre-recorded simulation data.

         **Model Description**

      -   **Address Detection:** This model detects the numbers on an address plaque.
      -   **Address Recognition:** This model recognizes the target address and sends an alert when the address number is reached.

         >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

         ![A web app dashboard showing the Dashboard.](docs/address-recognition-and-analytics-recognition-ri-dashboard.png)

         Figure 7: Configure Use Case


      -   Click on the **Browse** button and search for video on the following path:
      `<INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.2/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase/config/VideoIngestion/test_videos/`

      -   After selecting the video sample, select the target device for all models. Options include CPU or GPU. Click on **Run Use Case.**

            >**NOTE:** To use a GPU device, you must set the proper group for the device with the command:
            >
            > `sudo chown root:video /dev/dri/renderD128`

      -   The application will start the Visualizer App that will detect address plaques on the surfaces of buildings:
         >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

         ![A web app dashboard showing output from the visualizer.](docs/address-recognition-and-analytics-recognition-ri-visualizer.png)

         Figure 8: Visualizer Output


5. After the visualizer starts, you can go to the ThingsBoard link and check the
   alerts sent by the reference implementation. If you configured the AWS
   credentials, you will also have access to video snapshots taken by the
   application on the video stream.

    ![A browser window showing the ThingsBoard link with the Intel Fleet Manager dashboard in the main view. Several components are displayed, including Alerts, Temperature, and a map showing the vehicle location.](docs/address-recognition-and-analytics-recognition-ri-tb-dashboard-with-data.png)

    Figure 9: Intel Fleet Manager Dashboard shown in ThingsBoard


6. You can also check the cloud storage from the Reference Implementation **Storage** tab.
   >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

    ![A web app dashboard showing the Storage tab.](docs/address-recognition-and-analytics-recognition-ri-aws-storage.png)

    Figure 10: Reference Implementation Storage Tab


## Run in Parallel with Work Zone Analytics Reference Implementation

To run this task you will need to download and install [Work Zone Analytics](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/work_zone_analytics) Reference Implementation.

### Prerequisites

-   Two terminals

-   Follow the steps to install [Work Zone Analytics](https://www.intel.com/content/www/us/en/developer/articles/reference-implementation/work-zone-analytics.html ) after installing [Address Recognition and Analytics](#step-1-install-the-reference-implementation)

### Steps to Run the Application

1.  Change directory to **Work Zone Analytics Use Case** path on terminal 1:

    ```bash
    cd <INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.2/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase
    ```

    ![A window showing 2 system consoles in side-by-side view.](docs/address-recognition-and-analytics-change-directory.png)

    Figure 11: Set Up System Console Windows


2.  Change directory to **Address Recognition and Analytics** path on terminal 2:

    ```bash
    cd <INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.2/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase
    ```

    ![A window showing 2 system consoles. Each console is displaying a different directory.](docs/address-recognition-and-analytics-change-directory2.png)

    Figure 12: System Console Windows Displaying Different Directories

3.  Run the following command on terminal 1 to start the webserver application.

    Copy and run the `make webui` command from the end of the installation log:

    ```bash
    make webui EII_BASE=<INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_<version>/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_<version>/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase
    ```

    For example:

    ```bash
    make webui EII_BASE=<INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.2/IEdgeInsights REPO_FOLDER=/home/intel/work_zone_analytics/Work_Zone_Analytics_2022.2/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase
    ```


4.  Run the following command on terminal 2 to start the webserver application.

    Copy and run the `make webui` command from the end of the installation log:

    ```bash
    make webui EII_BASE=<INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_<version>/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_<version>/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase
    ```

    For example:

    ```bash
    make webui EII_BASE=/home/intel/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.2/IEdgeInsights REPO_FOLDER=/home/intel/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.2/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase
    ```

    ![A window showing 2 system consoles. Each console is running a different application.](docs/address-recognition-and-analytics-webserver-app.png)

    Figure 13: System Console Windows Running Different Applications

5.  Open your browser and go to **127.0.0.1:9096**.

6.  Configure Work Zone Analytics by setting the **video source** and the **target**. Click on **Run Use Case**.

7.  Wait for Visualizer to get up and running.

8.  Open the Address Recognition and Analytics page by going to address **127.0.0.1:9097**.

9.  Configure all available cameras with the desired videos and set the target
    for each model. Options include **CPU** or **GPU**. Click **Run Use Case**.
    >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

    ![A browser window showing 2 application dashboards in a side-by-side view.](docs/address-recognition-and-analytics-configure-wza.png)

    Figure 14: Set Up Reference Implementation Dashboards

At this point Work Zone Analytics will close and after that both use cases will start.
>**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

![A browser window showing output of 2 visualizers in a side-by-side view.](docs/address-recognition-and-analytics-two-use-cases.png)

Figure 15: Visualizer Output for 2 Reference Implementations


>**NOTE:** If you reinstall the first reference implementation, you must also reinstall the second one.

## Summary and Next Steps

On a last-mile delivery van, a camera is mounted on the side of the vehicle. The
camera is connected to an in-vehicle Edge PC based on the Intel® Core™ processor
or Intel Atom® processor. When the vehicle stops, it detects address plaques on
the surfaces of buildings and records the addresses on the plaques.

As a next step, extend the reference implementation to:

-   Collate the address plaque detection outputs with the navigation SW result to detect driver or mapping errors.
-   Provide reports and evidence to delivery fleet managers to review if there are package delivery issues.

## Learn More

To continue your learning, see the following guides and software resources:

-   For additional reference implementations, visit [Edge Insights for Fleet](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/fleet-recipes.html?s=Newest).
-   [Intel® Distribution of OpenVINO™ toolkit documentation](http://docs.openvinotoolkit.org/2019_R3/index.html)

## Known Issues

### Uninstall Reference Implementation

If you uninstall one of the reference implementations, you need to reinstall
the other ones because the Docker images will be cleared.

## Troubleshooting

### Installation Failure

If the host system already has Docker images and its containers running, you
will have issues during the RI installation. You must stop/force stop existing
containers and images.

-  To remove all stopped containers, dangling images, and unused networks:

    ```bash
    sudo docker system prune --volumes
    ```

-  To stop Docker containers:

    ```bash
    sudo docker stop $(sudo docker ps -aq)
    ```

-  To remove Docker containers:

    ```bash
    sudo docker rm $(sudo docker ps -aq)
    ```

-  To remove all Docker images:

    ```bash
    sudo docker rmi -f $(sudo docker images -aq)
    ```


### Docker Image Build Failure

If Docker image build on corporate network fails, follow the steps below.

1.  Get DNS server using the command:

    ```bash
    nmcli dev show | grep 'IP4.DNS'
    ```

2.  Configure Docker to use the server. Paste the line below in the `/etc/docker/daemon.json` file:

    ```bash
    { "dns": ["<dns-server-from-above-command>"]}
    ```

3.  Restart Docker:

    ```bash
    sudo systemctl daemon-reload && sudo systemctl restart docker
    ```

### Installation Failure Due to Ubuntu Timezone Setting

While building the reference implementation, if you see: `/etc/timezone &&
apt-get install -y tzdata && ln -sf /usr/share/zoneinfo/${HOST_TIME_ZONE}
/etc/localtime && dpkg-reconfigure -f noninteractive tzdata' returned a non-zero
code: 1 make: *** [config] Error 1`


Run the following command in your terminal:

```bash
sudo timedatectl set-local-rtc 0
```

### Installation Encoding Issue

While building the reference implementation, if you see: `ERROR: 'latin-1' codec
can't encode character '\\u2615' in position 3: ordinal not in range(256)`

Run the following command in your terminal:

```bash
export LANG=en_US.UTF-8
```

### Can't Connect to Docker Daemon

If you can't connect to docker daemon at http+docker://localhost, run the
following command in your terminal:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in to Ubuntu.

Check before retrying to install if group docker is available for you by running
the following command in a terminal:

```bash
groups
```

The output should contain “docker”.

### Support Forum
If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
