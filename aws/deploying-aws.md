


## VPC
#### Process
1. Create VPC
    - VPC-MCE-Data
    - CIDR 10.0.0.0/16
2. Create Subnets
    - 2 Public and 2 Private Subnets
        - CIDR 10.0.0.0/24
        - Per AZ within the same region
3. Create Internet Gateway
    - attach Internet Gateway to Public Subnet(s)
4. Create Route Tables and associate with correct Subnets
    - e.g. Public Subnet with Public Route Table
    - Also, make sure the Public Route Table has the IGW to access the internet

5. Security Groups( Stateful Firewall)
    - Aware of connections being made to it, inbound or outbound connections are allowed to return whichever leg it is on.
    - Public Security Groups are typically associated with an application and an auto-scaling group therefore you usually only have ONE SG for all your public subnets so it can have the same rules across those resources
    - Private Security Groups, such as those on a Database, will have their own Security Group per resource (e.g. DB)
6. NACLs (Stateless)
    - Explicit Inbound and Outbound Traffic must be stated (no automatic return traffic allowed)
    - e.g. HTTP (80), HTTPS (443), Postgres(5432) must be stated inbound and outbound
    - Associate Public/Private Subnets with appropriate NACL group
    

- Building 2 and 3 Tier Architectures
- Public and Private Subnets
- Bastion Host (Jump Box)
- SSH
- Roles
- [VPC Traffic Mirroring – Capture & Inspect Network Traffic](https://aws.amazon.com/blogs/aws/new-vpc-traffic-mirroring/)
- [AWS Docs - Best Practices for Managing AWS Access Keys](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)
## RDS


## RedShift


## S3


## Athena


## Lambda


## Kinesis


## Glue


## EMR


## SageMaker


## DataPipelines


## CodeDeploy

