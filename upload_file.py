import os, sys


def curl_upload_file(filepath, machine_id, user_id, assay_id):
    """ Uses curl to upload a file. Returns a bool with the success state. """
    curl_cmd = "curl --form upload=@'{0}' --form machine_id='{1}' --form user_id='{2}' --form assay_id='{3}'  http://localhost:5000/upload_file".format(filepath, machine_id, user_id, assay_id)

    return os.system(curl_cmd) == 0


def print_usage():
    print ""
    print "Usage: Upload_file <absolute_filepath> <machine_id> <user_id> <assay_id>"
    print ""

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print_usage()
        sys.exit(-1)
    sys.exit(curl_upload_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
