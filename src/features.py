def identify_important_weeks(df, target_col='Weekly_Sales', group_col='Store', method='IQR', multiplier=1.5):
    """
    Identify important weeks per store:
    - High sales weeks (data-driven)
    - Holiday weeks (Holiday_Flag)
    - Year-end weeks (last week of the year)
   
    Returns df with new columns:
    - High_Sales_Event_Flag (1 = high sales)
    - Holiday_Event_Flag (1 = holiday)
    - Year_End_Flag (1 = last week of year)
    - Important_Week_Flag (1 = any of the above)
    - Important_Week_Reason (textual reason)
    """
    df = df.copy()
   
    # Convert Holiday_Flag to boolean
    df['Holiday_Event_Flag'] = df['Holiday_Flag'].astype(bool)
   
    # Initialize High Sales Flag
    df['High_Sales_Event_Flag'] = 0
   
    # Identify high sales weeks per store
    for store, group in df.groupby(group_col):
        if method == 'IQR':
            Q1 = group[target_col].quantile(0.25)
            Q3 = group[target_col].quantile(0.75)
            IQR = Q3 - Q1
            upper_bound = Q3 + multiplier * IQR
            high_sales_idx = group[group[target_col] > upper_bound].index
            df.loc[high_sales_idx, 'High_Sales_Event_Flag'] = 1
        elif method == 'Z-score':
            mean = group[target_col].mean()
            std = group[target_col].std()
            high_sales_idx = group[(group[target_col] - mean) / std > 2].index
            df.loc[high_sales_idx, 'High_Sales_Event_Flag'] = 1
   
    # Identify Year-End weeks (assuming week 52 as last week)
    df['Year_End_Flag'] = (df['Week'] == 52).astype(int)
   
    # Combine all flags into one important week flag
    df['Important_Week_Flag'] = (
        df['High_Sales_Event_Flag'].astype(bool) |
        df['Holiday_Event_Flag'] |
        df['Year_End_Flag'].astype(bool)
    ).astype(int)
   
    # Add textual reason
    def get_reason(row):
        reasons = []
        if row['High_Sales_Event_Flag']: reasons.append('HighSales')
        if row['Holiday_Event_Flag']: reasons.append('Holiday')
        if row['Year_End_Flag']: reasons.append('YearEnd')
        return ','.join(reasons) if reasons else 'Normal'
   
    df['Important_Week_Reason'] = df.apply(get_reason, axis=1)
   
    return df