from PythonSeleniumPractice.UtilitiesDemo.utilites import GeneratingLogs

logger = GeneratingLogs.generate_logs()
logger.info("Python Code execution started")
for i in range(1,6):
    print(i)
    logger.info("The current value of i is: "+ str(i))

logger.info("Python Code execution ended")