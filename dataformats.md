# Data Formats

# Rat Node
JSON representation of the data from the sensors.

    0.1:{"t":421622,"y":-143.15,"p":6.25,"r":-37.31,"X":181,"Y":153,"Z":-279}
    0.2:{"time":381245,"ypr":{"y":88.66,"p":0.90,"r":0.79},"acceleration":{"x":-8,"y":4,"r":-79}}

    error:{"msg": "FIFO overflow","data":{"int":19,"count":1024}}


# Data Node
A java object of the Rat Node + stamp of the phone


# Callback
TBD
    (time "", phoneStamp "", state "", strength float, reason "", engine {}, metadata {})

# Intents
## BT setup 
## BT list
## State change
## Error
## Start recording
## Stop recording
## Dump session
