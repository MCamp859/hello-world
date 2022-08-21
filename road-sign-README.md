# Road Sign Detection and Classification Reference Implementation
## Overview

The Road Sign Detection Reference Implementation monitors the exterior of a
vehicle and send alerts to Cloud Dashboard. It uses a camera placed in the front
of the vehicle facing forward to detect and recognize traffic signs while
driving. The OpenVINO™ Semantic Segmentation model is able to detect and
classify the traffic signs, and the Signs Recognition model is also implemented
for this Use Case, allowing the vehicle to recognize different traffic signs
placed on the road, such as speed limits, no entry, turn left or right ahead,
road work, pedestrians, children crossing, no passing of heavy vehicles, etc.


Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/road_sign_detection_and_classification) to download the reference implementation and the software listed below.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/road_sign_detection_and_classification)

>**Legal Disclaimers**\
Recipient is solely responsible for compliance with all applicable regulatory standards and safety, privacy, and security related requirements concerning Recipient's use of the Intel hardware and software.\
Recipient is solely responsible for any and all integration tasks, functions, and performance in connection with use of the Intel hardware or software as part of a larger system. Intel does not have sufficient knowledge of any adjoining, connecting, or component parts used with or possibly impacted by the Intel hardware or software or information about operating conditions or operating environments in which the Intel hardware or software may be used by Recipient.  Intel bears no responsibility, liability, or fault for any integration issues associated with the inclusion of the Intel hardware or software into a system.  It is Recipient’s responsibility to design, manage, and assure safeguards to anticipate, monitor, and control component, system, quality, and or safety failures.


-  **Time to Complete:** Approximately 60 minutes
-  **Programming Language:** Python*
-  **Available Software:** Intel® Distribution of OpenVINO™ toolkit 2021.4.2 Release



### Recommended Hardware

The below hardware is recommended for use with this reference implementation. See the [Recommended Hardware](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/hardware.html?s=Newest) page for other suggestions. 

-   [ADLINK MXE-5500 Series](https://www.adlinktech.com/Products/Industrial_PCs_Fanless_Embedded_PCs/IntegratedFanlessEmbeddedComputers/MXE-5500_Series?lang=en)

-   [NEXCOM VTC 7252-7C4IP](https://www.nexcomusa.com/Products/mobile-computing-solutions/in-vehicle-pc/security-vtc/in-vehicle-computer-vtc-vtc-7252-7c4ip)

## Target System Requirements

-   Ubuntu* 20.04 LTS

-   6th to 10th Generation Intel® Core™ processors with Intel® Iris® Plus graphics or Intel® HD Graphics

## How It Works


The reference implementation contains a full pipeline of analytics on video
streams from IP cameras mounted inside a car area with a front angle and a
computer using an Intel® Core™ processor or an Intel Atom® processor onboard the
bus. Pretrained models are used to inference, detect and classify road signs.

This reference implementation contains a notification subsystem which includes a cloud
dashboard and a cloud storage for the bus operator and fleet manager.


![The architecture is represented by a complex block diagram.](docs/road-sign-detection-and-classification-ri-architecture.png)

Figure 1: Architecture Diagram

## Get Started

### Step 1: Install the Reference Implementation

Select [Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/road_sign_detection_and_classification) to download the reference implementation and then follow the steps below to install it.

>**NOTE:** The images provided in the reference implementation are ONLY to be used
for validating the accuracy of detection events.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/road_sign_detection_and_classification)

>**NOTE:** If the host system already has Docker* images and containers,
you might encounter errors while building the reference implementation
packages. If you do encounter errors, refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document before starting the reference
implementation installation.

1. Open a new terminal, go to the downloaded folder and unzip the downloaded RI package.

   ```bash
   unzip road_sign_detection_and_classification.zip
   ```

2. Go to the `road_sign_detection_and_classification/` directory.

   ```bash
   cd road_sign_detection_and_classification/
   ```

3. Change permission of the executable *edgesoftware* file.

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

   ![A console window showing a system prompt to enter the product key.](docs/road-sign-detection-and-classification-ri-product-key.png)

   Figure 2: Product Key

6. When the installation is complete, you see the message "Installation of
   package complete" and the installation status for each module.

   ![A console window showing system output during the install process. At the end of the process, the system displays the message “Installation of package complete” and the installation status for each module. ](docs/road-sign-detection-and-classification-ri-install.png)

   Figure 3: Installation Success


   >**NOTE:** If you encounter any issues, please refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document. Installation failure logs will be
available at the path:
`/var/log/esb-cli/Road_Sign_Detection_and_Classification_2022.1/output.log`

7. In order to start the application, you need to change the directory using the
   cd command printed at the end of the installation process:

   ```bash
   cd <INSTALL_PATH>/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/Road_Sign_Detection_and_Classification/EII-RoadSignDetection-UseCase
   ```

### Step 2: Run the Application

#### Prerequisites

- [Set Up ThingsBoard* Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-thingsboard-cloud-data.html)
- [Set Up Amazon Web Services* Cloud Storage](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-amazon-web-services-cloud-storage.html)

1. Run the application. Copy and run the `make webui` command from the end of the installation:

   ```bash
   make webui EII_BASE=<INSTALL_PATH>/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/Road_Sign_Detection_and_Classification/EII-RoadSignDetection-UseCase
   ```

   For example:

   ```bash
   make webui EII_BASE=/home/intel/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/IEdgeInsights REPO_FOLDER=/home/intel/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/Road_Sign_Detection_and_Classification/EII-RoadSignDetection-UseCase
   ```

2. Open the Web UI: Go to **127.0.0.1:9098** on your web browser.

   ![A browser window showing the reference implementation dashboard.](docs/road-sign-detection-and-classification-ri-open-webgui.png)

   Figure 4: Reference Implementation Dashboard

3. If you installed your ThingsBoard Cloud Server and you have enabled S3 Bucket Server
on your AWS account, you can provide your configured **AWS Access Key ID**, **AWS Secret Access Key**,
**Thingsboard IP**, **Thingsboard Port** and **Thingsboard Device token** on the **Cloud Data Configuration** tab.
After you completed the Cloud configuration, make sure you click on **Save Credentials** and **Save Token** buttons.
Now you can import the ThingsBoard dashboard as described at the end of the [Set Up ThingsBoard* Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-thingsboard-cloud-data.html)
to enable all dashboard features, including the cloud storage.

   ![A web app dashboard showing the Configuration tab. Certain fields are
   covered with a blue bar for security](docs/road-sign-detection-and-classification-ri-aws.png)

   Figure 5: Configuration Tab Contents

   > **NOTE:** If you don't have an AWS account you will not be able to access Storage Cloud. You can still enable the Thingsboard Cloud Data if you configured it locally or on another machine.

4. Access the Road Sign Detection and Classification Dashboard with the following steps.

   -  Go to sidebar and select **Run Use Case**.

      ![A web app dashboard showing the Run Use Case tab.](docs/road-sign-detection-and-classification-ri-run-usecase.png)

      Figure 6: Select Run Use Case Tab

   -  Configure the use case by selecting the video sample and the CPU or GPU
      device for the inference model to run on it.

      **Model Description**

      **Semantic Segmentation:** The OpenVINO™ Semantic Segmentation model
         detects and classifies the traffic signs.

      **Sign Recognition:** The OpenVINO™ Signs Recognition model recognizes
          different traffic signs placed on the road, such as speed limits, no
          entry, turn left or right ahead, road work, pedestrians, children
          crossing, no passing of heavy vehicles, etc.


      ![A web app dashboard showing the Dashboard.](docs/road-sign-detection-and-classification-ri-dashboard.png)

      Figure 7: Configure Use Case

   -  Click on the **Browse** button and search for the sample video delivered with the application at the following path:
    `<INSTALL_PATH>/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/Road_Sign_Detection_and_Classification/EII-RoadSignDetection-UseCase/config/VideoIngestion/test_videos/`
    and select the one available.

      >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

      ![A web app dashboard showing the sample video to be uploaded.](docs/road-sign-detection-and-classification-ri-test-video.png)

      Figure 8: Select Sample Video

   -  After selecting the video sample, select the device for the inference model. Options include CPU or GPU. Click on **Run Use Case.**

   -  The application will start the Visualizer App that will detect yawns, blinks, drowsiness and distraction status as in the following image:

      >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.


      ![A web app showing output from the visualizer.](docs/road-sign-detection-and-classification-ri-visualizer.png)

      Figure 9: Visualizer Output

5. After the visualizer starts, you can go to the ThingsBoard link and check the alerts sent by the
reference implementation. If you configured the AWS credentials, you will also have access to
pictures taken by the application on the video stream.

   ![A browser window showing the ThingsBoard link with the Intel Fleet Manager dashboard in the main view. Several components are displayed, including Alerts, Temperature, and a map showing the vehicle location.](docs/road-sign-detection-and-classification-ri-tb-dashboard-with-data.png)

   Figure 10: Intel Fleet Manager Dashboard shown in ThingsBoard

6. You can also check the cloud storage from the Reference Implementation **Storage** tab.

    >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

   ![A web app dashboard showing the Storage tab.](docs/road-sign-detection-and-classification-ri-aws-storage.png)

   Figure 11: Reference Implementation Storage Tab


## Run in Parallel with Driver Action Recognition Reference Implementation

To run this task you will need to download and install [Driver Action Recognition](https://www.intel.com/content/www/us/en/developer/articles/reference-implementation/road-sign-detection-and-classification.html) Reference Implementation.

### Prerequisites

-   Two terminals

-   Follow the steps to install [Driver Action Recognition](https://www.intel.com/content/www/us/en/develop/articles/driver-action-recognition.html#install) after installing [Road Sign Detection and Classification](#step-1-install-the-reference-implementation)

### Steps to Run the Application

1. Change directory to **Road Sign Detection and Classification Use Case** path on terminal 1:

   ```bash
   cd <INSTALL_PATH>/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/Road_Sign_Detection_and_Classification/EII-RoadSignDetection-UseCase
   ```

   ![A window showing 2 system consoles in side-by-side view.](docs/driver-action-recognition-change-directory.png)

   Figure 12: Set Up System Console Windows

2. Change directory to **Driver Action Recognition Use Case** path on terminal 2:

   ```bash
   cd <INSTALL_PATH>/driver_action_recognition/Driver_Action_Recognition_2022.1/Driver_Action_Recognition/EII-DriverActionRecognition-UseCase
   ```

   ![A window showing 2 system consoles. Each console is displaying a different directory.](docs/driver-action-recognition-change-directory2.png)

   Figure 13: System Console Windows Displaying Different Directories

3. Run the following command on terminal 1 to start the webserver application.
   Copy and run the `make webui` command from the end of the installation:

   ```bash
   make webui EII_BASE=<INSTALL_PATH>/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/Road_Sign_Detection_and_Classification/EII-RoadSignDetection-UseCase
   ```

4. Run the following command on terminal 2 to start the webserver application.
   Copy and run the `make webui` command from the end of the installation:

   ```bash
   make webui EII_BASE=<INSTALL_PATH>/road_sign_detection_and_classification/Road_Sign_Detection_and_Classification_2022.1/IEdgeInsights REPO_FOLDER=<INSTALL_PATH>/driver_action_recognition/Driver_Action_Recognition_2022.1/Driver_Action_Recognition/EII-DriverActionRecognition-UseCase
   ```

   ![A window showing 2 system consoles. Each console is running a different application.](docs/driver-action-recognition-webserver-app.png)

   Figure 14: System Console Windows Running Different Applications

5. Open your browser and go to **127.0.0.1:9098**.

6. Configure Road Sign Detection and Classification by setting the **video
   source**, the **target** and click on **Run Use Case**.

7. Wait for the Visualizer to get up and running.

8. Open the Driver Action Recognition page by going to address **127.0.0.1:9099**.

9. Configure all available cameras with the desired videos and set the target for each one (**CPU** or **GPU**) and click **Run Use Case**.

   >**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

   ![A browser window showing 2 application dashboards in a side-by-side view.](docs/driver-action-recognition-configure-rsdc.png)

   Figure 15: Set Up Reference Implementation Dashboards

At this point, Road Sign Detection and Classification will close and after that both use cases will start.
>**NOTE:** These images are ONLY to be used for validating the accuracy of detection events.

![A browser window showing output of 2 visualizers in a side-by-side view.](docs/driver-action-recognition-two-use-cases.png)

Figure 16: Visualizer Output for 2 Reference Implementations

>**NOTE:** If you reinstall the first RI, you must reinstall the second one.

## Summary and Next Steps

This application successfully implements Intel® Distribution of OpenVINO™ toolkit plugins to
detect and classify road signs.


As a next step, try the following:

Extend the RI further to provide support for feed from network stream (RTSP camera),
and the algorithm can be optimized for better performance.

## Learn More

To continue your learning, see the following guides and software resources:

-  Visit [Edge Insights for Fleet](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/fleet-recipes.html?s=Newest) for additional reference implementations.
-  [Intel® Distribution of OpenVINO™ toolkit documentation](http://docs.openvinotoolkit.org/2019_R3/index.html)

## Known Issues

### Uninstall Reference Implementation

If you uninstall one of the reference implementations, you need to reinstall the other reference implementations
because the Docker images will be cleared. 

## Troubleshooting

### Installation Failure

If the host system already has Docker images and its containers running, you will have issues during the RI installation.
You must stop/force stop existing containers and images.

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

1. Get DNS server using the command:

   ```bash
   nmcli dev show | grep 'IP4.DNS'
   ```

2. Configure Docker to use the server. Paste the line below in the `/etc/docker/daemon.json` file:

   ```bash
   { "dns": ["<dns-server-from-above-command>"]}
   ```

3. Restart Docker:

   ```bash
   sudo systemctl daemon-reload && sudo systemctl restart docker
   ```

### Installation Failure Due to Ubuntu Timezone Setting

While building the reference implementation, if you see `/etc/timezone && apt-get install -y tzdata && ln -sf
/usr/share/zoneinfo/${HOST_TIME_ZONE} /etc/localtime && dpkg-reconfigure -f noninteractive tzdata' returned a non-zero code: 1 make: ***
[config] Error 1`

Run the following command in your terminal:

```bash
sudo timedatectl set-local-rtc 0
```

### Installation Encoding Issue

While building the reference implementation, if you see `ERROR: 'latin-1' codec can't encode character '\\u2615' in position 3: ordinal not in range(256)`

Run the following command in your terminal:

```bash
export LANG=en_US.UTF-8
```

### Can't Connect to Docker Daemon

If you can't connect to docker daemon at http+docker://localhost, run the following command in your terminal:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in to Ubuntu.

Check before retrying to install if group Docker is available for you by running the following command in a terminal:

```bash
groups
```

The output should contain “docker”.

### Support Forum
If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
