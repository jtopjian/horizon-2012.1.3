Horizon 2012.1.3 Modified
=========================

This repository contains my modifications to the OpenStack Horizon dashboard (version 2012.1.3). See the individual commits for details on the changes.

In summary, they include:

1. Resolving the `KeyError` issue when an admin views all Instances and Volumes. The `KeyError` will happen when other projects have running instances and attached volumes.

2. Enabling Regions. By default, if Keystone hosts multiple services in different regions, you can utilize the different regions by using the command-line tools, but not through Horizon. This is now resolved.

3. Since Django's drop-down boxes are in the form of `(value, key)`, regions have to be listed as `(url, region-name)`. This prevents the ability to use one Keystone service to provide authentication to multiple regions (unless that Keystone service is hosted on multiple IPs). This is now resolved as well.

ToDo
----
* Make sure regions are supported in `api/keystone.py` and `api/swift.py`.
