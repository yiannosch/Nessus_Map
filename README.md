# Nessus Map
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&v=1.0)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

**Nessus XML Praser**
<img src="https://i.imgur.com/gtw4lVP.png" />

### Requirements
- Python3
- Django
- Docker
- docker-compose

### Tested on
- Ubuntu 18.04

### What it does
- Vulnerability based parsing
- Service based parsing
- Host bases parsing
- Unsupported OS parsing
- Generate Executive Summary of scan
- Export parsed .nessus(s) to JSON file(s)  
- Import JSON file in Nessus_Map

### How it works
<pre>Create XML directory in Nessus_Map home directory and place all .nessus files under XML directory and start server.</pre>

### Setting up with Docker
- Run the code
```bash
$ git clone https://github.com/yiannosch/Nessus_Map
$ cd Nessus_Map
$ docker-compose up
```
- Access web server on `http://127.0.0.1:1337`
- Login using administrator user. Default credentials are included in `entrypoint.sh` file. (:warning:Don't forget to change the default password via django admin page)

### How to Setup
- Clone this repo `https://github.com/Ebryx/Nessus_Map.git`
- Change directory `cd Nessus_Map`
- Create a directory named `XML`
- Copy all `.nessus` files in `XML` directory
- Start server with `python3 manage.py runserver`

### Setting up with Python's Virtualenv
```bash
git clone https://github.com/Ebryx/Nessus_Map
cd Nessus_Map
mkdir env
mkdir XML
cd env
python3 -m venv . 
source bin/activate
cd ..
pip3 install -r requirements.txt
python manage.py runserver
```

### Authentication Page
<img src="https://i.imgur.com/Vrs2qxt.png" />

### Vulnerability Parsing

<img src="https://i.imgur.com/etrzGc3.gif" />


### Host Parsing

<img src="https://i.imgur.com/sgZp1AI.png" />


### Services Parsing

<img src="https://i.imgur.com/FZUFRKm.png" />


### Executive Reoprt

<img src="https://i.imgur.com/J4vrkD7.png" />

<img src="https://i.imgur.com/vWeU257.png" />


### Export parsed .nessus(s) to JSON file(s)

<img src="https://i.imgur.com/aQaPBZm.gif" />


### Import JSON file in Nessus_Map

<img src="https://i.imgur.com/oDBuD8r.gif" />
