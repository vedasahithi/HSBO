# CloudSim modules
from Main.Cloudsim.Scenario import *
from Main.Cloudsim.Scheduler import *
from Main.Cloudsim.SchedulingAlgos import *
from Main.Cloudsim.TaskGenerator import *
from Main.Cloudsim.Task import *
from Main.Cloudsim.AbstractResource import *
from Main.Cloudsim.CloudMachine import *
from Main.Cloudsim.Parameters import Entities

# Used in round robin scheduler
from Main.Cloudsim.cloud_parameters import cloud_compute
inputFile = 'input'
totalJobs = 0

def cloud_sim():
    currentMachine = 0
    '''arguments = [
                 ('--input', 'input file', 'input file path',  ),
                 ('--conf', 'simulation conf file', 'config file path', )
                 ]'''

    arguments = [
        ['--input', 'input', '', ],
        ['--conf', 'scheduler.conf', '', ]
    ]

    inputFile = 'input'
    conf = 'scheduler.conf'

    def usage():
        string = 'USAGE:\n'
        global arguments
        for arg in arguments:
            string = string + ('Argument: %s (%s) - type: %s\n' % arg)

        string += '\nArguments are passed as follow: simgrid.py --argument-name value'
        return string

    def parse_args():

        import sys

        if len(sys.argv) == 1:
            print()

        args = sys.argv[0:]

        if (len(args) < 4):
            print()

        scenario = None
        index = 0
        args = arguments
        while index < len(args):

            # input files
            if args[index][0] == '--conf':
                conf = args[index][1]
                scenario = CloudSimScenario(conf)
            elif args[index][0] == '--input':
                global inputFile
                inputFile = args[index][1]
                print("Input File : ", inputFile)
            else:
                raise (Exception, 'Unknown option:' + str(args[index]))
            index += 1

        return scenario

    def run(scenario, verbose=True):

        initialize()
        scenario.init_objects()
        print_initial_data(scenario)
        init_task_generators(scenario)
        scenario.printSep()
        simulate(until=scenario.sim_time)
        scenario.finish_objects()
        print_result(scenario)
        scenario.executeMonitorPlots()
        return scenario, now()

    def init_task_generators(scenario):
        global inputFile
        global totalJobs
        inputFile = open('input', 'r')
        # Remove trailing endline characters
        temp = map(lambda x: x.strip(), inputFile.readlines())
        params = []
        for each in temp:
            y = each.split()
            # Remove commas from each input element except the last
            # params = (map(lambda x: x[:-1], y[:-1]) + [y[-1]])
            params = 10
            taskGenerator = TaskGenerator(scenario, [params])  # Generate one TaskGenerator per input line
            totalJobs += taskGenerator.numJobs()
            activate(taskGenerator, taskGenerator.run(scenario.sim_time))

        scenario.remainingTasks = len(list(temp))

        scenario.printSep()

    def print_initial_data(scenario):
        scenario.printSep()


    def print_result(scenario):

        allMachines = list(scenario.scheduler.activeMachines.values()) + scenario.scheduler.destroyedMachines

        # Calculate total execution time,
        # wasted time, CPU time and total cost
        cpuTime = 0
        wastedTime = 0
        wastedSwStartup = 0
        wastedPart = 0
        totalCost = 0
        paidTime = 0
        for machine in allMachines:
            cpuTime += machine.getExecutionTime()
            paidTime += machine.getPaidTime()
            wastedTime += machine.getWastedTime()
            wastedSwStartup += machine.getWastedSwapAndStartup()
            wastedPart += machine.getWastedPartialHours()
            totalCost += machine.getExecutionCost()

        jobRTs = scenario.monitors["jobRT"]
        taskRTs = scenario.monitors["taskRT"]
        completedJobs = scenario.scheduler.completedJobs
        scenario.printSep()
    def main():
        # scenario = parse_args()
        scenario = CloudSimScenario(conf)
        return run(scenario)

    print("\n--------------- CloudSim ----------------")
    print("- Scenario initiated")
    from Main import Read_data

    Data = Read_data.read_input()         # Input network traffic data
    
    return Data
