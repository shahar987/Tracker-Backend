from mongoengine import *
import json

from model import Checklist
from model import ClientChecks
from model import Users
from model import Card
from model import EndPoints


# Insert one document to collection
def create_user(email, password, company):
    print("\nCREATE:\n --------------")
    user_exist = Users.objects(company=company, email=email)
    if user_exist:
        print("user already exist")
    else:
        print("created")
        new_user = Users(email=email,
                         password=password,
                         company=company)
        new_user.save()
        return json.loads(new_user.to_json())


# Read user by his company and email
def read_user(email):
    print("\nREAD:\n --------------")
    users = Users.objects(email=email)
    if users:
        for endpoint in users:
            print(f'email: {endpoint.email} \npassword:{endpoint.password}')
            return json.loads(endpoint.to_json())
    else:
        print("user does not exist")


# Change company by email and password
def update_user_company(new_company, email, password):
    print("\nUPDATE:\n --------------")
    user_company = Users.objects(email=email, password=password)
    if user_company:
        print(f'new company: {new_company}')
        Users.objects(email=email, password=password).update(company=new_company)
    else:
        print("user does not exist")


# Change email by company and password
def update_user_email(company, new_email, password):
    print("\nUPDATE:\n --------------")
    user_email = Users.objects(company=company, password=password)
    if user_email:
        print(f'new email: {new_email}')
        Users.objects(company=company, password=password).update(email=new_email)
    else:
        print("user does not exist")


# Change password by company and email
def update_user_password(company, email, new_password):
    print("\nUPDATE:\n --------------")
    user_password = Users.objects(company=company, email=email)
    if user_password:
        print(f'new password: {new_password}')
        Users.objects(company=company, email=email).update(password=new_password)
    else:
        print("user does not exist")


# Delete user from db by his ip
def delete_user(company, email, password):
    print("\nDELETE:\n --------------")
    user = Users.objects(company=company, email=email, password=password)
    if user:
        Users.objects(company=company, email=email, password=password).delete()
        print("deleted")
    else:
        print("user does not exist")


# Create new checklist
def create_checklist(name, number):
    print("\nCREATE:\n --------------")
    checklist_exist = Checklist.objects(name=name, number=number)
    if checklist_exist:
        print("checklist already exist")
    else:
        print("created")
        new_checklist = Checklist(name=name, number=number)
        new_checklist.save()
        return json.loads(new_checklist.to_json())


# Read checklist by number
def read_checklist():
    print("\nREAD:\n --------------")
    checklist = Checklist.objects()
    checklist_name = []
    if checklist:
        for endpoint in checklist:
            checklist_name.append(endpoint.name)
        return checklist_name
    else:
        print("checklist does not exist")


# Change checklist by number
def update_user_checklist(new_name, number):
    print("\nUPDATE:\n --------------")
    user_checklist = Checklist.objects(number=number)
    if user_checklist:
        print(f'new checklist: {new_name}')
        user_checklist.objects(number=number).update(name=new_name)
    else:
        print("checklist does not exist")


# Change checklist by name
def update_checklist(name, new_number):
    print("\nUPDATE:\n --------------")
    chanage_checklist = Checklist.objects(name=name)
    if chanage_checklist:
        print(f'new checklist: {new_number}')
        chanage_checklist.objects(name=name).update(number=new_number)
    else:
        print("checklist does not exist")


# Delete checklist from db by his number
def delete_checklist(number):
    print("\nDELETE:\n --------------")
    checklist = Checklist.objects(number=number)
    if checklist:
        Users.objects(number=number).delete()
        print("deleted")
    else:
        print("checklist does not exist")


# Create clientcheck
def create_clientChecks(company, client_name, client_list):
    print("\nCREATE:\n --------------")
    checklist_exist = ClientChecks.objects(client_name=client_name, company=company)
    if checklist_exist:
        print("ClientChecks already exist")
    else:
        print("created")
        new_checklist = ClientChecks(client_name=client_name, company=company, client_list=client_list)
        new_checklist.save()
        return json.loads(new_checklist.to_json())

# Read clientchecks
def read_clientchecks(company, client_name):
    print("\nREAD:\n --------------")
    clientchecks = ClientChecks.objects(client_name=client_name, company=company)
    if clientchecks:
        for endpoint in clientchecks:
            return json.loads(endpoint.to_json())  #למה למחוק את הפרינט שהיה פה?
    else:
        print("clientchecks does not exist")


# Change the client name in checklist
def update_clientcheck(company, new_client_name, client_list):
    print("\nUPDATE:\n --------------")
    clientcheck = ClientChecks.objects(company=company, client_list=client_list)
    if clientcheck:
        print(f'new clientcheck: {new_client_name}')
        clientcheck.objects(company=company, client_list=client_list).update(client_name=new_client_name)
    else:
        print("clientcheck does not exist")



# Delete clientcheck company
def delete_clientcheck_company(company):
    print("\nDELETE:\n --------------")
    clientcheck = Checklist.objects(company=company)
    if clientcheck:
        ClientChecks.objects(company=company).delete()
        print("deleted")
    else:
        print("clientcheck does not exist")


# Delete clientcheck client name
def delete_clientcheck_clientname(client_name):
    print("\nDELETE:\n --------------")
    clientcheck = Checklist.objects(client_name=client_name)
    if clientcheck:
        ClientChecks.objects(client_name=client_name).delete()
        print("deleted")
    else:
        print("clientcheck does not exist")


# Delete clientcheck client list
def delete_clientcheck_clientlist(client_list):
    print("\nDELETE:\n --------------")
    clientcheck = Checklist.objects(client_list=client_list)
    if clientcheck:
        ClientChecks.objects(client_list=client_list).delete()
        print("deleted")
    else:
        print("clientcheck does not exist")

# Insert one document to collection (table client status numbers
def create_client(client_name, error_number, ip, company) -> dict:
    print("\nCREATE:\n --------------")
    client_name_exist = Card.objects(client_name=client_name)

    if client_name_exist:
        print("client already exist")
    else:
        clientstatusnumbers = Card(
            client_name=client_name, error_number=error_number, ip=ip, company=company)
        clientstatusnumbers.save()
        return json.loads(clientstatusnumbers.to_json())


# Read client by his name
def read_client(name) -> dict:
    print("\nREAD:\n --------------")
    matches = Card.objects(client_name=name)
    if matches:
        return json.loads(matches.first().to_json())


# Read client by  company
def read_client_by_company(company) -> list:
    print("\nREAD:\n --------------")
    matches = Card.objects(company=company)
    if matches:
        return [json.loads(match.to_json()) for match in matches]


# Change client ok_number / error_number by his name
def update_client_by_name(name, n: int, add: bool):
    print("\nUPDATE:\n --------------")
    client = Card.objects(client_name=name).first()
    if client:
        client.error_number += n if add else n * -1
        return json.loads(client.to_json())
    else:
        print("client does not exist")


# Delete client from db by his name
def delete_client_by_name(name):
    print("\nDELETE:\n --------------")
    client = Card.objects(client_name=name)
    if client:
        ret = json.loads(client.to_json())
        client.delete()
        return ret
    else:
        print("client does not exist")


# Insert one document to collection table - endpoint
def create_end_points(company: str):
    error_client_number = 0
    total_clients_number = 0
    company_exist = EndPoints.objects(company=company)
    if company_exist:
        all_company_card = Card.objects(company=company)
        for card in all_company_card:
            if card.error_number > 0:
                error_client_number = error_client_number + 1
                total_clients_number = total_clients_number + 1
            else:
                total_clients_number = total_clients_number + 1
        EndPoints.objects(company=company).update(error=error_client_number, ok=(total_clients_number- error_client_number), total=(total_clients_number))
        print("update company number status")
    else:
        all_company_card = Card.objects(company=company)
        for card in all_company_card:
            if card.error_number > 0:
                error_client_number = error_client_number + 1
                total_clients_number = total_clients_number + 1
            else:
                total_clients_number = total_clients_number + 1
        endPoints = EndPoints(total=total_clients_number,
                              ok=total_clients_number - error_client_number,
                              error=error_client_number,
                              company=company)
        endPoints.save()
        print("created new company number status")



# Read company details by company name
def read_end_points(company):
    print("\nREAD:\n --------------")
    endPoints = EndPoints.objects(company=company)
    if endPoints:
        return [json.loads(endpoints.to_json()) for endpoints in endPoints]
    else:
        print("company does not exist")


# Change company name
def update_company_name(company, new_company):
    print("\nUPDATE:\n --------------")
    temp_company = EndPoints.objects(company=company)
    if temp_company:
        check_company = EndPoints.objects(company=new_company)
        if check_company:
            print("company is already exists")
        else:
            print(f'new name: {new_company}')
            EndPoints.objects(company=company).update(company=new_company)
    else:
        print("company does not exist")

# Change company clients details
def update_company_clients(company: str, n: int, add: bool, ok: bool):
    print("\nUPDATE:\n --------------")
    ep = EndPoints.objects(company=company).first()

    _n = n if add else n * -1

    if ok:
        ep.ok += _n
    else:
        ep.error += _n

    ep.total = ep.ok + ep.error
    ep.save()


# Delete company from db by company name
def delete_end_points(company):
    print("\nDELETE:\n --------------")
    endpoints = EndPoints.objects(company=company)
    if endpoints:
        EndPoints.objects(company=company).delete()
        print("deleted company")
    else:
        print("company does not exist")



