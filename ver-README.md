# Vehicle Event Recording Reference Implementation
## Overview

The Vehicle Event Recording Reference Implementation (RI) applies Artificial Intelligence (AI) to monitor the exterior of a vehicle and send events to the cloud dashboard. This includes event-based recording, remote view, driver coaching, and traffic violation detection features. The information is used for historical analysis, evidence support, and driver coaching by fleet management.

The RI includes an interface for the driver to be able to review events and check camera status on demand when the vehicle is not moving. The RI also sends event notifications and video clips to Amazon Web Services* (AWS*), which can be displayed on the cloud dashboard.

Select **Configure & Download** to download the reference implementation and the software listed below.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/vehicle_event_recording)


![Screenshot of running Vehicle Event Recording.](docs/vehicle-event-recording-landing.png)



-   **Time to Complete:**  Approximately 60 minutes
-   **Programming Language:**  Python*
-   **Available Software:**  Intel® Distribution of OpenVINO™ toolkit 2021.4.2 Release

### Recommended Hardware

The below hardware is recommended for use with this reference implementation.
For other suggestions, see [Recommended Hardware](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/hardware.html?s=Newest).

-   [Lenovo* ThinkEdge-SE30](https://www.lenovo.com/us/en/p/desktops/thinkcentre/m-series-tiny/thinkedge-se30/len102c0004)

-   [NEXCOM* VTC 7252-7C4IP](https://www.nexcomusa.com/Products/mobile-computing-solutions/in-vehicle-pc/security-vtc/in-vehicle-computer-vtc-vtc-7252-7c4ip)

## Target System Requirements

-   Ubuntu* 20.04

-   6th to 10th Generation Intel® Core™ processors with Intel® Iris® Plus graphics or Intel® HD Graphics

## How It Works

Vehicle Event Recording utilizes external facing cameras to detect objects and provide event-based video recording, remote view and driver coaching, and traffic violation detection features.

The RI is used for historical analysis, evidence support and driver coaching by fleet management.

Vehicle Event Recording has an interface for the driver to be able to review events and check camera status on demand when the vehicle is not moving.

The RI sends event notifications and video clips to AWS, which can be displayed on a dashboard.

![The architecture is represented by a complex block diagram.](docs/vehicle-event-recording-arch-diagram.png)

Figure 1: Architecture Diagram

## Get Started

### Step 1: Install the Reference Implementation

Select **Configure & Download** to download the reference implementation and then follow the steps below to install it.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/vehicle_event_recording)

>**NOTE:** If the host system already has Docker images and containers,
you might encounter errors while building the reference implementation
packages. If you do encounter errors, refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document before starting the reference
implementation installation.

1. Open a new terminal, go to the downloaded folder and unzip the downloaded RI package.

    ```bash
    unzip vehicle_event_recording.zip
    ```

2. Go to the `vehicle_event_recording/` directory.

    ```bash
    cd vehicle_event_recording/
    ```

3. Change permission of the executable *edgesoftware* file.

    ```bash
    chmod 755 edgesoftware
    ```

4. Run the command below to install the Reference Implementation.

    ```bash
    ./edgesoftware install
    ```

5. During the installation, you will be prompted for the **Product Key**. The **Product Key** is contained in the email you received from Intel confirming your download.

    ![A console window showing a system prompt to enter the product key.](docs/vehicle-event-recording-product-key.png)

    Figure 2: Product Key

6. When the installation is complete, you see the message "Installation of package complete" and the installation status for each module.

    ![A console window showing system output during the install process. At the end of the process, the system displays the message “Installation of package complete” and the installation status for each module. ](docs/vehicle-event-recording-install-success.png)

    Figure 3: Installation Success

    >**NOTE:** If you encounter any issues, refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document. Installation failure logs are
available at the path:
`/var/log/esb-cli/Vehicle_Event_Recording_<version>/output.log`

7. In order to start the application, change the directory using the cd command printed at the end of the installation process:

    ```bash
    cd /opt/intel/eif/EII-UseCaseManager
    ```

### Step 2: Run the Application

**Prerequisites**

- [Set Up ThingsBoard* Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top.html)
- [Set Up Amazon Web Services* Cloud Storage](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top.html)

1. Run the application. Copy and run the `make webui` command from the end of the installation log:

    ```bash
    make webui
    ```

2. Open the Web UI and go to **127.0.0.1:9090** on your web browser.

    ![A browser window showing the reference implementation dashboard.](docs/vehicle-event-recording-webui.png)

    Figure 4: Reference Implementation Dashboard

3. If you installed your ThingsBoard Cloud Server and you have enabled S3 Bucket Server
on your AWS account, you can provide your configured **AWS Access Key ID**, **AWS Secret Access Key**,
**Thingsboard IP**, **Thingsboard Port** and **Thingsboard Device token** on the **Cloud Data Configuration** tab.
After you complete the Cloud configuration, make sure you click on the **Save Credentials** and **Save Token** buttons.
Now you can import the ThingsBoard dashboard as described at the end of the [Set Up ThingsBoard* Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top.html)
to enable all dashboard features, including the cloud storage.

    ![A web app dashboard showing the Configuration tab. Certain fields are
   covered with a blue bar for security](docs/vehicle-event-recording-config-set-aws.png)

   Figure 5: Configuration Tab Contents

    > **NOTE:** If you don't have an AWS account, you will not be able to access Storage Cloud. You can still enable the ThingsBoard Cloud Data if you configured it locally or on another machine.

4. Access the Video Event Recording Dashboard with the following steps.

    -  Go to sidebar and select the **Run Application** menu option.

       ![A web app dashboard showing the Run Application menu option.](docs/vehicle-event-recording-select-run-use-case.png)

       Figure 6: Select Run Application Menu Option

    -  Configure the use case. Select video samples for all available streams and configure target devices for the selected models.
    -  Optionally, you can also set the simulation data that you want to use. You can choose between using the [KnowGo Simulator](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-know-go-simulator.html) or simply use the CSV pre-recorded simulation data.

        ![A web app dashboard showing the Dashboard.](docs/vehicle-event-recording-config-use-case.png)

        Figure 7: Configure Use Case

    -   Click on the **Browse** button and search for one of the sample videos delivered with the application at the following path:
        `/opt/intel/eif/EII-UseCaseManager/modules/EII-EVMSC-UseCase/config/VideoIngestion/test_videos/`
    -   After you configure all four videos, select the target CPU, GPU or Hetero (which will combine CPU and GPU) for all models selected. Click on **Run Application**.


    **Model Description**
    -   Obstacles Detection is enabled by default - this model will detect cars, pedestrians or other obstacles on the street.
    -   Road Segmentation will classify each pixel into four classes: BG, road, curb, mark.

    Depending on the number of cameras configured, the application will start the Visualizer App that will analyze the video sample or video samples selected.

    ![A web app dashboard showing output from the visualizer.](docs/vehicle-event-recording-run-use-case-results.png)

    Figure 8: Visualizer Output

    At this point, you can see that the algorithm is analyzing the traffic from the video streams.


5. After the visualizer starts, you can go to the ThingsBoard link and check the alerts sent by the
reference implementation. If you configured the AWS credentials, you will also have access to
video snapshots taken by the application on the video stream.

    ![A browser window showing the ThingsBoard link with the Intel Fleet Manager dashboard in the main view. Several components are displayed, including Alerts, Temperature, and a map showing the vehicle location.](docs/vehicle-event-recording-ri-tb-alerts.png)

    Figure 9: Intel Fleet Manager Dashboard shown in ThingsBoard

6. You can also check the cloud storage from the Reference Implementation **Storage** menu option.

    ![A web app dashboard showing the Storage menu option.](docs/vehicle-event-recording-ri-cloud-storage.png)

    Figure 10: Reference Implementation Storage Menu Option

## Run in Parallel with Driver Behavior Analytics Reference Implementation

To run this task, you will need to download and install [Driver Behavior Analytics](https://www.intel.com/content/www/us/en/develop/articles/driver-behavior-analytics.html#install) Reference Implementation.

For more details about parallel execution, see the Edge Insights for Fleet [Use Case
Manager](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/use-case-manager.html) documentation.

### Prerequisites

-   Follow the steps to install [Driver Behavior Analytics](https://www.intel.com/content/www/us/en/develop/articles/driver-behavior-analytics.html#install) after installing [Vehicle Event Recording](#step-1-install-the-reference-implementation)

### Steps to Run the Application

1.  Change directory to **Use Case Manager**:

    ```bash
    cd /opt/intel/eif/EII-UseCaseManager
    ```

2.  Run the following command on your terminal to start the web server application.

    ```bash
    make webui
    ```

3.  Open your browser and go to **127.0.0.1:9090**.

4.  Configure both installed reference implementations by setting the **video source** and the **target** (**CPU**, **GPU** or **HETERO**). Click on **Run Application**.
     >**NOTE:** Configure each reference implementation by selecting the desired tab. For example, click the **Run Application** menu option, then click on **VER** to configure the Vehicle Event Recording RI. Next, click on **DBA** to configure the Driver Behavior Analytics RI.

    ![A browser window showing application with VER and DBA tabs - VER selected.](docs/vehicle-event-recording-configure-ver.png)

    Figure 11: Configure Vehicle Event Recording Reference Implementation

    ![A browser window showing application with VER and DBA tabs - DBA selected.](docs/vehicle-event-recording-configure-dba.png)

    Figure 12: Configure Driver Behavior Analytics Reference Implementation


5.  Wait for both Visualizers to get up and running.

    ![A browser window showing output of 2 visualizers in a side-by-side view.](docs/vehicle-event-recording-two-use-cases.png)

    Figure 13: Visualizer Output for 2 Reference Implementations

## Summary and Next Steps

This reference implementation successfully implements Intel® Distribution of OpenVINO™ toolkit plugins for detecting objects and provides event-based video recording. It uses Edge Insights for Fleet framework to cover historical analysis, evidence support, driver coaching, remote view, and traffic violation detection.

As a next step, try one the following:

-   Use deep learning models, Edge Insights for Fleet framework and a live external video camera stream to capture evidence support, remote view, traffic violations and coach the decisions that must be made by the algorithm.

-   This reference implementation uses Intel® Distribution of OpenVINO™ toolkit Open Model Zoo pre-trained models and 3rd party models, but you can extend it to use your own models.

## Learn More

To continue your learning, see the following guides and software resources:

-   For additional reference implementations, visit [Edge Insights for Fleet](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/fleet-recipes.html?s=Newest).
-   [Intel® Distribution of OpenVINO™ toolkit documentation](http://docs.openvinotoolkit.org/2019_R3/index.html)

## Known Issues

### Uninstall Reference Implementation

If you uninstall one of the reference implementations, you need to reinstall the other reference implementations because the Docker images will be cleared.

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

The output should contain "docker".

### Installation Timeout When Using pip or apt Commands

You may experience a timeout issue when using the People's Republic of China (PRC)
internet network.

Make sure that you have a stable internet connection while installing the
packages. If you experience timeouts due to Linux* apt or Python* pip
installation, try to reinstall the package.

### Support Forum
If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
