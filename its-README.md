# Intelligent Traffic Searching Reference Implementation

## Overview

A reference implementation for a solution that monitors vehicles in traffic to
extract information useful for several applications for cities. The solution is
using Intel® Edge Video Infrastructure Reference Architecture and Intel® Smart
Edge.

*  Intel® Edge Video Infrastructure Reference Architecture: A containerized,
   microservice architecture used to easily deploy video processing, AI, and
   edge video applications with big data analysis.

*  Intel® Smart Edge: An Edge Native software framework solutions enabling
   microservices-based workload (for edge applications and network services)
   onboarding, orchestration and management with diverse optimization on Intel
   hardware.

To run the Intelligent Traffic Searching (ITS) reference implementation, you
will need to first download and install the [Intel® Smart Edge Developer
Experience Kit (DEK)](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Once you have installed the Intel® Smart Edge Developer Experience Kit (DEK),
select **Configure & Download** to download the reference implementation and the
software listed below.

> **NOTE: Intelligent Traffic Searching Reference Implementation, version 1.0 is a
> beta release** that does not include the latest functional and security updates.
> **Intelligent Traffic Searching Reference Implementation, version 2.0** is targeted
> to be released and will include additional functional and security updates.
> Customers should update to the latest version as it becomes available.

[Configure & Download](https://edgesoftwaretestingwebui.intel.com/iot/edgesoftwarehub/download/home/intelligent-traffic-searching)

-  **Time to Complete:** Approximately 60 - 90 minutes
-  **Programming Language:** Python\*, C++
-  **Software:** Intel® Smart Edge Developer Experience Kit (DEK) version 22.03.03


## Target System Requirements

### Intel® Smart Edge Nodes

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
After you complete the installation, you will have the following edge services:

* Intelligent Traffic Searching Web UI, which provides a user interface enabling the user to input an image of a vehicle and show images of similar vehicles.
* Query edge service, which calls the Search Image by Image edge service and the Storage REST service to obtain images of similar vehicles.
* Search Image by Image edge service, which enables searching images by using input images.
* Feature Matching edge service, which receives requests from the Search Image by Image edge service to obtain the most similar features.
* Media & AI inference edge service, which receives requests from the Search Image by Image edge service to detect vehicles and extract features from input images.
* Clustering & Archiving Edge Service performs clustering analysis on vehicle features and metadata to cluster similar feature vectors and archive them into the vehicle’s history. This service can be triggered on-demand or periodically.
* Storage REST edge service, which stores metadata that can be searched through a REST interface.

### Architecture

![The architecture is represented by a complex block diagram.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-arch-diagram.png)

Figure 1: Architecture Diagram

### Typical Workflow

![The typical workflow is represented by a complex block diagram.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-typical-workflow.png)

Figure 2: ITS RI Typical Workflow

The ITS RI typical workflow leverages the Media & AI Inference and Feature Matching Service to search the target image(s) in huge database. It invokes the Media & AI Inference service to decode the input image and extract the vehicle feature from it, and then sends the feature to Feature Matching Edgeservice which will do the feature matching/searching against the huge amount of database and returns the best matching pictures to the user.  The following steps show the details of the ITS RI typical workflow.
1. The user uploads a vehicle image in Intelligent Traffic Searching WebUI to be searched, then the WebUI sends image search request tothe Queryedge service.
1. Query edge service parses the requests and sends it tothe Search Image by Imageedge service.
1. The Search Image by Imageedge service need to get feature vector of the vehicle from input image first, so images and additional job requirements (e.g., models, pre-processing and post-processing mechanism) are transferred to Media & AI Inference edge service to extract feature vector.
1. Media & AI Inference edge service parses the job and builds an inference pipeline to process the images and  and extract feature vector from the image. Extracted feature vectors are sent back to the Search Image by Image edge service.
1. The Search Image by Image edge service receives the feature vector from the Media & AI Inference edge service, then calls the Feature Matching Edge service to get similar feature vectors.
1. The Feature Matching Edge service calculates the similarity between the input feature vectors and the ones in the database. The k most similar feature vectors are sent back tothe Search Image by Image edge service.
1. The Query edge service gets a response from the Search Image by Image edge service and queries the storage for full information of the feature vectors. Then the WebUI shows the corresponding images on the map.

## Get Started

### Prerequisites

To run the reference implementation, you will need to first download and install the [Intel® Smart Edge Developer Experience Kit (DEK)](https://software.intel.com/iot/edgesoftwarehub/download/home/Smart_Edge_Open_Developer_Experience_Kits).

Make sure that Intel® Smart Edge Developer Experience Kit (DEK) package is installed properly as per installation guide to ensure a smooth installation of ITS RI.

Refer to the link below:
[Intel® Smart Edge Developer Experience Kit (DEK) Install](https://github.com/smart-edge-open/docs/blob/main/experience-kits/developer-experience-kit.md#install-the-developer-experience-kit)

Configure the Docker\* logging driver to prevent running out of storage space by editing `/etc/docker/daemon.json`:

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

[Configure & Download](https://edgesoftwaretestingwebui.intel.com/iot/edgesoftwarehub/download/home/intelligent-traffic-searching)

1. Make sure that the [Target System Requirements](#target-system-requirements) are accomplished properly before proceeding further.

    * For single-device mode, only one machine is needed. (Both controller and edge node will be on same device.)

    > NOTE: Multi-device mode is not supported in the current release.

2. If you are behind a proxy network, be sure that proxy addresses are configured in the system:

    ```bash
    export http_proxy=proxy-address:proxy-port
    export https_proxy=proxy-address:proxy-port
    ```

3. Under the user deploy Intel® Smart Edge Developer Experience Kit (DEK), for example `smartedge`, download the ITS RI package:

    ```bash
    mkdir <path-of-downloaded-directory>
    ```

4. Move the downloaded zip package to the `/home/smartedge` folder.

    ```bash
    mv <path-of-downloaded-directory>/intelligent-traffic-searching.zip /home/smartedge
    ```

5. Go to the `/home/smartedge` directory using the following command and unzip the RI:

    ```bash
    cd /home/smartedge
    unzip intelligent-traffic-searching.zip
    ```

6. Go to the `intelligent-traffic-searching/` directory:

    ```bash
    cd intelligent-traffic-searching/
    ```

7. Change permission of the executable edgesoftware file:

    ```bash
    chmod 755 edgesoftware
    ```

8. Run the command below to install the Reference Implementation:

    ```bash
    ./edgesoftware install
    ```

    >**NOTE:** Installation logs are available at the following path:
    ``/var/log/esb-cli/Intelligent_Traffic_Searching_Reference_Implementation_<version>/output.log``

9. When the installation is complete, you see the message “Installation of package complete” and the installation status for each module.

    ![A console window showing system output during the install process.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-install-success.png)

    Figure 3: Install Success

    >**NOTE:** If the pods have a status of “ContainerCreating”, please wait
    for some time, since Kubernetes will pull the images from the registry
    and then deploy them. This happens the first time the containers
    are deployed, and the wait time will depend upon the network bandwidth
    available.

10. If Intel® Smart Edge Developer Experience Kit (DEK) is installed, running the following command should show output similar
    to the outputs below. All the pods should be either in running or completed stage.

    ```bash
    $ kubectl get pods -A
    ```

    ![A console window showing system output after running the "kubectl get pods" command. The system displays a list of all the pods and the pod status. The expected status is "Running" or "Completed".](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-pods-status.png)

    Figure 4: Pods Status

11. If ITS RI is installed, running the following command should show output as follows:

    ```bash
    kubectl get pods -n smartedge-apps
    ```

    ![A console window showing system output after running the "kubectl get pods" command.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-its-pods.png)

    Figure 5: ITS Pods Status

##  Demonstration

This section will walk you through the ITS demo.

### Prepare Test Data

Create `/home/data` folder:

```bash
sudo mkdir -p /home/data && sudo chown $USER: $_
```

Download [DETRAC-test-data.zip](https://detrac-db.rit.albany.edu/Data/DETRAC-test-data.zip) to `/home/data/` and extract it.

```bash
cd /home/data
unzip ./DETRAC-test-data.zip
```

Create two folders:

```bash
mkdir -p /home/data/{images,metadata_ms}
```

Run the following commands to create script `select_subset_images.sh`:

   ```shell
   $ cat << 'EOF' > select_subset_images.sh
   #!/bin/bash

      function rand(){
       min=$1
       max=$(($2 - $min + 1))
       num=$(($RANDOM+1000000000))
       echo $(($num%$max + $min))

      }


   if [ $# -ne 2   ];then
       echo "USAGE $0 <ORIGINAL_DATASET_DIRECTORY> <CONVERTED_DATASET_DIRECTORY>"
       exit 1
   fi

   ORIGINAL_DATASET_DIRECTORY=$1
   CONVERTED_DATASET_DIRECTORY=$(realpath $2)

   mkdir -p ${CONVERTED_DATASET_DIRECTORY}
   cd ${ORIGINAL_DATASET_DIRECTORY} || { echo "${ORIGINAL_DATASET_DIRECTORY} no exit!"; exit 2;  }

   echo "start convert ......"
   for directory_name in $(ls)
   do
       cd $directory_name
       for filename in $(ls)
       do
           rand_no=$(rand 1 100)
           if [ $rand_no -le 10  ] # extract 10% of the dataset
           then
               cp $filename ${CONVERTED_DATASET_DIRECTORY}/${directory_name}_${filename}
               echo "cp $filename ${CONVERTED_DATASET_DIRECTORY}/${directory_name}_${filename}"
           fi
       done
       cd ..
   done
   echo "All done."
   ```

Use the script to select the subset images of dataset:

   ```shell
   $ bash select_subset_images.sh /hom/data/Insight-MVT_Annotation_Test /home/data/images
   ```

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

### Search Image

#### Login

Find the port number of *Intelligent Traffic Searching Web UI* using the command:

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

Figure 6: EVI Login Screen

> **NOTE**: The browser will display a warning for self-signed certificate, click **Advanced** and then **Proceed to…** link to continue.

#### Input image to search

![A browser window showing a large map of a city. Many vehicles are identified on the map. A rectangular area is highlighted in blue.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-query-image.png)

Figure 7: Map in Browser

1. Select the **rectangle icon** at the top right corner of the map, click and drag to select an area on the map.
2. Upload a vehicle image from the test dataset.
3. Specify filter criteria. The valid date range is `2021.08.10 - 2021.08.12`.
4. Click **Search** button.

#### Get Search Result

After you click *Search* button, the most-similar vehicle images will be shown in the WebUI as show in the following picture.

![A browser window showing a large map of a city. The right side of the window shows the search results pane.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-query-history.png)

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
    cd /home/smartedge/intelligent-traffic-searching
    ./edgesoftware list
    ```
    ![A console window showing the output of the "edgesoftware list" command. The installed modules are listed.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-esh-list.png)

    Figure 9: Module List

2. Run the command below to uninstall all the modules:

    ```bash
    ./edgesoftware uninstall -a
    ```

3. Run the command below to uninstall the Intelligent Traffic Searching reference implementation:

    ```bash
    ./edgesoftware uninstall <its-id>
    ```

    ![A console window showing the output of the "edgesoftware uninstall" command. At the end of the process, the system displays the message "Uninstall finished" and the uninstallation status for each module.](/content/dam/develop/external/us/en/images/reference-implementation/intelligent-traffic-searching-ri-esh-uninstall.png)

    Figure 10: Uninstallation Successful


## Summary and Next Steps

ITS is an easy-to-deploy cloud native software suite to meet the "image
searching in huge database" requirements in smart traffic management in diverse
applications for cities. As a next step, you can extend the Reference
Implementation with customized services helping widerapplication. You can also
visit ESH to try other Reference Implementations.


## Learn More

To continue learning, see the following guides:

-   [Intel® Smart Edge Developer Experience Kit (DEK)](https://smart-edge-open.github.io/ido-specs/doc/architecture/)
-   [Intel® Distribution of OpenVINO™ Toolkit](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)


## Support Forum

If you're unable to resolve your issues, contact the [Support
Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes).
