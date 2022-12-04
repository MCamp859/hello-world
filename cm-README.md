# Cargo Management Reference Implementation
## Overview

Use an Intel® RealSense™ camera to create a solution that detects regular and irregularly shaped packages and tracks newly added and removed packages in the cargo area of a transportation vehicle.

Select **Configure & Download** to download the reference implementation and the software listed below.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/cargo_management)


![Screenshot of running Cargo Management.](docs/cargo-management-ri-landing-page.png)


-   **Time to Complete:** Approximately 60 minutes
-   **Programming Language:** Python*

### Recommended Hardware

The below hardware is recommended for use with this reference implementation.
For other suggestions, see [Recommended Hardware](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/hardware.html?s=Newest).


-   [ADLINK MXE-5500 Series](https://www.adlinktech.com/Products/Industrial_PCs_Fanless_Embedded_PCs/IntegratedFanlessEmbeddedComputers/MXE-5500_Series?lang=en)

-   [NEXCOM VTC 7252-7C4IP](https://www.nexcomusa.com/Products/mobile-computing-solutions/in-vehicle-pc/security-vtc/in-vehicle-computer-vtc-vtc-7252-7c4ip)

## Target System Requirements

-   Ubuntu* 20.04

-   6th to 10th Generation Intel® Core™ processors with Intel® Iris® Plus graphics or Intel® HD Graphics

-   Intel® RealSense™ D400 series camera

-   Minimum 20 GB free space

## How It Works

Cargo Management Reference Implementation does the following:

-   Detects regularly shaped box’s Length, Width and Height dimensions up to 53 ft.

-   Detects an irregularly shaped package’s Length, Width and Height dimensions using an outline bounding box, up to 53 ft for each dimension and a minimum of 2 inches.

-   Provides a simple User Interface to interact with the driver for tracking and reviewing detected events.

-   Sends the detected packages and their dimensions as notifications to Amazon Web Services* (AWS) to display them on a Dashboard.

![The architecture is represented by a complex block diagram.](docs/cargo-management-ri-arch-diagram.png)

Figure 1: Architecture Diagram

## Get Started

### Prerequisites

-   Install Intel® RealSense™ SDK for Ubuntu using instructions on [GitHub](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md).

-   Print configuration chessboard from [GitHub](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md) on page A4. Place it on camera view on a horizontal setup.

### Step 1: Install the Reference Implementation

Select **Configure & Download** to download the reference implementation and then follow the steps below to install it.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/ri/cargo_management)

>**NOTE:** If the host system already has Docker images and containers,
you might encounter errors while building the reference implementation
packages. If you do encounter errors, refer to the
[Troubleshooting](#troubleshooting)
section at the end of this document before starting the reference
implementation installation.

1. Open a new terminal, go to the downloaded folder and unzip the downloaded RI package.

    ```bash
    unzip cargo_management.zip
    ```

2. Go to the `cargo_management/` directory.

    ```bash
    cd cargo_management/
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

    ![A console window showing a system prompt to enter the product key.](docs/cargo-management-ri-product-key.png)

    Figure 2: Product Key

6. When the installation is complete, you see the message "Installation of package complete" and the installation status for each module.

    ![A console window showing system output during the install process. At the end of the process, the system displays the message “Installation of package complete” and the installation status for each module. ](docs/cargo-management-ri-install.png)

    Figure 3: Installation Success

    >**NOTE:** If you encounter any issues, please refer to the
[Troubleshooting](#troubleshooting) section at the end of this document.
Installation failure logs will be available at the path:
`/var/log/esb-cli/Cargo_Management_<version>/output.log`

7. In order to start the application, you need to change the directory using the cd command printed at the end of the installation process:

    ```bash
    cd /opt/intel/eif/EII-UseCaseManager
    ```

### Step 2: Run the Application

#### Prerequisites

-   [Set Up ThingsBoard* Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-thingsboard-cloud-data.html)
-   [Set Up Amazon Web Services* Cloud Storage](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-amazon-web-services-cloud-storage.html)

1. Run the application. Copy and run the `make webui` command from the end of the installation:

    ```bash
    make webui
    ```

2. Open the Web UI and go to **127.0.0.1:9090** on your web browser.

    ![A browser window showing the reference implementation dashboard.](docs/cargo-management-ri-web-ui.png)
    Figure 4: Reference Implementation Dashboard

3. If you installed your ThingsBoard Cloud Server and you have enabled S3 Bucket Server
on your AWS account, you can provide your configured **AWS Access Key ID**, **AWS Secret Access Key**,
**Thingsboard IP**, **Thingsboard Port** and **Thingsboard Device token** on the **Cloud Data Configuration** tab.
After you complete the Cloud configuration, make sure you click on the **Save Credentials** and **Save Token** buttons.
Now you can import the ThingsBoard dashboard as described at the end of the [Set Up ThingsBoard* Cloud Data](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-thingsboard-cloud-data.html)
to enable all dashboard features, including the cloud storage.

    ![A web app dashboard showing the Configuration menu option. Certain fields are
    covered with a blue bar for security](docs/cargo-management-ri-access-key.png)

    Figure 5: Configuration Menu Option Contents

4. Access the Cargo Management Dashboard by selecting **Run Application**. The web application should detect the camera. Configure as below.

    ![A web app dashboard showing the Run Application tab.](docs/cargo-management-ri-run-usecase.png)

    Figure 6: Select Run Application Menu Option

    -  Optionally, you can also set the simulation data that you want to use. You can choose between using the [KnowGo Simulator](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/set-up-know-go-simulator.html) or simply use the CSV pre-recorded simulation data.

5. After 30-40 seconds, the Visualizer should pop up and the camera should be configured. If the Visualizer does not pop up, make sure you have placed the calibration chessboard in camera view.

    ![A web app dashboard showing output from the visualizer.](docs/cargo-management-ri-visualizer.png)

    Figure 7: Visualizer Output

6. Place one object at a time on the chessboard calibration area to have the object measured. The images below show how the objects are measured.

    ![A web app dashboard showing output from the visualizer.](docs/cargo-management-ri-visualizer2.png)

    Figure 8: Visualizer Output

    ![A web app dashboard showing output from the visualizer.](docs/cargo-management-ri-visualizer3.png)

    Figure 9: Visualizer Output

7. After the visualizer starts, you can go to the ThingsBoard link and check the alerts sent by the
reference implementation. If you configured the AWS credentials, you will also have access to
pictures taken by the application on the video stream.

    ![A browser window showing the ThingsBoard link with the Intel Fleet Manager dashboard in the main view. Several components are displayed, including Alerts, Temperature, and a map showing the vehicle location.](docs/cargo-management-ri-tb-dashboard-with-data.png)

    Figure 10: Intel Fleet Manager Dashboard shown in ThingsBoard

8. You can also check the cloud storage from the Reference Implementation **Storage** menu option.

    ![A web app dashboard showing the Storage menu option.](docs/cargo-management-ri-aws-storage.png)

    Figure 11: Reference Implementation Storage Menu Option

## Run in Parallel with Automated License Plate Recognition Reference Implementation

To run this task, you will need to download and install the [Automated License Plate Recognition](https://www.intel.com/content/www/us/en/develop/articles/automated-license-plate-recognition.html#install) Reference Implementation.

For more details about parallel execution, see the Edge Insights for Fleet
[Use Case Manager](https://www.intel.com/content/www/us/en/develop/documentation/edge-insights-fleet-doc/top/reference-implementations/use-case-manager.html) documentation.

### Prerequisites

-   Follow the steps to install [Automated License Plate Recognition](https://www.intel.com/content/www/us/en/develop/articles/automated-license-plate-recognition.html#install) after installing [Cargo Management](#step-1-install-the-reference-implementation)

### Steps to Run the Application

1.  Change directory to **EII-UseCaseManager**:

    ```bash
    cd /opt/intel/eif/EII-UseCaseManager
    ```

2.  Run the following command to start the web server application.

    ```bash
    make webui
    ```

3.  Open your browser and go to **127.0.0.1:9090**.

    >**NOTE:** Configure each reference implementation by selecting the desired
    >tab. For example, click the **Run Application** menu option, then click on
    >**CM** to configure the Cargo Management RI. Next, click
    >on **ALPR** to configure the Automated License Plate Recognition RI.


4. Access the Cargo Management Dashboard. The web application should detect the camera. Configure as below.

    ![A browser window showing application with CM and ALPR tabs - CM selected.](docs/cargo-management-configure-cm.png)

    Figure 12: Configure Cargo Management Reference Implementation

5.  Configure Automated License Plate Recognition Reference Implementation by
    setting the **video source** and the **target** (**CPU**, **GPU** or
    **HETERO**). Click on **Run Application**.

    ![A browser window showing application with CM and ALPR tabs - ALPR selected.](docs/cargo-management-configure-alpr.png)

    Figure 13: Configure Automated License Plate Recognition Reference Implementation

6.  Wait for both Visualizers to get up and running.

    ![A browser window showing output of 2 visualizers in a side-by-side view.](docs/cargo-management-two-use-cases.png)

    Figure 14: Visualizer Output for 2 Reference Implementations


## Summary and Next Steps

You successfully ran the Cargo Management application and displayed the result using Amazon Web Services* (AWS).

As next step, try the following: Using the current implementation, try to make the algorithm more reliable or make a preconfigured calibration. This will make it possible to detect multiple objects at the same time.

## Learn More

To continue your learning, see the following guides and software resources:

-   For additional reference implementations, visit [Edge Insights for Fleet](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/fleet-recipes.html?s=Newest).
-   [Intel® Distribution of OpenVINO™ toolkit documentation](http://docs.openvinotoolkit.org/2019_R3/index.html)
-   [Intel® RealSense™ SDK Documentation](https://github.com/IntelRealSense/librealsense)

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
    { "dns": ["<dns-server-from-above-command>"] }
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

Check before retry to install if group Docker is available for you by running the following command in a terminal: 

```bash
groups
```

The output should contain **Docker**.


### Visualizer Does Not Start

Make sure you have updated the camera firmware and the chessboard calibration is placed on camera view.

To update the camera firmware, download the latest [firmware](https://www.intel.com/content/www/us/en/download/19242/30419/firmware-for-intel-realsense-d400-product-family.html?v=t).

### Installation Timeout When Using pip or apt Commands

You may experience a timeout issue when using the People's Republic of China (PRC)
internet network.

Make sure that you have a stable internet connection while installing the
packages. If you experience timeouts due to Linux* apt or Python* pip
installation, try to reinstall the package.


### Support Forum
If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
