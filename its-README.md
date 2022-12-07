# Intelligent Traffic Searching Reference Implementation

## Overview

Create a solution that monitors vehicles in traffic using Intel® Edge Video
Infrastructure Reference Architecture and Intel® Smart Edge Open.

*  Intel® Edge Video Infrastructure Reference Architecture: A containerized,
   microservice architecture used to easily deploy video processing, AI, and big
   data edge video applications.

*  Intel® Smart Edge Open: A software toolkit for building edge platforms.

To run the Intelligent Traffic Searching (ITS) reference implementation, you
will need to first download and install the [Intel® Smart Edge Open Developer
Experience Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Once you have installed the Intel® Smart Edge Open Developer Experience Kit,
select **Configure & Download** to download the reference implementation and the
software listed below.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/intelligent-traffic-searching)

-  **Time to Complete:** Approximately 60 - 90 minutes
-  **Programming Language:** Python\*, C++
-  **Software:** Intel® Smart Edge Open Developer Experience Kit version 22.03.03


## Target System Requirements

### Intel® Smart Edge Open Nodes

* Intel® Xeon® Scalable Processor, such as
    * Intel® Xeon® Gold 6330 Processor @ 2.00 GHz
    * Intel® Xeon® Silver 4310 Processor @ 2.10 GHz
* At least 64 GB RAM.
* At least 100 GB SSD as the system disk.
* At least 1.3 TB HDD as the data disk.
* Ubuntu\* Server 20.04 LTS.
* Internet connection.

## How It Works

Intelligent Traffic Searching (ITS) is a reference implementation demonstrating
the capabilities of Intel® Edge Video Infrastructure Reference Architecture.
After you complete the installation, you will have the following components:

*  Query Web, which provides a user interface from which the user can input an image of
   a vehicle and obtain the historical record of the vehicle.
*  Query REST, which receives API requests from Query Web, then queries Search
   Image by Image service and Storage REST service to obtain and reconstruct the
   data.
*  Search Image by Image service, which receives requests from Query REST and sends
   requests to Feature Matching services to obtain related features.

### Architecture

![The architecture is represented by a complex block diagram.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-arch-diagram.png)

Figure 1: Architecture Diagram

### Typical Workflow

![The typical workflow is represented by a complex block diagram.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-typical-workflow.png)

Figure 2: ITS RI Typical Workflow

1. The user uploads an image to search, the browser sends `get data-source` request to *Query* service via *API Gateway*.
1. Browser sends `reverse image search` request to *Query* service via *API Gateway*.
1. *Query* service parses the request and finds out the query as a `reverse image search` query, then sends it to *Search Image by Image* service and waits for the response.
1. *Search Image by Image* service needs to convert the unstructured images into feature vector at first, so images and additional job requirements (e.g., models, pre-processing and post-processing mechanism) are transferred to *Structuring* service for computer vision inference. Additionally, *Search Image by Image* service waits for the response from *Structuring* service.
1. *Structuring* service parses the job and builds an inference pipeline which is then sent to *AI Inference* service together with the images to be queried. *Structuring* service waits for the response of *AI Inference* service. As models and dependencies are pre-loaded in *AI Inference* service, the service can process the images and turn them into feature vectors. Extracted feature vectors are sent back to *Structuring* service.
1. *Search Image by Image* service receives the response from *Structuring* service and moves on to feature matching. *Feature Matching* service calculates the similarity between the feature vectors of the images to be queried and the ones in the database. The k most similar feature vectors are sent back to *Search Image by Image* service.
1. *Query* service gets a response from *Search Image by Image* service and queries the storage for full information of the feature vectors.
1. The user selects one vehicle from the top-k result to further get the history of the details.

### Example Use Case: Search Image by Image

The Use Case diagram below shows the workflow of search image by image use case.

![The Use Case for search image by image is represented by a complex block
diagram.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-use-case.png)

Figure 3: Use Case Diagram

The Search Image by Image Sample Application leverages the *Media & AI
Inference* and *Feature Matching* Service to search the target image(s) in huge
database. It invokes the *Media & AI Inference* service to decode the input
image and extract the vehicle feature from it, and then sends the feature to
*Feature Matching* service which will do the feature matching/searching against
the huge amount of database and returns the best matching pictures to the user.

## Get Started

### Prerequisites

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Open Developer Experience Kit](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Make sure that Intel® Smart Edge Open Developer Experience Kit package is
installed properly as per installation guide to ensure a smooth installation of
ITS RI.

Refer to the link below:
[Intel® Smart Edge Open Developer Experience Kit Install](https://github.com/smart-edge-open/docs/blob/main/experience-kits/developer-experience-kit.md#install-the-developer-experience-kit)

Configure the Docker\* logging driver to prevent running out of storage space by
editing `/etc/docker/daemon.json`:

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
   * first partition 10 GB: Allocate to Consul service to store storage encryption key and other related information.
   * second partition 100 GB: Allocate to the Psql database to store media metadata and other related information.
   * third partition 400 GB: Allocate to Media Storage to store pictures or videos.
   * fourth partition 500 GB: Allocate to Hbase to store archive data.
   * fifth partition 200 GB: Used to store local images or videos and corresponding metadata data.

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

Use the script to prepare disks by passing the drive path dedicated to the
application, e.g. `/dev/sdd`:

```shell
sudo apt-get install xfsprogs
bash mount_disks.sh /dev/sdd
```


### Install the Application


Select **Configure & Download** to download the reference implementation and
then follow the steps below to install it.

[Configure & Download](https://software.intel.com/iot/edgesoftwarehub/download/home/intelligent-traffic-searching)

1. Make sure that the [Target System Requirements](#target-system-requirements) are accomplished properly before proceeding further.

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

5. Move the downloaded zip package to the `/home/smartedge-open` folder.

    ```bash
    sudo mv <path-of-downloaded-directory>/intelligent-traffic-searching.zip /home/smartedge-open
    ```

6. Go to the `/home/smartedge-open` directory using the following command and unzip the RI:

    ```bash
    cd /home/smartedge-open
    unzip intelligent-traffic-searching.zip
    ```

7. Go to the `intelligent-traffic-searching/` directory: 

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
    ``/var/log/esb-cli/Intelligent_Traffic_Searching_Reference_Implementation_<version>/output.log``

10. When the installation is complete, you see the message “Installation of package complete” and the installation status for each module.

    ![A console window showing system output during the install process.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-install-success.png)

    Figure 4: Install Success

    >**NOTE:** If the pods have a status of “ContainerCreating”, please wait
    for some time, since Kubernetes will pull the images from the registry
    and then deploy them. This happens the first time the containers
    are deployed, and the wait time will depend upon the network bandwidth
    available.

11. If Intel® Smart Edge Open Developer Experience Kit is installed, running the following command should show output similar
    to the outputs below. All the pods should be either in running or completed stage.

    ```bash
    $ kubectl get pods -A
    ```

    ![A console window showing system output after running the "kubectl get pods" command. The system displays a list of all the pods and the pod status. The expected status is "Running" or "Completed".](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-pods-status.png)

    Figure 5: Pods Status

12. If ITS RI is installed, running the following command should show output as follows:

    ```bash
    kubectl get pods -n smartedge-apps
    ```

    ![A console window showing system output after running the "kubectl get pods" command.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-its-pods.png)

    Figure 6: ITS Pods Status

##  Demonstration

This section will walk you through the ITS demo.

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
# Enter the evi-test-tool pod.
kubectl exec -ti -n smartedge-apps "$(kubectl get pod -l app=evi-test-tool -o jsonpath='{.items[0].metadata.name}' -n smartedge-apps)" -- /bin/bash

# Check the help message.
./evi_test_tool -h

# Upload media data and metadata to storage.
./evi_test_tool -f configuration/evi-test-tool.json -i

# Trigger AI Inference.
./evi_test_tool -f configuration/evi-test-tool.json -s

# Exit the pod.
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

![A browser window showing the EVI login screen.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-query-evi-login.png)

Figure 7: EVI Login Screen

> **NOTE**: The browser will display a warning for self-signed certificate, click **Advanced** and then **Proceed to…** link to continue.

#### Query Image

![A browser window showing a large map of a city. Many vehicles are identified on the map. A rectangular area is highlighted in blue.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-query-image.png)

Figure 8: Map in Browser

1. Select the **rectangle icon** at the top right corner of the map, click and drag to select an area on the map.
2. Upload a vehicle image from the test dataset.
3. Specify filter criteria. The valid date range is `2021.08.10 - 2021.08.12`.
4. Click **Search** button.

![A browser window showing a large map of a city. The right side of the window shows the search results pane.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-query-history.png)

Figure 9: Search Results

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
    ![A console window showing the output of the "edgesoftware list" command. The installed modules are listed.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-esh-list.png)

    Figure 10: Module List

2. Run the command below to uninstall all the modules:

    ```bash
    ./edgesoftware uninstall -a
    ```

3. Run the command below to uninstall the Intelligent Traffic Searching reference implementation:

    ```bash
    ./edgesoftware uninstall <its-id>
    ```

    ![A console window showing the output of the "edgesoftware uninstall" command. At the end of the process, the system displays the message "Uninstall finished" and the uninstallation status for each module.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-esh-uninstall.png)

    Figure 11: Uninstallation Successful


## Summary and Next Steps

ITS is an easy-to-deploy cloud native software suite to meet the "image
searching in huge database" requirements in smart traffic management in video
domain. As a next step, you can extend the RI with customized service and
application modules. You can also visit ESH to try other Reference Implementations.


## Learn More

To continue learning, see the following guides:

-  [Intel® Smart Edge Open Developer Experience Kit](https://smart-edge-open.github.io/ido-specs/doc/architecture/)
-  [Intel® Distribution of OpenVINO™ Toolkit](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)


## Support Forum

If you're unable to resolve your issues, contact the [Support
Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
