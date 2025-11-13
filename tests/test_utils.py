
def test_load_data():
    from telco_churn.utils import load_data
    import pandas as pd
    df = load_data('data/Telco-Customer-Churn.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty