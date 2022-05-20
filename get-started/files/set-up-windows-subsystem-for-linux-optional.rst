.. _set-up-windows-subsystem-for-linux-optional:

Set Up Windows\* Subsystem for Linux\* (Optional)
=================================================


You can use the Windows\* Subsystem for Linux\* (WSL) if you don't want
to install a standalone Ubuntu\* machine.


**Prerequisites**


-  Minimum Windows 10 is required.


   To check your windows version, press the **Windows logo key + R**.
   Type ``winver`` and select **OK**.


-  You must have at least 40 GB storage available.


Procedure
---------


-  If your Windows 10 version is older than 2004, you must do the first
   5 steps in this guide before continuing:


   https://docs.microsoft.com/en-us/windows/wsl/install-manual


   Then continue with the steps below.


-  If your version is 2004 (Build 19041) or higher, perform the steps
   below.


#. Open Windows PowerShell*.


#. Run the following command to install the Ubuntu 18.04 distribution:


   .. code-block:: bash


      wsl --install -d Ubuntu-18.04


   As a result, Ubuntu 18.04 will start and in a few minutes a pop-up
   window will ask you for username and password. After the install
   ends, the pop-up window is a Ubuntu18.04 terminal.


   You must follow the instructions in the order shown to complete the
   installation successfully.


#. If your machine is behind a proxy network, make sure you set proxies
   for ``apt`` and for the system. If your machine is not behind a
   proxy, you can skip this step.


   .. note::


      Replace the http/https links and ports in the commands presented
      below with your proxies links and ports.


   a. Set up apt proxies:


      .. code-block:: bash


         sudo touch /etc/apt/apt.conf.d/proxy.conf
         sudo echo "Acquire::http::proxy \"http://http_proxy_link:http_proxy_port/\";" | sudo tee -a /etc/apt/apt.conf.d/proxy.conf
         sudo echo "Acquire::https::proxy \"http://https_proxy_link:https_proxy_port/\";" | sudo tee -a /etc/apt/apt.conf.d/proxy.conf


   b. Add your proxy settings to ``~/.bashrc`` as well for http, https
      and no_proxy.


      .. code-block:: bash


         export http_proxy=http://<http_proxy_link>:<http_proxy_port>
         export https_proxy=http://<https_proxy_link>:<https_proxy_port>
         export no_proxy=localhost,127.0.0.1/8, hostIp


   c. Reboot from the Windows PowerShell by using the following steps:


      i.   Open another Windows PowerShell as administrator and run the
           following command:


           .. code-block:: bash


              Get-Service LxssManager | Restart-Service


      ii.  In the user Windows PowerShell, run the following command to
           relaunch Ubuntu.


           .. code-block:: bash


              wsl -d Ubuntu-18.04 


      iii. At this point, Windows PowerShell will give access to Ubuntu
           and the prompt should look like this:


           .. code-block:: bash


              user@<hostname>:/mnt/c/Users/User


#. Update your Ubuntu distribution with the command:


   .. code-block:: bash


      sudo apt-get update && sudo apt-get upgrade -y


#. Set up Windows RDP in order to cover the Reference Implementation
   prerequisites where you need GUI.


   a. Install ``xfce`` with the command:


      .. code-block:: bash


         sudo apt-get install -y xfce4 xfce4-goodies


   b. Install ``xrdp`` with the command:


      .. code-block:: bash


         sudo apt-get install -y xrdp


   c. Configure ``xrdp`` with the following commands:


      i.   Comment the last two lines, add "``startxfce4``" at the end
           of the following file, and save:


           .. code-block:: bash


              sudo nano /etc/xrdp/startwm.sh 


      ii.  Copy the original ini file as bak format.


           .. code-block:: bash


              sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak


      iii. Change the xrdp port to not have a conflict with windows OS
           port and complete configuration by running the following
           commands:


           .. code-block:: bash


              sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
              sudo sed -i 's/max_bpp=32/#max_bpp=32\nmax_bpp=128/g' /etc/xrdp/xrdp.ini
              sudo sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini
              echo xfce4-session > ~/.xsession


      iv.  Enable ``dbus`` and start both ``dbus`` and ``xrdp`` services
           with the commands:


           .. code-block:: bash


              sudo systemctl enable dbus
              sudo /etc/init.d/dbus start
              sudo /etc/init.d/xrdp start


#. Install missing component with the command:


   .. code-block:: bash


      sudo apt-get install –y zenity


#. Bypass timedatectl to allow EII core Docker images to be deployed:


   .. code-block:: bash


      sudo rm /usr/bin/timedatectl
      sudo nano /usr/bin/timedatectl


   Add the content:


   .. code-block:: bash


      #!/bin/bash
      exit 0


#. Enter the command:


   .. code-block:: bash


      sudo chmod 777 /usr/bin/timedatectl


#. Open Remote Desktop Connection windows application and type
   localhost:3390 for "Computer" and connect, login with the username
   and password from step 1.


#. After login, click on **Use Default Config**.


#. Set up for Reference Implementations.


   a. Run ``source /etc/environment`` if you are behind a proxy.


   b. Install your preferred browser. This example uses Firefox*.


      .. code-block:: bash


         sudo apt-get install -y firefox


   c. Create a Docker group and add your user to the group with the
      commands:


      .. code-block:: bash


         sudo groupadd docker
         sudo usermod -aG docker $USER


   d. Log out and reconnect via the Remote Desktop Connection windows
      application.


#. Open a terminal and start a web browser in the background. This
   example uses Firefox.


   a. ::


         firefox &


   b. Open the <RI link>.


   c. Download the recommended archive.


   d. In the terminal, run the command:


      .. code-block:: bash


         cp <archive> ~/ 


   e. Unzip the archive and install.


.. note::


   To delete the distro, use the command:
   ``wsl --unregister Ubuntu-18.04``


Known Limitations
-----------------


#. WSL distros are based on init.d not systemd, so the Docker daemon is
   not started after installation. The first installation will fail. The
   workaround is to start the Docker daemon first, before retrying the
   installation:


   .. code-block:: bash


      sudo /etc/init.d/docker start


#. After restarting the WSL distro, you have to manually start ``dbus``,
   ``xrdp``, and Docker using the commands:


   .. code-block:: bash


      sudo /etc/init.d/dbus start
      sudo /etc/init.d/xrdp start
      sudo /etc/init.d/docker start


#. If you receive the Docker error ``toomanyrequests``, you may need to
   create an account for Docker Hub. After that, login using your
   credentials:


   .. code-block:: bash


      sudo docker login


#. If Visualizer does not start, try to restart the ``dbus`` and
   reconnect via ``rdp`` with WSL Ubuntu virtual machine:


   .. code-block:: bash


      sudo /etc/init.d/dbus restart


#. GPU and VPU are not available in WSL. The RI can be launched only on
   CPU.

