my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

print(my_dict['name'])
print(my_dict.get('age'))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())



ec2_info = {
    "name": "instance-01",
    "Type": "t2.micro",
    "public ip": "54.67.98.45",
}
print(ec2_info)
print(ec2_info['name'])
print(ec2_info.get('Type'))
print(ec2_info.keys())
print(ec2_info.values())
print(ec2_info.items())


# Multiple EC2 instances
ec2_instances_info = [
    {
        "id": "instance-001",
        "type": "t2.micro"
    },
    {
        "id": "instance-002", 
        "type": "t2.medium"
    },
    {
        "id": "instance-003",
        "type": "t2.xlarge"
    }
]

# Accessing specific instance type
print(ec2_instances_info[0]["type"])
print(ec2_instances_info[1]["type"])
print(ec2_instances_info[2]["type"])
