<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

  - [access2sqlite](#access2sqlite)
  - [Requirements](#requirements)
- [Installation](#installation)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### access2sqlite

Import access databases into SQLITE   

### Requirements

docker must be installed

## Installation

```
git clone https://github.com/serioca/access2sqlite
cd access2sqlite
./docker-build
cp [your-access-db-file].mdb ./data
cp [another-access-db-file].mdb ./data
./docker-run
```

the tool will create for each `[file].mdb` present in the directory `./data` a new converted `[file].sqlite` :

`[your-access-db-file].sqlite`

`[another-access-db-file].sqlite`

