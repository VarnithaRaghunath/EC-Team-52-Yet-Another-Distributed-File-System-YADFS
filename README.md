# EC-Team-52-Yet-Another-Distributed-File-System-YADFS

Yet Another Distributed File System (YADFS) is a project developed as part of the Big Data Course (UE21CS343AB2) at PES University. The primary goal of YADFS is to create a distributed file system that efficiently manages and stores large volumes of data across multiple machines. This system is designed to handle big data workloads, providing fault tolerance, scalability, and ease of use.

# High Level Architecture
<img width="476" alt="image" src="https://github.com/VarnithaRaghunath/EC-Team-52-Yet-Another-Distributed-File-System-YADFS/assets/150449637/d9a01467-bb0b-49d4-a358-2910d88dabe0">

## Procedure To Run

### Using Docker Containers

1.Start [Docker Desktop](https://www.docker.com/products/docker-desktop/) \
2.cd into directory containing repository \

3.Run 
```sh
docker pull VarnithaRaghunath/yadfs-node
```
4.(Use only to build docker image from Dockerfile)  Ignore this step if image is pulled through docker hub
```sh
docker build -t yadfs-node -f .\Dockerfile3 .
```
5.Start Docker Containers   (Here ubuntu=Number of Datanodes + Namenode)
```sh
docker-compose up -d --scale ubuntu=6
```
6.Retrieve IP Addresses of docker containers by running DockerNetwork.py which stores IPAddresses to config.json  (Locally in Host OS)
```sh
python DockerNetwork.py
```
7.Use separate terminals to run Client, Namenode and Datanodes, follow this sequence \
To Start Datanode n (n=1 is reserved for Namenode and n=2 is reserved for Client) use
```sh
docker exec -it yet-another-distributed-file-system-main-ubuntu-n python3 /usr/files/DataNode.py
```
To Start Namenode
```sh
docker exec -it yet-another-distributed-file-system-main-ubuntu-1 python3 /usr/files/NameNode.py
```

To Start Client (Make sure the files you want to Upload to the DFS is in the files folder)
```sh
docker exec -it yet-another-distributed-file-system-main-ubuntu-2 python3 /usr/files/Client.py
```
<img width="288" alt="image" src="https://github.com/VarnithaRaghunath/EC-Team-52-Yet-Another-Distributed-File-System-YADFS/assets/150449637/f4f4ec9e-cb51-4ebd-af77-dec66e592448">
