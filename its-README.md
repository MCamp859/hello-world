# Intelligent Traffic Searching Reference Implementation

## Overview

The **Intel® Edge Video Infrastructure Reference Architecture** is a containerized micro-service architecture, modularized and extensible software platform on Edge Cloud side to support video applications and services. Intel offers it to Edge Video users and developers (OxM and end-user) to easily deploy video processing, AI and big data related edge video applications.
**Intelligent Traffic Searching** (**ITS**) is a reference implementation demonstrating its capability. This document will walk you through deploying **ITS** on the target system.

Once done, you will have the following:

* *Query Web*, a front-end service that provides a user interface, from which the user can input an image of the vehicle and obtain the historical track of the vehicle.
* *Query REST*, which receives API requests from *Query Web* and then query *Search Image by Image* service and *Storage REST* service to obtain and reconstruct data.
* *Search Image by Image* service, which receives requests from *Query REST* and send requests to *Feature Matching* services to obtain related features.

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Developer Experience Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Once you have installed the Intel® Smart Edge Open Developer Experience Kit, select
[**Configure & Download**](https://software.intel.com/iot/edgesoftwarehub/download/home/intelligent-traffic-searching) to
download the reference implementation and the software listed below.


-  **Time to Complete:** Approximately 60 - 90 minutes
-  **Programming Language:** Python\*, C++
-  **Software:** Intel® Smart Edge Open Developer Experience Kit version 22.03.03


## Target System Requirements

### Intel® Smart Edge Open Nodes

* Intel® Xeon® Scalable Processor, such as
    * Intel® Xeon® Gold 6330 CPU @ 2.00 GHz
    * Intel® Xeon® Silver 4310 CPU @ 2.10 GHz
* At least 64 GB RAM.
* At least 100 GB SSD as the system disk.
* At least 1.3 TB HDD as the data disk.
* Ubuntu\* Server 20.04 LTS.
* Internet connection.

## How It Works

### Architecture

![The architecture is represented by a complex block diagram.](./images/ITS-framework.png)

Figure 1: Architecture Diagram

1.	Browser sends get data-source request to Query service via API Gateway.
2.	Browser sends reverse image search request to Query service via API Gateway.
3.	Query service parses the request and finds out the query as a reverse image search query, then sends it to Search Image by Image service and waits for the response.
4.	Search Image by Image service needs to convert the unstructured images into feature vector at first, so images as well as additional job requirements (e.g., models, pre-processing/post-processing mechanism, etc.) are transferred to Structuring pod for computer vision inference. Also, Search Image by Image service waits for the response from Structuring pod.
5.	Structuring pod parses the job and builds an inference pipeline which is then sent to AI Inference pod together with query images. Structuring pod waits for the response of AI Inference pod. As models and dependencies are pre-loaded in AI Inference pod, the pod can process the query images and turn them into feature vectors. Extracted feature vectors are sent back to Structuring pod.
6.	Search Image by Image service receives the response from Structuring pod and moves on to feature matching. Since there’re two tasks parsed for feature matching, Search Image by Image service firstly sends extracted feature vectors to Feature Matching service to acquire matched archived images. Feature Matching service calculates the distances between query feature vectors and feature vectors from archived images. Matched top k results are sent back to Search Image by Image service.
7.	Query service has got response from Search Image by Image pod and queries the full information of received archived and unarchived top k results from structured storage.
8.	Query vehicle history request is triggered by user being sent to Query service via API Gateway.
9.	Query service query vehicle history through storage.

### ITS example use case: Search Image by Image

The Use Case diagram below shows the workflow of search image by image use case.

![The Use Case for search image by image is represented by a complex block
diagram.](./images/ITS-use-case.png)

Figure 2: Use Case Diagram

## Get Started

### Prerequisites

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Developer Experience Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Make sure that Intel® Smart Edge Open Developer Experience Kit package is installed properly as per installation guide to ensure a smooth installation of ITS RI.

Refer to the link below:
[Intel® Smart Edge Open Developer Experience Kit Install](https://github.com/smart-edge-open/docs/blob/main/experience-kits/developer-experience-kit.md#install-the-developer-experience-kit)

Configure Docker's logging driver to prevent running out of storage space by editing /etc/docker/daemon.json:

```console
"log-driver": "json-file",
"log-opts": {
  "max-size": "300m",
  "max-file": "3"
}
```

Restart Docker daemon:

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

#### Partition, format, and mount different disks to the specific directories

Prepare a disk larger than **1.3 TB** to mount to the machine, and then divide the disk into 5 partitions.
   * first partition 10GB: Allocat to Consul service to store storage encryption key and other related information.
   * second partition 100GB: Allocat to the Psql database to store media metadata and other related information.
   * third partition 400GB: Allocat to Media Storage to store pictures or videos.
   * fourth partition 500GB: Allocated to Hbase to store archive data.
   * fifth partition 200GB: Used to store local images or videos and corresponding metadata data.

Run the following commands to create the script `mount_disks.sh`:

```bash
$ cat << 'EOF' > mount_disks.sh
#!/bin/bash

# $1 indicates the path of the disk, such as: /dev/sdd
DISK_PATH="$1"
if [[ -z $DISK_PATH ]]; then
    echo "Please input a valid disk path...Aborted"
    exit 1
fi

# partition the disks
echo "partition the disks......"
sudo parted --script "$DISK_PATH" \
    mklabel gpt \
    mkpart primary 4096s 10240MiB \
    mkpart primary 10240MiB 112640MiB \
    mkpart primary 112640MiB 522240MiB \
    mkpart primary 522240MiB 1034240MiB \
    mkpart primary 1034240MiB 1239040MiB
echo "partition the disks done."

# format the disks
echo "format the disks......"
sudo mkfs.xfs -f "${DISK_PATH}1"
sudo mkfs.xfs -f "${DISK_PATH}2"
sudo mkfs.xfs -f "${DISK_PATH}3"
sudo mkfs.xfs -f "${DISK_PATH}4"
sudo mkfs.xfs -f "${DISK_PATH}5"
echo "format the disks done."

# create paths and mount the disks
echo "create paths and mount the disks......"
sudo mkdir -p /mnt/consul \
    /mnt/postgresql \
    /mnt/minio \
    /mnt/disks \
    /home/data

cat << NestedEOF | sudo tee -a /etc/fstab
${DISK_PATH}1 /mnt/consul xfs defaults 0 0
${DISK_PATH}2 /mnt/postgresql xfs defaults 0 0
${DISK_PATH}3 /mnt/minio xfs defaults 0 0
${DISK_PATH}4 /mnt/disks xfs defaults 0 0
${DISK_PATH}5 /home/data xfs defaults 0 0
NestedEOF

sudo mount -a
EOF
echo "create paths and mount the disks done."
echo "All done."
```

Use the script to prepare disks by passing the drive path dedicated to the application, e.g. `/dev/sdd`:

```shell
sudo apt-get install xfsprogs
bash mount_disks.sh /dev/sdd
```


### Install the Application


Select [**Configure & Download**](https://software.intel.com/iot/edgesoftwarehub/download/home/intelligent-traffic-searching) to
download the reference implementation and then follow the steps below to install it.


1. Make sure that the Target System Requirements as mentioned earlier are accomplished properly before proceeding further.

    * For single-device mode, only one machine is needed. (Both controller and edge node will be on same device.)

    > NOTE : Multi-device mode is not supported in the current release.

2. Create a user account for Intel® Smart Edge Open:

    ```bash
    sudo adduser "smartedge-open"
    sudo passwd "smartedge-open"
    echo "smartedge-open ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/smartedge-open
    ```

3. Open a new terminal as smartedge-open user:

    ```bash
    su - smartedge-open
    ```

4. Generate an SSH key under smartedge-open user:

    ```bash
    ssh-keygen
    ssh-copy-id smartedge-open@target_server_IP
    ```

5. Move the downloaded zip package to the ``/home/smartedge-open`` folder.

    ```bash
    sudo mv <path-of-downloaded-directory>/intelligent-traffic-searching.zip /home/smartedge-open
    ```

6. Go to the /home/smartedge-open directory using the following command and unzip the RI:

    ```bash
    cd /home/smartedge-open
    unzip intelligent-traffic-searching.zip
    ```

7. Go to the intelligent-traffic-searching/ directory: 

    ```bash
    cd intelligent-traffic-searching/
    ```

8. Change permission of the executable edgesoftware file: 

    ```bash
    chmod 755 edgesoftware
    ```

9. Run the command below to install the Reference Implementation: 

    ```bash
    ./edgesoftware install
    ```

    >**NOTE:** Installation logs are available at the following path:
    ``/var/log/esb-cli/Intelligent\_Traffic\_Searching\_Reference\_Implementation\_<version\>/output.log``

10. When the installation is complete, you see the message “Installation of package complete” and the installation status for each module.

    ![A console window showing system output during the install process.](images/esh-install.png)

    Figure 3: Install Success

    >**NOTE:** If the pods have a status of “ContainerCreating”, please wait
    for some time, since Kubernetes will pull the images from the registry
    and then deploys them. This happens only the first time the containers
    are deployed, and the wait time will depend upon the network bandwidth
    available.

11. If Intel® Smart Edge Open Developer Experience Kit is installed, running the following command should show output similar
    to the outputs below. All the pods should be either in running or completed stage.

    ```bash
    $ kubectl get pods -A
    ```

    ![A console window showing system output after running the "kubectl get pods" command. The system displays a list of all the pods and the pod status. The expected status is "Running" or "Completed".](images/esh-pod-all.png)

    Figure 4: Pods Status

12. If ITS RI is installed, running the following command should show output as follows:

    ```bash
    kubectl get pods -n smartedge-apps
    ```

    ![A console window showing system output after running the "kubectl get pods" command.](images/esh-pod-its.png)

    Figure 5: Smart Edge Pods Status

##  Demonstration

This section will work you through the ITS demo.

### Prepare Test Data

Create `/home/data` folder:

```bash
sudo mkdir -p /home/data && sudo chown $USER: $_
```

Create two folders:

```bash
mkdir -p /home/data/{images,metadata_ms}
```

Download [BIT-Vehicle Dataset](http://shujujishi.com/dataset/ff01a9be-f417-4e73-923b-1bc6408ee7aa.html) and extract to `/home/data/images`.

> **NOTE**: If you don't have an account yet, you need to create one.

Generate metadata for each image by the following command:

```bash
# goto its-repo directory
cd intelligent-traffic-searching/Intelligent_Traffic_Searching_Reference_Implementation_<version>/Intelligent_Traffic_Searching/its-repo
# install deps
python3 -m pip install -r ./image_into_metadata_requirements.txt
# will take about 2 minutes, be patient
python3 ./image_into_metadata.py
```

> **NOTE**: Run `python3 ./image_into_metadata.py -h` for more information.

### Inject Test Data

Inject the test data into the database with the following commands:

```bash
# enter the evi-test-tool pod
kubectl exec -ti -n smartedge-apps "$(kubectl get pod -l app=evi-test-tool -o jsonpath='{.items[0].metadata.name}' -n smartedge-apps)" -- /bin/bash

# check the help message
./evi_test_tool -h

# upload media data and metadata to storage.
./evi_test_tool -f configuration/evi-test-tool.json -i

# Trigger AI Inference.
./evi_test_tool -f configuration/evi-test-tool.json -s

# Exit the pod
exit
```

Restart **FM worker** to reload data:

```bash
kubectl -n smartedge-apps delete pod evi-fm-worker-fs-0
```

### Search Image by Image

#### Login

Find the port number of *Query Web* using the command:

```bash
kubectl get svc istio-ingressgateway -n istio-system | perl -ne 'print "$1\n" if /\b443:(\d+)/'
```

> **NOTE**:
> * Use `$port` to represent the port number
> * Use `$host` to represent the IP address of the machine
> * Use `$name` to represent the hostname of the machine

Follow [this tutorial](https://www.hostinger.com/tutorials/how-to-edit-hosts-file) to map hostname to IP address.

```bash
$host $name
```

Now, visit `https://$host:$port` through a browser (such as Chrome\*). Login with

* User: `evi`
* Password: `evi`

![A browser window showing the EVI login screen.](images/query-evi-login.png)

Figure 6: EVI Login Screen

> **NOTE**: The browser will display a warning for self-signed certificate, click **Advanced** and then **Proceed to…** link to continue.

#### Query Image

![A browser window showing a large map of a city. Many vehicles are identified on the map. A rectangular area is highlighted in blue.](images/query-image.png)

Figure 7: Map in Browser

1. Select the **rectangle icon** at the top right corner of the map, click and drag to select an area on the map.
2. Upload a vehicle image from the test dataset.
3. Specify filter criteria. The valid date range is `2021.08.10 - 2021.08.12`.
4. Click **Search** button.

![A browser window showing a large map of a city. The right side of the window shows the search results pane.](images/query-history.png)

Figure 8: Search Results

> **KNOWN ISSUE**: The result images can't be shown correctly on the first run. To work around it, right-click on the image and select **Open image in new tab**, then click **Previous** button, and search again.

### Reset Data

To remove all the data generated in the database by the demo:

> **NOTE**: Run `bash ./reset_demo_data.sh -h` for more information.

```bash
cd intelligent-traffic-searching/Intelligent_Traffic_Searching_Reference_Implementation_<version>/Intelligent_Traffic_Searching/its-repo
bash ./reset_demo_data.sh -y
```

### Uninstall the Application

1. Check installed modules with the following command:

    ```bash
    cd /home/smartedge-open/intelligent-traffic-searching
    ./edgesoftware list
    ```
    ![A console window showing the output of the "edgesoftware list" command. The installed modules are listed.](images/esh-list.png)

    Figure 9: Module List

2. Run the command below to uninstall all the modules:

    ```bash
    ./edgesoftware uninstall -a
    ```

3. Run the command below to uninstall the Intelligent Traffic Searching reference implementation:

    ```bash
    ./edgesoftware uninstall <its-id>
    ```

    ![A console window showing the output of the "edgesoftware uninstall" command. At the end of the process, the system displays the message "Uninstall finished" and the uninstallation status for each module.](images/esh-uninstall.png)

    Figure 10: Uninstallation Successful


## Summary and Next Steps

*OPEN: Provide 2-3 line description of what they have successfully done and
where they should go to as the next step.*


## Learn More

To continue learning, see the following guides:

-  [Intel® Smart Edge Open Developer Experience Kit](https://smart-edge-open.github.io/ido-specs/doc/architecture/)
-  [relevant link title](URL) *OPEN*
-  [relevant link title](URL) *OPEN*


## Support Forum

If you're unable to resolve your issues, contact the [Support
Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
