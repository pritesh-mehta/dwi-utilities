#!/usr/bin/env python

"""
@author: pritesh-mehta
"""

import numpy as np
from scipy.optimize import curve_fit
from pathlib import Path
from argparse import ArgumentParser

from dwi_utilities.monoexponential_decay import log_func
import dwi_utilities.nifti_utilities as nutil

def adc_map_case(case_dir, save_case=False, output_dir=None, extension='.nii.gz'):
    """Generate ADC map using b-value DWI
    return: ADC map with units 10^-6 mm^2/s
    """
    eps = 1e-8 
    million = 1000000
    
    data_stack = []
    bval_list = []
    filepaths = nutil.path_generator(case_dir)
    for path in filepaths:
        name, nii, data = nutil.load(path)
        data_stack.append(data)
        bval_list.append(name.replace('.nii.gz','').replace('b',''))
        
    # order data stack in order of ascending b-value
    bval_list, data_stack = \
        zip(*sorted(zip(bval_list, data_stack)))
    
    # generate adc map
    bval_list = np.array(bval_list)
    data = np.array(data_stack)
    
    shape = np.shape(data[0])
    adc_data = np.zeros(shape)
            
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                y = []
                for array in data:
                    y.append(array[i][j][k])
                x = bval_list
                y = np.array(y) + eps
                z = np.log(y)
                popt, pcov = curve_fit(log_func, x, z)
                if popt[1] < 0: # noisy measurements
                    adc_data[i][j][k] = 0
                else:
                    adc_data[i][j][k] = popt[1] * million
    
    if save_case:
        case_name = Path(case_dir).parts[-1]
        save_path = Path(output_dir) / (case_name + extension)
        nutil.save(save_path, nii, adc_data)
    
    return adc_data

def adc_map_dir(cases_dir, output_dir, extension='.nii.gz'):
    """Generate ADC map using b-value DWI
    """
    for case_dir in Path(cases_dir).iterdir():
        print("Processing:", case_dir)
        adc_map_case(case_dir, save_case=True, output_dir=output_dir, extension=extension)
    return None

def process():
    parser = ArgumentParser()
    parser.add_argument('--input_dir', required=True, type=str)
    parser.add_argument('--output_dir', required=True, type=str)
    parser.add_argument('--case', required=False, action="store_true")
    parser.add_argument('--extension', required=False, type=str, default='.nii.gz')
      
    args = parser.parse_args()
    
    if args.case:
        adc_map_case(args.input_dir, save_case=True, output_dir=args.output_dir, 
                extension=args.extension)
    else:
        adc_map_dir(args.input_dir, args.output_dir,
                 extension=args.extension)
    
if __name__ == "__main__":
    process()