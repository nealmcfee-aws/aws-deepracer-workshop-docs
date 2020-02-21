---
title: "Workshop Clean-up"
chapter: true
weight: 35
description: "At the end of the session, considering cleaning up the resources that were created.  AWS only charges for consumed resources."
---

# Workshop cleanup



1. Delete the **S3 bucket** by selecting the bucket then clicking *Delete* from above the list of buckets.

2. From the **AWS RoboMaker console**, make sure there are no simulation jobs in progress. If there are, select them and click *Actions->Cancel*.

3. Also from the **AWS RoboMaker Console**, from Development->Development environments, click on the environment name, *Edit*, then *Delete* from the AWS Cloud9 console.

4. In **CloudFormation**, select the stack you created and click **Delete Stack**.