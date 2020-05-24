# EMR, MRJob

## Process
1. Create config file for MRJob (as follows)
2. Create MRJob py file for main program
3. Run py file by one commend line (config runner, input file, output file)
`When use AWS: use runner EMR-Elastic MapReduce, AWS automatically create EMR instance and destroy it after completed, meanwhile S3 bucket is created`

## Config file for MRJob
```
runners:
  emr:
    aws_access_key_id:
    aws_secret_access_key:
    ec2_key_pair: ka200510
    ec2_key_pair_file: /home/ubuntu/ka200510.pem
    region: us-west-2 # http://docs.aws.amazon.com/general/latest/gr/rande.html
    master_instance_type: # https://aws.amazon.com/emr/pricing/
    instance_type:
    num_core_instances: 1
    ssh_tunnel: true
```
