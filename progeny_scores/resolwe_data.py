from resdk import Resolwe
from resdk.exceptions import ResolweServerError
from resdk.tables import RNATables
from anndata import AnnData
import numpy as np
import config


def connect_to_resolwe():
    """Connect to the Resolwe server."""
    try:
        res = Resolwe(url=config.RESOLWE_URL)
        return res
    except ResolweServerError as e:
        print(f"Failed to connect to Resolwe server: {e}")
        return None
    

def get_tpm_data(slug):
    """Return TPM-normalized reads in AnnData object."""
    res = connect_to_resolwe()
    if res is not None:
        try:
            collection = res.collection.get(slug)
            tables = RNATables(collection)
            
            exp = tables.exp
            exp_type = exp.attrs['exp_type']
            
           
            if exp_type == config.GENE_EXPRESSION_TYPE:
                
                exp.columns = exp.columns.map(str)
                exp.rename(columns=tables.readable_columns, inplace=True)
               
                adata = AnnData(X=exp, obs=tables.meta, dtype=np.float32)
                adata.var_names_make_unique(join='_')

                return adata
                    
            else:
                raise ValueError(f"The collection does not contain {config.GENE_EXPRESSION_TYPE} data. Found exp_type: {exp_type}")

        except Exception as e:
            print(f"Failed to retrieve or identify data: {e}")
            return None
    else:
        print("Connection to Resolwe failed.")
    return None




