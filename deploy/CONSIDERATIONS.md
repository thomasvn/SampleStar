# Deployment Considerations

Requirements:

- Eight-nines availability (0.3s downtime per year). This service will be used by some high-visibility, and very prestigious games

Constraints:

- 

**Idea 1** (Winner):

- Deploy API app to a public cloud service. App makes network requests over the internet to our innovative hardware
- Optimize for availability
- Sacrifice speed (latency between public cloud app and our special hardware)

Idea 2:

- Deploy API app in a private datacenter. Co-located with our innovative hardware
- Optimize for speed (low latency network requests to the special hardware)
- Sacrifice availability (difficult to maintain your own highly available servers)

## Cloud Services Considerations

Must Haves for high availability:

- App can handle failures, restarts, & reboots. Resume operation immediately after.
- Horizontally scale app instances & load balance across instances
- Spread app across cloud availability zones
- Deploy app to multiple clouds
- Use DNS to have one hostname point to the load balancers deployed across zones/clouds
- Automation to detect outage (monitoring & alerts)
- Automation to quickly redeploy (backups, terraform)

**Idea 1** (Winner): AWS Elastic Beanstalk

- Pros:
  - quickly provision all necessary AWS resources (given time constraints)
    - ec2 instances
    - autoscaling groups
    - elastic load balancers to distribute traffic across nodes
    - cloudwatch alarms
    - security groups
    - subnets / VPCs
  - deploy across availability zones
- Cons:
  - flexibility
  - repeatability
  - only provides high-order functionality (future difficulty when our use case becomes more complex)

Idea 2: Managed Kubernetes

- Pros:
  - horizontal scaling during increased load
- Cons:
  - complexity of deployment/maintenance
  - increased complexity & dependency on varying services can decrease availability

## References

- Flask Deployments:
  - <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html#python-flask-deploy>
- Kubernetes
  - <https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/>
  - <https://microk8s.io/high-availability>
