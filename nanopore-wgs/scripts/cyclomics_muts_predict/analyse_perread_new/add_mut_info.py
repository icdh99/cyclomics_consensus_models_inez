import time
start = time.time()
import pandas as pd
import pysam
import os

df_pred = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/csv_files_perregion/cycl_muts_predict_t2t_perread.csv')
print(f'number of reads per model before removing duplicates: {df_pred["model-cov"].value_counts()}')
print(f'number of rows before removing duplicates based on region readid and model cov: {df_pred.shape}')
print(list(df_pred.columns))
print(df_pred.head(1))

df_pred = df_pred.sort_values('pred-align_length', ascending=False).drop_duplicates(subset=['region_readid', 'model-cov'])
print(f'number of rows after removing duplicates based on region readid and model cov: {df_pred.shape}')
print(f'number of reads after model after removing duplicates: {df_pred["model-cov"].value_counts()}')

print(df_pred['region'].value_counts())

exit()
"""
Mutation 1
7577900 G>A
for each bamfile/model 
change in big pred dataframe
"""
region = 'region3'
directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred'
for filename in os.listdir(directory):
    if filename.endswith('.bam') and region in filename:
        print(filename)
        f = os.path.join(directory, filename)
        print(f)
        s1 = filename.split('.')[0].split('_')
        model_type = s1[3]
        coverage_model = s1[4]
        model_cov = model_type + '_' + coverage_model
        print(model_type, coverage_model, model_cov)
        bamfile = pysam.AlignmentFile(f, 'rb')
        for pileupcolumn in bamfile.pileup("chr17", 7577899, 7577900, max_depth = 400000, min_base_quality = 0, truncate = True ):
            # 7577 899 in pileup is 757 7900 mutations
            print(f'pileup column position: {pileupcolumn.pos}')
            count = 0
            print(len(pileupcolumn.get_query_sequences()))
            print(len(pileupcolumn.get_query_names()))
            names_with_mut1 = []
            for base, readid in zip(pileupcolumn.get_query_sequences(), pileupcolumn.get_query_names()):
                if base == 'A': names_with_mut1.append(readid)
            print(f'number of readids to change for mut1: {len(names_with_mut1)}')
        for i, readid in enumerate(names_with_mut1): 
            df_pred.loc[(df_pred['region_readid'] == f'{region}_{readid}') & (df_pred['model-cov'] == model_cov), 'mut1'] = 1

        # break # DO FOR THE FIRST BAM FILE ONLY

"""
Mutation 2
7577926 C>T
for each bamfile/model 
change in big pred dataframe
"""
region = 'region3'
directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred'
for filename in os.listdir(directory):
    if filename.endswith('.bam') and region in filename:
        print(filename)
        f = os.path.join(directory, filename)
        print(f)
        s1 = filename.split('.')[0].split('_')
        model_type = s1[3]
        coverage_model = s1[4]
        model_cov = model_type + '_' + coverage_model
        print(model_type, coverage_model, model_cov)
        bamfile = pysam.AlignmentFile(f, 'rb')
        for pileupcolumn in bamfile.pileup("chr17", 7577925, 7577926, max_depth = 400000, min_base_quality = 0, truncate = True ):
            # 7577 899 in pileup is 757 7900 mutations
            print(f'pileup column position: {pileupcolumn.pos}')
            count = 0
            print(len(pileupcolumn.get_query_sequences()))
            print(len(pileupcolumn.get_query_names()))
            names_with_mut2 = []
            for base, readid in zip(pileupcolumn.get_query_sequences(), pileupcolumn.get_query_names()):
                if base == 'T': names_with_mut2.append(readid)
            print(f'number of readids to change for mut2: {len(names_with_mut2)}')
        for i, readid in enumerate(names_with_mut2): df_pred.loc[(df_pred['region_readid'] == f'{region}_{readid}') & (df_pred['model-cov'] == model_cov), 'mut2'] = 1
        # break # DO FOR THE FIRST BAM FILE ONLY

"""
Mutation 3
7577927 G>A
for each bamfile/model 
change in big pred dataframe
"""
region = 'region3'
directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred'
for filename in os.listdir(directory):
    if filename.endswith('.bam') and region in filename:
        print(filename)
        f = os.path.join(directory, filename)
        print(f)
        s1 = filename.split('.')[0].split('_')
        model_type = s1[3]
        coverage_model = s1[4]
        model_cov = model_type + '_' + coverage_model
        print(model_type, coverage_model, model_cov)
        bamfile = pysam.AlignmentFile(f, 'rb')
        for pileupcolumn in bamfile.pileup("chr17", 7577926, 7577927, max_depth = 400000, min_base_quality = 0, truncate = True ):
            # 7577 899 in pileup is 757 7900 mutations
            print(f'pileup column position: {pileupcolumn.pos}')
            count = 0
            print(len(pileupcolumn.get_query_sequences()))
            print(len(pileupcolumn.get_query_names()))
            names_with_mut3 = []
            for base, readid in zip(pileupcolumn.get_query_sequences(), pileupcolumn.get_query_names()):
                if base == 'A': names_with_mut3.append(readid)
            print(f'number of readids to change for mut3: {len(names_with_mut3)}')
        for i, readid in enumerate(names_with_mut3): df_pred.loc[(df_pred['region_readid'] == f'{region}_{readid}') & (df_pred['model-cov'] == model_cov), 'mut3'] = 1
        # break # DO FOR THE FIRST BAM FILE ONLY

"""
Mutation 4
7578324 T>A
for each bamfile/model 
change in big pred dataframe
"""
region = 'region4'
directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred'
for filename in os.listdir(directory):
    if filename.endswith('.bam') and region in filename:
        print(filename)
        f = os.path.join(directory, filename)
        print(f)
        s1 = filename.split('.')[0].split('_')
        model_type = s1[3]
        coverage_model = s1[4]
        model_cov = model_type + '_' + coverage_model
        print(model_type, coverage_model, model_cov)
        bamfile = pysam.AlignmentFile(f, 'rb')
        for pileupcolumn in bamfile.pileup("chr17", 7578323, 7578324, max_depth = 400000, min_base_quality = 0, truncate = True ):
            # 7577 899 in pileup is 757 7900 mutations
            print(f'pileup column position: {pileupcolumn.pos}')
            count = 0
            print(len(pileupcolumn.get_query_sequences()))
            print(len(pileupcolumn.get_query_names()))
            names_with_mut4 = []
            for base, readid in zip(pileupcolumn.get_query_sequences(), pileupcolumn.get_query_names()):
                if base == 'A': names_with_mut4.append(readid)
            print(f'number of readids to change for mut4: {len(names_with_mut4)}')
        for i, readid in enumerate(names_with_mut4): df_pred.loc[(df_pred['region_readid'] == f'{region}_{readid}') & (df_pred['model-cov'] == model_cov), 'mut4'] = 1
        # break # DO FOR THE FIRST BAM FILE ONLY

"""
Mutation 5
7578387 A>C
for each bamfile/model 
change in big pred dataframe
"""
region = 'region4'
directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred'
for filename in os.listdir(directory):
    if filename.endswith('.bam') and region in filename:
        print(filename)
        f = os.path.join(directory, filename)
        print(f)
        s1 = filename.split('.')[0].split('_')
        model_type = s1[3]
        coverage_model = s1[4]
        model_cov = model_type + '_' + coverage_model
        print(model_type, coverage_model, model_cov)
        bamfile = pysam.AlignmentFile(f, 'rb')
        for pileupcolumn in bamfile.pileup("chr17", 7578386, 7578387, max_depth = 400000, min_base_quality = 0, truncate = True ):
            # 7577 899 in pileup is 757 7900 mutations
            print(f'pileup column position: {pileupcolumn.pos}')
            count = 0
            print(len(pileupcolumn.get_query_sequences()))
            print(len(pileupcolumn.get_query_names()))
            names_with_mut5 = []
            for base, readid in zip(pileupcolumn.get_query_sequences(), pileupcolumn.get_query_names()):
                if base == 'C': names_with_mut5.append(readid)
            print(f'number of readids to change for mut5: {len(names_with_mut5)}')
        for i, readid in enumerate(names_with_mut5): df_pred.loc[(df_pred['region_readid'] == f'{region}_{readid}') & (df_pred['model-cov'] == model_cov), 'mut5'] = 1
        # break # DO FOR THE FIRST BAM FILE ONLY


df_pred.to_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/csv_files_perregion/cycl_muts_predict_t2t_perread_mutinfo.csv')

end = time.time()
print("The time of execution is :", end-start)