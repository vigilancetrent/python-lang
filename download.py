# download file
def download(sock, remote_filename, local_filename=None):
	# check if file exists
	if not local_filename:
		local_filename = remote_filename
	try:
		f = open(local_filename, 'wb')
	except IOError:
		print "Error opening file.\n"
		Send(sock, "cd .")
		return
	# start transfer
	Send(sock, "download "+remote_filename)
	print "Downloading: " + remote_filename + " > " + local_filename
	time.sleep(interval)
	fileData = Receive(sock)
	print "> File size: " + str(len(fileData))
	time.sleep(interval)
	f.write(fileData)
	time.sleep(interval)
	f.close()

# upload file
def upload(sock, local_filename, remote_filename=None):
	# check if file exists
	if not remote_filename:
		remote_filename = local_filename
	try:
		g = open(local_filename, 'rb')
	except IOError:
		print "Error opening file.\n"
		Send(sock, "cd .")
		return
	# start transfer
	Send(sock, "upload "+remote_filename)
	print 'Uploading: ' + local_filename + " > " + remote_filename
	while True:
		fileData = g.read()
		if not fileData: break
		Send(sock, fileData, "")
		print "File size: " + str(len(fileData))
	g.close()
	time.sleep(interval)
	Send(sock, "")
	time.sleep(interval)
	
# refresh clients
def refresh():
	clear()
	print '\nListening for clients...\n'
	if len(clients) > 0:
		for j in range(0,len(clients)):
			print '[' + str((j+1)) + '] Client: ' + clients[j] + '\n'
	else:
		print "...\n"
	# print exit option
	print "---\n"
	print "[0] Exit \n"
	print "\nPress Ctrl+C to interact with client."
