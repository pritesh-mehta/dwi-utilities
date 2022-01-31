# DWI-Utilities

This repository contains functionality for apparent diffusion coefficient (ADC) map and computed high b-value diffusion-weighted (DWI) magnetic resonance image (MRI) generation.

## Installation instructions 

1) Clone/download repository.

2) Change directory into repository.

3) Install:
	```
	pip install .
    ```
	
## How to use it 

- Function imports.

- Command line:

	- ADC map:
		```
		adc_map --input_dir .\sample_data\0_sample_low_b_val_dwi --output_dir .\sample_data\1_output_adc_maps
		```
	
	- Computed high b-value e.g. b2000:
		```
		comp_high_b --input_dir .\sample_data\0_sample_low_b_val_dwi --target_bval 2000 --output_dir .\sample_data\1_output_cb2000_dwi
		```