# Work Zone Analytics Reference Implementation
## Overview

Based on Intel® Edge Insights for Fleet (EIF) framework, the Work Zone Analytics Reference Implementation delivers DL models, computer vision algorithms, 
OpenVINO™ toolkit, Edge2Cloud connectivity, and other software dependencies.
The Work Zone Analytics Reference Implementation uses an IP camera which is mounted at the back of construction machinery. 
The camera is placed at road work zone and is connected to a Power over Ethernet (PoE) port of an in-vehicle Edge PC based on the Intel® Core™ processor or 
Intel Atom® processor. 
The models will detect people standing or walking behind the vehicle, and if an individual person is wearing required Personal Protective Equipment (PPE), 
which is a hard hat and a lighted vest.

Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/work_zone_analytics) to download the reference implementation and the software listed below.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/work_zone_analytics)

>**Legal Disclaimers**\
Recipient is solely responsible for compliance with all applicable regulatory standards and safety, privacy, and security related requirements concerning Recipient's use of the Intel hardware and software.\
Recipient is solely responsible for any and all integration tasks, functions, and performance in connection with use of the Intel hardware or software as part of a larger system. Intel does not have sufficient knowledge of any adjoining, connecting, or component parts used with or possibly impacted by the Intel hardware or software or information about operating conditions or operating environments in which the Intel hardware or software may be used by Recipient.  Intel bears no responsibility, liability, or fault for any integration issues associated with the inclusion of the Intel hardware or software into a system.  It is Recipient’s responsibility to design, manage, and assure safeguards to anticipate, monitor, and control component, system, quality, and or safety failures.

| Table 1 |  |
| ----------- | ----------- |
| Time to Complete | Approximately 60 minutes |
| Programming Language | Python* |
| Available Software | Intel® Distribution of OpenVINO™ toolkit 2020 Release |


**Recommended Hardware**

The below hardware is recommended for use with this reference implementation. See the [Recommended Hardware](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/hardware.html?s=Newest) page for other suggestions. 

-   [ADLINK MXE-5500 Series](https://www.adlinktech.com/Products/Industrial_PCs_Fanless_Embedded_PCs/IntegratedFanlessEmbeddedComputers/MXE-5500_Series?lang=en)

-   [NEXCOM VTC 7252-7C4IP](https://www.nexcomusa.com/Products/mobile-computing-solutions/in-vehicle-pc/security-vtc/in-vehicle-computer-vtc-vtc-7252-7c4ip)

## Target System Requirements

-   Ubuntu* 18.04.3 LTS

-   6th to 10th Generation Intel® Core™ processors with Intel® Iris® Plus graphics or Intel® HD Graphics

## How It Works

The reference implementation contains a full pipeline of analytics on video streams from a camera which is mounted at the back of construction machinery 
and is connected with an Intel® Core™ or Intel Atom® processor-based computer.
Pretrained models are used to detect people standing or walking behind the vehicle, and if an individual person is wearing required 
Personal Protective Equipment (PPE), which is a hard hat and a lighted vest.

This reference implementation contains a notification subsystem which includes a local dashboard, and a cloud dashboard.


<img src="docs/work-zone-analytics-ri-arch.png"/>

## Get Started

### Step 1: Install the Reference Implementation

Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/work_zone_analytics) to download the reference implementation and then follow the steps below to install it.

>**NOTE:** The images provided in the reference implementation are ONLY to be used
for validating the accuracy of detection events.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/work_zone_analytics)

>**NOTE:** If the host system already has Docker* images and containers,
you might encounter errors while building the reference implementation
packages. If you do encounter errors, refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document before starting the reference
implementation installation.

1. Open a new terminal, go to the downloaded folder and unzip the downloaded RI package.

`unzip work_zone_analytics.zip`

2. Go to the *work_zone_analytics/* directory.

`cd work_zone_analytics/`

3. Change permission of the executable *edgesoftware* file.

`chmod 755 edgesoftware`

4. Run the command below to install the Reference Implementation.

`./edgesoftware install`

5. During the installation, you will be prompted for the **Product Key**. The **Product Key** is contained in the email you received from Intel confirming your download.


<img src="docs/work-zone-analytics-ri-product-key.png"/>

6. When the installation is complete, you see the message "Installation of package complete" and the installation status for each module.

<img src="docs/work-zone-analytics-ri-install.png"/>

>**NOTE:** If you encounter any issues, please refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document. Installation failure logs will be
available at the path:
`/var/log/esb-cli/Work_Zone_Analytics_2022.1/output.log`

7. In order to start the application, you need to change the directory using the cd command printed at the end of the installation process:

`cd <INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.1/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase`

### Step 2: Run the Application

**Prerequisites**
- [Set Up ThingsBoard* Local Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/tutorials/set-up-thingsboard-local-cloud-data.html)
- [Set Up Amazon Web Services* Cloud Storage](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/tutorials/set-up-amazon-web-services-cloud-storage.html)

1. Run the application:

Copy and run the `make webui` command from the end of the installation log:

`make webui EII_BASE=<INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.1/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase`

For example:

`make webui EII_BASE=/home/intel/work_zone_analytics/Work_Zone_Analytics_2022.1/IEdgeInsights REPO_FOLDER=/home/intel/work_zone_analytics/Work_Zone_Analytics_2022.1/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase`

2. Open the Web UI: Go to **127.0.0.1:9096** on your web browser.

<img src="docs/work-zone-analytics-ri-open-webgui.png" />

3. If you installed your ThingsBoard Local Cloud Server and you have enabled S3 Bucket Server
on your AWS account, you can provide your configured **AWS Access Key ID**, **AWS Secret Access Key**,
**Thingsboard IP**, **Thingsboard Port** and **Thingsboard Device token** on **Cloud Data Configuration** tab.
After you complete the Cloud configuration, make sure you click on the **Save Credentials** and **Save Token** buttons.
Now you can import the ThingsBoard dashboard as described at the end of the [Set Up ThingsBoard* Local Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/tutorials/set-up-thingsboard-local-cloud-data.html)
to enable all dashboard features, including the cloud storage.

<img src="docs/work-zone-analytics-ri-aws.png" />

>**NOTE:** If you don't have an AWS account, you can still enable the ThingsBoard Cloud Data.

4. Access the Work Zone Analytics Dashboard with the following steps.

-   Go to sidebar and select **Run Use Case**.

<img src="docs/work-zone-analytics-ri-run-usecase.png" />

-   Configure the use case. Select video sample and the CPU or GPU device to run on it.
    >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

<img src="docs/work-zone-analytics-ri-dashboard.png" />

-   Click on the **Browse** button and search for video on the following path:
    `<INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.1/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase\config\VideoIngestion\test_videos`

-   After selecting the video sample, select the target CPU or GPU and click on **Run Use Case.**

-   The application will start the Visualizer App that will detect Personal Protective Equipment (PPE), which is a hard hat and a lighted vest as shown in the following image:
    >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

<img src="docs/work-zone-analytics-ri-visualizer.png"/>

5. After the visualizer starts, you can go to the ThingsBoard link and check the alerts sent by the
reference implementation. If you configured the AWS credentials, you will also have access to
video snapshots taken by the application on the video stream.

<img src="docs/work-zone-analytics-ri-tb-dashboard-with-data.png"/>

6. You can also check the cloud storage from the Reference Implementation **Storage** tab.
   >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

<img src="docs/work-zone-analytics-ri-aws-storage.png"/>


## Run in Parallel with Address Recognition and Analytics Reference Implementation

To run this task you will need to download and install [Address Recognition and Analytics](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/address_recognition_and_analytics) Reference Implementation.

### Prerequisites

-   Two terminals

-   Follow the steps to install [Address Recognition and Analytics](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/address_recognition_and_analytics.html#install) after installing [Work Zone Analytics](#step-1-install-the-reference-implementation)

### Steps to Run the Application

1.  Change directory to **Address Recognition and Analytics Use Case** path on terminal 1:

`cd <INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.1/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase`

<img src="docs/address-recognition-and-analytics-change-directory.png" />

2.  Change directory to **Work Zone Analytics Use Case** path on terminal 2:

`cd <INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.1/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase`

<img src="docs/address-recognition-and-analytics-change-directory2.png" />

3.  Run the following command on terminal 1 to start the webserver application.

Copy and run the `make webui` command from the end of the installation log:

`make webui EII_BASE=<INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.1/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase`

For example:

`make webui EII_BASE=/home/intel/work_zone_analytics/Work_Zone_Analytics_2022.1/IEdgeInsights REPO_FOLDER=/home/intel/address_recognition_and_analytics/Address_Recognition_And_Analytics_2022.1/Address_Recognition_And_Analytics/EII-AddressDetection-UseCase`


4.  Run the following command on terminal 2 to start the webserver application.

Copy and run the `make webui` command from the end of the installation log:

`make webui EII_BASE=<INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/work_zone_analytics/Work_Zone_Analytics_2022.1/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase`

For example:

`make webui EII_BASE=/home/intel/work_zone_analytics/Work_Zone_Analytics_2022.1/IEdgeInsights REPO_FOLDER=/home/intel/work_zone_analytics/Work_Zone_Analytics_2022.1/Work_Zone_Analytics/EII-WorkZoneDetection-UseCase`


<img src="docs/address-recognition-and-analytics-webserver-app.png" />

5.  Open your browser and go to **127.0.0.1:9097**.

6.  Configure Address Recognition and Analytics by setting the **video source**, the **target** and click on **Run Use Case**.

7.  Wait for Visualizer to get up and running.

8.  Open the Work Zone Analytics page by going to address **127.0.0.1:9096**.

9.  Configure all available cameras with the desired videos and set the target for each one (**CPU** or **GPU**) and click **Run Use Case**.
    >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

<img src="docs/address-recognition-and-analytics-configure-wza.png" />

At this point Address Recognition and Analytics will close and after that both use cases will start.
>**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

<img src="docs/address-recognition-and-analytics-two-use-cases.png" />

>**NOTE:** If you reinstall the first reference implementation, you must also reinstall the second one.

## Summary and Next Steps

This application successfully implements Intel® Distribution of OpenVINO™ toolkit plugins to
detect if an individual person is wearing required Personal Protective Equipment (PPE), which is a hard hat and a lighted vest.

Extend the reference implementation to:

- Detect other types of PPE, such as boots, with other DL models.  
- Add distance detection by adding calibration parameters and logic. 
- Support work zone manager alerts and notifications by extending the reference Cloud Dashboard.

## Learn More

To continue your learning, see the following guides and software resources:

-   [Intel® Distribution of OpenVINO™ toolkit documentation](http://docs.openvinotoolkit.org/2019_R3/index.html)

## Known Issues

### Uninstall Reference Implementation

If you uninstall one of the reference implementations, you need to reinstall
the other ones because the Docker images will be cleared.

## Troubleshooting

### Installation Failure

If the host system already has Docker images and its containers running, you will have issues during the RI installation.
You must stop/force stop existing containers and images.

-   To remove all stopped containers, dangling images, and unused networks:

`sudo docker system prune --volumes`

-   To stop Docker containers:

`sudo docker stop $(sudo docker ps -aq)`

-   To remove Docker containers:

`sudo docker rm $(sudo docker ps -aq)`

-   To remove all Docker images:

`sudo docker rmi -f $(sudo docker images -aq)`

### Docker Image Build Failure

If Docker image build on corporate network fails, follow the steps below.

1.  Get DNS server using the command:

`nmcli dev show | grep 'IP4.DNS'`

2.  Configure Docker to use the server. Paste the line below in the `/etc/docker/daemon.json` file:

`{ "dns": ["<dns-server-from-above-command>"]}`

3.  Restart Docker:

`sudo systemctl daemon-reload && sudo systemctl restart docker`

### Installation Failure Due to Ubuntu Timezone Setting

While building the reference implementation, if you see `/etc/timezone && apt-get install -y tzdata && ln -sf
/usr/share/zoneinfo/${HOST_TIME_ZONE} /etc/localtime && dpkg-reconfigure -f noninteractive tzdata' returned a non-zero code: 1 make: ***
[config] Error 1`

Run the following command in your terminal:

`sudo timedatectl set-local-rtc 0`

### Installation Encoding Issue

While building the reference implementation, if you see `ERROR: 'latin-1' codec can't encode character '\\u2615' in position 3: ordinal not in range(256)`

Run the following command in your terminal:

`export LANG=en_US.UTF-8`

### Can't Connect to Docker Daemon

If you can't connect to docker daemon at http+docker://localhost, run the following command in your terminal:

`sudo usermod -aG docker $USER`

Log out and log back in to Ubuntu.

Check before retrying to install if group docker is available for you by running the following command in a terminal:

`groups`

The output should contain “docker”.

### Support Forum
If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
