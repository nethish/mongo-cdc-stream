# MongoDB CDC Stream 
## Python
* Install pymongo
* Start up the server
* Insert docs 
```
docker exec -it mongo1 mongosh

use test

db.users.insertOne({name: "nethi", age: 25})
```

* The change events should be reflected in the python output

## Go
* `go run main.go`
* Same as above
