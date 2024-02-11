import decoupler as dc
from  progeny_scores import resolwe_data

def run_model(adata):
    """
   Calculate PROGENy scores for pathway activity inference from gene expression data.
   Utilizes the PROGENy model, specifically tailored for the human organism and focusing on the top 500 most responsive genes, to predict biological pathway activities. 
   This method employs a multivariate linear model (MLM) for estimating pathway activities and returns these estimates.

    Parameters:
    - adata (AnnData): An AnnData object containing gene expression data where observations are samples and variables are genes.

    Returns:
    - mlm_estimate (pandas.DataFrame): A DataFrame of PROGENy scores indicating inferred pathway activities for each sample.
    """     
    
    try:
        # Get the PROGENy model
        progeny_model = dc.get_progeny()
        #Run model 
        dc.run_mlm(mat=adata, net=progeny_model, use_raw=False)
        # PROGENy scores
        mlm_estimate = adata.obsm['mlm_estimate']  
    
        return mlm_estimate
    
    except Exception as e:
        print(f"An error occurred while calculating PROGENy scores: {e}")
        return None




def get_progeny_scores(slug):
    """
    Fetches TPM-normalized gene expression data for a given slug and calculates PROGENy scores.

    Parameters:
    - slug (str): Identifier for the data collection.

    Returns:
    - DataFrame: PROGENy scores for the data collection.
    """
    try:
        adata = resolwe_data.get_tpm_data(slug)
        if adata is None:  # Check if get_tpm_data returned an error indicator
            raise ValueError("Failed to retrieve data.")
        progeny_scores = run_model(adata)
        return progeny_scores
    except Exception as e:
        print(f"Error: {e}")
        return None




