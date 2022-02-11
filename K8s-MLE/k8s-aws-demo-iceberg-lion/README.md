# comments

## manual upgrade of certificate

|Item|Value|Link|
|-|-|-|
|load balancer|`ab153a680f5a64941b777ad3bb5d9b3b`|[EC2 Load balancers](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LoadBalancers:sort=desc:loadBalancerName)|
|certificate| `arn:aws:acm:eu-west-1:411447780843:certificate/c970143d-39e9-41bf-9ee4-5c134fe7b93b`|[Certificate Manager](https://eu-west-1.console.aws.amazon.com/acm/home?region=eu-west-1#/)|

## Example

``` bash
aws elb set-load-balancer-listener-ssl-certificate --load-balancer-name ab153a680f5a64941b777ad3bb5d9b3b --load-balancer-port 443 --ssl-certificate-id arn:aws:acm:eu-west-1:411447780843:certificate/c970143d-39e9-41bf-9ee4-5c134fe7b93b
```