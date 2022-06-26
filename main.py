import argparse
import copyFunctions
from xml.etree.ElementTree import ElementTree
import time

def getDeployInfoByName(deploy_name):
    try:
        deploy_info = {"name": "", "source_files": [], "destination_path": "", "backup_path": "", 'name': deploy_name}
        # COLLECT ALL DEPLOYS NODES OF XML
        tree = ElementTree()

        root = tree.parse(deploy_name + '.xml')

        # GET THE DEPLOY NODE BY NAME
        deploy_node = root.find('.//deploy[@name="' + deploy_name + '"]')
        if deploy_node is not None:
            source_files_nodes = deploy_node.findall('.//sourceFilePath')
            for source in source_files_nodes:
                deploy_info['source_files'].append(source.text)

            destination_path_node = deploy_node.find('.//destinationPath')
            if destination_path_node is not None:
                deploy_info['destination_path'] = destination_path_node.text

            backup_path_node = deploy_node.find('.//backupPath')
            if backup_path_node is not None:
                deploy_info['backup_path'] = backup_path_node.text

    except Exception as error:
        print("Error: getDeployInfoByName")
        print(str(error))

    return deploy_info

def deploy(args):
    try:
        confirm_input = input("Are you sure to deploy " + args.deploy[0] + " ? (S/n) : ")

        if confirm_input == "S":

            print("Getting deploy info ...")
            time.sleep(1)
            deploy_info = getDeployInfoByName(args.deploy[0])
            print("Start backup ...")
            time.sleep(1)
            backup_result = copyFunctions.backupFolder(deploy_info['destination_path'], deploy_info['backup_path'])
            print(backup_result['message'])
            if backup_result['error'] == False:
                time.sleep(0.5)
                print("Start deploy ...")
                time.sleep(1)
                deploy_result = copyFunctions.copyFilesToDir(deploy_info['source_files'], deploy_info['destination_path'])
                print(deploy_result['message'])

        else:
            print("Canceled")

    except Exception as ex:
        print('Error:' + str(ex))

def main():
    # create parser object
    parser = argparse.ArgumentParser(description="A deploy manager!")

    # defining arguments for parser object
    parser.add_argument("-d", "--deploy", type=str, nargs=1,
                        metavar="file_name", default=None,
                        help="Execute the specified deploy based on xml configuration file.")


    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.deploy != None:
        deploy(args)

if __name__ == "__main__":
    # calling the main function
    main()
