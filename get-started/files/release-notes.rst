.. _release-notes:

Release Notes
=============


New in this Release
-------------------


-  Vehicle Event Recording Reference Implementation - Added an option to
   use the Road Segmentation model in parallel with the already
   delivered Obstacle Detection model on all video streams.


-  Address Recognition and Analytics Reference Implementation


-  Work Zone Analytics Reference Implementation


Known Limitation
----------------


The Reference Implementations (RIs) in the 2022.1 release do not support
parallel execution with older versions of Edge Insights for Fleet. The
compatibility matrix below shows that RIs listed in the same column can
be executed in parallel.


For example, in Edge Insights for Fleet version 2022.1 only three
reference implementation may run in parallel: Vehicle Event Recording
version 2022.1, Address Recognition and Analytics version 2022.1 and
Work Zone Analytics 2022.1


.. list-table:: 
   :header-rows: 1

   * -  **Reference Implementation**
     -  **Parallel Execution Feature**
     -  *DELETE ME*
     -  *DELETE ME*
     -  *DELETE ME*
   * -  *DELETE ME*
     -  **Edge Insights for Fleet 2021.1**
     -  **Edge Insights for Fleet 2021.2**
     -  **Edge Insights for Fleet 2021.3**
     -  **Edge Insights for Fleet 2022.1**
   * -  **Vehicle Event Recording**
     -  Not Supported (1)
     -  Supported (2)
     -  Supported (2)
     -  Supported (2)
   * -  **Driver Behavior Analytics**
     -  Not Supported (1)
     -  Supported (2)
     -  Supported (2)
     -  N/A
   * -  **Cargo Management**
     -  N/A
     -  Supported (2)
     -  Supported (2)
     -  N/A
   * -  **Public Transit Analytics**
     -  N/A
     -  N/A
     -  Supported (2)
     -  N/A
   * -  **Automated License Plate Recognition**
     -  N/A
     -  N/A
     -  Supported (2)
     -  N/A
   * -  **Address Recognition and Analytics**
     -  N/A
     -  N/A
     -  N/A
     -  Supported (2)
   * -  **Work Zone Analytics**
     -  N/A
     -  N/A
     -  N/A
     -  Supported (2)




**Table Notes:**


#. Not Supported - Parallel execution was not implemented on Edge
   Insights for Fleet 2021.1.
#. Supported - The RI can be executed in parallel with other RIs using
   the same Edge Insights for Fleet version, which are listed in the
   same column.
#. N/A - The Reference Implementation was not delivered for this version
   of Edge Insights for Fleet.


Edgesoftware CLI Features
-------------------------


Initial Features for Recommended Configuration


-  


   .. container::
      :name: LI_919D9BE2982744769F8262151DD8C733


      Installs Docker CE\*


-  


   .. container::
      :name: LI_77A2E68C36CB4A6DA1903AFE1BB51E17


      Installs Docker Compose\*


-  


   .. container::
      :name: LI_5533C6209A654B92B6A1DD1741D524AB


      Installs all the prerequisites and dependencies for the Edge
      Insights for Fleet.


-  


   .. container::
      :name: LI_7F887EE696BE4BA3BABB0EB4BB7F8166


      Installs and sets up Edge Insights for Fleet.


-  


   .. container::
      :name: LI_8FD16B3AAF814F2186FA15C6CA400EF0


      Brings up all container images as per the use case selected during
      Edge Insights for Fleet installation.


-  


   .. container::
      :name: LI_9E0BC0BA8BA3485BB12C4C833D9CA1F8


      Supports the following reference implementations:


      -  


         .. container::
            :name: LI_CB20E6535E744168A84B65123CB785FE


            Vehicle Event Recording


      -  


         .. container::
            :name: LI_FF6FAB8FDAF84CD0B34071545B9D95C6


            Driver Behavior Analytics


      -  Cargo Management


**Edge Insights for Fleet Features:**


-  Video Analytics


-  Video Ingestion


-  Training and Learning Suite (TLS)


-  Image Store

