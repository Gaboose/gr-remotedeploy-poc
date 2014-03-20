import execnet
import time

WAIT_SECS = 10

if __name__ == '__main__':
    gw = execnet.makegateway()
    f = open('dial_tone.py', 'r')
    ch = gw.remote_exec(f.read())
    f.close()

    print "Remote application started."
    print "Request termination in %d seconds." % WAIT_SECS
    time.sleep(WAIT_SECS)
    ch.send("stop")
    print "Remote application stopped."
    gw.exit()
