# test rig
import sys
from vs import virtsim

from time import sleep


tty_path = "/dev/tty.Bluetooth-Incoming-Port"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        testfile_name = sys.argv[1]
    else:
        testfile_name = "v2_20170205_test_data"

    sleep_time = float(1)/float(3) # little slow, but good for debugging at the moment

    vsim = virtsim(tty_path)
    counter = 0;
    with open(testfile_name, "r") as ins:
        for line in ins:
            vsim.send(line)
            print(counter)
            sleep(sleep_time)
            counter += 1
    print("")
    print("~ Fini ~")
