# Name of RI or Use Case
## Overview 
Provide a 2-3 line description of what this RI/use case allows the developer to do. 

>NOTE: Keep this section easy to understand. The goal of the RI should be
>clearly defined to showcase a key feature or function. Make it easy for users
>to understand what the input and output is.

Select **Configure & Download** to download the reference implementation and the software listed below.   

[Configure & Download](URL for downloading from ESH)

>NOTE: All indents must be 4 spaces for correct import into the AEM tool.

-   **Time to Complete:** 

    >NOTE: Provide an accurate time for how long it will take the user to
    >complete the RI install through completion. This should be easy to download
    >and install. The installation of an entry-level RI should take minutes and
    >not hours. 

-   **Programming Language:** 

-   **Available Software:** 

-   **GitHub Source Code:** 

    >NOTE: Please provide an alternate option for install for PRC users. 


### Recommended Hardware
The hardware below is recommended for use with this reference implementation. See the [Recommended Hardware](https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/hardware.html?s=Newest) page for other suggestions. 
-   Name of HW
-   Name of HW


## Target System Requirements 
-   Disk Space needed 
-   Other Reqs
    -   sub-bullet
    -   sub-bullet

 
## How It Works 
>NOTE: Provide description, including architecture diagram, of how the RI/use
>case works. All diagrams and screenshots must have alt-text and captions.

![Add alt-text description of image here.](images/ri-name-simple-arch-diagram.png)

Figure 1: Simple Architecture Diagram  

![Add alt-text description of image here.](images/ri-name-complex-arch-diagram.png)

Figure 2: Complex Architecture Diagram

>NOTE: Please provide 2 architecture diagrams. The first should be simple and
>easy to understand. The second can be more complex and contain more details.
>Both should include written descriptions for the caption for users who are
>unable to see the diagrams.  

## Get Started  
Provide step-by-step instructions for getting started.

>NOTE: Keep these easy to run. Avoid coding and manual configurations after
>installation. The input, or the configuration of the input, must be included in
>the package.  
 

### Step 1: Install the Reference Implementation 

Select **Configure & Download** to download the reference implementation and then
follow the steps below to install it.

[Configure & Download](URL for downloading from ESH)

>NOTE: All indents must be 4 spaces for correct import into the AEM tool.
>Code snippets must have the file type, we use "bash" for most instances.

1.  Open a new terminal, go to the downloaded folder and unzip the downloaded RI
    package.

    ```bash
    name_of_ri.zip
    ```


2.  Go to the ``name_of_ri/`` directory.

    ```bash
    cd name_of_ri /
    ```


3.  Change permission of the executable edgesoftware file.

    ```bash
    chmod 755 edgesoftware
    ```
 

4.  Run the command below to install the Reference Implementation.

    ```bash
    ./edgesoftware install
    ```


5.  During the installation, you will be prompted for the **Product Key**. The
    **Product Key** is contained in the email you received from Intel confirming
    your download.

    <Screenshot of Product Key terminal with key removed>

    ![A console window showing a system prompt to enter the product key.](images/ri-name-product-key.png)

    Figure 3: Product Key

6.  When the installation is complete, you see the message "Installation of
    package complete" and the installation status for each module.

    <Screenshot of Install Success>

    ![A console window showing system output during the install process. At the end of the process, the system displays the message "Installation of package complete" and the installation status for each module. ](images/ri-name-install-success.png)

    Figure 4: Installation Success
 
### Step 2: Provide Name of Action 
Provide details of what should happen in this step. 

1.  step 1

    ```bash
    code snippet
    ```

2.  step 2



## Run the Application 
Provide detailed steps of running the application. 

1.  step 1

    ```bash
    code snippet
    ```

2.  step 2


## Build a Solution Based on the RI/use case 
Provide a description/procedure for how they build a solution based on RI/use case.  

1.  step 1

    ```bash
    code snippet
    ```

2.  step 2


## Summary and Next Steps 
Provide 2-3 line description of what they have successfully done and where they should go to as the next step. 


## Learn More 
To continue learning, see the following guides and software resources: 
-   Provide a bullet list of relevant links
-   Provide a bullet list of relevant links


## Troubleshooting 
Provide Troubleshooting steps.

## Known Issues 
-   Provide a bullet list of issues
-   Provide a bullet list of issues
 
### Support Forum 
If you're unable to resolve your issues, contact the [Support Forum](https://software.intel.com/en-us/forums/intel-edge-software-recipes). 
