from typing import List, Optional

from data.owners import Owner
from data.cages import Cage

def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email

    owner.save()

    return owner

def find_account_by_email(email:str) -> Owner:
    owner = Owner.objects().filter(email=email).first()
    return owner


def register_cage(active_account: Owner,
                  name, allow_dangerous, has_toys,
                  carpeted, meters, price) -> Cage:
    cage = Cage()

    cage.name = name
    cage.square_meters = meters
    cage.is_carpeted = carpeted
    cage.has_toys = has_toys
    cage.allow_dangerous_snakes = allow_dangerous
    cage.price = price

    cage.save()

    account = find_account_by_email(active_account.email)
    account.cage_ids.append(cage.id)
    account.save()

    return cage


def find_cages_for_user(account: Owner) -> List[Cage]:
    #can use $in as below
    query = Cage.objects(id__in=account.cage_ids)
    cages = list(query)

    return cages
