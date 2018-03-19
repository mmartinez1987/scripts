import os

class run(object):
	
	def __init__(self, cmd):
		self.cmd = cmd

	def run(self):
		execute = os.system
		execute(self.cmd)
		print('%s command has been executed' % self.cmd)
		
def main():
	cmd = raw_input("Please enter command to run: ")
	test = run(cmd)
	test.run()
	
	

if __name__=='__main__':
	main()
  



