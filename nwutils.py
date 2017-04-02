import urllib2
import subprocess

def download_and_save(url, dest_dir):
	f = urllib2.urlopen(url)
	fname = url.split("/")[-1]	
	with open("%s/%s" % (dest_dir,fname), 'wb') as output:
		output.write(f.read())

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print proc_stdout


def download_and_install(url):
	f = urllib2.urlopen(url)
        data = f.read()
        cmd_set = ""
        for cmd in data.split("\n"):
            print "running: ", cmd
            cmd_set += cmd + " ; "
        print "Command Set: ", cmd_set
        subprocess_cmd(cmd_set)

if __name__ == "__main__":
    download_and_install("http://weavebytes.com/pitools/camera_setup.txt")




