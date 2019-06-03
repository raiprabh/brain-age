data_root = '/shared/'

ixi_root = data_root + 'ixi-dataset/'

ixi_t1_root = ixi_root + 'IXI-T1/'

fcp_root = data_root + 'fcp/'

adni_root = '/data/ADNI/'

fcp_data_directories = ['Baltimore', 'Bangor', 'Beijing_Zang', 'Berlin_Margulies', 'Cambridge_Buckner', 'Dallas', 'ICBM', 'Leiden_2180', 'Leiden_2200', 'Leipzig', 'Milwaukee_a', 'Milwaukee_b', 'Munchen', 'Newark', 'NewHaven_a', 'NewHaven_b', 'NewYork_a_ADHD', 'NewYork_a', 'NewYork_b', 'Ontario', 'Orangeburg', 'Oulu', 'Oxford', 'PaloAlto', 'Pittsburgh', 'Queensland', 'SaintLouis', 'Taipei_a', 'Taipei_b', 'Atlanta', 'AnnArbor_a', 'AnnArbor_b']

fcp_data_directories_no_demographics = ['Milwaukee_a', 'Ontario', 'Taipei_a', 'Taipei_b']

fcp_data_directories_with_demographics = list(set(fcp_data_directories) - set(fcp_data_directories_no_demographics))
