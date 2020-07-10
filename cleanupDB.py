import os
import sys
import time
import platform
import ms.version
from argparse import ArgumentParser
from datetime import date

db2_module_version = '11.1.3.1'
db2_module = 'ibmdb2/client/{}'.format(db2_module_version)
system_os = platform.system()
ibm_db_version = ('2.0.8-W-py37', '2.0.8-%s-py37'% db2_module_version)[system_os == 'Linux']

ms.version.addpkg('ibm.db', ibm_db_version)
ms.version.addpkg('ms.db2', '1.0.4')
ms.version.addpkg('ms.modulecmd', '1.0.9')
ms.version.addpkg('ms.log', '1.1.0')
ms.version.addpkg('dateutil', '2.6.9')
ms.version.addpkg('six', '1.9.0')

import ms.modulecmd
ms.modulecmd.load(db2_module)

'''
validation to check whether db2_module loaded is correct'''

incompatible_modules = [x for x in ms.modulecmd.list() if x.startswith('ibmdb2/' and x!=db2_module)]
if incompatible_modules:
    print("Incompatible module(s) loaded: %s. Please upload these modles and then re-run the program" %(''.join(incompatible_modules)))
    sys.exit(1)

import ms.log
import ms.db2
import ibm_db
from dateutil.relativedelta import relativedelta

def parse_args():
    '''
     parse_args: argument parser for cleanup script
    :return:
    '''
    parser=ArgumentParser()
    parser.add_argument('s','--server', required=True, help='DB Server Name')
    parser.add_argument('-t', '--schema', required=True, help='Schema Name', type=str)
    parser.add_argument('-1', '--logDir', help='log directory locaiton', type=str)
    parser.add_argument('-b', '-batchSize', help='Delta batch size [Default batchSiez =  100000]', type=int,
                        default=100000)
    parser.add_argument()

