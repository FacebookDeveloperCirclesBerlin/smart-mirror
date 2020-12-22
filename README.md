PRIVATE Smart-Mirror
===

Description
---
This is my version of the smart mirror I am building. I am using Python3 and `tkinter`.

Run the project
---

To make it work on mac, you need to do some steps:
- install xquartz & allow client connection (https://www.xquartz.org)
- add xhost: `xhost + 127.0.0.1` to allow access to the screen from localhost. You might have to re-run that command after every reboot.

And then:

run
```
make run-last
```

build the project

```
make build
```

Run the last succeeded built

```
make run
```

Installation
---

Create a .env file with the following content:

```
API_CITY=Berlin,DE
API_METRICS_UNIT=metric
API_APP_ID=xxx
WEATHER_DISPLAY_CITY=Berlin, Germany
FIRSTNAME=yyy
```