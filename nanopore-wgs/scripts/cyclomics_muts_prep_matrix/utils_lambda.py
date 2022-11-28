import pysam
import pandas as pd
from cyvcf2 import VCF
import numpy as np
from os import path


def read_vcf_cyvcf(vcf_path: str):
    return VCF(vcf_path)


# Read VCF
def read_vcf_pandas(vcf_path: str,
             top_x_rows: int = None,
             random_fraction: float = None):
    """

    :param vcf_path: str
    :param top_x_rows: interger
    :param random_fraction: float from 0 to 1
    :return:
    """
    # VCF is now read in with pandas. Change to cyvcf2
    if random_fraction is None:
        skiprows = None
    else:
        skiprows = lambda i: i > 0 and random.random() > random_fraction

    def _split_sample_field(row, ind):
        if row != '.':
            return row.split(":")[ind]
        else:
            return np.nan

    def _get_dp_ref(row, ind):
        if row != '.':
            return int(row.split(":")[ind].split(",")[0])
        else:
            return np.nan

    def _get_dp_alt(row, ind):
        try:
            dp_alt = int(row.split(":")[ind].split(",")[1])
        except IndexError as e:
            dp_alt = np.nan
        return dp_alt

    # Read in variants
    iter_csv = pd.read_csv(vcf_path,
                           sep="\t",
                           comment='#',
                           names=["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "NGS"],
                           nrows=top_x_rows,
                           skiprows=skiprows,
                           iterator=True,
                           chunksize=100000)
    variants = pd.concat(iter_csv)

    # split format field. By getting the order of format.
    # format = variants['FORMAT'][0].split(":")
    #variants['GT'] = variants["NGS"].apply(lambda x: _split_sample_field(x, format.index("GT")))
    #variants['DP'] = variants["NGS"].apply(lambda x: float(_split_sample_field(x, format.index("DP"))))
    #variants['AD_REF'] = variants["NGS"].apply(lambda x: _get_dp_ref(x, format.index("AD")))
    #variants['AD_ALT'] = variants["NGS"].apply(lambda x: _get_dp_alt(x, format.index("AD")))
    # drop unused columns
    variants.drop(columns= [ "QUAL", "FILTER","INFO", "FORMAT", "NGS"], inplace = True)
    #print("This is the dataframe with info from the vcf file:")
    #display(variants)
    #dataset = variants.values
    #print(dataset) #nice to show

    return variants #dataframe with info from vcf file


def get_substitution_type(df):
    base_substitution = df.apply(lambda x: "".join([str(df['REF']),">", str(df['ALT'])]))
    # pandas series
    return base_substitution


# Read bam file
def read_bam(bamfile):
    # check if there is bam.bai (or bai)
    # if not path.exists(f"{bamfile}.bai"):
    pysam.index(bamfile)
    bam = pysam.AlignmentFile(bamfile)
    return bam