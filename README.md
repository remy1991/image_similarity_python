# Image Similarity App

<!-- vim-markdown-toc GFM -->

* [Introduction](#introduction)
* [How does the application work?](#how-does-the-application-work?)
* [How to use?](#how-to-use-the-application?)
* [How to make sure the code works?](#how-to-make-sure-the-code-works?)
* [How to check for updates?](#how-to-check-for-updates?)
* [How to push updates (For maintainers)?](#how-to-push-updates?)

<!-- vim-markdown-toc -->

## Introduction

This project has been created to help anyone who wants to check similarity between pair of images by giving a similarity score where 0 signifies that the images are same. The main application is written in python3 where the python script takes a csv file as input and outputs in a csv format into a file if given else spills it out on stdout. The design decisions, why a particular approach was chosen and steps taken to implement the application have been described in details in the following sections where each section describes way to use, maintain and effectively distribute the application making it more intuitive to use. 

## How does the application work?

The python script (similarity.py) is using two important python modules namely Pillow and ImageHash. ImageHash is the important module using which we are able to calculate hash of the images not based on binary content but based on visual appearance. 
> Perceptual hashes are a different concept compared to cryptographic hash functions like MD5 and SHA1. With cryptographic hashes, the hash values are random. The data used to generate the hash acts like a random seed, so the same data will generate the same result, but different data will create different results. Comparing two SHA1 hash values really only tells you two things. If the hashes are different, then the data is different. And if the hashes are the same, then the data is likely the same. (Since there is a possibility of a hash collision, having the same hash values does not guarantee the same data.) In contrast, perceptual hashes can be compared -- giving you a sense of similarity between the two data sets.

Using the imagehashes of the pair of images, the similarity fuction is returning the similarity score which is ultimately stored in the output. 

## How to use the application?

The project has been packaged in two way. The decision of chosing either way is based on ease of using, better distribution, being platform agnostic and keeping team collaboration in mind. Following are the two way in which one can chose to use the application

### Git
Git simplifies the processing of working with teams across the board, reduces collaboration issues across team members. Team members can work independently without creating any kind of hinderance. Following are the steps that need to be executed in order to install all the necessary packages, modules, access the app and run the scripts

```
On Terminal (MacOS)

$ brew install python
$ brew install git
$ git clone https://github.com/remy1991/image_similarity_python.git
$ cd image_similarity_python
$ pip install -r requirements.txt
$ python3 similarity.py --help 			# Printing help to check all the available arguments
$ python3 similarity.py --input-csv <absolute path to input csv> --output-csv <absolute path to output csv>
```

```
On Powershell (Windows)

Download and install required components first
- Download git from https://git-scm.com/download/win and install
- Download python using https://docs.microsoft.com/en-us/windows/python/beginners

After installation, execute following commands on powershell
PS C:\Users\ravi\> git clone https://github.com/remy1991/image_similarity_python.git
PS C:\Users\ravi\> cd image_similarity_python
PS C:\Users\ravi\image_similarity_python\> pip install -r requirements.txt
PS C:\Users\ravi\image_similarity_python\> python3 similarity.py --help   # Printing help to check all the available arguments
PS C:\Users\ravi\image_similarity_python\> python3 similarity.py --input-csv <absolute path to input csv> --output-csv <absolute path to output csv>
```

**Note that '--input-csv' is mandatory argument whereas '--output-csv' is optional. In case '--output-csv' is missing, output will printed on stdout**

### Docker
Docker has been chosen as a packaging medium because of docker being agnostic of platorm. One can package a complete application along with all the dependencies using a docker image and the user just needs to have docker installed and rest can be taken care by running docker commands. Considering how it makes using an application convenient without worrying abaout the dependeny cycles, the application has been packaged as a docker image and following are the steps that needs to be executed in order to access the application. 

```
On Terminal (MacOS)

$ brew install docker
$ docker pull remy1991/image_similarity_app
$ docker run -v <host path where input/output csv is present>:<container path for input/output csv> -v <host path where all the images are present>:<container path to be same as host path> image_similarity_app:<latest tag of image> --input-csv <path to input csv> --output-csv <path to output csv>
```

```
On Powershell (Windows)

Download and install docker for windows following steps from https://docs.docker.com/docker-for-windows/install/

After Installation
PS C:\Users\ravi\> docker pull remy1991/image_similarity_app
PS C:\Users\ravi\> docker run -v <host path where input/output csv is present>:<container path for input/output csv> -v <host path where all the images are present>:<container path to be same as host path> image_similarity_app:<latest tag of image> --input-csv <path to input csv> --output-csv <path to output csv>
```

## How to make sure the code works?

Since the application is written in python, python unittest module has been used to assert functionality of various code components. More unittests can be added to assert the functionality of future addition or changes to existing code. **unittests.py** has all the test cases where one can modify the existing test cases or add new ones. 

## How to check for updates?

There is a provision in the python script (check\_for\_updates.py) which essentially checks if there is any update present by comparing current local git tag and what is the latest tag present at the repository. The code snippet will be executed along with the main script (similarity.py) but the updates will be checked based on specified timeframe and then it will be cached till the next time. For e.g. the updates will be checked every 24 hours as per the threshold in the code. **git tag** has been used as the base for checking for future updates. Though the user does not have to worry about the intimation of the update but in order to use the latest version, manual steps are involved (but can be easily automated with few tweaks)

Sample output

```
If there is no update present
>>> python check_for_updates.py
... Everything is up to date

If there is update present
>>> python check_for_updates.py
... There is a new update. Please perform "git pull" first. In case of docker, please do "docker pull image_similarity_app:<given tag>"
```

## How to push updates?

The application is very simple to understand making it easy for other developers to contribute, purpose and implement changes, optimize it further based on requirements. Supportive scripts have been added to the git repository so that simple continous integration and continous delivery is supported. Following are various ways in which one can actively develop and maintain the application. 

Since everything is maintained via a git repository, after every change, following steps should be executed from the git cloned directory

```
$ cd image_similarity_python
$ git commit -am "<commit message>"
$ git tag -a <tag>
$ git push -u origin master --follow-tags
$ ./build.sh <tag>
```
**build.sh** will create a docker image and push it to docker hub under namespace remy1991. This can be modified as per requirement and the information of the new docker image should be circulated amongst the users. **git tag** command is necessary since the 'check for updates' code is completely dependent on that and in case something is not correct with the tags, users wont be able to get the updated version of the application. Also make good use of **unittests.py** before pushing the changes to make sure everything works as expected. 


## Notes

There are various other things that could have been considered while implementing like packaging the application using deb/rpm packages or included more granular control with bash scripts but since there is a requirement to support multiple operating systems, not all implementaions are straighforward and hence the approaches which are platform agnostic are given preference here. 