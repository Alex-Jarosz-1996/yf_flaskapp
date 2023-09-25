# Yahoo Finance Australia/US Stock Screener
This project allows the user to screen Australian and US stocks.
The user can compare Australian or US stocks on over 50 different metrics.
(Full list of metrics are found in the stock_metrics.md file)


## Use me
The app can either be used via the command line, or through the RunApp.bat file:
### Command line terminal
Enter the following command into a bash terminal:
```
$ python app.py
```

### RunApp.bat file
Open the application in the **yf_flaskapp** directory;
1. Double-click on the RunApp.bat file
2. Select the http weblink (hold the ctrl command, click the http link)

Link will be http://127.0.0.1:5000

## Docker
The program can be built and ran through Docker with the following steps:
1. Build the docker image:
```
$ docker build -t yf_app:1.0 .
```

2. Run the docker container:
```
$ docker run -p 5000:5000 yf_app:1.0
```

The program can be accessed in thr browser in the following address:
```
http://localhost:5000
```
or
```
http://127.0.0.1:5000
```