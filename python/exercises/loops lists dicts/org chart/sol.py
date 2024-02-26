org_chart_large = {
    "name": "CEO",
    "subordinates": [
        {
            "name": "CTO",
            "subordinates": [
                {
                    "name": "Development",
                    "subordinates": [
                        {"name": "Engineering Manager"},
                        {
                            "name": "Software Engineers",
                            "subordinates": [
                                {"name": "Senior Developer"},
                                {"name": "Developer"},
                                {"name": "Junior Developer"}
                            ]
                        }
                    ]
                },
                {
                    "name": "QA",
                    "subordinates": [
                        {"name": "QA Manager"},
                        {"name": "QA Engineers"}
                    ]
                }
            ]
        },
        {
            "name": "CFO",
            "subordinates": [
                {"name": "Finance Manager"},
                {
                    "name": "Accounting",
                    "subordinates": [
                        {"name": "Senior Accountant"},
                        {"name": "Junior Accountant"}
                    ]
                }
            ]
        },
        {
            "name": "COO",
            "subordinates": [
                {
                    "name": "Operations",
                    "subordinates": [
                        {"name": "Operations Manager"},
                        {"name": "Logistics Team"}
                    ]
                },
                {
                    "name": "HR",
                    "subordinates": [
                        {"name": "HR Manager"},
                        {"name": "Recruitment Team"}
                    ]
                }
            ]
        }
    ]
}



def rec(node, workers_counter = 0, departments_list = [], is_under_CTO = False, under_CTO_list = [], developers = []):
    # count every worker:
    # I've assumed here that a worker would have no "subordinates"
    if "name" in node and "subordinates" not in node:
        workers_counter += 1
        # If we are under the CTO and there is no "subordinates", then this is an employee that works
        # under the CTO:
        if is_under_CTO: under_CTO_list.append(node["name"])

        # is it a developer?
        if "develop" in node["name"].lower():
            developers.append(node["name"])

    # Set a flag when we reach the CTO node:
    if node["name"] == "CTO": is_under_CTO = True

    # If there are "subordinates" in that node, then this is not a person, but a department:
    if "subordinates" in node:
        departments_list.append(node["name"])

        # Let's loop over all of the children of this node recursivly:
        for item in node["subordinates"]:
            workers_counter, departments_list, is_under_CTO, under_CTO_list, developers = rec(item, workers_counter, departments_list, is_under_CTO, under_CTO_list, developers)

    # Let's reset the CTO flag after finishing from all of their node children:
    if node["name"] == "CTO": is_under_CTO = False
    return workers_counter, departments_list, is_under_CTO, under_CTO_list, developers
    

workers_counter, departments_list, is_under_CTO, under_CTO_list, developers = rec(org_chart_large)
print("Total workers:", workers_counter)
print("Total employees work under CTO:", len(under_CTO_list))
print("Names of the developers:", developers)
print("Total departments:", len(departments_list))
print("Names of the departments:", departments_list)