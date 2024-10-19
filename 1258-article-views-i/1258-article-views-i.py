import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    new_df = views[views['author_id'] == views['viewer_id']]
    unique_author_df = new_df['author_id'].unique()
    sorted_df = sorted(unique_author_df)
    result_df = pd.DataFrame({'id': sorted_df})
    return result_df