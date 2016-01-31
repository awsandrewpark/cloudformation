#!/usr/bin/env python
import sys
import json
import yaml

try:
    print yaml.dump(yaml.load(json.dumps(json.loads(open(sys.argv[1]).read()))), default_flow_style=False, allow_unicode=True)
except Exception as error:
    print "Oops! Something was overlooked! {error_msg}".format(error_msg=str(error)) 