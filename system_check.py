import subprocess

def system_check():
	system = subprocess.check_output(['uname', '-a'])
	disk_space = subprocess.check_output(['df', '-h'])
	interfaces= subprocess.check_output(['ifconfig', '-s'])
	return system + disk_space + interfaces
	
def write(data):
	print(data)
	subprocess.call(['echo %s' % data, '>', 'system_data.txt'])
	print('Data written to file.')
	

def main():
	data = system_check()
	write(data)

if __name__ == '__main__':
	main()
