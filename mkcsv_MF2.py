


import csv

#header = ['tomo_name', 'raw_tomo', 'filtered_tomo', 'no_mask']
header = ['tomo_name','tomo','masking_file','class_name_mask','path_to_motl_clean_class_name']

data = ['neuron5_ts003_10Apx','tomo/neuron5_ts_003_unsorted_10.00Apx.mrc','','']

new_file_name = 'neuron5_ts003_10Apx_metadata.csv'

with open(new_file_name, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)

