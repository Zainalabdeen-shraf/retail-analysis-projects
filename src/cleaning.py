import pandas as pd

def analyze_outliers(df, numeric_columns, holiday_col='Holiday_Flag'):
    """
    Function to detect outliers, link to real causes, and document them.
   
    Parameters:
    df : pandas.DataFrame
        The dataset
    numeric_columns : list
        List of numeric columns to check for outliers
    holiday_col : str
        Column name that indicates holidays (default 'Holiday_Flag')
       
    Returns:
    outliers_df : pandas.DataFrame
        DataFrame with all outliers, their bounds, and possible causes
    """
    all_outliers = []

    for col in numeric_columns:
        # Compute IQR bounds
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5*IQR
        upper = Q3 + 1.5*IQR
       
        # Extract outliers
        outliers = df[(df[col] < lower) | (df[col] > upper)].copy()
        outliers['Outlier_Column'] = col
        outliers['Lower_Bound'] = lower
        outliers['Upper_Bound'] = upper
       
        # Assign possible cause based on data
        def cause(row):
            # Example for Weekly_Sales
            if col == 'Weekly_Sales':
                if row[holiday_col] == 1:
                    return 'Holiday Week'
                elif row[col] > upper:
                    return 'High Sales Event'
                elif row[col] < lower:
                    return 'Low Sales Event'
                else:
                    return 'Unknown'
            # Example for Temperature
            elif col == 'Temperature':
                if row[col] > upper:
                    return 'Unusually Hot'
                elif row[col] < lower:
                    return 'Unusually Cold'
                else:
                    return 'Unknown'
            # Example for Unemployment
            elif col == 'Unemployment':
                if row[col] > upper:
                    return 'High Unemployment'
                elif row[col] < lower:
                    return 'Low Unemployment'
                else:
                    return 'Unknown'
            # Default for other numeric columns
            else:
                return 'Outlier'
       
        outliers['Possible_Cause'] = outliers.apply(cause, axis=1)
       
        all_outliers.append(outliers)
   
    # Combine all outliers
    outliers_df = pd.concat(all_outliers, ignore_index=True)
    return outliers_df

