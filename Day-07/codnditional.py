import sys

environment = sys.argv[1]

if environment == "dev":
    print("Development environment - No restrictions")
elif environment == "staging":
    print("Staging environment - Limited resources")
elif environment == "prod":
    print("Production environment - Full monitoring required")
else:
    print("Invalid environment. Use: dev, staging, or prod")


import sys

service_status = sys.argv[1]

if service_status == "running":
    print("Service is healthy")
elif service_status == "stopped":
    print("Service needs to be started")
elif service_status == "error":
    print("Service requires troubleshooting")
else:
    print("Unknown service status")


config_type = sys.argv[1]

if config_type == "nginx":
    print("Configuring Nginx web server")
elif config_type == "apache":
    print("Configuring Apache web server")
elif config_type == "docker":
    print("Configuring Docker containers")
else:
    print("Unsupported configuration type")

deployment_size = sys.argv[1]

if deployment_size == "small":
    print("Deploying 1-2 instances")
elif deployment_size == "medium":
    print("Deploying 3-5 instances")
elif deployment_size == "large":
    print("Deploying 6-10 instances")
else:
    print("Invalid deployment size")