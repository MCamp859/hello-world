# Public Transit Analytics Reference Implementation
## Overview

Public Transit Analytics (PTA) reference implementation delivers deep
learning models, computer vision algorithms, OpenVINO and other software
dependencies on the Edge Insights for Fleet middleware architecture.
Video streams from cameras in a bus passenger area are analyzed to extract
passenger count, and if a passenger is wearing face masks.
The results are available for the bus driver, and the bus fleet operators via
a cloud dashboard.


Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/public_transit_analytics) to download the reference implementation and the software listed below.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/public_transit_analytics)

<img src="docs/public-transit-analytics-ri-landing.png"/>

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


The reference implementation contains a full pipeline of analytics on video streams from
IP cameras mounted inside a bus in the passenger area with an Intel
Core or Atom processor-based computer onboard the bus.
Pretrained models are used to inference and calculate the number
of passengers.

This reference implementation contains a notification subsystem which includes a local
dashboard for the bus driver, and a cloud dashboard for the bus operator and fleet manager


<img src="docs/public-transit-analytics-ri-architecture.png"/>

## Get Started

### Step 1: Install the Reference Implementation

Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/public_transit_analytics) to download the reference implementation and then follow the steps below to install it.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/public_transit_analytics)

>**NOTE:** If the host system already has Docker* images and containers,
you might encounter errors while building the reference implementation
packages. If you do encounter errors, refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document before starting the reference
implementation installation.

1. Open a new terminal, go to the downloaded folder and unzip the downloaded RI package.

`public_transit_analytics.zip`

2. Go to the *public_transit_analytics/* directory.

`cd public_transit_analytics/`

3. Change permission of the executable *edgesoftware* file.

`chmod 755 edgesoftware`

4. Run the command below to install the Reference Implementation.

`./edgesoftware install`

5. During the installation, you will be prompted for the **Product Key**. The **Product Key** is contained in the email you received from Intel confirming your download.


<img src="docs/public-transit-analytics-ri-product-key.png"/>

6. When the installation is complete, you see the message "Installation of package complete" and the installation status for each module.

<img src="docs/public-transit-analytics-ri-install.png"/>

>**NOTE:** If you encounter any issues, please refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document. Installation failure logs will be
available at the path:
`/var/log/esb-cli/Public_Transit_Analytics_2021.1/output.log`

7. In order to start the application, you need to change the directory using the cd command printed at the end of the installation process:

`cd <INSTALL_PATH>/public_transit_analytics/Public_Transit_Analytics_2021.1/Public_Transit_Analytics/EII-PassengerCounting-UseCase`

### Step 2: Run the Application

**Pre-requisites**
- [Install Thingsboard Local Cloud dashboard](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top.html)
- [Prepare AWS S3 bucket server](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top.html)

1. Run the application:

        Please copy and run the "make webui" command from the end of the installation:

`make webui EII_BASE=<INSTALL_PATH>/public_transit_analytics/Public_Transit_Analytics_2021.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/public_transit_analytics/Public_Transit_Analytics_2021.1/Public_Transit_Analytics/EII-PassengerCounting-UseCase`

`Eg. make webui EII_BASE=/home/intel/public_transit_analytics/Public_Transit_Analytics_2021.1/IEdgeInsights REPO_FOLDER=/home/intel/public_transit_analytics/Public_Transit_Analytics_2021.1/Public_Transit_Analytics/EII-PassengerCounting-UseCase`

2. Open the Web UI: Go to **127.0.0.1:9094** on your web browser.

<img src="docs/public-transit-analytics-ri-open-webgui.png" />

3. If you installed your Thingsboard Local Cloud Server and you have enabled S3 Bucket Server
on your AWS account you can provide your configured **AWS Access Key ID**, **AWS Secret Access Key**,
**Thingsboard IP**, **Thingsboard Port** and **Thingsboard Device token on Cloud Data Configuration tab**
After you completed the Cloud configuration make sure you click on Save Credentials and Save Token buttons.
Now you can import the Thingsboard dashboard as described at the end of the [Thingsboard setup](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top.html)
to enable all dashboard features which include the cloud storage.

<img src="docs/public-transit-analytics-ri-aws.png" />

>**NOTE:** If you don't have an AWS account you can still enable the Thingsboard Cloud Data

4. Access the Public Transit Analytics Dashboard with the following steps.

-   Go to sidebar and select **Run Use Case**.
<img src="docs/public-transit-analytics-ri-run-usecase.png" />

-   Configure the use case. Select video sample and the CPU or GPU device to run on it.
<img src="docs/public-transit-analytics-ri-dashboard.png" />

-   Click on the **Browse** button and search for one of the sample videos delivered with the application at the following path:
    `<INSTALL_PATH>/public_transit_analytics/Public_Transit_Analytics_2021.1/Public_Transit_Analytics/EII-PassengerCounting-UseCase/config/VideoIngestion/test_videos/`
    and select one of the two available.
<img src="docs/public-transit-analytics-ri-test-video.png" />

-   After selecting the video sample, select the target CPU or GPU and click on **Run Use Case.**

-   The application will start the Visualizer App that will detect yawns, blinks, drowsiness and distraction status as in the following image:
<img src="docs/public-transit-analytics-ri-visualizer.png"/>

5. After the visualiser started you can go to Thingsboard Link and check the alerts sent by the
reference implementation. If you configured the AWS credentials you will have access also to
pictures taken by the application on the video stream
<img src="docs/public-transit-analytics-ri-tb-dashboard-with-data.png"/>

6. You can also check the cloud storage from the Reference Implementation Storage tab
<img src="docs/public-transit-analytics-ri-aws-storage.png"/>


## Run in Parallel with Automated License Plate Recognition Reference Implementation

To run this task you will need to download and install [Automated License Plate Recognition](https://www.intel.com/content/www/us/en/developer/articles/reference-implementation/public-transit-analitics.html) Reference Implementation.

### Pre-requisites

-   Two terminals

-   Follow the steps to install [Automated License Plate Recognition](https://www.intel.com/content/www/us/en/develop/articles/automated-license-plate-recognition.html#install) after installing [Public Transit Analytics](#step-1-install-the-reference-implementation)

### Steps to Run the Application

1.  Change directory to **Public Transit Analytics Use Case** path on terminal 1:

`cd <INSTALL_PATH>/public_transit_analytics/Public_Transit_Analytics_2021.1/Public_Transit_Analytics/EII-PassengerCounting-UseCase`

<img src="docs/public-transit-analytics-change-directory.png" />

2.  Change directory to **Automated License Plate Recognition Use Case** path on terminal 2:

`cd <INSTALL_PATH>/automated_license_plate_recognition/Automated_License_Plate_Recognition_2021.1/Automated_License_Plate_Recognition/EII-LicensePlateRecognition-UseCase`

<img src="docs/public-transit-analytics-change-directory2.png" />

3.  Run the following common on terminal 1 to start the webserver application:

    Please copy and run the "make webui" command from the end of the installation:

`make webui EII_BASE=<INSTALL_PATH>/public_transit_analytics/Public_Transit_Analytics_2021.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/public_transit_analytics/Public_Transit_Analytics_2021.1/Public_Transit_Analytics/EII-PassengerCounting-UseCase`

4.  Run the following command on terminal 2 to start the webserver application:

    Please copy and run the "make webui" command from the end of the installation:

`make webui EII_BASE=<INSTALL_PATH>/public_transit_analytics/Public_Transit_Analytics_2021.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/automated_license_plate_recognition/Automated_License_Plate_Recognition_2021.1/Automated_License_Plate_Recognition/EII-LicensePlateRecognition-UseCase`

<img src="docs/public-transit-analytics-webserver-app.png" />

5.  Open your browser and go to **127.0.0.1:9094**.

6.  Configure Public Transit Analytics by setting the **video source**, the **target** and click on **Run Use Case**.

7.  Wait for Visualizer to get up and running.

8.  Open the Automated License Plate Recognition page by going to address **127.0.0.1:9095**.

9.  Configure all available cameras with the desired videos and set the target for each one (**CPU** or **GPU**) and click **Run Use Case**.

<img src="docs/public-transit-analytics-configure-alpr.png" />

At this point Public Transit Analytics will close and after that both use cases will start.

<img src="docs/public-transit-analytics-two-use-cases.png" />

>NOTE: If you reinstall the first RI, you must reinstall the second one.

## Summary and Next Steps

This application successfully implements Intel® Distribution of OpenVINO™ toolkit plugins to
calculate the number of passengers.


As a next step, try the following:

It can be extended further to provide support for feed from network stream (RTSP camera),
and the algorithm can be optimized for better performance.

## Learn More

To continue your learning, see the following guides and software resources:

-   [Intel® Distribution of OpenVINO™ toolkit documentation](http://docs.openvinotoolkit.org/2019_R3/index.html)

## Known Issues

### Uninstall use case known issue

If you uninstall one of the use cases, you need to reinstall the other ones because the Docker images will be cleared.

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

Check before retry to install if group docker is available for your user:

In a terminal, run the following command:
`groups`

The output should contain “docker”.

### Support Forum
If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
