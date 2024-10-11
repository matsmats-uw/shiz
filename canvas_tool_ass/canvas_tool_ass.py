#!python3 

# requires adding or having a header row, at least for the config blob
# select et.canvas_id, aa.id, aa.canvas_id, aa.sis_id, aa.account_name, aa.account_type, et.config from \
# lti_manager_externaltool et join astra_account aa on et.account_id = aa.id
# tool_id,acct_id,acct_canvas_id,acct_sis_id,acct_name,acct_type,config

import json
import pandas as pd
import pprint

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('/Users/willey/Desktop/canvas_sis_externaltool_waccount_edit_2024-10-09 (14_58_06).csv')

for index, row in df.iterrows():
    cdict = json.loads(row['config'])
    # pprint.pprint(jblob)
    if row['account_id'] == 83919 and cdict['assignment_selection'] is not None:
        print(cdict['name'], "-", cdict['assignment_selection']['label'])
