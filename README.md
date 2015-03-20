# Weather Application

## Introduction
---
<Project Name> is an AGL Open Source HTML5 proof-of-concept application. It is capable of <X>, <Y>, and <Z>.

## Maintainers
---
The primary maintainer of the project is <FirstName LastName>
He/She can be contacted at <email>@jaguarlandrover.com

## Dependencies
---
To run the software, the project requires the following:
* A platform running AGL release <x>.<y> or greater
* Installed extension version <x>.<y>
* A network connection with access to server <server_name.com>
* The built widget, installed on the platform.
* GBS, meeting the requirements laid out at Crosswalk (https://crosswalk-project.org/documentation/tizen_ivi_extensions.html)

## Getting Started
---
Built releases of <project name> are available at the [Automotive Grade Linux site](https://www.automotivelinux.org/software/). It is recommended if you simply want to interact with the software that you get the most recent stable release from AGL. Further instructions are provided below for building and deploying from source.

## Building
---
#### Building Widgets
Make files are provided in repositories to package widgets for installation on AGL. 

To build and copy the wgt files to the platform: `make deploy`  
To build and install widgits on the platform: `make install.feb1`  
To build, install and run on the platform: `make run.feb1`

#### GBS Build Process
Makefiles should work for HomeScreen but spec files need to be updated so an rpm build won't work.  
To build, use: `gbs build -A i586`

All extensions are identified with the _ext suffix of their directory name. 
 * *extension_common* is a static library that must be linked into all extensions.
 * *extension_tools* contains the tool to create the XWalk boilerplate code from the javascript template.

## Contributing
------------
If you would like to contribute to the project, please fork into your github account. Develop your code changes, test and commit. Issue a pull request to the <project repo name>. The pull request will go through the review process at GerritHub and merged, or rejected if necessary.




